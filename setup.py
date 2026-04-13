"""
setup.py - Package configuration for DevInit CLI
"""

from setuptools import setup, find_packages

setup(
    name="devinit",
    version="1.0.0",
    description="Node.js project scaffolding CLI for developers",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="DevInit",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            # Properly references the package — works on Windows, Mac, Linux
            "devinit=devinit_cli.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Software Development :: Code Generators",
    ],
)
