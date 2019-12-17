import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="startergateid",
    version="0.0.2",
    author="startergate",
    author_email="startergate36@gmail.com",
    description="SID Client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/startergate/SID.py",
    packages=setuptools.find_packages('./src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)