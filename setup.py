from os.path import dirname
from os.path import join
import setuptools


def readme() -> str:
    """Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to put
    a raw string in below.
    :return: content of README.md
    """
    return open(join(dirname(__file__), "README.md")).read()


setuptools.setup(
    name="streamlit_tags",
    version="1.0.0",
    author="Gagan Bhatia",
    author_email="gbhatia880@gmail.com",
    description="TBD",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/gagan3012/resumacy",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'],
    python_requires=">=3.6",
    install_requires=[
        "spacy>=3.0.1,<3.1.0",
    ]
)