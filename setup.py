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


# When psqlgraph 2.x gets released on pypi, remove it from dependency_links
setup(
    name="datamodelutils",
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        "cdisutils",
        "psqlgraph~=2.0",
        "dictionaryutils>=1.2.0",
        "gen3dictionary~=2.0",
        "gen3datamodel~=2.0",
    ],
    dependency_links = [
        "git+https://git@github.com/uc-cdis/psqlgraph.git@2.0.1#egg=psqlgraph",
    ],
    entry_points={
        "console_scripts": [
            "datamodel_postgres_admin=datamodelutils.postgres_admin:main",
            "datamodel_repl=datamodelutils.repl:main",
        ]
    },
)
