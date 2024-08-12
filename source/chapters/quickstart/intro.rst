Brief Intro
------------
Lets start with an organic chemistry problem::

    How to predict the pKa of a small organic molecule?

One can always measure pKa experimentally, but this seems time-consuming if done on every molecule.
Basic **knowledge** about organic chemistry tells us that pKa values are related to functional groups such as amine and carboxylic acid.
It is easy for a chemistry student to determine whether an organic molecule is acidic or basic based on functional groups,
and easy for an organic chemistry expert to give an "OK" prediction of pKa values if they have quantitative estimations of these functional groups.

We make the **assumption** "pKa values are related to functional groups such as amine and carboxylic acid" based on our knowledge or experience.
In order to better solve this problem, we need to add more quantitative details to this assumption,
e.g., "the pKa value is a linear combination of the count of each functional group in an organic molecule". 

Under this quantitative assumption, we can **parameterize** the problem as :math:`y = \sum_{i=1}^{N} w_{i}*x_{i} + b`, 
where :math:`y\in \mathbb{R}` is the pKa value to predict, :math:`N\in \mathbb{N}` is the number of functional group categories,
:math:`x_{i}\in \mathbb{N}` is the count of :math:`i` th functional group in the molecule, :math:`w_{i}\in \mathbb{R}` is coefficients, 
and :math:`b\in \mathbb{R}` is the bias. Based on this assumption, 
we can predict pKa values of new organic molecules once we know the parameters.
We will later on refer to :math:`y` as the **target**, :math:`x_{i}` as **feature**, 
:math:`w_{i}` and :math:`b` as **parameters**, and this linear combination as **model**. 

.. _note_1:
.. note::
    Linear regression including bias and random distribution noise: :math:`y = \sum_{i=0}^{N} w_{i}*x_{i} + \mathcal{N} (\epsilon)`.

Instead of hard-coding parameters, parameters can be found by models using **data** 
that contains features and targets obtained from existing molecules in a **machine-learned** way.

Beyond the linear relationship, machine learning shows its power at capturing nonlinearities. 
For example, we can assume that the pKa value is a nonlinear combination of the count of each functional group in an organic molecule. 
This assumption is parameterized as :math:`y = f(\mathbf{\textit x}; \mathbf{\textit w})`, 
where :math:`f(\cdot ; \mathbf{\textit w})` is machine learning models. 
Various machine learning / deep learning models will be discussed in the following chapters.

In plain language, deep learning in the field of chem/bioinformatics is to 
represent molecules (e.g. small molecules, biomolecules) as :math:`\mathbf{\textit x}`, 
design models :math:`f`,
and optimize :math:`\mathbf{\textit w}`, such that the model trained on existing molecules can predict for new ones.



**Objective function**


**Backpropogation**


**Evaluation**


**Example**

Lets firstly work on the previously mentioned linear assumption: :math:`y = \sum_{i=0}^{N} w_{i}*x_{i} + \mathcal{N} (\epsilon)`.




.. Typical bioinformatics problems that can be solved by deep learning 
.. --------------------------------------------------------------------
.. Typical questions that bioinformatics want to solve: https://github.com/liyu95/Deep_learning_examples

