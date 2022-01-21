Building upon / modifying [Python Testing and Continuous
Integration](https://carpentries-incubator.github.io/python-testing/)


Write file with function to calculate GC content - `gccalc.py`:

```python gccalc.py
def calc_gc_content(seq):
    gc_count = (seq.upper().count("G") + seq.upper().count("C")) * 100
    gc_value = gc_count / len(seq)
    return gc_value
```

Write file with tests. The function to be tested is imported. `test_gccalc.py`

```python
from gccalc import calc_gc_content

def test_mid_gc():
    seq = "GCGCGCATATAT"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp

def test_high_gc():
    seq = "GGGGGCCCCC"
    obs = calc_gc_content(seq)
    exp = 100.0
    assert obs == exp

def test_low_gc():
    seq = "ATATATAT"
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp    

def test_empty_seq():
    seq = ""
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp

test_mid_gc()
test_high_gc()
test_low_gc()
test_empty_seq()
```

The test functions are called at the end of the file. I the file is
executed with Python they are run.

```
$ python test_gccalc.py
Traceback (most recent call last):
  File "/home/kuf/data/Arbeit/ZB_MED/The_Carpentries/Bits_and_pieces_for_the_carpentries_workshops/python/Python_Testing_and_Continuous_Integration_extension/test_gccalc.py", line 30, in <module>
    test_empty_seq()
  File "/home/kuf/data/Arbeit/ZB_MED/The_Carpentries/Bits_and_pieces_for_the_carpentries_workshops/python/Python_Testing_and_Continuous_Integration_extension/test_gccalc.py", line 23, in test_empty_seq
    obs = calc_gc_content(seq)
  File "/home/kuf/data/Arbeit/ZB_MED/The_Carpentries/Bits_and_pieces_for_the_carpentries_workshops/python/Python_Testing_and_Continuous_Integration_extension/gccalc.py", line 5, in calc_gc_content
    gc_value = gc_count / len(seq)
ZeroDivisionError: division by zero
```

We remove the function calls at the end of the file in the `test_gccalc.py:

```python
from gccalc import calc_gc_content

def test_mid_gc():
    seq = "GCGCGCATATAT"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp

def test_high_gc():
    seq = "GGGGGCCCCC"
    obs = calc_gc_content(seq)
    exp = 100.0
    assert obs == exp

def test_low_gc():
    seq = "ATATATAT"
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp    

def test_empty_seq():
    seq = ""
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp
```

... and now use pytest.

```
$ pytest

============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: [...]/python/Python_Testing_and_Continuous_Integration_extension
collected 0 items / 1 error

==================================== ERRORS ====================================
_______________________ ERROR collecting test_gccalc.py ________________________
test_gccalc.py:30: in <module>
    test_empty_seq()
test_gccalc.py:23: in test_empty_seq
    obs = calc_gc_content(seq)
gccalc.py:3: in calc_gc_content
    gc_value = gc_count / len(seq)
E   ZeroDivisionError: division by zero
=========================== short test summary info ============================
ERROR test_gccalc.py - ZeroDivisionError: division by zero
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.05s ===============================
			
```

To adresse the error in the GC calculation of we extend the
function. `test_gccalc.py`:

```python
def calc_gc_content(seq):
    if len(seq) == 0:
        return 0.0
    gc_count = (seq.upper().count("G") + seq.upper().count("C")) * 100
    gc_value = gc_count / len(seq)
    return gc_value
```

Now all test pass:

```
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: [...]/Python_Testing_and_Continuous_Integration_extension
collected 4 items

test_gccalc.py ....                                                      [100%]

============================== 4 passed in 0.01s ===============================
```

Let's run pytest with the `-v` flag.

```pytest -v
============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- python3.9
cachedir: .pytest_cache
rootdir: [...]/Python_Testing_and_Continuous_Integration_extension
collecting ... collected 4 items

test_gccalc.py::test_mid_gc PASSED                                       [ 25%]
test_gccalc.py::test_high_gc PASSED                                      [ 50%]
test_gccalc.py::test_low_gc PASSED                                       [ 75%]
test_gccalc.py::test_empty_seq PASSED                                    [100%]

============================== 4 passed in 0.01s ===============================
```

Extend `test_gccalc.py` to 

```python
from gccalc import calc_gc_content

def test_mid_gc():
    seq = "GCGCGCATATAT"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp

def test_high_gc():
    seq = "GGGGGCCCCC"
    obs = calc_gc_content(seq)
    exp = 100.0
    assert obs == exp

def test_low_gc():
    seq = "ATATATAT"
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp    

def test_empty_seq():
    seq = ""
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp

def test_invalid_characters():
    seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp
```

```pytest
============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: [...]/Python_Testing_and_Continuous_Integration_extension
collected 5 items

test_gccalc.py ....F                                                     [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_characters ____________________________

    def test_invalid_characters():
        seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
        obs = calc_gc_content(seq)
        exp = 50.0
>       assert obs == exp
E       assert 40.0 == 50.0

test_gccalc.py:31: AssertionError
=========================== short test summary info ============================
FAILED test_gccalc.py::test_invalid_characters - assert 40.0 == 50.0
========================= 1 failed, 4 passed in 0.02s ==========================

```

Extending `test_gccalc.py` to skip the test:

```python
from gccalc import calc_gc_content
import pytest

def test_mid_gc():
    seq = "GCGCGCATATAT"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp

def test_high_gc():
    seq = "GGGGGCCCCC"
    obs = calc_gc_content(seq)
    exp = 100.0
    assert obs == exp

def test_low_gc():
    seq = "ATATATAT"
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp    

def test_empty_seq():
    seq = ""
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp

@pytest.mark.skip(reason="Cleaning not yet implemented.")    
def test_invalid_characters():
    seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp
```


When surring Not the `s` indicated to be skipped:

```pytest
============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: [...]/Python_Testing_and_Continuous_Integration_extension
collected 5 items

test_gccalc.py ....s                                                     [100%]

========================= 4 passed, 1 skipped in 0.01s =========================

```

an the the verbose version:

```pytest -v
============================= test session starts ==============================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- python3.9
cachedir: .pytest_cache

rootdir: [...]/Python_Testing_and_Continuous_Integration_extension
collecting ... collected 5 items

test_gccalc.py::test_mid_gc PASSED                                       [ 20%]
test_gccalc.py::test_high_gc PASSED                                      [ 40%]
test_gccalc.py::test_low_gc PASSED                                       [ 60%]
test_gccalc.py::test_empty_seq PASSED                                    [ 80%]
test_gccalc.py::test_invalid_characters SKIPPED (Cleaning not yet im...) [100%]

========================= 4 passed, 1 skipped in 0.01s =========================

```
