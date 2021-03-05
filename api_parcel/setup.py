"""Setup configuration and dependencies for api_parcel."""

from setuptools import find_packages
from setuptools import setup


REQUIREMENTS = [requirement for requirement in open("requirements.txt").readlines()]

COMMANDS = [
    "example_command=api_parcel.tools.example:main",
    "start_api_server=api_parcel.app:main",
]

setup(
    name="api_parcel",
    version="0.0.0.alpha0",
    author="@@ki",
    author_email="yellowfoxh4xor@gmail.com",
    url="",
    include_package_data=True,
    description="Parcel status checker",
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    python_requires=">=3.6.6",
    entry_points={"console_scripts": COMMANDS},
    install_requires=REQUIREMENTS,
)
