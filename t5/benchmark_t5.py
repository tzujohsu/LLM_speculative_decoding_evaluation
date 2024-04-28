#%%
import time
import random
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from autoregressive_sampling_updated import autoregressive_sampling
from speculative_sampling_updated import speculative_sampling
from utils_updated import load_data, check_function
import numpy as np
import argparse

torch.backends.cudnn.benchmark =  True
torch.backends.cudnn.enabled =  True


#%%

def parse_arguments():
    parser = argparse.ArgumentParser(description='args for main.py')

    parser.add_argument('--approx_model_name', type=str, default="double7/vicuna-68m")
    parser.add_argument('--target_model_name', type=str, default="lmsys/vicuna-7b-v1.3")
    parser.add_argument('--seed', '-s', type=int, default=None, help='set a random seed, which can makes the result reproducible')
    parser.add_argument('--max_tokens', '-M', type=int, default=30, help='max token number generated.')
    parser.add_argument('--gamma', '-g', type=int, default=4, help='# guess time.')
    parser.add_argument('--temperature', '-t', type=int, default=0, help='temperature')
    parser.add_argument('--datafile_path', '-f', type=str, default='combined_data.jsonl', help='temperature')
    parser.add_argument('--output_dir', '-o', type=str, default='/outputs', help='output-txt')
    parser.add_argument('--subtask_result', type=bool, default=True, help='whether print out subtask result')
    args = parser.parse_args()
    return args


#%%

args = parse_arguments()
device = "cuda" if torch.cuda.is_available() else "cpu"

if "t5" in args.target_model_name.lower():
    target_model = AutoModelForSeq2SeqLM.from_pretrained(args.target_model_name).to(device).bfloat16()
else:
    target_model = AutoModelForCausalLM.from_pretrained(args.target_model_name).to(device)

if "t5" in args.approx_model_name.lower():
    draft_model = AutoModelForSeq2SeqLM.from_pretrained(args.approx_model_name).to(device).bfloat16()
else:
    draft_model = AutoModelForCausalLM.from_pretrained(args.approx_model_name).to(device)

tokenizer = AutoTokenizer.from_pretrained(args.target_model_name)
print("finished loading model")

print("Target Model:", target_model.config._name_or_path)
print("Approx Model:", draft_model.config._name_or_path)
print()

#%%
jsonl_file = args.datafile_path
texts, subtasks = load_data(jsonl_file)
MAX_NEW_TOKENS = args.max_tokens
TEMPERATURE = args.temperature
inputs_sample = tokenizer(texts[-1], return_tensors="pt").to(device)
sub_result_sps = {'multi-turn':[0,0], 'translation':[0,0], 'summarization':[0,0], 'qa':[0,0],
               'math_reasoning':[0,0], 'rag':[0,0], 'law analytics':[0,0], 'grammar correction':[0,0]}
sub_result_as = {'multi-turn':[0,0], 'translation':[0,0], 'summarization':[0,0], 'qa':[0,0],
               'math_reasoning':[0,0], 'rag':[0,0], 'law analytics':[0,0], 'grammar correction':[0,0]}

print("finished loading data")
print("# data instances: ",len(texts))
print()

# check_function(target_model, draft_model, tokenizer, inputs_sample, MAX_NEW_TOKENS, autoregressive_sampling, speculative_sampling)
# print("function check done")


#%% 
print("Benchmarking naive Autoregressive Sampling...")
## Autoregressive
# Warmup
tokens = autoregressive_sampling(target_model, initial_prompt_seq=inputs_sample.input_ids, 
                                 target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), temperature=TEMPERATURE)

time_taken = 0
new_tokens = 0
for i in tqdm(range(len(texts))):
  # Empty cache
  torch.cuda.empty_cache()
  if subtasks[i] == 'multi-turn':
    turns = texts[i][0]
    tmp_new_tokens, tmp_time_taken = 0, 0
    # turn 1
    inputs = tokenizer(turns[0], return_tensors="pt").to(device)
    start_len = len(inputs.input_ids)

    start_time = time.time_ns()
    tokens = autoregressive_sampling(target_model, initial_prompt_seq=inputs.input_ids, 
                                     target_len=MAX_NEW_TOKENS+len(inputs.input_ids), temperature=TEMPERATURE)
    end_time = time.time_ns()
    new_tokens += len(tokens[0]) - start_len
    time_taken += (end_time - start_time) / 1_000_000_000
    tmp_new_tokens += len(tokens[0]) - start_len
    tmp_time_taken += (end_time - start_time) / 1_000_000_000

    # turn 2
    response = tokenizer.decode(tokens[0], skip_special_tokens=True)
    response += (" " + turns[1])
    inputs = tokenizer(response, return_tensors="pt").to(device)
    start_len = len(inputs.input_ids)
    start_time = time.time_ns()
    tokens = autoregressive_sampling(target_model, initial_prompt_seq=inputs.input_ids, 
                                     target_len=MAX_NEW_TOKENS+len(inputs.input_ids), temperature=TEMPERATURE)
    end_time = time.time_ns()

    new_tokens += len(tokens[0]) - start_len
    time_taken += (end_time - start_time) / 1_000_000_000
    tmp_new_tokens += len(tokens[0]) - start_len
    tmp_time_taken += (end_time - start_time) / 1_000_000_000

    sub_result_as[subtasks[i]][0]+= (tmp_new_tokens)
    sub_result_as[subtasks[i]][1]+= (tmp_time_taken)
  else:
    text = texts[i]
    inputs = tokenizer(text, return_tensors="pt").to(device)
    start_len = len(inputs.input_ids)

    start_time = time.time_ns()
    tokens = autoregressive_sampling(target_model, initial_prompt_seq=inputs.input_ids, 
                                     target_len=MAX_NEW_TOKENS+len(inputs.input_ids), temperature=TEMPERATURE)
    end_time = time.time_ns()

    new_tokens += len(tokens[0]) - start_len
    time_taken += (end_time - start_time) / 1_000_000_000
    sub_result_as[subtasks[i]][0]+= (len(tokens[0]) - start_len)
    sub_result_as[subtasks[i]][1]+= (((end_time - start_time) / 1_000_000_000))

