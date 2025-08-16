from setuptools import setup, find_packages

setup(
    name="numseq",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # aici pui alte librării necesare, dacă există
    author="Luca Vlad",
    author_email="vladluca70@gmail.com",
    description="Librărie pentru secvențe numerice",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vladluca70/NumSeq--Python-Library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
