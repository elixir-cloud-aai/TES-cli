from setuptools import (setup, find_packages)

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='tes_client',
    version='0.2.1',
    author='ELIXIR Europe',
    author_email='vani11537@one.ducic.ac.in',
    description='bravado generated mock GA4GH TES client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    url='https://github.com/elixir-europe/TES-cli',
    packages=find_packages(),
    keywords=(
        'ga4gh tes elixir client restful api app openapi '
        'swagger python bravado'
    ),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=['bravado[fido]'],
    python_requires='>=3'
)
