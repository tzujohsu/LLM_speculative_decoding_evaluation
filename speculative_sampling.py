import torch
from utils import sample_from_draft_model, get_distribution, sample
from transformers import AutoTokenizer

def speculative_sampling(target_model, draft_model, prefix, target_len, tokenizer, gamma=4, temperature=1.0):
    '''
    Implementation of Algorithm 2 of the paper - Accelerating Large Language Model Decoding 
    with Speculative Sampling (https://arxiv.org/abs/2302.01318)
    '''
    assert prefix.shape[0] == 1, 'Batch size should be 1'

    n = prefix.shape[-1]
    fin_prompt_seq = prefix.detach().clone()

    while n < target_len:

        N = fin_prompt_seq.shape[-1]
        # sample gamma times from the draft model
        draft_outputs, draft_logits = sample_from_draft_model(draft_model, fin_prompt_seq, gamma=gamma, temperature=temperature)
        # run target model 
        target_logits = target_model(draft_outputs).logits[:, -gamma-1:, :]

        target_model_distribution = get_distribution(target_logits, temperature)
        draft_model_distribution = get_distribution(draft_logits, temperature)

        accepted_flag = 1
        for t in range(gamma):
            numerator = target_model_distribution[:, t, draft_outputs[0, N+t]]
            denominator = draft_model_distribution[:, t, draft_outputs[0, N+t]]
            ratio = (numerator / denominator)
            r = torch.rand_like(numerator) # uniform_distribution
            ones_tensor = torch.ones_like(numerator)
            
            # Rejection Sampling
            ## Acceptance
            if (r < torch.min(ones_tensor, ratio)).any():
                fin_prompt_seq = torch.concat([fin_prompt_seq, draft_outputs[:, N+t].unsqueeze(dim=-1)], dim=-1)
                n += 1

            ## Rejection
            else:
                new_dist = (target_model_distribution[:, t, :] - draft_model_distribution[:, t, :])
                new_dist = torch.max(torch.zeros_like(new_dist), new_dist)
                new_dist = new_dist / new_dist.sum(dim=-1, keepdim=True)
                token_id = torch.multinomial(new_dist, num_samples=1)[0]
                fin_prompt_seq = torch.concat([fin_prompt_seq, token_id[None,...]], dim=-1)
                accepted_flag = 0
                break
        
        # if none tokens from draft model get rejected
        if accepted_flag == 1:
            sample_token = sample(target_logits[:, -1, :], temperature=temperature)
            fin_prompt_seq = torch.concat([fin_prompt_seq, sample_token[None,...]], dim=-1)

        n += 1

    return fin_prompt_seq
