import torch
import torch.nn as nn
from utils import sample_from_draft_model, get_distribution, sample
from transformers import AutoTokenizer, AutoModelForCausalLM
import numpy as np

crossentropy_loss = nn.CrossEntropyLoss(reduce=False)

def BiLD(target_model, draft_model, prefix, target_len, fallback_threshold, rollback_threshold, temperature=1.0):
    """
    implementation of Algorithm 1 from 
    https://arxiv.org/pdf/2302.07863
    referenced the official repository: https://github.com/kssteven418/BigLittleDecoder/blob/ad37f5641d403c955e7e7c90d946b0ebc3986eb1/src/transformers/models/t5/modeling_t5.py#L1885
    """
    assert prefix.shape[0] == 1, 'Batch size should be 1'

    n = prefix.shape[-1]
    fin_prompt_seq = prefix.detach().clone()
    init_n = fin_prompt_seq.shape[-1]
    
    while n < target_len:

        # pS ← SmallModel(y)
        draft_logits = draft_model(fin_prompt_seq).logits
        sample_token_logits = draft_logits[:, -1, :]
        # sample_token_prob = get_distribution(sample_token_logits, 0)
        sample_token_prob = torch.softmax(sample_token_logits, dim=-1)
        token_max_prob = sample_token_prob.max()
        
        # if max(pS[−1]) > αFB
        if token_max_prob > fallback_threshold:
            sample_token = sample(sample_token_logits, temperature=temperature)
            # y ← y + [sample(pS[−1])]
            fin_prompt_seq = torch.concat([fin_prompt_seq, sample_token[None,...]], dim=-1)
            n += 1
            # print("accept draft!!!")
        
        # Fallback to the large model
        else:
            # pL ← LargeModel(y)
            large_model_logits = target_model(fin_prompt_seq).logits
            
            if large_model_logits.shape[1] != 1:
                
                # m ← min. index such that d(pL[m], pS[m]) > αRB            
                large_prob = torch.softmax(large_model_logits, dim=-1)
                large_model_prediction = large_prob.argmax(-1)

                small_prob = torch.softmax(draft_logits, dim=-1)
                small_model_prediction = small_prob.argmax(-1)
                
                loss = crossentropy_loss(large_model_logits[0,init_n-1:], small_model_prediction[0,init_n-1:])
                # print("loss",loss)
                
                loss_above_thres = loss > rollback_threshold
                
                if loss_above_thres.any():
                    # roll back
                    # print("roll back")
                    # print("threshold", loss_above_thres)
                    # print("index", loss_above_thres.to(torch.int).argmax())
                    m = loss_above_thres.to(torch.int).argmax() + init_n - 1  # m
                    
                    # print("m", m)
                    fin_prompt_seq = torch.concat([fin_prompt_seq[:,:m+1], large_model_prediction[:,m:]], dim=-1)
                    n = fin_prompt_seq.shape[1]
                else:
                    # print("dont roll back")
                    fin_prompt_seq = torch.concat([fin_prompt_seq, large_model_prediction[:,-1:]], dim=-1)
                    n += 1
        
        # print("len of final seq", fin_prompt_seq.shape)
    return fin_prompt_seq


# device = "cuda" if torch.cuda.is_available() else "cpu"
# MAX_NEW_TOKENS = 15
# target_model_name = 'facebook/opt-2.7b'
# approx_model_name = 'facebook/opt-350m'
# target_model = AutoModelForCausalLM.from_pretrained(target_model_name).to(device)
# draft_model = AutoModelForCausalLM.from_pretrained(approx_model_name).to(device)
# tokenizer = AutoTokenizer.from_pretrained(target_model_name)
# print("finish loading models")
# inputs_sample = tokenizer("Give a another try", return_tensors="pt").to(device)
# # inputs_sample = tokenizer("How's your day?", return_tensors="pt").to(device)

# tokens = biLD(target_model, draft_model, prefix=inputs_sample.input_ids, 
#                               target_len=MAX_NEW_TOKENS+len(inputs_sample.input_ids), tokenizer=tokenizer, temperature=0)
# response = tokenizer.decode(tokens[0], skip_special_tokens=True)
# print("BiLD output", response)

