import torch
from utils_updated import sample

torch.backends.cudnn.benchmark =  True
torch.backends.cudnn.enabled =  True

def autoregressive_sampling(model, initial_prompt_seq, target_len, temperature=1.0):
    fin_prompt_seq = initial_prompt_seq.detach().clone()

    if hasattr(model.config, "is_encoder_decoder") and model.config.is_encoder_decoder:
        while len(fin_prompt_seq[0]) < target_len:
            sample_token_logits = model(input_ids=fin_prompt_seq, decoder_input_ids=fin_prompt_seq).logits[:, -1, :]
            sample_token = sample(sample_token_logits, temperature=temperature)
            fin_prompt_seq = torch.cat((fin_prompt_seq, sample_token.unsqueeze(0)), dim=-1)
    else:
        n = initial_prompt_seq.shape[-1]
        while n < target_len:
            sample_token_logits = model(fin_prompt_seq).logits[:, -1, :]
            sample_token = sample(sample_token_logits, temperature=temperature)
            fin_prompt_seq = torch.concat([fin_prompt_seq, sample_token[None,...]], dim=-1)
            n += 1

    return fin_prompt_seq