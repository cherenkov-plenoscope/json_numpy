import numpy as np
import json
import os
import glob


class Encoder(json.JSONEncoder):
    """
    json encoder for numpy types
    Thanks to:
        github-user: schouldsee, 'Bridging Bio and informatics'
        stackoverflow-user: tsveti_iko

    """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def write(path, out_dict, indent=4):
    with open(path, "wt") as f:
        f.write(json.dumps(out_dict, indent=indent, cls=Encoder))


def read(path):
    with open(path, "rt") as f:
        out_dict = json.loads(f.read())
    return out_dict


def obj_to_array(obj):
    out = {}
    for key in obj:
        item = obj[key]
        if isinstance(item, dict):
            out[key] = obj_to_array(item)
        elif isinstance(item, list):
            tmp = np.array(item)
            if tmp.dtype.str[1:] in ['f8', 'i8']:
                out[key] = tmp
            else:
                out[key] = item
        else:
            out[key] = item
    return out


def read_tree(path):
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
