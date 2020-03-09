# setup.py
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-aklefebvere",
    version="1.1",
    author="aklefebvere",
    author_email="aklefebvere@gmail.com",
    description="This is an example",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/aklefebvere/lambdata-aklefebvere",
    keywords="example",
    packages=find_packages() # ["my_lambdata"]
)