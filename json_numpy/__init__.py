"""
JSON-NUMPY
----------
Load and dump numpy-arrays from and to JSON when possible.

If a JSON-object can initialize a numpy-array with VALID_DTYPES,
then we return this numpy-array.

When a numpy-array can be dumped into a generic list, float, or int,
then we dump this generic representation into JSON.
"""
from .version import __version__
import numpy
import json
import os
import glob

VALID_DTYPES = ["f8", "i8"]


class Encoder(json.JSONEncoder):
    """
    Tries to convert numpy objects to generic types.
    - numpy.array to list()
    - numpy.integer to int()
    - numpy.floating to float()

    Thanks to:
        github-user: schouldsee, 'Bridging Bio and informatics'
        stackoverflow-user: tsveti_iko
    """

    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def object_hook(obj, valid_dtypes=VALID_DTYPES):
    """
    Tries to convert generic lists and as numpy.arrays.
    Only if the dtype of the converted numpy.array is a valid_dtype, the
    numpy.array is returned.

    This function can be used in json.loads as object_hook.

    Parameters
    ----------
    obj : dict, list, int, float or string
            An object that may or may not be converted into a numpy.array.
    valid_dtypes : list of strings
            The valid dtypes of numpy.array(obj).dtype.str to be accepted
            in an conversion to numpy.array.
            The endianness-markers '<', '>' are stripped.
    """
    if isinstance(obj, dict):
        return _hook_dict(dic=obj, valid_dtypes=valid_dtypes)
    elif isinstance(obj, list):
        return _hook_list(lis=obj, valid_dtypes=valid_dtypes)
    else:
        return obj


def _hook_dict(dic, valid_dtypes):
    out = {}
    for key in dic:
        item = dic[key]
        if isinstance(item, dict):
            out[key] = _hook_dict(dic=item, valid_dtypes=valid_dtypes)
        elif isinstance(item, list):
            out[key] = _hook_list(lis=item, valid_dtypes=valid_dtypes)
        else:
            out[key] = item
    return out


def _hook_list(lis, valid_dtypes):
    tmp = numpy.array(lis)
    if tmp.dtype.str[1:] in valid_dtypes:
        return tmp
    else:
        return lis


def dumps(obj, cls=Encoder, **kwargs):
    return json.dumps(obj, cls=cls, **kwargs)


def loads(s, object_hook=object_hook, **kwargs):
    obj = json.loads(s, **kwargs)
    return object_hook(obj=obj)
