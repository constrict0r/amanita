.. amanita documentation master file, created by
   sphinx-quickstart on Fri Nov  2 22:28:21

Amanita
=======

Create customizable python projects from a simple package
directory layout to a web application.

This program has ben written and tested on `Debian <https://debian.org>`_.

Ingredients
===========

  .. image:: ../../resources/img/python.png
     :target: https://www.python.org
     :alt: Python

  .. image:: ../../resources/img/reestructuredtext.png
     :target: http://docutils.sourceforge.net/rst.html
     :alt: RestructuredText

  .. image:: ../../resources/img/debian.png
     :target: https://www.debian.org
     :alt: Debian

  .. image:: ../../resources/img/git.png
     :target: https://git-scm.com
     :alt: Git

  .. image:: ../../resources/img/direnv.png
     :target: https://direnv.net
     :alt: Direnv

  .. image:: ../../resources/img/poetry.png
     :target: https://poetry.eustace.io
     :alt: PyPoetry

  .. image:: ../../resources/img/click.png
     :target: https://click.palletsprojects.com/en/7.x
     :alt: Click

  .. image:: ../../resources/img/sphinx.png
     :target: http://www.sphinx-doc.org/en/stable
     :alt: Sphinx

  .. image:: ../../resources/img/amanita.png
     :target: https://es.wikipedia.org/wiki/Amanita_muscaria
     :alt: Amanita

Installation
============

.. code-block:: sh

  pip install amanita

Requirements
------------

All requirements are installed (with the user approval) when needed:

  - `pypoetry <https://poetry.eustace.io>`_.
  - `direnv <https://direnv.net>`_: optional, Linux or MacOS only.
  - `git <https://git-scm.com>`_: optional.

Usage
=====

To create a simple package directory:

.. code-block:: sh

  amanita my_project

To create a package with a virtual enviroment:

.. code-block:: sh

  amanita my_project -v

To create a package with development profile:

.. code-block:: sh

  amanita my_project --dev

A development profile includes:

  - A virtual enviroment.
  - `Direnv <https://direnv.net>`_ configuration.
  - `Sphinx <http://www.sphinx-doc.org/en/stable>`_ configuration.
  - A `git <https://git-scm.com/>`_ repository.

To create a web application with `flask <https://flask.pocoo.org>`_ from an `openapi <https://swagger.io/specification>`_ specification:

.. code-block:: sh

  amanita my_project -a /home/user/api.yml

Options
=======

This package offers multiple options to customize the project creation
process:

  -V, --version         Show the version and exit.
  -d, --direnv          Install and configure  `direnv <https://direnv.net>`_ console enviroment
                        switcher.
  -v, --venv            Create and configure a virtual enviroment inside the
                        project.
  -e, --venv-path TEXT  Create and configure a virtual enviroment on the given
                        path.
  -h, --help            Show help and exit.

Compatibility
=============

Python 3.

License
=======

MIT. See the `LICENSE <https://raw.githubusercontent.com/constrict0r/amanita/master/LICENSE>`_ file for more details.

API
===

* :ref:`modindex`
* :ref:`genindex`

Authors
=======

`amanita` was written by `constrict0r <constrict0r@protonmail.com>`_.

Enjoy!!

  .. image:: ../../resources/img/enjoy.png
     :alt: Enjoy!!
