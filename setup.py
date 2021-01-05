import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="resolved",
    version="0.0.1",
    description="reSolved is an upcoming captcha solving service, capable of solving reCaptcha, hCaptcha, GeeTest as fast as sub 5 seconds. reSolved is designed to handle heavy workloads, unlike other captcha solving services. We strive to improve the reSolved experience every single day - which is why we are releasing libraries that make an already simple integration process completely seamless.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/resolved-gg/python/",
    author="mechaadi",
    author_email="as808780@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=['requests'],
    include_package_data=True,
)
