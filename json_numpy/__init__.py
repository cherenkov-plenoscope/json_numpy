import numpy
import json
import os
import glob


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


def object_hook(obj, valid_dtypes=['f8', 'i8']):
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
    out = {}
    for key in obj:
        item = obj[key]
        if isinstance(item, dict):
            out[key] = object_hook(item)
        elif isinstance(item, list):
            tmp = numpy.array(item)
            if tmp.dtype.str[1:] in valid_dtypes:
                out[key] = tmp
            else:
                out[key] = item
        else:
            out[key] = item
    return out


def dumps(obj, cls=Encoder, **kwargs):
    return json.dumps(obj, cls=cls, **kwargs)


def loads(s, object_hook=object_hook, **kwargs):
    return json.loads(s, object_hook=object_hook, **kwargs)


def write(path, out_dict, indent=4):
    with open(path, "wt") as f:
        f.write(json.dumps(out_dict, indent=indent, cls=Encoder))


def read(path):
    with open(path, "rt") as f:
        out_dict = loads(f.read())
    return out_dict


def read_tree(path):
    """
    Walks down a directory path and reads every json-file into an object.
    Returns one combined object with the top-level keys beeing the dirnames
    and basenames of the json-files.
    """
    out = {}
    _paths = glob.glob(os.path.join(path, "*"))
    for _path in _paths:
        file_path, file_extension = os.path.splitext(_path)
        file_basename = os.path.basename(file_path)
        if str.lower(file_extension) == ".json":
            out[file_basename] = read(_path)
        if os.path.isdir(_path):
            out[file_basename] = read_tree(_path)
    return out
