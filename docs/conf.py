# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import shutil

import jinja2

# Environment to process Jinja templates.
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))

# Jinja templates to render out.
templates = []

# Render templates and output files without the last extension.
# For example: 'install.md.jinja' becomes 'install.md'.
for template in templates:
    rendered = jinja_env.get_template(template).render()
    with open(os.path.splitext(template)[0], "w") as file:
        file.write(rendered)

shutil.copy2("../RELEASE.md", "./about/release-notes.md")

latex_engine = "xelatex"
latex_elements = {
    "fontpkg": r"""
\usepackage{tgtermes}
\usepackage{tgheros}
\renewcommand\ttdefault{txtt}
"""
}

# configurations for PDF output by Read the Docs
project = "ROCm Documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."
version = "6.1.2"
release = "6.1.2"
setting_all_article_info = True
all_article_info_os = ["linux", "windows"]
all_article_info_author = ""

# pages with specific settings
article_pages = [
    {"file": "about/release-notes", "os": ["linux", "windows"], "date": "2024-06-04"},
    {"file": "about/changelog", "os": ["linux", "windows"], "date": "2024-06-04"},
    {"file": "how-to/deep-learning-rocm", "os": ["linux"]},
    {"file": "how-to/gpu-enabled-mpi", "os": ["linux"]},
    {"file": "how-to/system-debugging", "os": ["linux"]},
    {"file": "how-to/tuning-guides", "os": ["linux", "windows"]},
]

exclude_patterns = ["temp"]

external_toc_path = "./sphinx/_toc.yml"

extensions = ["rocm_docs", "sphinx_reredirects"]

external_projects_current_project = "rocm"

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "https://rocm-stg.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

html_theme = "rocm_docs_theme"
html_theme_options = {"flavor": "rocm-docs-home"}

html_static_path = ["sphinx/static/css"]
html_css_files = ["rocm_custom.css"]

html_title = "ROCm Documentation"

html_theme_options = {"link_main_doc": False}

redirects = {"reference/openmp/openmp": "../../about/compatibility/openmp.html"}
