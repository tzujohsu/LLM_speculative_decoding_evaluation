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
        sample_token_logits = model(fin_prompt_seq).logits[:, -1, :]
        sample_token = sample(sample_token_logits, temperature=temperature)
        fin_prompt_seq = torch.concat([fin_prompt_seq, sample_token[None,...]], dim=-1)
        out_logits.append(sample_token_logits)

    out_logits = torch.stack(out_logits, dim=1)
    return fin_prompt_seq, out_logits

    