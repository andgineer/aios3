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
    description="Asyncio S3 file operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andgineer/aios3",
    packages=setuptools.find_packages(exclude="tests"),
    # package_dir={"": "src"},
    include_package_data=True,
    install_requires=requirements,
    keywords="asyncio boto3 botocore s3 aws",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
