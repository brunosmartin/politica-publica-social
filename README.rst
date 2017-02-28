=============================
politica-publica-social
=============================

.. image:: https://badge.fury.io/py/politica-publica-social.svg
    :target: https://badge.fury.io/py/politica-publica-social

.. image:: https://travis-ci.org/brunosmartin/politica-publica-social.svg?branch=master
    :target: https://travis-ci.org/brunosmartin/politica-publica-social

.. image:: https://codecov.io/gh/brunosmartin/politica-publica-social/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/brunosmartin/politica-publica-social

Your project description goes here

Documentation
-------------

The full documentation is at https://politica-publica-social.readthedocs.io.

Quickstart
----------

Install politica-publica-social::

    pip install politica-publica-social

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'politica_publica_social.apps.PoliticaPublicaSocialConfig',
        ...
    )

Add politica-publica-social's URL patterns:

.. code-block:: python

    from politica_publica_social import urls as politica_publica_social_urls


    urlpatterns = [
        ...
        url(r'^', include(politica_publica_social_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
