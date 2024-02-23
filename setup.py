from setuptools import setup, find_packages
import pkg_resources
import pathlib

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

if __name__ == '__main__':
    setup(
        name='db_translator',
        version='0.0.1',
        author='rodya',
        packages=find_packages(),
        include_package_data=True,
        install_requires=install_requires
    )