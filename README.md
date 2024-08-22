The research field of chem/bio-informatics with deep learning is quickly evolving, highly competitive and comprehensively interdiscplined, which is the major motivation to wrap up this tutorial.

## Document WebPage
The tutorial document is still under development. A stable (but not complete) version built upon `source/` is available [here](https://mingyixue.github.io/deep-learning-for-bioinformatics-101/), supported by `sphinx`.

## Quick Notebook Preview
Preview of executed notebooks under `code/` is available [here](https://nbviewer.org/github/MingyiXue/deep-learning-for-bioinformatics-101/tree/develop/code/), supported by `nbviewer`.

## Quick Notebook Execution
Jupyter notebooks are runnable interactively, supported by [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MingyiXue/deep-learning-for-bioinformatics-101/develop?labpath=code). It may take some time to build the environment.


## Topic Plans
- [ ] Quick start
    - [ ] Tutorials
    - [x] Notebooks
- [ ] Dataset
- [ ] Data representations
- [ ] Discriminative models
    - [ ] Tutorials
    - [x] Notebooks
- [ ] Generative models
    - [ ] Tutorials
    - [ ] Notebooks
- [ ] Useful packages
- [x] Resources
- [ ] Set up notebooks in Colab, Binder and nbviewer

## Compiling Document Environment
The web pages are available [here](https://mingyixue.github.io/deep-learning-for-bioinformatics-101/), but you can also compile this documentation locally:
```bash
conda create -n sphinx python=3.10
conda activate sphinx
python -m pip install -U sphinx
pip install nbsphinx furo
make html
```

