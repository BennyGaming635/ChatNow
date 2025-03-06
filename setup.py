from pathlib import Path

import setuptools

VERSION = "0.0.2"  # PEP-440

NAME = "chatnow"

INSTALL_REQUIRES = [
    "colorama==0.4.6",
    "emoji==2.5.0",
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="LAN Chat CLI tool in Python.",
    url="https://github.com/bennygaming635/ChatNow",
    project_urls={
        "Source Code": "https://github.com/bennygaming635/ChatNow",
    },
    author="Benjamin Graetz",
    author_email="benjamingraetz@icloud.com",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Students",
        "Intended Audience :: Fun",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    # Snowpark requires Python 3.8
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["chatnow"],
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)