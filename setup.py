from setuptools import setup, find_packages

setup(
    name = "py4neo",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['docutils>=0.3', 'distribute'],
    author = "Tim McNamara",
    author_email = "paperless@timmcnamara.co.nz",
    description = "A Python client for Neo4j's REST interface.",
    license = "GPLv3",
    keywords = ["Neo4j","REST"],
    url = "https://github.com/timClicks/py4neo",
    classifiers = [
    "Development Status :: 3 - Alpha", 
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Topic :: Database",
    "Topic :: Utilities"],
    long_description = open('README').read())
