# Tagger Comparison - Report
## Practical 03  
## Santiago Arróniz

#### POS Tagger 1: UDPipe

To train the tagger for the Finnish treebank using UDPipe, a trainable pipeline for tagging CoNLL-U files, the following commands were executed in the Terminal:   
```
# Train UDPipe for the UD_Finnish-TDT treebank
$ cat fi_tdt-ud-train.conllu | udpipe --tokenizer=none --parser=none --train fi.udpipe

# Use the output from previous command for tagging
$ cat fi_tdt-ud-test.conllu | udpipe --tag fi.udpipe > fi_tdt-ud-test_output.conllu

# Use the script to evaluate the tagger performance
$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu fi_tdt-ud-test_output.conllu
```

The first command outputs a model file named `fi.udpipe`, which will be used in the second command for tagging. The final command uses a python script to evaluate the tagger performance, which produces the following data:

    Metrics    | Precision |    Recall |  F1 Score | AligndAcc  
    -----------+-----------+-----------+-----------+------------
    Tokens     |    100.00 |    100.00 |    100.00 |
    Sentences  |    100.00 |    100.00 |    100.00 |
    Words      |    100.00 |    100.00 |    100.00 |
    UPOS       |     94.74 |     94.74 |     94.74 |     94.74
    XPOS       |     95.89 |     95.89 |     95.89 |     95.89
    Feats      |     91.00 |     91.00 |     91.00 |     91.00
    AllTags    |     89.98 |     89.98 |     89.98 |     89.98
    Lemmas     |     84.97 |     84.97 |     84.97 |     84.97
    UAS        |    100.00 |    100.00 |    100.00 |    100.00
    LAS        |    100.00 |    100.00 |    100.00 |    100.00

Tokens, Sentences, Words, UAS, and LAS all got 100% of performance for F1 score. For Universal Part of Speech (UPOS), this tagger got a 94.74% of performance, and for XPOS a 95.89%. The lowest scores were found for Feat (91%), AllTags (89.98%), and Lemmas (84.97).

#### POS Tagger 2: Simple Perceptron-based tagger

To train the tagger for the Finnish treebank using a [simple Perceptron-based tagger](https://github.com/ftyers/conllu-perceptron-tagger), the following commands were executed in the Terminal:

```
# Train UDPipe for the UD_Finnish-TDT treebank
$ cat fi_tdt-ud-train.conllu | python3 tagger.py -t model.dat

# Use the output from previous command for tagging
$ cat fi_tdt-ud-test.conllu | python3 tagger.py model.dat > PerceptronOutput.txt

# Use the script to evaluate the tagger performance
$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu PerceptronOutput.txt > PerceptronOutputTable.txt
```

The first command outputs a model file named `model.dat`, which will be used in the second command for tagging. The final command uses a python script to evaluate the tagger performance, which produces the following data:

    Metrics    | Precision |    Recall |  F1 Score | AligndAcc
    -----------+-----------+-----------+-----------+-----------
    Tokens     |    100.00 |    100.00 |    100.00 |
    Sentences  |    100.00 |    100.00 |    100.00 |
    Words      |    100.00 |    100.00 |    100.00 |
    UPOS       |     90.73 |     90.73 |     90.73 |     90.73
    XPOS       |    100.00 |    100.00 |    100.00 |    100.00
    Feats      |    100.00 |    100.00 |    100.00 |    100.00
    AllTags    |     90.73 |     90.73 |     90.73 |     90.73
    Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
    UAS        |    100.00 |    100.00 |    100.00 |    100.00
    LAS        |    100.00 |    100.00 |    100.00 |    100.00

In this case, the performance test scored higher than with the first tagger in general. However, F1 score for UPOS (90.73%) was lower than with UDPipe (94.74%).

#### POS Tagger 3: Hunpos

I also tried with hunpos, but I had some issues running it, so I couldn't get any analysis done with this method. 
