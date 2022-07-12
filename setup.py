from setuptools import setup

setup(
    name='arxiv',
    version="0.1",
    description="",
    url='https://gitlab.idiap.ch/apannatier/arxiv',
    author="Arnaud Pannatier",
    author_email="arnaud.pannatier@idiap.ch",
    license="MIT",
    packages=[""],
    entry_points={
        'console_scripts': [
            'arxivsave=arxiv.cli:save',
        ],
    },
)
