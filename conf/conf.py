# -*- coding: utf-8 -*-
#
# Plone Developer Manual documentation build configuration file, created by
# sphinx-quickstart on Sun Aug 16 13:38:00 2009.
#
# This file is execfile()d with the current directory set to its containing dir
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    #'collective.sphinx.autoatschema',
    #'collective.sphinx.includedoc'
    #'sphinxcontrib.contributors',
    'sphinxcontrib_robotframework',
    'sphinx.ext.autosummary',
    'sphinxcontrib.spelling',
]

# This is our wordlist with know words, like Github or Plone ...
spelling_word_list_filename='source/documentation/spelling_wordlist.txt'

# Enable Robot Framework tests during Sphinx compilation:
sphinxcontrib_robotframework_enabled = True  # 'True' is the default
sphinxcontrib_robotframework_quiet = True  # 'False' is the default

# Configure Robot Frameowrk tests to use Firefox
sphinxcontrib_robotframework_variables = {
    "BROWSER": "Firefox"  # 'Firefox' is the default
}

# See http://sphinx-doc.org/ext/todo.html#confval-todo_include_todos
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../source/documentation/_templates']

locale_dirs = ["../source/documentation/_locales"]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Plone Documentation'
copyright = u'''The text and illustrations in this website are licensed by the Plone Foundation under a Creative Commons Attribution 4.0 International license.
        Plone and the Plone<sup>®</sup> logo are registered trademarks of the Plone Foundation, registered in the United States and other countries.
        For guidelines on the permitted uses of the Plone trademarks, see https://plone.org/foundation/logo
        All other trademarks are owned by their respective owners.'''
trademark_name = "Plone"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = [
#    '5.0',
    '4.3',
#    '3.3',
    ]
# The full version, including alpha/beta/rc tags.
release = '4.3'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['README.rst', '_*.rst']

# Announce that we have a opensearch plugin
html_use_opensearch = 'http://docs.plone.org'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = 'Italian'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
#exclude_trees = ['old-reference-manuals', 'adapt-and-extend', 'develop', 'working-with-content', 'manage']

# The reST default role (used for this markup: `text`) to use for all documents
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'plone_org_4'
import sphinx.themes.plone
html_theme_path = sphinx.themes.plone.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}
html_theme_options = {
#	"rightsidebar": "false",
    'doc_languages' : [
#        {'lang_code':'en','lang_name':'English'},
#        {'lang_code':'de','lang_name':'German'},
#        {'lang_code':'it','lang_name':'Italian'},
        ],
    'doc_language'  : 'en',
    'trademark_name' : 'Plone',
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '%(project)s v%(release)s' % {'project': project, 'release': release}

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_style='plone.css'
#html_logo='_static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = 'plone.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {
#    '**': ['localtoc.html', 'searchbox.html', 'plone.html', 'contributors.html'],
#}
# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'PloneDocumentation'


# -- Options for LaTeX output -------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
latex_documents = [
    ('index', 'PloneDocumentation.tex', u'Plone Documentation',
     u'The Plone community', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "../source/documentation/_static/logo_2x.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# Do not try do funny things on our characters
# http://sphinx-doc.org/config.html#confval-html_use_smartypants
html_use_smartypants = False

# Don't build Modules pages
html_domain_indices = False

# Don't build term index
html_use_index = False

# Don't copy sources with output HTML, as they live on GitHub
html_copy_source = False
