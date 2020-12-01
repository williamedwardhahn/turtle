import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turtle",
    version="0.0.1",
    author="William Edward Hahn",
    author_email="wiliamedwardhahn@gmail.com",
    description="Functional Pytorch: Turtles all the way down",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wiliamedwardhahn/turtle",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
