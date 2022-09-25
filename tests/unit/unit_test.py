from sentiment_analysis.utils import read_yaml

# from sentiment_analysis.utils
import pytest
from pathlib import Path
from ensure.main import EnsureError
from box import ConfigBox


def unit_test():
    assert True


def read_yaml_files():
    read_yaml(Path("tests\data\demo.yaml"))
    assert True


yaml_file = [
    "tests\data\demo.yaml",
    "tests\data\empty.yaml",
]


def test_read_yaml_empty():
    content = read_yaml(Path(yaml_file[0]))
    assert isinstance(content,ConfigBox)


def read_yaml_return_type():
    response = read_yaml(Path(yaml_file[-1]))
    assert isinstance(response, ConfigBox)


@pytest.mark.parametrize("path_to_yaml", read_yaml)
def read_yaml_bad_type(path_to_yaml):
    with pytest.raises(EnsureError):
        read_yaml(path_to_yaml)


# "D:\DataScience-60\SentimentAnalysis47"
