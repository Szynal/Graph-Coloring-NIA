# Graph-Coloring-NIA

## Authors

Paweł Szynal

Kamil Zdeb

## Dataset

The dataset for testing (graphs) is stored in the "graphs" folder. With the help of the program you can generate a new data set ("graphs.py").

## Running 

The program works in terminal (console version). The GUI  is under development. Please run the script with "menu.py"

Running is really easy. The only thing you need is [Python 3](https://www.python.org/downloads/).

Create a virtual environment via the command:

    python3 -m venv venv

This creates the folder `venv/` in your current directory. It will contain the necessary libraries for running the examples.

To activate the virtual environment, use the following command:

```
# On Windows:
call venv\Scripts\activate.bat
# On Mac / Linux:
source venv/bin/activate
```

Now execute the following to install the necessary dependencies:

    pip install -Ur src/requirements.txt

You'll find a `.py` file there, typically `main.py`. You can run it with the command:

    python main.py

Please note that the virtual environment must still be active for this to work.


## Using PySide2

This repository uses PyQt5 to use Qt from Python. Another, alternative binding is PySide2 (also called "Qt for Python"). It is less mature than PyQt5 but has the advantage that you can use it for free in commercial projects.

If you want to use PySide2 instead of PyQt5, simply replace all mentions of the latter by the former. For instance, in [`src/requirements.txt`](src/requirements.txt), replace `PyQt5` by `PySide2`. Similarly for any code examples: `from PyQt5.QtWidgets ...` becomes `from PySide2.QtWidgets ...` etc.
