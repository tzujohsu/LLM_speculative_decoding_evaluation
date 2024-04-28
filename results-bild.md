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

* Target: facebook/opt-6.7b
* Approx:  facebook/opt-350m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.6
* rollback_thres: 3

```bash

Overall Result: AS: 482.26 tokens/sec, SPS: 553.63         tokens/sec -> 1.15 X Speedup
Overall Result: AS: 482.26 tokens/sec, BiLD: 431.47         tokens/sec -> 0.89 X Speedup
==================
Subtask Result: 
Subtask: multi-turn, AS: 33.58 tokens/sec, SPS: 41.92 tokens/sec -> 1.2483621203097082 X Speedup
Subtask: multi-turn, AS: 33.58 tokens/sec, BiLD: 28.92 tokens/sec -> 0.8612269207861823 X Speedup

Subtask: translation, AS: 1099.8 tokens/sec, SPS: 1021.2 tokens/sec -> 0.9285324604473542 X Speedup
Subtask: translation, AS: 1099.8 tokens/sec, BiLD: 1245.53 tokens/sec -> 1.1325059101654846 X Speedup

Subtask: summarization, AS: 30088726.85 tokens/sec, SPS: 28878492.11 tokens/sec -> 0.9597778016320421 X Speedup
Subtask: summarization, AS: 30088726.85 tokens/sec, BiLD: 25842467.12 tokens/sec -> 0.8588753937257402 X Speedup

Subtask: qa, AS: 25.43 tokens/sec, SPS: 30.24 tokens/sec -> 1.1891466771529688 X Speedup
Subtask: qa, AS: 25.43 tokens/sec, BiLD: 23.8 tokens/sec -> 0.9359024773889107 X Speedup

Subtask: math_reasoning, AS: 3016.16 tokens/sec, SPS: 3184.25 tokens/sec -> 1.055729802132513 X Speedup
Subtask: math_reasoning, AS: 3016.16 tokens/sec, BiLD: 2630.5 tokens/sec -> 0.8721354304811416 X Speedup

Subtask: rag, AS: 28487564.8 tokens/sec, SPS: 27260241.19 tokens/sec -> 0.9569172156828232 X Speedup
Subtask: rag, AS: 28487564.8 tokens/sec, BiLD: 26577721.36 tokens/sec -> 0.9329586978245329 X Speedup

Subtask: law analytics, AS: 5797205.68 tokens/sec, SPS: 5598722.43 tokens/sec -> 0.9657622549628082 X Speedup
Subtask: law analytics, AS: 5797205.68 tokens/sec, BiLD: 5416399.61 tokens/sec -> 0.9343121339796936 X Speedup

Subtask: grammar correction, AS: 46.69 tokens/sec, SPS: 51.8 tokens/sec -> 1.1094452773613193 X Speedup
Subtask: grammar correction, AS: 46.69 tokens/sec, BiLD: 42.45 tokens/sec -> 0.9091882630113516 X Speedup
```

* Target: facebook/opt-6.7b
* Approx:  facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.6
* rollback_thres: 4


```bash
Overall Result: AS: 479.62 tokens/sec, SPS: 684.58         tokens/sec -> 1.43 X Speedup
Overall Result: AS: 479.62 tokens/sec, BiLD: 503.65         tokens/sec -> 1.05 X Speedup
==================
Subtask Result: 
Subtask: multi-turn, AS: 33.39 tokens/sec, SPS: 51.65 tokens/sec -> 1.546870320455226 X Speedup
Subtask: multi-turn, AS: 33.39 tokens/sec, BiLD: 33.57 tokens/sec -> 1.005390835579515 X Speedup

Subtask: translation, AS: 1095.96 tokens/sec, SPS: 1219.8 tokens/sec -> 1.1129968247016313 X Speedup
Subtask: translation, AS: 1095.96 tokens/sec, BiLD: 1325.88 tokens/sec -> 1.2097886784189205 X Speedup

Subtask: summarization, AS: 30672623.76 tokens/sec, SPS: 29632325.46 tokens/sec -> 0.9660838176694669 X Speedup
Subtask: summarization, AS: 30672623.76 tokens/sec, BiLD: 28689359.99 tokens/sec -> 0.9353409155500297 X Speedup

Subtask: qa, AS: 25.26 tokens/sec, SPS: 36.91 tokens/sec -> 1.4612034837688042 X Speedup
Subtask: qa, AS: 25.26 tokens/sec, BiLD: 28.0 tokens/sec -> 1.1084718923198733 X Speedup

Subtask: math_reasoning, AS: 2994.44 tokens/sec, SPS: 3422.26 tokens/sec -> 1.1428714550967793 X Speedup
Subtask: math_reasoning, AS: 2994.44 tokens/sec, BiLD: 3138.39 tokens/sec -> 1.0480724275657551 X Speedup

Subtask: rag, AS: 29141830.49 tokens/sec, SPS: 24229750.08 tokens/sec -> 0.8314422832263204 X Speedup
Subtask: rag, AS: 29141830.49 tokens/sec, BiLD: 26685039.37 tokens/sec -> 0.9156953740142355 X Speedup

Subtask: law analytics, AS: 5891315.1 tokens/sec, SPS: 5732409.86 tokens/sec -> 0.9730272040617893 X Speedup
Subtask: law analytics, AS: 5891315.1 tokens/sec, BiLD: 5458870.16 tokens/sec -> 0.9265961958137328 X Speedup

Subtask: grammar correction, AS: 46.58 tokens/sec, SPS: 66.85 tokens/sec -> 1.4351653069987118 X Speedup
Subtask: grammar correction, AS: 46.58 tokens/sec, BiLD: 49.94 tokens/sec -> 1.0721339630742808 X Speedup

```