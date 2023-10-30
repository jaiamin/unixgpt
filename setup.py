from setuptools import setup
from unixgpt.settings import VERSION

setup(
    name="unixgpt",
    version=VERSION,
    packages=["unixgpt"],
    entry_points={
        "console_scripts": [
            "unixgpt = unixgpt.cli:main",
        ],
    },
)