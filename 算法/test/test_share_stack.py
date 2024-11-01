def test_push1(share_stack):
    share_stack.push2(1)
    assert not share_stack.push1(3)


def test_push2(share_stack):
    share_stack.push2(8)
    assert not share_stack.push2(3)

def test_pop1(share_stack):
    assert share_stack.pop1() == 11
    assert share_stack.pop1() == 8
    share_stack.pop1()
    share_stack.pop1()
    share_stack.pop1()
    assert not share_stack.pop1()


def test_pop2(share_stack):
    assert share_stack.pop2() == 1
    assert share_stack.pop2() == 9
    share_stack.pop2()
    share_stack.pop2()
    assert not share_stack.pop2()


def test_is_empty(share_stack):
    share_stack.pop1()
    share_stack.pop1()
    share_stack.pop1()
    share_stack.pop1()
    share_stack.pop1()
    assert share_stack.is_empty1()

    share_stack.pop2()
    share_stack.pop2()
    share_stack.pop2()
    share_stack.pop2()
    assert share_stack.is_empty2()

def test_size(share_stack):
    assert share_stack.size() == 9

    share_stack.pop2()
    assert share_stack.size() == 8
