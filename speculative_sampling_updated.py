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
    alpha = 0
    betas = []

    # Check if the models are T5 models
    is_t5 = hasattr(target_model.config, "is_encoder_decoder") and target_model.config.is_encoder_decoder

    while n < target_len:
        n_orig = n
        N = fin_prompt_seq.shape[-1]
        draft_outputs, draft_logits = sample_from_draft_model(draft_model, fin_prompt_seq, gamma=gamma, temperature=temperature, is_t5=is_t5)
        
        if is_t5:
            target_logits = target_model(input_ids=draft_outputs, decoder_input_ids=draft_outputs).logits[:, -gamma-1:, :]
        else:
            target_logits = target_model(draft_outputs).logits[:, -gamma-1:, :]

        target_model_distribution = get_distribution(target_logits, temperature)
        draft_model_distribution = get_distribution(draft_logits, temperature)

        p_probs = target_model_distribution[:, :gamma, :]
        q_probs = draft_model_distribution[:, :gamma, :]

        beta = (torch.minimum(p_probs, q_probs)).sum(dim=(1, 2)) / gamma
        betas.append(beta)

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

        if accepted_flag == 1:
            sample_token = sample(target_logits[:, -1, :], temperature=temperature)
            fin_prompt_seq = torch.concat([fin_prompt_seq, sample_token[None,...]], dim=-1)
            n += 1

    if len(betas) > 0:
        alpha = torch.stack(betas).mean()

    return fin_prompt_seq, alpha