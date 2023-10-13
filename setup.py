from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()

VERSION = "0.0.10"
DESCRIPTION = "A web scraper for TIU student system"

setup(
    name="tiupy",
    version=VERSION,
    description=DESCRIPTION,
    author="HeroMR",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/heromr/tiupy",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords=["tiu uni", "tishk university", "tiu scraper", "tiu API"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
