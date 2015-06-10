rio-crop
========

A Rasterio CLI command plugin for cropping datasets.

Usage
-----

Given two datasets, ``rio crop`` crops the second dataset to the bounds of the first dataset.

.. code-block:: console

    $ rio crop source.tif target.tif cropped.tif

Installation
------------

If you've already 
`installed Rasterio <https://github.com/mapbox/rasterio#installation>`__,
installation is just ``pip install rio-crop``.