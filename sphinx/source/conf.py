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

import sphinx_rtd_theme
import guzzle_sphinx_theme


sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))

print("@@@@@@@@@@@@@@@@@@@@@@@")
print(sys.path)
print("@@@@@@@@@@@@@@@@@@@@@@@")

# -- Project information -----------------------------------------------------

project = ' Quket'
copyright = '''2019-2022 TEN-NO RESEARCH GROUP. All rights Reserved.'''
author = 'Takashi Tsuchimochi, et.al'

# The full version, including alpha/beta/rc tags
release = '0.9'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx.ext.viewcode',
    ]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    }


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates/']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#html_theme_path = guzzle_sphinx_theme.html_theme_path()
#html_theme = 'guzzle_sphinx_theme'
#extensions.append("guzzle_sphinx_theme")
#html_theme_options = {
#    # Set the name of the project to appear in the left sidebar.
#    "project_nav_name": "Quket",
#    # Allow a separate homepage from the master_doc
#    "homepage": "index",
#    # Allow the project link to be overriden to a custom URL.
#    "projectlink": "http://github.com/quket/quket.url",
#    # Visible levels of the global TOC; -1 means unlimited
#    "globaltoc_depth": 6,
#    # If False, expand all TOC entries
#    "globaltoc_collapse": False,
#    # If True, show hidden TOC entries
#    "globaltoc_includehidden": False,
#    }

html_theme = "sphinx_book_theme"
## "sphinx_book_theme"
## "furo"
## "sphinx_rtd_theme"
## "sphinx_material"
html_theme_options = {
    "use_download_button": True,
    "repository_url": "https://github.com/quket/quket",
    "use_repository_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 6,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# autoapi
extensions.append('autoapi.extension')
autoapi_dirs = ['../../quket']
autoapi_type = "python"
autoapi_add_toctree_entry = True
autoapi_python_class_content = "both"
autoapi_keep_files = True
autoapi_ignore = ["/_*", "_*.*", "/templates", "func_*.py", "*.rst"]
autoapi_template_dir = '_templates/autoapi'

autoapi_options = [
    "members",
    "undoc-members",
    "special-members",
    "show-module-summary",
    "show-inheritance",
    "sphinx.ext.githubpages",
    ]


def skip_util_classes(app, what, name, obj, skip, options):

    if ( name.startswith('_')
        or name.startswith('func_')
        or name.endswith(".rst")
        ):
        skip = True

    return skip

def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_util_classes)


# Sphinx Configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html
add_module_names = False
add_function_parentheses = True
modindex_common_prefix = []
numfig = True