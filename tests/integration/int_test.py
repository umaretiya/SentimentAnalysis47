# from pathlib import Path 
# from sentiment_analysis.utils import read_yaml
# import yaml

def test_yaml():
    assert True
    
# path = "D:\DataScience-60\SentimentAnalysis47\.github\workflows\CI.yml"

# content = read_yaml(Path(path))
# print(content)

# ci_file ={'name': 'Sentiment Analysis', 
#     True: {'push': 
#      {'pull_request': 
#          {'branches': ['main']}, 
#          'push': 
#              {'branches': ['main']}}
#      }, 
#     'permissions': 
#      {'contents': 'read'}, 
#     'jobs': 
#         {'build': 
#             {'runs-on': 
#                 '${{ matrix.os }}', 
#                 'strategy': 
#                     {'matrix': 
#                         {'os': 
#                             ['ubuntu-latest', 'windows-latest'], 
#                             'python-version': ['3.9']}
#                         }, 
#                     'steps': [{'uses': 'actions/checkout@v3'}, 
#                             {'name': 'Set up Python ${{ matrix.python-version }}', 
#                             'uses': 'actions/setup-python@v3', 
#                             'with': {'python-version': '${{ matrix.python-version }}'}
#                             }, 
#                             {'name': 'Install dependencies', 
#                             'run': 'python -m pip install --upgrade pip\npip install flake8 pytest tox tox-gh-actions\npip install -r requirements.txt\n'}, 
#                             {'name': 'Test with tox', 'run': 'tox'}]
#                     }
#             }
#         }
# with open(r'ci_file.yaml', 'w') as ciFile:
#     docs = yaml.dump(ci_file, ciFile)