from setuptools import setup, find_packages
from subprocess import check_output


def get_version():
    # https://github.com/uc-cdis/dictionaryutils/pull/37#discussion_r257898408
    try:
        tag = check_output(
            ["git", "describe", "--tags", "--abbrev=0", "--match=[0-9]*"]
        )
        return tag.decode("utf-8").strip("\n")
    except Exception:
        raise RuntimeError(
            "The version number cannot be extracted from git tag in this source "
            "distribution; please either download the source from PyPI, or check out "
            "from GitHub and make sure that the git CLI is available."
        )


setup(
    name="datamodelutils",
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        "cdisutils",
        "psqlgraph~=1.2",
        "dictionaryutils>=1.2.0",
        "gdcdictionary~=1.2",
        "gdcdatamodel~=1.1",
    ],
    entry_points={
        "console_scripts": [
            "datamodel_postgres_admin=datamodelutils.postgres_admin:main",
            "datamodel_repl=datamodelutils.repl:main",
        ]
    },
)
