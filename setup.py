from setuptools import setup, find_packages

setup(
    name='datamodelutils',
    version='0.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'datamodel_postgres_admin=datamodelutils.postgres_admin:main',
            'datamodel_repl=datamodelutils.repl:main'
        ]
    },
)
