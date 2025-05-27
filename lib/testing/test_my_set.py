import pytest
from lib.MySet import MySet

def test_init_with_values():
    s = MySet([1, 2, 2, 3])
    assert s.size() == 3
    assert s.has(1)
    assert s.has(2)
    assert s.has(3)

def test_add():
    s = MySet()
    s.add(5)
    assert s.has(5)
    assert s.size() == 1

def test_has():
    s = MySet([1, 2])
    assert s.has(1)
    assert not s.has(3)

def test_delete():
    s = MySet([1, 2, 3])
    s.delete(2)
    assert not s.has(2)
    assert s.size() == 2

def test_size():
    s = MySet([1])
    assert s.size() == 1
    s.add(2)
    assert s.size() == 2
    s.delete(1)
    assert s.size() == 1

def test_clear():
    s = MySet([1, 2, 3])
    s.clear()
    assert s.size() == 0
    assert not s.has(1)

def test_str():
    s = MySet([10, 20])
    output = str(s)
    # Accept either order since dict keys are unordered
    assert output in ["MySet: {10, 20}", "MySet: {20, 10}"]
