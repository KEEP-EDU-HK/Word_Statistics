# Word_Statistics
[![Build Status](https://api.travis-ci.com/FlyingTwigs/Word_Statistics.svg?branch=master)](https://travis-ci.com/github/FlyingTwigs/Word_Statistics)

Produce a word statistics in form of JSON

# Installation

```pip install -r requirements.txt```

# Help

```
python3 lib/main.py -h
```

As this program may cause error from not having the language library from SpaCy, please download it first by executing
``` 
python -m spacy download en_core_web_sm

sudo apt-get install libopencc-dev
sudo apt-get install libhunspell-dev

git clone https://github.com/KEEP-EDU-HK/vgnlp.git
pip install -e ./vgnlp/vglib
```
before using this program


In Python scripts:

```
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from vglib.vglib2 import Vglib
```

```
python3 lib/main.py pdf_concept_category/001.txt
```

## Key Phrases

```
cd Word_Statistics
git clone https://github.com/kenchan0226/keyphrase-generation-rl.git keyphrase_generation_rl
```

edit `keyphrase_generation_rl/interactive_predict.py`, replace the import statement as the following:

```
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) + "/keyphrase_generation_rl" )

import torch
from sequence_generator import SequenceGenerator
import config
import argparse
from preprocess import *
from keyphrase_generation_rl.preprocess import read_tokenized_src_file
from utils.data_loader import load_vocab
```

edit `keyphrase_generation_rl/preprocess.py`, comment this function:

```
# def read_tokenized_src_file(path, remove_eos=True):
#   ....
#   ....
```

**Datasets**

Visit and follow the instruction mentioned in [this page](https://github.com/kenchan0226/keyphrase-generation-rl#dataset):

Download pre-trained model, and put it under `keyphrase_generation_rl/model/`

Place training data under `keyphrase_generation_rl/data/`
