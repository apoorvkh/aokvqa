from setuptools import find_packages, setup

setup(
    name="aokvqa",
    version="1.0",
    url="https://github.com/allenai/aokvqa",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.7",
    ],
    description="Dataset utilities for A-OKVQA.",
    packages=find_packages(),
)
