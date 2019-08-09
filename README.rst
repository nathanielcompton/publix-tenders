:Version: 0.1
:Authors:
	Nathaniel Compton

===============
Publix Tendies
===============

Overview
-----------------
	
An installable Python package to determine if Publix brand chicken tender submarine sandwiches are on sale.

Getting Started
---------------

Development Installation
	Follow standard git practices for installation. This repo uses pipenv_ for virtual environment management.

	| ``$ git clone <repo git URL>``
	| ``$ cd publix-tendies``
	| ``$ pipenv shell``
	| ``(publix-tendies)$ pipenv install --dev``

Documentation: Sphinx
	This repo uses Sphinx_ to generate documentation. The Makefile script contains a number of commands which make life easier for the Sphinx user.

	To build and serve HTML-compatible documentation, run:

	| ``(publix-tendies)$ make clean``
	| ``(publix-tendies)$ make html``
	| ``(publix-tendies)$ python -m http.server``

	From there, documentation will be served at: ``localhost:8000/_build/html``

	*Note:* Make sure to ``make clean`` Sphinx directories before committing code.

Testing
-------

This repo implements **pytest**.  Test configuration is located in ``pytest.ini``

.. _pipenv: https://docs.pipenv.org
.. _Sphinx: http://www.sphinx-doc.org
