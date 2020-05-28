import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Scrapec",
    version="git-c3c4c89",
    author="Scrape Authors",
    author_email="contact@paullee.dev",
    description="Scrapec is a program that compiles .sb3 files into .scrape files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scraterpreter/scrapec",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Compilers",
    ],
    python_requires='>=3.6',
    scripts=['src/scrapec'],
)
