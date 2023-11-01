from setuptools import setup, find_packages

from unixgpt.constants import VERSION

setup(
    name="unixgpt",
    version=VERSION,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "unixgpt = unixgpt.__main__:main"
        ]
    },
)

"""unixgpt -i "Create two directories in CWD: hello-world and test-project. After creating bot
h of these, list the files"""
