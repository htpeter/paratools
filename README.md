# `paratools``
A python library that lets you import Python code blocks from your Obsidian PARA project into a python project. Write notes when researching and import than later without needing to have 2 things open at once. Focus on your current studies!!!!

# Install

The most recent version deployed to PyPi was [[INSERT PYPI WIDGET HERE]]
```
python -m pip install paratools
```

# Defining Code Blocks

```python
# {"executable" : "true", "lib" : "para.matrix_generators"}
import numpy as np

rand_int_array = lambda size: np.random.randint(0, 60, size=size)
```

And then in the project with paratools installed, you'd use it like 

```python
from para.matrix_generators import rand_int_array

rand_array = rand_int_array(size = 5)
print(rand_array)
```

#### How would paratools install?

```
pip install paratools

paratools init

vim paratools.config

[default]
path=/Username/pmk/Dropbox/PARA
libname=para
```

Then it builds `./paratools` and appends that to `PYTHONPATH`.

```
paratools build
```