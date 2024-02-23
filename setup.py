from setuptools import setup, find_packages



if __name__ == '__main__':
    setup(
        name='db_translator',
        version='0.0.1',
        author='rodya',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'greenlet == 3.0.3',
            'Jinja2 == 3.1.3',
            'MarkupSafe == 2.1.5',
            'psycopg2 == 2.9.9',
            'python-dotenv == 1.0.0',
            'SQLAlchemy == 2.0.27',
            'typing_extensions == 4.9.0',
        ]
    )