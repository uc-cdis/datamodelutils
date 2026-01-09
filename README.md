# datamodelutils

Wrapper utils to allow gen3datamodel.models to be loaded after initialization.

For example

```
from datamodelutils import models
from dictionaryutils import DataDictionary, dictionary

d = DataDictionary(url="https://s3.amazonaws.com/dictionary-artifacts/bhcdictionary/feat/s3/schema.json")

dictionary.init(d)
# Always import gen3datamodel after dictionary has been initialized.
# Creates a singleton for life of python session.
# Required for backward compatibility. 
from gen3datamodel import models as md
models.init(md)

print(models)
```

will produce output of

```
<module 'gen3datamodel.models' from '/Users/phillis/Documents/work/datamodelutils/venv/lib/python3.9/site-packages/gen3datamodel/gen3datamodel/models/__init__.py'>
```

# CLI Utilities

## datamodel_postgres_admin
Script to do database creation and migration
```
# setup all tables, this should be run when you initialize the database
> export PG_HOST=localhost
> export PG_USER=test
> export PG_PASS=test
> export PG_NAME=test_graph
> export DICTIONARY_URL="https://s3.amazonaws.com/dictionary-artifacts/<dictionary_repl>/<branch>/schema.json"
> datamodel_postgres_admin create-all

# setup/create new graph tables, this should be run for dictionary migrations that needs to setup new tables
datamodel_postgres_admin graph-create
```
## datamodel_repl
repl to interact with datamodel
```
> export PG_HOST=localhost
> export PG_USER=test
> export PG_PASS=test
> export PG_NAME=test_graph
> export DICTIONARY_URL="https://s3.amazonaws.com/dictionary-artifacts/<dictionary_repl>/<branch>/schema.json"
> datamodel_repl
Python 2.7.10 (default, Feb  7 2017, 00:08:15)
Type "copyright", "credits" or "license" for more information.

IPython 5.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: g.nodes(md.Project).first()
Out[1]: <Project(a77f549b-c74b-563e-80bb-570b5a4dde88)>
```
