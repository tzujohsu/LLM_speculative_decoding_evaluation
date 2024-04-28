### Experiment results


#### OPT


* Target: facebook/opt-6.7b
* Approx:  facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.6
* rollback_thres: 3


```bash

Overall Result: AS: 483.03 tokens/sec, SPS: 692.54         tokens/sec -> 1.43 X Speedup
Overall Result: AS: 483.03 tokens/sec, BiLD: 504.7         tokens/sec -> 1.04 X Speedup

Subtask Result: 

Subtask: multi-turn, AS: 33.61 tokens/sec, SPS: 52.06 tokens/sec -> 1.5489437667360906 X Speedup
Subtask: multi-turn, AS: 33.61 tokens/sec, BiLD: 33.69 tokens/sec -> 1.0023802439750074 X Speedup
Subtask: translation, AS: 1102.45 tokens/sec, SPS: 1245.74 tokens/sec -> 1.1299741484874597 X Speedup
Subtask: translation, AS: 1102.45 tokens/sec, BiLD: 1345.61 tokens/sec -> 1.2205632908521926 X Speedup
Subtask: summarization, AS: 29904890.34 tokens/sec, SPS: 29010157.21 tokens/sec -> 0.9700807085454105 X Speedup
Subtask: summarization, AS: 29904890.34 tokens/sec, BiLD: 27836975.38 tokens/sec -> 0.9308502744370872 X Speedup
Subtask: qa, AS: 25.48 tokens/sec, SPS: 37.48 tokens/sec -> 1.4709576138147564 X Speedup
Subtask: qa, AS: 25.48 tokens/sec, BiLD: 27.98 tokens/sec -> 1.098116169544741 X Speedup
Subtask: math_reasoning, AS: 3017.37 tokens/sec, SPS: 3502.01 tokens/sec -> 1.1606166959968451 X Speedup
Subtask: math_reasoning, AS: 3017.37 tokens/sec, BiLD: 3126.1 tokens/sec -> 1.036034692463967 X Speedup
Subtask: rag, AS: 28625985.43 tokens/sec, SPS: 27242888.46 tokens/sec -> 0.9516838652286005 X Speedup
Subtask: rag, AS: 28625985.43 tokens/sec, BiLD: 25565287.33 tokens/sec -> 0.8930797296922958 X Speedup
Subtask: law analytics, AS: 5796073.78 tokens/sec, SPS: 5592614.91 tokens/sec -> 0.9648971221342872 X Speedup
Subtask: law analytics, AS: 5796073.78 tokens/sec, BiLD: 5290270.73 tokens/sec -> 0.9127335038857977 X Speedup
Subtask: grammar correction, AS: 46.81 tokens/sec, SPS: 67.77 tokens/sec -> 1.4477675710318307 X Speedup
Subtask: grammar correction, AS: 46.81 tokens/sec, BiLD: 50.04 tokens/sec -> 1.0690023499252297 X Speedup

```