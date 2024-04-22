### A repo for eecs598 final project

run benchmark:

```bash
python benchmark.py \
    --target_model_name lmsys/vicuna-7b-v1.3 \
    --approx_model_name double7/vicuna-68m \
    --temperature 0 \
    --max_tokens 30
```

The speculative decoding code for this version is from this [repo](https://github.com/shreyansh26/Speculative-Sampling/tree/main)



lmsys/vicuna-7b-v1.3 and double7/vicuna-68m output:
```bash
Overall Result, AS: 569.57 tokens/sec, SPS: 730.66   tokens/sec -> 1.28 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 33.79 tokens/sec, SPS: 40.52 tokens/sec -> 1.1991713524711454 X Speedup
Subtask: translation, AS: 372.93 tokens/sec, SPS: 536.17 tokens/sec -> 1.437722897058429 X Speedup
Subtask: summarization, AS: 35497211.32 tokens/sec, SPS: 34471769.21 tokens/sec -> 0.9711120374849773 X Speedup
Subtask: qa, AS: 27.17 tokens/sec, SPS: 41.72 tokens/sec -> 1.5355171144644828 X Speedup
Subtask: math_reasoning, AS: 76179.33 tokens/sec, SPS: 57529.05 tokens/sec -> 0.7551792592557588 X Speedup
Subtask: rag, AS: 33191047.13 tokens/sec, SPS: 33233189.33 tokens/sec -> 1.0012696857629992 X Speedup
Subtask: law analytics, AS: 6515392.2 tokens/sec, SPS: 6310176.96 tokens/sec -> 0.9685030104557635 X Speedup
Subtask: grammar correction, AS: 52.63 tokens/sec, SPS: 70.34 tokens/sec -> 1.33650009500285 X Speedup
```

bloom7b and bloom650m output:
```bash
Overall Result: AS: 446.78 tokens/sec, SPS: 439.7   tokens/sec -> 0.98 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 32.96 tokens/sec, SPS: 37.61 tokens/sec -> 1.1410800970873787 X Speedup
Subtask: translation, AS: 265.52 tokens/sec, SPS: 158.35 tokens/sec -> 0.5963769207592649 X Speedup
Subtask: summarization, AS: 30019437.98 tokens/sec, SPS: 24928218.81 tokens/sec -> 0.8304025820406115 X Speedup
Subtask: qa, AS: 24.04 tokens/sec, SPS: 23.6 tokens/sec -> 0.9816971713810317 X Speedup
Subtask: math_reasoning, AS: 2926.31 tokens/sec, SPS: 3707.19 tokens/sec -> 1.2668480099510988 X Speedup
Subtask: rag, AS: 20601220.53 tokens/sec, SPS: 23683979.07 tokens/sec -> 1.1496396068141113 X Speedup
Subtask: law analytics, AS: 5662084.29 tokens/sec, SPS: 5381896.86 tokens/sec -> 0.9505151432494835 X Speedup
Subtask: grammar correction, AS: 42.67 tokens/sec, SPS: 43.71 tokens/sec -> 1.0243730958518866 X Speedup
```

facebook opt6.7b and opt125m:
```bash
Overall Result: AS: 474.44 tokens/sec, SPS: 663.45   tokens/sec -> 1.4 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 33.04 tokens/sec, SPS: 49.73 tokens/sec -> 1.5051452784503632 X Speedup
Subtask: translation, AS: 1080.62 tokens/sec, SPS: 1188.35 tokens/sec -> 1.099692768965964 X Speedup
Subtask: summarization, AS: 24450952.62 tokens/sec, SPS: 24090995.45 tokens/sec -> 0.9852783989403517 X Speedup
Subtask: qa, AS: 25.01 tokens/sec, SPS: 36.06 tokens/sec -> 1.4418232706917233 X Speedup
Subtask: math_reasoning, AS: 2962.89 tokens/sec, SPS: 3326.98 tokens/sec -> 1.1228834010037498 X Speedup
Subtask: rag, AS: 22118811.11 tokens/sec, SPS: 19199562.64 tokens/sec -> 0.8680196482766565 X Speedup
Subtask: law analytics, AS: 5782247.8 tokens/sec, SPS: 5413548.28 tokens/sec -> 0.936235953083851 X Speedup
Subtask: grammar correction, AS: 45.93 tokens/sec, SPS: 64.95 tokens/sec -> 1.4141084258654475 X Speedup
```
