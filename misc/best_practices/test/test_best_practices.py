from best_practices import best_practices


def test_fib() -> None:
    assert best_practices.fib(0) == 0
    assert best_practices.fib(1) == 1
    assert best_practices.fib(2) == 1
    assert best_practices.fib(3) == 2
    assert best_practices.fib(4) == 3
    assert best_practices.fib(5) == 5
    assert best_practices.fib(10) == 55
