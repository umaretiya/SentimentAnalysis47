from sentiment_analysis.utils import read_yaml

# from sentiment_analysis.utils
import pytest
from pathlib import Path
from ensure.main import EnsureError
from box import ConfigBox


def unit_test():
    assert True

print(read_yaml(Path("tests\data\demo.yaml")))
      
def read_yaml_files():
    read_yaml(Path("tests\data\demo.yaml"))


read_yaml_files()


class Test_yaml_file:
    lists_files = [
        "tests\data\demo.yaml",
        "tests\data\empty.yaml",
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.lists_files[0]))

    def read_yaml_return_type(self):
        response = read_yaml(Path(self.lists_files[-1]))
        assert isinstance(response, ConfigBox)

    @pytest.mark.parametrize("path_to_yaml", read_yaml)
    def read_yaml_bad_type(self, path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)


# "D:\DataScience-60\SentimentAnalysis47"
