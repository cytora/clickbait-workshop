import sys

try:
    import pytest
except ImportError:
    print("Please install pytest.")
    sys.exit(0)

def test_python3():
    assert sys.version_info.major == 3

def test_pandas():
    import pandas

def test_sklearn():
    import sklearn
    from sklearn.model_selection import train_test_split

def test_matplotlib():
    import matplotlib

def test_notebook():
    import notebook

def test_flask():
    import flask

if __name__ == "__main__":
    pytest.main(["-v", __file__])
