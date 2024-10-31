
def test_insert(link):
    link.insert(3, 7)
    assert link.travel() == [1, 10, 7, 11, 6]

    link.insert(-5, 9)
    assert link.travel() == [9, 1, 10, 7, 11, 6]

    link.insert(19, 19)
    assert link.travel() == [9, 1, 10, 7, 11, 6, 19]


def test_remove_first(link):
    link.remove(1)
    assert link.travel() == [10, 11, 6]


def test_remove_mid(link):
    link.remove(10)
    assert link.travel() == [1, 11, 6]


def test_remove_last(link):
    link.remove(6)
    assert link.travel() == [1, 10, 11]

def test_remove_other(link):
    assert not link.remove('23')