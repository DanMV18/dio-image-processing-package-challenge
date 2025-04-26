from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_image_processing",
    version="0.0.1",
    author="DanMV18",
    description="This is a simple package with easy to use image processing tools",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanMV18/dio-image-processing-package-challenge.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
    )