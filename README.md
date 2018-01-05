# datamodelutils
wrapper utils to allow gdcdatamodel.models to be loaded after initialization

```
In [1]: from dictionaryutils import DataDictionary, dictionary

In [2]: from datamodelutils import models

In [3]: d = DataDictionary(url="https://s3.amazonaws.com/dictionary-artifacts/bhcdictionary/feat/s3/schema.json")

In [4]: dictionary.init(d)

In [5]: from gdcdatamodel import models as md

In [6]: models.init(md)

In [7]: models
Out[7]: <module 'gdcdatamodel.models' from '/Users/phillis/Documents/work/gdcdatamodel/gdcdatamodel/models/__init__.pyc'>
```
