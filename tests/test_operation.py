from appgithubaction.src.math_operation import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_subtract():
    assert sub(2,3)==-1
    assert add(7,5)==2