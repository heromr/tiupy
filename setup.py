from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

VERSION = "1.1.2"
DESCRIPTION = "A robust web scraper and API wrapper for TIU student system"

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
    install_requires=[
        "httpx>=0.24.1",  # For making HTTP requests
        "beautifulsoup4>=4.12.2"  # For parsing HTML content
    ],
    keywords=["tiu uni", "tishk university", "tiu scraper", "tiu API", "university system"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
