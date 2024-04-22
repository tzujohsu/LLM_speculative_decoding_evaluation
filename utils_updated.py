import torch
import json

def load_data(jsonl_file):
    texts, subtasks = [], []
    multi = ['writing', 'roleplay', 'reasoning', 'math', 'coding', 'extraction', 'stem', 'humanities']
    with open(jsonl_file, 'r') as file:
        for line in file.readlines():
            data = json.loads(line)
            category = data['category']

            # multi-turn conversation
            if category in multi:
                category = 'multi-turn'
                texts.append(data['turns'])
                subtasks.append(category)

            # add prompt to grammar correction task
            elif category == 'grammar correction':
                t = 'Please correct the grammar for the following sentence : ' + data['turns'][0]
                texts.append(t)
                subtasks.append(data['category'])
            else:
                texts.append(data['turns'][0])
                subtasks.append(data['category'])
    return texts, subtasks

def check_function(target_model, draft_model, tokenizer, inputs_sample, MAX_NEW_TOKENS, AS, SPS):
    """
    check if all functions work
    """
    tokens = target_model.generate(**inputs_sample, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)
    print("HF's generate")
    print("Count of new tokens:", len(tokens[0]) - len(inputs_sample.input_ids))
    print(tokenizer.decode(tokens[0]))
    print("******")

    tokens = AS(target_model, initial_prompt_seq=inputs_sample.input_ids, target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), temperature=TEMPERATURE)
    print("Naive Autoregressive with temperature")
    print("Count of new tokens:", len(tokens[0]) - len(inputs_sample.input_ids))
    print(tokenizer.decode(tokens[0]))
    print("******")

    tokens = SPS(target_model, draft_model, prefix=inputs_sample.input_ids, target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), tokenizer=tokenizer, temperature=TEMPERATURE, debug=False)
    print("Speculative Sampling with temperature")
    print("Count of new tokens:", len(tokens[0]) - len(inputs_sample.input_ids))
    print(tokenizer.decode(tokens[0]))
    print("******")
    print()

def get_distribution(logits, temperature):
    probs = torch.softmax(logits / (temperature + 1e-10), dim=-1)
    return probs

def sample(logits, temperature):
    probs = get_distribution(logits, temperature)
    return torch.multinomial(probs, num_samples=1)[0]

def sample_from_draft_model(model, initial_prompt_seq, gamma, temperature=1.0):
    fin_prompt_seq = initial_prompt_seq.detach().clone()
    out_logits = []

    for _ in range(gamma):
        if hasattr(model.config, "is_encoder_decoder") and model.config.is_encoder_decoder:
            sample_token_logits = model(input_ids=fin_prompt_seq, decoder_input_ids=fin_prompt_seq).logits[:, -1, :]
        else:
            sample_token_logits = model(fin_prompt_seq).logits[:, -1, :]

        sample_token = sample(sample_token_logits, temperature=temperature)
        fin_prompt_seq = torch.concat([fin_prompt_seq, sample_token[None, ...]], dim=-1)
        out_logits.append(sample_token_logits)

    out_logits = torch.stack(out_logits, dim=1)
    return fin_prompt_seq, out_logits