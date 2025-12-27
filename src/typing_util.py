from typing import Any


def assert_some[T](val: T | None) -> T:
    assert val is not None, "Exepected `val` to be not None"
    return val


def assert_type[T](value: Any, type_: type[T]) -> T:
    assert isinstance(value, type_), f"value {value} is not of type {type_}"
    return value
