rio-clip
========

A Rasterio CLI command plugin for clipping datasets.

Usage
-----

Given two datasets, ``rio clip`` clips the second dataset to the bounds of the first dataset.

.. code-block:: console

    $ rio clip source.tif target.tif cropped.tif

Installation
------------

If you've already 
`installed Rasterio <https://github.com/mapbox/rasterio#installation>`__,
installation is just ``pip install rio-clip``.