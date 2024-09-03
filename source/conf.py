# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Deep Learning in Bioinformatics 101'
copyright = '2024, Mingyi Xue'
author = 'Mingyi Xue'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'myst_nb',
    # 'nbsphinx',
    # 'sphinx_gallery.load_style',
    # 'sphinx_gallery.gen_gallery',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',   
]

# nbsphinx specific configuration
# sphinx_gallery_conf = {
#     'examples_dirs': '../code',   # path to your example scripts
#     'gallery_dirs': '_code',  # path to where to save gallery generated output
#     'example_extensions': {'.ipynb'},
#     'filename_pattern': r'.*\.ipynb',
#     'ignore_pattern': r'__init__\.py',
#     'only_warn_on_example_error': True
# }

nbsphinx_allow_errors = True  # allow errors in your notebooks
nbsphinx_execute = 'never'  # this can be set to 'always' 'never' or 'auto'
source_suffix = [".rst"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']
