## Dependency Management in Python

Managing project dependencies (external libraries) is an important part of Python development. Proper management ensures
your project works consistently across different computers and servers.

---

### UNDERSTANDING PIP

`pip` is the **standard package manager** for Python. It allows you to install and manage additional libraries that are
not
part of the Python standard library. These libraries are usually hosted on the Python Package Index (PyPI).

1. **INSTALLING A LIBRARY**: To install a library, use the `install` command in your terminal:
   `pip install <library-name>`. Example: `pip install Django` where this command will download and install the **Django
   Web Framework** so you can use it in your code.
2. **SAVING YOUR DEPENDENCIES**: To share your project, you need a list of everything you've installed. We store this in
   a file called `requirements.txt`. To create this file, run: `pip freeze > requirements.txt`.
3. **INSTALLING FROM A REQUIREMENTS FILE**: If you download someone else's project and see a `requirements.txt` file,
   you can install everything listed in it at once using: `pip install -r requirements.txt`

Before running `pip install`, it is best practice to create a **Virtual Environment**. This is a private _sandbox_ for
your project so that your libraries don't conflict with other projects on your computer.

---