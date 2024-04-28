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

* Target: facebook/opt-6.7b
* Approx:  facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.6
* rollback_thres: 5

```bash
Overall Result: AS: 481.88 tokens/sec, SPS: 691.95         tokens/sec -> 1.44 X Speedup
Overall Result: AS: 481.88 tokens/sec, BiLD: 503.87         tokens/sec -> 1.05 X Speedup
==================
Subtask Result: 
Subtask: multi-turn, AS: 33.54 tokens/sec, SPS: 52.11 tokens/sec -> 1.5536672629695887 X Speedup
Subtask: multi-turn, AS: 33.54 tokens/sec, BiLD: 33.66 tokens/sec -> 1.003577817531306 X Speedup

Subtask: translation, AS: 1095.82 tokens/sec, SPS: 1238.1 tokens/sec -> 1.1298388421456078 X Speedup
Subtask: translation, AS: 1095.82 tokens/sec, BiLD: 1338.61 tokens/sec -> 1.2215601102370828 X Speedup

Subtask: summarization, AS: 30341139.51 tokens/sec, SPS: 29283168.98 tokens/sec -> 0.9651308241191366 X Speedup
Subtask: summarization, AS: 30341139.51 tokens/sec, BiLD: 28547780.15 tokens/sec -> 0.9408934737138354 X Speedup

Subtask: qa, AS: 25.42 tokens/sec, SPS: 37.31 tokens/sec -> 1.467741935483871 X Speedup
Subtask: qa, AS: 25.42 tokens/sec, BiLD: 27.94 tokens/sec -> 1.099134539732494 X Speedup

Subtask: math_reasoning, AS: 3005.74 tokens/sec, SPS: 3538.17 tokens/sec -> 1.1771377431181673 X Speedup
Subtask: math_reasoning, AS: 3005.74 tokens/sec, BiLD: 3143.88 tokens/sec -> 1.0459587322922144 X Speedup

Subtask: rag, AS: 27261378.72 tokens/sec, SPS: 26815607.09 tokens/sec -> 0.9836482360419665 X Speedup
Subtask: rag, AS: 27261378.72 tokens/sec, BiLD: 27039116.06 tokens/sec -> 0.9918469765493945 X Speedup

Subtask: law analytics, AS: 5778198.56 tokens/sec, SPS: 5538794.29 tokens/sec -> 0.9585676629984139 X Speedup
Subtask: law analytics, AS: 5778198.56 tokens/sec, BiLD: 5494626.5 tokens/sec -> 0.9509237944914098 X Speedup

Subtask: grammar correction, AS: 46.7 tokens/sec, SPS: 67.85 tokens/sec -> 1.4528907922912204 X Speedup
Subtask: grammar correction, AS: 46.7 tokens/sec, BiLD: 49.84 tokens/sec -> 1.067237687366167 X Speedup

```

* Target: facebook/opt-6.7b
* Approx:  facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.5
* rollback_thres: 5


```bash
Overall Result: AS: 482.34 tokens/sec, SPS: 693.16         tokens/sec -> 1.44 X Speedup
Overall Result: AS: 482.34 tokens/sec, BiLD: 542.1         tokens/sec -> 1.12 X Speedup
==================
Subtask Result: 
Subtask: multi-turn, AS: 33.59 tokens/sec, SPS: 52.07 tokens/sec -> 1.5501637392080976 X Speedup
Subtask: multi-turn, AS: 33.59 tokens/sec, BiLD: 36.06 tokens/sec -> 1.0735337898183983 X Speedup

Subtask: translation, AS: 1099.6 tokens/sec, SPS: 1240.81 tokens/sec -> 1.128419425245544 X Speedup
Subtask: translation, AS: 1099.6 tokens/sec, BiLD: 1422.04 tokens/sec -> 1.293233903237541 X Speedup

Subtask: summarization, AS: 31054392.8 tokens/sec, SPS: 29943483.72 tokens/sec -> 0.9642269907785799 X Speedup
Subtask: summarization, AS: 31054392.8 tokens/sec, BiLD: 28742160.38 tokens/sec -> 0.9255425010274231 X Speedup

Subtask: qa, AS: 25.43 tokens/sec, SPS: 37.55 tokens/sec -> 1.4766024380652771 X Speedup
Subtask: qa, AS: 25.43 tokens/sec, BiLD: 30.21 tokens/sec -> 1.1879669681478568 X Speedup

Subtask: math_reasoning, AS: 3020.62 tokens/sec, SPS: 3516.11 tokens/sec -> 1.1640358601876437 X Speedup
Subtask: math_reasoning, AS: 3020.62 tokens/sec, BiLD: 3243.13 tokens/sec -> 1.0736636849388537 X Speedup

Subtask: rag, AS: 29282270.09 tokens/sec, SPS: 28331071.86 tokens/sec -> 0.9675162401317773 X Speedup
Subtask: rag, AS: 29282270.09 tokens/sec, BiLD: 26902016.31 tokens/sec -> 0.9187134818207668 X Speedup

Subtask: law analytics, AS: 5990492.04 tokens/sec, SPS: 5741301.21 tokens/sec -> 0.9584022767518776 X Speedup
Subtask: law analytics, AS: 5990492.04 tokens/sec, BiLD: 5541275.07 tokens/sec -> 0.9250116739993198 X Speedup

Subtask: grammar correction, AS: 46.71 tokens/sec, SPS: 67.86 tokens/sec -> 1.4527938342967244 X Speedup
Subtask: grammar correction, AS: 46.71 tokens/sec, BiLD: 53.98 tokens/sec -> 1.155641190323271 X Speedup
```


