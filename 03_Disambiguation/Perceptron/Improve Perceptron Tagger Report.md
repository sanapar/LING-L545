# Improving Perceptron Tagger - Report
## Practical 03  
## Santiago Arróniz

### UD_Spanish-GSD

For this task, I used a Spanish data set obtained from [https://github.com/UniversalDependencies/UD_Spanish-GSD](https://github.com/UniversalDependencies/UD_Spanish-GSD).

First, I trained UDPipe tagger using the file `es_gsd-ud-train.conllu`. After that, I run the tagger with `es_gsd-ud-test.conllu`. It evaluated the output using the same python script as before (CoNLL-2017 evaluation script).

```
# Train UDPipe for the UD_Spanish-TDT treebank
$ cat ../UD_Spanish-GSD/es_gsd-ud-train.conllu | python3 tagger.py -t es-ud.dat

# Use the output from previous command for tagging
$ cat ../UD_Spanish-GSD/es_gsd-ud-test.conllu | python3 tagger.py es-ud.dat > es-ud-test.out

# Use the script to evaluate the tagger performance
$ python3 conll17_ud_eval.py --verbose ../UD_Spanish-GSD/es_gsd-ud-test.conllu es-ud-test.out > esPerceptronOutput.txt
```
These are the results for the analysis:


    Metrics    | Precision |    Recall |  F1 Score | AligndAcc
    -----------+-----------+-----------+-----------+-----------
    Tokens     |    100.00 |    100.00 |    100.00 |
    Sentences  |    100.00 |    100.00 |    100.00 |
    Words      |    100.00 |    100.00 |    100.00 |
    UPOS       |     94.69 |     94.69 |     94.69 |     94.69
    XPOS       |    100.00 |    100.00 |    100.00 |    100.00
    Feats      |    100.00 |    100.00 |    100.00 |    100.00
    AllTags    |     94.69 |     94.69 |     94.69 |     94.69
    Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
    UAS        |    100.00 |    100.00 |    100.00 |    100.00
    LAS        |    100.00 |    100.00 |    100.00 |    100.00

In order to improve the perceptron tagger, I modified pretty much all of the values included in the `_get_features()` part of the `tagger.py`file. However, when running it again, the F1 score for UPOS decreased.

```
def _get_features(self, i, word, context, prev, prev2):
  '''Map tokens into a feature representation, implemented as a
  {hashable: float} dict. If the features change, a new model must be
  trained.
  '''
  def add(name, *args):
    features[' '.join((name,) + tuple(args))] += 1

  i += len(self.START)
  features = defaultdict(int)
  # It's useful to have a constant feature, which acts sort of like a prior
  add('bias')
  add('i suffix', word[-3:]) # Changed this index to -1, -2, -4, -5, and -6
  add('i pref1', word[0]) # By increasing this index, it produces an index error
  add('i-1 tag', prev)
  add('i-2 tag', prev2)
  add('i tag+i-2 tag', prev, prev2)
  add('i word', context[i])
  add('i-1 tag+i word', prev, context[i])
  add('i-1 word', context[i-1]) # Changed this index to -2, -3
  add('i-1 suffix', context[i-1][-3:]) # Changed this index to [i-1][-5:]
  add('i-2 word', context[i-2]) # Changed this index to [i-3]
  add('i+1 word', context[i+1]) # Changed this index to [i+2]
  add('i+1 suffix', context[i+1][-3:]) # Changed this index to [i+1][-2:], [i+1][-4:]
  add('i+2 word', context[i+2]) # Changed this index to [i+1]
  #print(word, '|||', features)
  return features
```

The only success in improving the tagger was by changing `add('i suffix', word[-3:])` to `add('i suffix', word[-5:])`, and `add('i+1 word', context[i+1])` to `add('i+1 word', context[i+2])`, which increased the F1 score for UPOS very slightly:

    Metrics    | Precision |    Recall |  F1 Score | AligndAcc
    -----------+-----------+-----------+-----------+-----------
    Tokens     |    100.00 |    100.00 |    100.00 |
    Sentences  |    100.00 |    100.00 |    100.00 |
    Words      |    100.00 |    100.00 |    100.00 |
    UPOS       |     94.73 |     94.73 |     94.73 |     94.73
    XPOS       |    100.00 |    100.00 |    100.00 |    100.00
    Feats      |    100.00 |    100.00 |    100.00 |    100.00
    AllTags    |     94.73 |     94.73 |     94.73 |     94.73
    Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
    UAS        |    100.00 |    100.00 |    100.00 |    100.00
    LAS        |    100.00 |    100.00 |    100.00 |    100.00


All of the other changes performed didn't have any impact on the F1 scores for UPOS, so we could assume that the perceptron tagger is already pretty accurate for the dataset considered in this case.
