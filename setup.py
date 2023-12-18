from setuptools import setup, find_packages



with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="key_shuffler",
    version='0.1.0',
    author="indicatedl",
    author_email="indcated@gmail.com",
    url="https://github.com/indicatedl/key_shuffler.git",
    download_url=f"https://github.com/indicatedl/key_shuffler/archive/refs/tags/v0.1.0.zip",
    description="Simply python library for encrypting private keys using character shuffle method",
    packages=['key_shuffler'],
    install_requires=[],
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Communications :: Email",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    python_requires='>=3.10.0'
)