* Target: facebook/opt-6.7b
* Approx:  facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.7
* rollback_thres: 5

```bash
Overall Result: AS: 481.34 tokens/sec, SPS: 693.58         tokens/sec -> 1.44 X Speedup
Overall Result: AS: 481.34 tokens/sec, BiLD: 480.57         tokens/sec -> 1.0 X Speedup
==================
Subtask Result: 
Subtask: multi-turn, AS: 33.49 tokens/sec, SPS: 52.13 tokens/sec -> 1.5565840549417735 X Speedup
Subtask: multi-turn, AS: 33.49 tokens/sec, BiLD: 32.19 tokens/sec -> 0.9611824425201552 X Speedup

Subtask: translation, AS: 1096.19 tokens/sec, SPS: 1253.63 tokens/sec -> 1.1436247365876353 X Speedup
Subtask: translation, AS: 1096.19 tokens/sec, BiLD: 1311.78 tokens/sec -> 1.1966721097619937 X Speedup

Subtask: summarization, AS: 30039393.27 tokens/sec, SPS: 27723156.6 tokens/sec -> 0.9228933604223892 X Speedup
Subtask: summarization, AS: 30039393.27 tokens/sec, BiLD: 28550229.61 tokens/sec -> 0.9504263069957805 X Speedup

Subtask: qa, AS: 25.4 tokens/sec, SPS: 37.55 tokens/sec -> 1.4783464566929134 X Speedup
Subtask: qa, AS: 25.4 tokens/sec, BiLD: 26.43 tokens/sec -> 1.0405511811023622 X Speedup

Subtask: math_reasoning, AS: 3013.96 tokens/sec, SPS: 3455.77 tokens/sec -> 1.1465878777422394 X Speedup
Subtask: math_reasoning, AS: 3013.96 tokens/sec, BiLD: 3004.48 tokens/sec -> 0.9968546364251683 X Speedup

Subtask: rag, AS: 27587161.27 tokens/sec, SPS: 23496754.16 tokens/sec -> 0.8517278718906043 X Speedup
Subtask: rag, AS: 27587161.27 tokens/sec, BiLD: 26585748.4 tokens/sec -> 0.9637000392973016 X Speedup

Subtask: law analytics, AS: 5849030.38 tokens/sec, SPS: 5660952.23 tokens/sec -> 0.9678445592207713 X Speedup
Subtask: law analytics, AS: 5849030.38 tokens/sec, BiLD: 5525266.8 tokens/sec -> 0.9446466236340526 X Speedup

Subtask: grammar correction, AS: 46.68 tokens/sec, SPS: 67.85 tokens/sec -> 1.4535132819194514 X Speedup
Subtask: grammar correction, AS: 46.68 tokens/sec, BiLD: 47.76 tokens/sec -> 1.0231362467866323 X Speedup

```

* Target: facebook/opt-6.7b
* Approx:  facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4
* fallback_thres: 0.5
* rollback_thres: 5

```bash
Overall Result: AS: 481.83 tokens/sec, SPS: 693.89         tokens/sec -> 1.44 X Speedup
Overall Result: AS: 481.83 tokens/sec, BiLD: 541.93         tokens/sec -> 1.12 X Speedup
==================
Subtask Result: 
Subtask: multi-turn, AS: 33.54 tokens/sec, SPS: 52.16 tokens/sec -> 1.5551580202742994 X Speedup
Subtask: multi-turn, AS: 33.54 tokens/sec, BiLD: 36.03 tokens/sec -> 1.0742397137745976 X Speedup

Subtask: translation, AS: 1099.68 tokens/sec, SPS: 1244.36 tokens/sec -> 1.1315655463407535 X Speedup
Subtask: translation, AS: 1099.68 tokens/sec, BiLD: 1425.18 tokens/sec -> 1.29599519860323 X Speedup

Subtask: summarization, AS: 29230486.44 tokens/sec, SPS: 28714933.76 tokens/sec -> 0.982362500841091 X Speedup
Subtask: summarization, AS: 29230486.44 tokens/sec, BiLD: 28247963.78 tokens/sec -> 0.966387057498452 X Speedup

Subtask: qa, AS: 25.4 tokens/sec, SPS: 37.55 tokens/sec -> 1.4783464566929134 X Speedup
Subtask: qa, AS: 25.4 tokens/sec, BiLD: 30.22 tokens/sec -> 1.189763779527559 X Speedup

Subtask: math_reasoning, AS: 3018.23 tokens/sec, SPS: 3532.34 tokens/sec -> 1.1703349314001916 X Speedup
Subtask: math_reasoning, AS: 3018.23 tokens/sec, BiLD: 3291.92 tokens/sec -> 1.0906789741007146 X Speedup

Subtask: rag, AS: 28636023.49 tokens/sec, SPS: 27101945.18 tokens/sec -> 0.9464283750662618 X Speedup
Subtask: rag, AS: 28636023.49 tokens/sec, BiLD: 26305155.13 tokens/sec -> 0.9186036301159635 X Speedup

Subtask: law analytics, AS: 5813043.98 tokens/sec, SPS: 5573239.52 tokens/sec -> 0.95874717947687 X Speedup
Subtask: law analytics, AS: 5813043.98 tokens/sec, BiLD: 5363619.52 tokens/sec -> 0.9226868983709288 X Speedup

Subtask: grammar correction, AS: 46.72 tokens/sec, SPS: 67.92 tokens/sec -> 1.4537671232876712 X Speedup
Subtask: grammar correction, AS: 46.72 tokens/sec, BiLD: 53.95 tokens/sec -> 1.1547517123287672 X Speedup
```

