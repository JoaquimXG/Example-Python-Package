from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='sample_package_xjg',

    version='0.0.2',

    description='A sample Python project',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # url='https://github.com/pypa/sampleproject',

    author='Joaquim Gomez',

    package_dir={'': 'src'},
    packages=find_packages(where='src'),

    python_requires='>=3.6, <4',

    install_requires=['click', 'pandas'],

    entry_points={
        'console_scripts': [
            'sample_package=sample_package.__main__:main'
        ],
    },
)