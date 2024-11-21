### Accelerating LLM inference with SPS and BiLD

Speculative Decoding has emerged as a pivotal approach in enhancing the efficiency of Large Language Models (LLMs), addressing the critical challenge of inference latency primarily caused by memory-bound computation limitations. The motivation is to explore how Speculative Decoding can be effectively adapted across different model series and configurations.

This repo aims to implement two algorithms: 
(1) Deepmind's Algorithm: Speculative Sampling (SpS) with Auto-Regressive Target and Draft Models
(2) Big Little Decoder Algorithm(BiLD) with Fallback and Rollback Policies

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

This is a project repo for eecs598:llm course.
