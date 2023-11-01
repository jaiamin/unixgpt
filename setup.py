from setuptools import setup

from unixgpt.constants import VERSION

setup(
    name="unixgpt",
    version=VERSION,
    packages=["unixgpt"],
    entry_points={
        "console_scripts": [
            "unixgpt = unixgpt.__main__:main"
        ]
    },
)