import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reSolved", # Replace with your own username
    version="0.0.1",
    author="mechaadi",
    author_email="as808780@gmail.com",
    description="reSolved is an upcoming captcha solving service, capable of solving reCaptcha, hCaptcha, GeeTest as fast as sub 5 seconds. reSolved is designed to handle heavy workloads, unlike other captcha solving services. We strive to improve the reSolved experience every single day - which is why we are releasing libraries that make an already simple integration process completely seamless.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)