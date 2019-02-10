=========
best-tags
=========

.. image:: https://img.shields.io/pypi/v/besttags.svg
        :target: https://pypi.python.org/pypi/besttags

I try to find the best hashtags for my post on instagram. There are some grate
web pages, but I wand a python package.

* Free software: MIT license

Install
-------

.. code-block:: shell

  $ pip install besttags

Command-line
------------

.. code-block:: shell

  $ besttags-web coding python programmer --fix fullstackhero

  #fullstackhero #coding #programming #programmer #html #css #javascript #developer
  #code #webdeveloper #coder #webdesign #webdevelopment #technology #php #java
  #software #tech #python #computer #computerscience #development #codinglife
  #linux #programmers #softwaredeveloper #bhfyp #web #webdesigner #c

See the help for more informations

.. code-block:: shell

  $ python -m besttags --help

or

.. code-block:: shell

  $ besttags-web --help

Examples
--------
The simple one-liner. It will save the best hashtags for the given tags in a file.

.. code-block:: python

  from besttags import WebAnalyzer as Analyzer

  # The tags you are interested in.
  tags = ['coder', 'programmers', 'python']

  Analyzer()(tags).save('best_hashtags.txt')

You can change the default settings and add additional tags and use print()
to show the tags

.. code-block:: python

  Analyzer(limit=10, fix=['fullstackhero'])(tags).save('10_best_hashtags.txt')

  print(Analyzer()(tags))

Use the Analyzer to create an object, which you can use multiple times. It is
callable and allows a list or single strings.

.. code-block:: python

  best = Analyzer(fix=['fullstackhero'])

  best('computer', 'instagood')
  best(['coder', 'programmers', 'python'])

The result is a class, with some basic functions. So you can iterate it and
get the length.

.. code-block:: python

  result = best('coder', 'programmers', 'python')

  print(len(result))

  for tag in result:
      print(tag)

  print(result)

  result.save('best_hashtags.txt')
