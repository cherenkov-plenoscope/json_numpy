JSON-NUMPY
==========

Transparent dumps and loads of numpy-arrays.

```Encoder``` 
-------------
to dump with ```json.dumps()```.

```object_hook```
-----------------
to load with ```json.loads()```.

example
-------
```python
import numpy
import json_numpy

obj = json_numpy.loads(s='{"a": [1.0, NaN]}')
assert isinstance(obj["a"], numpy.ndarray)

json_numpy.dumps(obj)
'{"a": [1.0, NaN]}'
```
