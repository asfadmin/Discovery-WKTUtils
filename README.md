# Discovery-WKTUtils

### To Install as Package, add the following line to requirements.txt:

```bash
git+https://github.com/asfadmin/Discovery-WKTUtils.git@prod#egg=WKTUtils
```

(The package name will be 'WKTUtils'. You can change 'prod' to desired branch).

### Install the requirements file:

```bash
python3 -m pip install -r requirements.ext --upgrade
```

### FilesToWKT:
You must open the file in read binary mode, before passing it into the function.

```python
from WKTUtils.FilesToWKT import filesToWKT
f = open("path/to/file.shp", "rb")
# NOTE: f can be a list of files too. filesToWKT([f1, f2, ...]).getWKT()
wkt = filesToWKT(f).getWKT()
```
