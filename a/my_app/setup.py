import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo_plug",
    version="0.0.1",
    author="yagnesh",
    author_email="yagneshnayi07@gmail.com",
    description="my Openedx ",
    long_description=long_description,
    long_description_content_type="text/markdown",
   
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "demo_plug"},
    packages=setuptools.find_packages(where="demo_plug"),
    python_requires=">=3.6",
)