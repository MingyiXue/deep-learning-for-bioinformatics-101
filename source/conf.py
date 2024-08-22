# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# import os, sys
# srcdir = os.path.abspath(__file__)
# sys.path.insert(0, os.path.join(os.path.dirname(srcdir), "code"))

project = 'Deep Learning in Bioinformatics 101'
copyright = '2024, Mingyi Xue'
author = 'Mingyi Xue'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "nbsphinx",
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',   
]

# nbsphinx specific configuration
# nbsphinx_allow_errors = True  # allow errors in your notebooks
# nbsphinx_execute = 'always'  # this can be also set to 'never' or 'auto'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']
