def test_pop(stack):
    assert stack.pop() == 6
    assert stack.pop() == 1
    assert not stack.pop()


def test_push(stack):
    stack.push(7)
    stack.push(3)
    stack.push(0)
    stack.push(2)
    stack.push(25)
    assert not stack.push(20)


def test_size(stack):
    assert stack.size() == 2


def test_get_top(stack):
    assert stack.get_top() == 6


def test_is_empty(stack):
    assert not stack.is_empty()
    stack.pop()
    stack.pop()
    assert stack.is_empty()
