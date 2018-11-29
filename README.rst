=======
Amanita
=======

  .. image:: https://img.shields.io/pypi/v/amanita.svg
     :target: https://pypi.python.org/pypi/amanita
     :alt: Latest PyPI version

  .. image:: https://api.travis-ci.com/constrict0r/amanita.svg
     :target: https://travis-ci.org/constrict0r/amanita
     :alt: Latest Travis CI build status

  .. image:: https://readthedocs.org/projects/amanita/badge
     :target: https://amanita.readthedocs.io
     :alt: Latest Readthedocs build status

Create customizable python projects from a simple package
directory layout to a web application.

Documentation on `read the docs <https://amanita.readthedocs.io>`_.

Ingredients
===========

  .. image:: resources/img/python.png
     :target: https://www.python.org
     :alt: Python

  .. image:: resources/img/reestructuredtext.png
     :target: http://docutils.sourceforge.net/rst.html
     :alt: RestructuredText

  .. image:: resources/img/debian.png
     :target: https://www.debian.org
     :alt: Debian

  .. image:: resources/img/git.png
     :target: https://git-scm.com
     :alt: Git

  .. image:: resources/img/direnv.png
     :target: https://direnv.net
     :alt: Direnv

  .. image:: resources/img/poetry.png
     :target: https://poetry.eustace.io
     :alt: PyPoetry

  .. image:: resources/img/click.png
     :target: https://click.palletsprojects.com/en/7.x
     :alt: Click

  .. image:: resources/img/travis.png
     :target: https://travis-ci.org
     :alt: Travis

  .. image:: resources/img/sphinx.png
     :target: http://www.sphinx-doc.org/en/master
     :alt: Sphinx

  .. image:: resources/img/amanita.png
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
- `sphinx <http://www.sphinx-doc.org/en/master>`_: optional.

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

- A package directory layout.
- A virtual enviroment.
- `Direnv <https://direnv.net>`_ configuration.
- `Travis CI <https://travis-ci.org>`_ configuration.
- `Sphinx doc <http://www.sphinx-doc.org/en/stable>`_ configuration.
- `A git <https://git-scm.com>`_ repository.

To create a web application with `flask <http://flask.pocoo.org>`_ from an `openapi <https://swagger.io/specification>`_ specification:

.. code-block:: sh

  amanita my_project -a /home/user/api.yml

Options
=======

This package offers multiple options to customize the project creation
process:

-V, --version         Show the version and exit.
-d, --direnv          Configure  `direnv <https://direnv.net>`_ console enviroment switcher.
-e, --venv-path TEXT  Create and configure a virtual enviroment on the given path.
-t, --travis          Create `travis ci <https://travis-ci.org>`_ configuration.
-v, --venv            Create and configure a virtual enviroment inside the project.
--venv-only           Only create a virtual enviroment on PATH.
-h, --help            Show help and exit.

Compatibility
=============

Python 3.

License
=======

MIT. See the `LICENSE <https://raw.githubusercontent.com/constrict0r/amanita/master/LICENSE>`_ file for more details.

API
===

- `Module Index <py-modindex.html>`_
- `Index <genindex.html>`_

Authors
=======

`amanita` was written by `constrict0r <constrict0r@protonmail.com>`_.

Enjoy!!

  .. image:: resources/img/enjoy.png
     :alt: Enjoy!!
