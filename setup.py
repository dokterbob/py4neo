from setuptools import setup, find_packages
setup(
    name = "py4neo",
    version = "0.1",
    packages = find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3', 'distribute'],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Tim McNamara",
    author_email = "paperless@timmcnamara.co.nz",
    description = "This is an Example Package",
    license = "GPLv3",
    keywords = "neo4j rest ",
    url = "https://github.com/timClicks/py4neo",
    classifiers = [
    "Development Status :: 3 - Alpha", 
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Topic :: Database",
    "Topic :: Utilities"
    ],
    long_description = open('README').read(),

    # could also include long_description, download_url, classifiers, etc.
)
