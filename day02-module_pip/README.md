## Day 3 - Modules and pip in Python!

Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:
1. Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
2. External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

## The pip command

It can be used as a package manager [pip](https://pip.pypa.io/en/stable/) to install a python module.
Lets install a module called pandas using the following command

```bash
pip install pandas
```

## Using a module in Python (Usage)
We use the import syntax to import a module in Python. Here is an example code:

```python
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file
 
```

Similarly we can install other modules and look into their documentations for usage instructions.

## what is REPL?
Once we have installed Python 3, we can do some minimal interaction with Python to assure ourselves that things are working. In the long run, we'll use a number of other tools to create Python programs. To start out, we'll interact directly on the command line.

Python's Read-Evaluate-Print Loop (REPL) is the foundation for Python programming. More sophisticated things—such as writing application scripts or web servers—are essentially the same as interaction with the REPL: the Python program reads statements from our application script file or web server script file and evaluates those statements.

This fundamental rule is one of the very appealing features of Python. We can write sophisticated scripts, or we can interact with the language in the REPL; the language is the same.

