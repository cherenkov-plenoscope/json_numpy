import json_numpy
import numpy
import json


def test_encoder_array():
    obj = {"a": numpy.array([0, 1])}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": [0, 1]}'


def test_encoder_array2d():
    obj = {"a": numpy.array([[0, 1], [2, 3], [4, 5]])}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": [[0, 1], [2, 3], [4, 5]]}'


def test_encoder_integer():
    obj = {"a": numpy.int(16)}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": 16}'


def test_encoder_float():
    obj = {"a": numpy.float(16)}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": 16.0}'


def test_encoder_float_nan():
    obj = {"a": numpy.float(float("nan"))}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": NaN}'


def test_encoder_float_inf():
    obj = {"a": numpy.float(float("inf"))}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": Infinity}'


def test_encoder_float_minus_inf():
    obj = {"a": numpy.float(-float("inf"))}
    s = json.dumps(obj=obj, cls=json_numpy.Encoder, indent=None)
    assert s == '{"a": -Infinity}'


def test_decoder_list():
    s = '{"a": [1]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (1,)
    assert obj["a"].dtype.str[1:] == "i8"
    assert obj["a"][0] == 1


def test_decoder_list2d():
    s = '{"a": [[1, 2], [3, 4]]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (2, 2)
    assert obj["a"].dtype.str[1:] == "i8"
    assert obj["a"][0, 0] == 1
    assert obj["a"][0, 1] == 2
    assert obj["a"][1, 0] == 3
    assert obj["a"][1, 1] == 4


def test_decoder_list_float():
    s = '{"a": [1.0]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (1,)
    assert obj["a"].dtype.str[1:] == "f8"
    assert obj["a"][0] == 1.0


def test_decoder_list_int_and_float():
    s = '{"a": [1.0, 2]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (2,)
    assert obj["a"].dtype.str[1:] == "f8"
    assert obj["a"][0] == 1.0
    assert obj["a"][1] == 2.0


def test_decoder_list_nan():
    s = '{"a": [1.0, NaN]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (2,)
    assert obj["a"].dtype.str[1:] == "f8"
    assert obj["a"][0] == 1.0
    assert numpy.isnan(obj["a"][1])


def test_decoder_list_nan():
    s = '{"a": [1.0, NaN]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (2,)
    assert obj["a"].dtype.str[1:] == "f8"
    assert obj["a"][0] == 1.0
    assert numpy.isnan(obj["a"][1])


def test_decoder_list_inf():
    s = '{"a": [1.0, Infinity]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], numpy.ndarray)
    assert obj["a"].shape == (2,)
    assert obj["a"].dtype.str[1:] == "f8"
    assert obj["a"][0] == 1.0
    assert obj["a"][1] == float("inf")


def test_decoder_list_invalid_dtype():
    s = '{"a": ["b", "c"]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], list)
    assert obj["a"][0] == "b"
    assert obj["a"][1] == "c"


def test_decoder_list_partly_invalid_dtype():
    s = '{"a": [1, "b", "c"]}'
    obj = json.loads(s=s, object_hook=json_numpy.object_hook)
    assert isinstance(obj["a"], list)
    assert obj["a"][0] == 1
    assert obj["a"][1] == "b"
    assert obj["a"][2] == "c"
