# A minimal package example

This is a template for a local package called `fiberoo`. To install this package in develop mode:

```sh
git clone http://github.com/patrickmineault/minimal-package.git
cd minimal-package
pip install -e .
```

`-e` enables development mode, meaning you don't need to reinstall your package everytime you change something inside. From this point on you can import this package from anywhere inside your environment - it doesn't matter what the path or the current irectory, you can always use:

```python
import fiberoo
```

Important bits:

* You should have a `setup.py` file which calls the setup function
* You should have a directory `package_name` that is refered to in setup.py
* You should have an `__init__.py` inside the `package_name` directory

By default, each file inside of the `package_name` directory will create its own module. For example, here we'd have to `import fiberoo.fib` to be able to access `fiberoo.fib.the_fibsteroo()`. We can change this behaviour by defining symbols inside of `__init__.py`. `from .fib import *` lifts `the_fibsteroo` to package level, that is, we can now use:

```python
import fiberoo
assert fiberoo.the_fibsteroo(30) == 832040
```

Original example lifted from: https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
