# lisPy

> A lisp inside python.

## Setup

- Download with `git clone https://github.com/a11ce/lispy.git`
- Get [pytest](pytest.org) with `python3 -m pip install pytest`
- Run tests with `python3 -m pytest tests.py`

## Usage

- For REPL, run `python3 lispy.py`.
- To use within Python (this will soon be much easier), do:
```python
import lispy
lispy.runProg("(* 2 3 7)")
```
- You can generally use [built-in python functions](https://docs.python.org/3/library/functions.html) and anything defined in [the initial dictionary](../master/initDefs.py) but things may be broken or missing. Please open an issue if you notice anything! Check [the tests](../master/tests.py) for usage examples. 

## File summary
- `lispy.py`: The interpreter
- `initDefs.py`: The initial dictionary and helper functions for lisPy
- `tests.py`: Tests, many of which come from the racket docs

--- 

All contributions are welcome by pull request or issue.

lisPy is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.
