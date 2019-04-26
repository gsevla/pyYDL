import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyydl",
    version="1.0",
    author="Gabriel Alves",
    author_email="gabrieltots@gmail.com",
    description="This is just another app for a presentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gsevla/pyYDL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)