# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "numpy-ml"
copyright = "2019, David Bourgin"
author = "David Bourgin"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    #  "numpydoc",
]

# Napoleon settings
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html#sphinxcontrib.napoleon.Config
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_use_keyword = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"

autoclass_content = "both"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}

html_theme_options = {
    #  'logo': 'logo.png',
    "github_user": "ddbourgin",
    "github_repo": "numpy-ml",
    "description": "Machine learning, in NumPy",
    #  'analytics_id': "", XXX: TODO
    "github_button": True,
    "show_powered_by": False,
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "numpy-mldoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "numpy-ml.tex", "numpy-ml Documentation", "David Bourgin", "manual")
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "numpy-ml", "numpy-ml Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "numpy-ml",
        "numpy-ml Documentation",
        author,
        "numpy-ml",
        "Machine learning, in NumPy.",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

autodoc_member_order = "bysource"


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("http://docs.scipy.org/doc/numpy/", None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for numpydocs extension -----------------------------------------
# https://numpydoc.readthedocs.io/en/latest/install.html

# Whether to produce plot:: directives for Examples sections that contain
# import matplotlib or from matplotlib import.
numpydoc_use_plots = True

# Whether to show all members of a class in the Methods and Attributes sections
# automatically. True by default.
numpydoc_show_class_members = True

#  Whether to show all inherited members of a class in the Methods and
#  Attributes sections automatically. If it’s false, inherited members won’t
#  shown. True by default.
numpydoc_show_inherited_class_members = True

#  Whether to create a Sphinx table of contents for the lists of class methods
#  and attributes. If a table of contents is made, Sphinx expects each entry to
#  have a separate page. True by default.
numpydoc_class_members_toctree = False

# A regular expression matching citations which should be mangled to avoid
# conflicts due to duplication across the documentation. Defaults to [\w-]+.
numpydoc_citation_re = r"[\w-]+"

# Until version 0.8, parameter definitions were shown as blockquotes, rather
# than in a definition list. If your styling requires blockquotes, switch this
# config option to True. This option will be removed in version 0.10.
numpydoc_use_blockquotes = False

# Whether to format the Attributes section of a class page in the same way as
# the Parameter section. If it's False, the Attributes section will be
# formatted as the Methods section using an autosummary table. True by default.
numpydoc_attributes_as_param_list = False

# Whether to create cross-references for the parameter types in the Parameters,
# Other Parameters, Returns and Yields sections of the docstring. False by
# default.
numpydoc_xref_param_type = False

#  Mappings to fully qualified paths (or correct ReST references) for the
#  aliases/shortcuts used when specifying the types of parameters. The keys
#  should not have any spaces. Together with the intersphinx extension, you can
#  map to links in any documentation. The default is an empty dict.  This
#  option depends on the numpydoc_xref_param_type option being True.
numpydoc_xref_aliases = {}

#  Words not to cross-reference. Most likely, these are common words used in
#  parameter type descriptions that may be confused for classes of the same
#  name. For example: {'type', 'optional', 'default'}. The default is an empty
#  set.
numpydoc_xref_ignore = set([])

#  Deprecated since version edit: your HTML template instead Whether to insert
#  an edit link after docstrings.
numpydoc_edit_link: bool