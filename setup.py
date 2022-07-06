from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

pypi_package_name = "Package Name"
cli_command = "cli-command"
local_package_name = "package_folder"

setup(
    version="Semantic version number", # Edit Me
    name=pypi_package_name,
    description="Short Description", # Edit Me
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url='',
    author="Joaquim Gomez",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["List", "Of", "Requirements"], # Edit Me
    entry_points={"console_scripts": [f"{cli_command}={local_package_name}.cli:main"]},
)