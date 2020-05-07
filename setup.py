# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-14", # the name that you will install via pip
    version="1.1",
    author="Your Full Name",
    author_email="your@email.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/lambdata-14",
    #keywords="",
    packages=["my_lambdata"] #find_packages() # ["my_lambdata"]
)
