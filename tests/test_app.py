from app.main import add_func, substract

def test_answer():
    assert add_func(10, 5) == 15

def test_substract():
    assert substract(10, 5) == 5