# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("./Scripts"))
sys.path.insert(0, os.path.abspath("./Scripts/data_structures"))
sys.path.insert(0, os.path.abspath("./Scripts/algorithms"))
sys.path.insert(0, os.path.abspath("../../algorithms/"))
sys.path.insert(0, os.path.abspath("../../DataStructures/"))
sys.path.insert(0, os.path.abspath("../../networking/"))

# -- Project information -----------------------------------------------------

project = "Interview Documentation"
copyright = "2021, Aditya Raman"
author = "Aditya Raman"

# The full version, including alpha/beta/rc tags
version = release = "v1.0.0"
today = str(date.today())
language = "en"
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/color.css",
]

html_style = "css/color.css"

master_doc = "index"

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    "preamble": "\\addto\\captionsenglish{\\renewcommand{\\contentsname}{Table of contents}}",
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}
latex_show_urls = "footnote"

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False
add_function_parentheses = False
show_authors = True
