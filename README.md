# Reproducible figures
Functions to help implement a reproducible figure making process in Python. 

Thijs's tutorial/explainer slides available in repo!

# Installation

### Instructions
Clone from github, then install using pip:
    
```
git clone https://github.com/prajayshah/reproducible_figures.git
(optional) # activate or create new conda environment (python >=3.6)
cd reproducible_figures  # go to the directory where setup.py is located
pip install -e .
```

### Troubleshooting
There is a previously known install error with setuptools and setup.py:

`AttributeError: type object 'Distribution' has no attribute '_finalize_feature_opts'`

If you encounter this error,
please refer to: https://stackoverflow.com/questions/70520120/attributeerror-module-setuptools-distutils-has-no-attribute-version

# Usage instructions

```
#: python

import reproducible_figures as rfv

# access a given function as:
rfv.<func_name>
```
