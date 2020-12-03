from distutils.core import setup
from sys import version_info as ver

setup(
    name = 'plagiotron',
    packages = ['text_matcher'], 
    download_url = 'https://github.com/JonathanReeve/text-matcher/tarball/0.1.6',
    install_requires = ['Click', 'nltk', 'termcolor'],
    keywords = ['NLP', 'text', 'text reuse'],
    entry_points='''
    [console_scripts]
    plagiotron = text_matcher.text_matcher:cli''',
)
