from project import *

def test_filter_python_resources():
    assert filter_python_resources("Articles", "Beginner") == "python"

def test_filter_cpp_resources():
    assert filter_cpp_resources("Articles", "Beginner") == "cpp"

def test_filter_java_resources():
    assert filter_java_resources("Articles", "Beginner") == "java"