print(f"Throughput (Autoregressive Sampling): {new_tokens/time_taken:.2f} tok/s")
overall_result_as = new_tokens/time_taken

# Empty cache
torch.cuda.empty_cache()

#%%
## Speculative Sampling
# Warmup
print("Benchmarking Speculative Sampling...")
tokens, alpha = speculative_sampling(target_model, draft_model, prefix=inputs_sample.input_ids, 
                              target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), tokenizer=tokenizer, temperature=TEMPERATURE)

time_taken = 0
new_tokens = 0
alphas = torch.tensor([alpha], device=device)

for i in tqdm(range(len(texts))):
  # Empty cache
  torch.cuda.empty_cache()
  if subtasks[i] == 'multi-turn':
    turns = texts[i][0]
    tmp_new_tokens, tmp_time_taken = 0, 0
    # turn 1
    inputs = tokenizer(turns[0], return_tensors="pt").to(device)
    start_len = len(inputs.input_ids)

    start_time = time.time_ns()
    tokens, alpha = speculative_sampling(target_model, draft_model, prefix=inputs.input_ids,  
                                  target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), temperature=TEMPERATURE, tokenizer=tokenizer)
    alphas = torch.cat((alphas, torch.tensor([alpha], device=device)))
             
    end_time = time.time_ns()
    new_tokens += len(tokens[0]) - start_len
    time_taken += (end_time - start_time) / 1_000_000_000
    tmp_new_tokens += len(tokens[0]) - start_len
    tmp_time_taken += (end_time - start_time) / 1_000_000_000

    # turn 2
    response = tokenizer.decode(tokens[0], skip_special_tokens=True)
    response += (" " + turns[1])
    inputs = tokenizer(response, return_tensors="pt").to(device)
    start_len = len(inputs.input_ids)
    start_time = time.time_ns()
    tokens, alpha = speculative_sampling(target_model, draft_model, prefix=inputs.input_ids,  
                                  target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), temperature=TEMPERATURE, tokenizer=tokenizer)
    alphas = torch.cat((alphas, torch.tensor([alpha], device=device)))

    end_time = time.time_ns()

    new_tokens += len(tokens[0]) - start_len
    time_taken += (end_time - start_time) / 1_000_000_000
    tmp_new_tokens += len(tokens[0]) - start_len
    tmp_time_taken += (end_time - start_time) / 1_000_000_000

    sub_result_sps[subtasks[i]][0]+= (tmp_new_tokens)
    sub_result_sps[subtasks[i]][1]+= (tmp_time_taken)
  else:
    text = texts[i]
    inputs = tokenizer(text, return_tensors="pt").to(device)
    start_len = len(inputs.input_ids)

    start_time = time.time_ns()
    tokens, alpha = speculative_sampling(target_model, draft_model, prefix=inputs.input_ids,  
                                  target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), temperature=TEMPERATURE, tokenizer=tokenizer)
                                  
    alphas = torch.cat((alphas, torch.tensor([alpha], device=device)))
   
    end_time = time.time_ns()

    new_tokens += len(tokens[0]) - start_len
    time_taken += (end_time - start_time) / 1_000_000_000
    sub_result_sps[subtasks[i]][0]+= (len(tokens[0]) - start_len)
    sub_result_sps[subtasks[i]][1]+= (((end_time - start_time) / 1_000_000_000))

overall_result_sps = new_tokens/time_taken
print(f"Throughput (Speculative Sampling): {new_tokens/time_taken:.2f} tok/s")
print(f"Average alpha: {alphas.mean().item():.2f}")

#%%
# print out all results
print("================")
print(f"Overall Result: AS: {round(overall_result_as, 2)} tokens/sec, SPS: {round(overall_result_sps,2)} \
  tokens/sec -> {round((overall_result_sps/overall_result_as), 2)} X Speedup")

print(f"Average alpha: {alphas.mean().item():.2f}")

if args.subtask_result:
  print("Subtask Result: ")
  for i in sub_result_as:
    AS = round((sub_result_as[i][0]/sub_result_as[i][1]),2)
    SPS = round((sub_result_sps[i][0]/sub_result_sps[i][1]),2)
    print(f"Subtask: {i}, AS: {AS} tokens/sec, SPS: {SPS} tokens/sec -> {(SPS/AS)} X Speedup")