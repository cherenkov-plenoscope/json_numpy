##########
JSON-NUMPY
##########
|TestStatus| |PyPiStatus| |BlackStyle|

Transparent ```dumps``` and ```loads``` of ```numpy-arrays```.

*************
```Encoder```
*************

to dump with ```json.dumps()```.

*****************
```object_hook```
*****************
to load with ```json.loads()```.

*******
example
*******

.. code-block:: python

    import numpy
    import json_numpy

    obj = json_numpy.loads(s='{"a": [1.0, NaN]}')
    assert isinstance(obj["a"], numpy.ndarray)

    json_numpy.dumps(obj)
    '{"a": [1.0, NaN]}'


.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |TestStatus| image:: https://github.com/cherenkov-plenoscope/json_numpy/actions/workflows/test.yml/badge.svg?branch=main
    :target: https://github.com/cherenkov-plenoscope/json_numpy/actions/workflows/test.yml

.. |PyPiStatus| image:: https://img.shields.io/pypi/v/json_numpy_sebastian-achim-mueller
    :target: https://pypi.org/project/json_numpy_sebastian-achim-mueller
