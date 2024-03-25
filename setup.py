from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name='coingecko',
    version='0.13',
    description='Python wrapper for the CoinGecko API',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/khooihzhz/coingecko-python",
    author='khooihzhz',
    author_email='khooihongzhe@gmail.com',
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': [
            'pytest-recording',
        ]
    },
    python_requires='>=3.0',
)
