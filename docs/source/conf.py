# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'proj-name_Sphinxy'
copyright = '2024, My_Name'
author = 'My_Name'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx_multiversion",
]

autoclass_content = 'both'

templates_path = [
    "_templates",
]
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/versions.html",
        "sidebar/scroll-end.html",
    ],
}

exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']

import os
from sphinx.application import Sphinx

#def generate_microcontroller_docs(app: Sphinx):
#    microcontrollers = ['test_case_1', 'test_case_2']
#    for mcu in microcontrollers:
#       mcu_doc_path = os.path.join(app.srcdir, mcu)
#        
#        # Проверка существования директории
#        if not os.path.exists(mcu_doc_path):
#            os.makedirs(mcu_doc_path)
#        
#        # Создание или обновление index.rst файла
#        index_rst_path = os.path.join(mcu_doc_path, 'index.rst')
#        with open(index_rst_path, 'w') as index_file:
#            index_file.write(f"{mcu} Documentation\n")
#            index_file.write("=" * (len(mcu) + 13) + "\n\n")
#            index_file.write(f".. toctree::\n")
#            index_file.write(f"   :maxdepth: 2\n\n")
#            index_file.write(f"   introduction\n")
#            
#            # Добавление ссылок на файлы документации
#            for doc in os.listdir(mcu_doc_path):
#                if doc.endswith('.rst') and doc != 'index.rst':
#                    docname, _ = os.path.splitext(doc)
#                    index_file.write(f"   {docname}\n")
#
#def setup(app: Sphinx):
#    app.connect('builder-inited', generate_microcontroller_docs)

import os
from sphinx.application import Sphinx

update_main_index = False

def generate_microcontroller_docs(app: Sphinx):
    microcontrollers = ['test_case_1', 'test_case_2']
    for mcu in microcontrollers:
        mcu_doc_path = os.path.join(app.srcdir, mcu)
        
        # Проверка существования директории
        if not os.path.exists(mcu_doc_path):
            os.makedirs(mcu_doc_path)
        
        # Создание или обновление index.rst файла для микроконтроллера
        index_rst_path = os.path.join(mcu_doc_path, 'index.rst')
        with open(index_rst_path, 'w') as index_file:
            index_file.write(f"{mcu} Documentation\n")
            index_file.write("=" * (len(mcu) + 13) + "\n\n")
            index_file.write(".. toctree::\n")
            index_file.write("   :maxdepth: 2\n\n")
            
            # Добавление разделов в index.rst каждого микроконтроллера
            sections = ['introduction', 'getting_started', 'advanced_features']
            for section in sections:
                doc_path = os.path.join(mcu_doc_path, f"{section}.rst")
                if not os.path.exists(doc_path):
                    with open(doc_path, 'w') as doc_file:
                        doc_file.write(f"{section}\n")
                        doc_file.write("=" * len(section) + "\n\n")
                        doc_file.write(f"Content for {mcu} {section} goes here.\n\n")
                index_file.write(f"   {section}\n")

    # Обновление корневого index.rst файла с toctree для всех микроконтроллеров
    if (update_main_index == True):
        root_index_path = os.path.join(app.srcdir, 'index.rst')
        with open(root_index_path, 'a') as root_index_file:
            root_index_file.write(".. toctree::\n")
            root_index_file.write("   :maxdepth: 2\n\n")
            for mcu in microcontrollers:
                root_index_file.write(f"   {mcu}/index\n")

def setup(app: Sphinx):
    app.connect('builder-inited', generate_microcontroller_docs)