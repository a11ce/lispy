# lisPy

> A lisp inside python.

## Setup

- Download with `git clone https://github.com/a11ce/lispy.git`
- Get [pytest](pytest.org) with `pip3 install pytest`
- Run tests with `pytest tests.py`

## Usage

- No standalone interpreter or REPL (yet), do:
```python
import lispy
lispy.runProg("(* 2 3 7)")
```
- You can generally use [built-in python functions](https://docs.python.org/3/library/functions.html) and anything defined in [the initial dictionary](../master/initDict.py) but there are (probably) a lot of caveats. Check [the tests](../master/tests.py) for usage examples. *I'll rewrite this once I figure out how to actually explain what the idea of this project is.*

## File summary
- `lispy.py`: The interpreter
- `initDict.py`: The initial dictionary for lisPy
- `tests.py`: Tests, many of which come from the racket docs

--- 

All contributions are welcome by pull request or issue.

lisPy is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.