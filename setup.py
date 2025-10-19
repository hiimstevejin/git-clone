from setuptools import setup

setup(
    name="gitgud",
    version="1.0",
    packages=["gitgud"],
    entry_points={"console_scripts": ["gitgud = gitgud.cli:main"]},
)
