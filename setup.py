from setuptools import setup, find_packages

from unixgpt.constants import VERSION


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="unixgpt",
    version=VERSION,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "unixgpt = unixgpt.__main__:main"
        ]
    },
)
