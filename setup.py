import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

from src.aios3 import version

setuptools.setup(
    name="aios3",
    version=version.VERSION,
    author="Andrey Sorokin",
    author_email="andrey@sorokin.engineer",
    description="Wrapper for aiobotocore to simplify reading of large files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://andgineer.github.io/aios3/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,
    python_requires=">=3.7",
    keywords="asyncio boto3 botocore s3 aws",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
