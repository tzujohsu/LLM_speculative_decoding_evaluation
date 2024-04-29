### Accerlating LLM inference with speculative decoding and BiLD

To run the experiment:
```
python benchmark.py    \
 --target_model_name facebook/opt-6.7b     \
 --approx_model_name facebook/opt-125m     \
 --temperature 0     \
 --max_tokens 30    \
 --fallback_thres 0.6 \
 --rollback_thres 3

```