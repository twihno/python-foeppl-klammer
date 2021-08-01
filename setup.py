"""Packaging for foepplklammer"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="foepplklammer",
    author="Thomas Schuster",
    author_email="twihno@gmail.com",
    description="Python Modul für die Verwendung von Föppl Klammern in Berechnungen",
    keywords="foeppl, mechanik",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/twihno/python-foeppl-klammer",
    project_urls={
        "Documentation": "https://github.com/twihno/python-foeppl-klammer",
        "Bug Reports": "https://github.com/twihno/python-foeppl-klammer/issues",
        "Source Code": "https://github.com/twihno/python-foeppl-klammer",
        # "Funding": "",
        # "Say Thanks!": "",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["numpy"],
)
