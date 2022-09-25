import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = "0.0.1"

REPO_NAME = "SentimentAnalysis47"
SEC_REPO = "sentiment_analysis"
AUTHOR_EMAIL = "umaretiya@gmail.com"
AUTHOR_USER_NAME = 'umaretiya'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A NLP python Projects using nltk and tensorflow",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src'),
)