The research field of chem/bio-informatics with deep learning is quickly evolving, highly competitive and comprehensively interdiscplined, which is the major motivation to wrap up this tutorial.

## Quick Notebook Execution

Jupyter notebooks are runnable interactively, supported by [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MingyiXue/deep-learning-for-bioinformatics-101/develop?labpath=code). It may take some time to build the environment.


## Topic Plans
- [ ] Quick start
- [ ] Dataset
- [ ] Data representations
- [ ] Discriminative models
- [ ] Generative models
- [ ] Useful packages
- [x] Resources

## Compiling Document Environment
The web pages are available [here](https://mingyixue.github.io/deep-learning-for-bioinformatics-101/), but you can also compile this documentation locally:
```bash
conda create -n sphinx python=3.10
conda activate sphinx
python -m pip install -U sphinx
pip install nbsphinx furo IPython pandoc
make html
```

