:Version: 0.2
:Authors:
	Nathaniel Compton

==================
Publix Tenders SDK
==================

Overview
-----------------

An installable Python package to programmatically determine if Publix brand
chicken tender sub sandwiches are on sale.

Quickstart
---------------

Development Installation
	Follow standard git and Python practices for dev installation.

	| ``$ git clone {repo_url}``
	| ``$ cd publix-tenders``
	| ``$ python3 -m venv venv``
	| ``$ source venv/bin/active``
	| ``(venv)$ pip install -r requirements.txt``
	| ``(venv)$ python src/main.py``


	From here, set environment variables as appropriate from `settings.py`

Documentation: Sphinx (TODO)
	This repo uses Sphinx_ to generate documentation. The Makefile script contains a number of commands which make life easier for the Sphinx user.

	To build and serve HTML-compatible documentation, run:

	| ``(venv)$ make clean``
	| ``(venv)$ make html``
	| ``(venv)$ python -m http.server``

	From here, documentation will be served at: ``localhost:8000/_build/html``

	*Note:* Make sure to ``make clean`` Sphinx directories before committing code.

Testing
-------

This repo implements pytest_.  Test configuration is located in ``pytest.ini``

| ``(venv)$ pytest``

.. _pytest: https://docs.pytest.org
.. _Sphinx: http://www.sphinx-doc.org
