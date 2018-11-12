.. amanita documentation master file, created by
   sphinx-quickstart on Fri Nov  2 22:28:21 

Amanita
=======

Create customizable python projects from a simple package
directory layout to a web application.

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

The development profile includes:

  - A virtual enviroment.
  - `Direnv <https://direnv.net>`_ configuration.
  - `Sphinx <http://www.sphinx-doc.org/en/stable>`_ configuration.
  - A `git <https://git-scm.com/>`_ repository.

To create a web application with flask from an openapi specification:

.. code-block:: sh

  amanita my_project -a /home/user/api.yml

Options
=======

API
===

* :ref:`modindex`
* :ref:`genindex`

