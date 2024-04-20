### A repo for eecs598 final project

run benchmark:

```bash
python benchmark.py \
    --target_model_name lmsys/vicuna-7b-v1.3 \
    --approx_model_name double7/vicuna-68m \
    --temperature 0 \
    --max_tokens 30
```

The speculative decoding code for this version takes from this [repo](https://github.com/shreyansh26/Speculative-Sampling/tree/main)