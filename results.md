### Experiment Results

#### Vicuna
Configuration:
* Target: lmsys/vicuna-7b-v1.3
* Approx: double7/vicuna-68m
* Temperature: 0
* max token length: 30
* gamma: 4

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

#### Bloom
Configuration:
* Target: bigscience/bloom-7b1
* Approx: bigscience/bloom-560m
* Temperature: 0
* max token length: 30
* gamma: 4

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


#### facebook/opt

Configuration:
* Target: facebook/opt-6.7b
* Approx: facebook/opt-125m
* Temperature: 0
* max token length: 30
* gamma: 4

```bash
Overall Result: AS: 492.17 tokens/sec, SPS: 811.33   tokens/sec -> 1.65 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 34.23 tokens/sec, SPS: 61.06 tokens/sec -> 1.7838153666374528 X Speedup
Subtask: translation, AS: 1122.54 tokens/sec, SPS: 1444.76 tokens/sec -> 1.2870454504961961 X Speedup
Subtask: summarization, AS: 33900131.68 tokens/sec, SPS: 33355023.42 tokens/sec -> 0.9839201727844145 X Speedup
Subtask: qa, AS: 25.97 tokens/sec, SPS: 43.94 tokens/sec -> 1.6919522525991528 X Speedup
Subtask: math_reasoning, AS: 3076.08 tokens/sec, SPS: 4069.54 tokens/sec -> 1.3229629918597696 X Speedup
Subtask: rag, AS: 32224956.63 tokens/sec, SPS: 30636222.54 tokens/sec -> 0.9506986430349154 X Speedup
Subtask: law analytics, AS: 6951608.08 tokens/sec, SPS: 6746547.05 tokens/sec -> 0.9705016411109298 X Speedup
Subtask: grammar correction, AS: 47.76 tokens/sec, SPS: 79.12 tokens/sec -> 1.6566164154103855 X Speedup
```

Configuration:
* Target: facebook/opt-6.7b
* Approx: facebook/opt-350m
* Temperature: 0
* max token length: 30
* gamma: 4

``` bash
Overall Result: AS: 492.5 tokens/sec, SPS: 701.39   tokens/sec -> 1.42 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 34.26 tokens/sec, SPS: 53.03 tokens/sec -> 1.5478692352597783 X Speedup
Subtask: translation, AS: 1123.66 tokens/sec, SPS: 1300.74 tokens/sec -> 1.1575921542103482 X Speedup
Subtask: summarization, AS: 34174197.28 tokens/sec, SPS: 33638012.56 tokens/sec -> 0.9843102468331043 X Speedup
Subtask: qa, AS: 25.98 tokens/sec, SPS: 38.53 tokens/sec -> 1.48306389530408 X Speedup
Subtask: math_reasoning, AS: 3078.13 tokens/sec, SPS: 3931.7 tokens/sec -> 1.2773014784950603 X Speedup
Subtask: rag, AS: 32307189.99 tokens/sec, SPS: 31421962.0 tokens/sec -> 0.9725996600052805 X Speedup
Subtask: law analytics, AS: 6936629.69 tokens/sec, SPS: 6776716.91 tokens/sec -> 0.9769466171402326 X Speedup
Subtask: grammar correction, AS: 47.77 tokens/sec, SPS: 65.23 tokens/sec -> 1.3655013606866233 X Speedup
```


Configuration:
* Target: facebook/opt-6.7b
* Approx: facebook/opt-1.3b
* Temperature: 0
* max token length: 30
* gamma: 4

``` bash
Overall Result: AS: 474.81 tokens/sec, SPS: 621.57   tokens/sec -> 1.31 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 33.08 tokens/sec, SPS: 48.43 tokens/sec -> 1.4640266021765418 X Speedup
Subtask: translation, AS: 1075.96 tokens/sec, SPS: 955.18 tokens/sec -> 0.8877467563849957 X Speedup
Subtask: summarization, AS: 21753786.36 tokens/sec, SPS: 20664999.06 tokens/sec -> 0.949949526855609 X Speedup
Subtask: qa, AS: 24.99 tokens/sec, SPS: 32.73 tokens/sec -> 1.3097238895558223 X Speedup
Subtask: math_reasoning, AS: 2937.73 tokens/sec, SPS: 3314.69 tokens/sec -> 1.1283167615812209 X Speedup
Subtask: rag, AS: 21447475.16 tokens/sec, SPS: 17603160.15 tokens/sec -> 0.8207567566195516 X Speedup
Subtask: law analytics, AS: 5761456.25 tokens/sec, SPS: 5475745.57 tokens/sec -> 0.9504099887940658 X Speedup
Subtask: grammar correction, AS: 46.13 tokens/sec, SPS: 57.96 tokens/sec -> 1.2564491654021244 X Speedup
```


Configuration:
* Target: facebook/opt-6.7b
* Approx: facebook/opt-2.7b
* Temperature: 0
* max token length: 30
* gamma: 4

``` bash
Overall Result: AS: 474.85 tokens/sec, SPS: 477.04   tokens/sec -> 1.0 X Speedup
Subtask Result: 
Subtask: multi-turn, AS: 33.1 tokens/sec, SPS: 36.57 tokens/sec -> 1.104833836858006 X Speedup
Subtask: translation, AS: 1089.11 tokens/sec, SPS: 856.4 tokens/sec -> 0.7863301227607864 X Speedup
Subtask: summarization, AS: 26269350.63 tokens/sec, SPS: 23055751.14 tokens/sec -> 0.8776673418668363 X Speedup
Subtask: qa, AS: 25.04 tokens/sec, SPS: 26.09 tokens/sec -> 1.0419329073482428 X Speedup
Subtask: math_reasoning, AS: 2954.0 tokens/sec, SPS: 2565.47 tokens/sec -> 0.8684732566012187 X Speedup
Subtask: rag, AS: 23609351.96 tokens/sec, SPS: 20427560.78 tokens/sec -> 0.8652317443786374 X Speedup
Subtask: law analytics, AS: 5607242.59 tokens/sec, SPS: 5359088.05 tokens/sec -> 0.9557439265348425 X Speedup
Subtask: grammar correction, AS: 45.83 tokens/sec, SPS: 45.0 tokens/sec -> 0.9818895919703251 X Speedup
```