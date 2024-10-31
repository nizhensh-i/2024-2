def test_travel(d_link):
    # assert d_link.travel() == [2,0,8,1]
    assert d_link.travel() == [9, 0, 1, 23]


def test_remove(d_link):
    d_link.remove(1)
    assert d_link.travel() == [9, 0, 23]

    d_link.remove(23)
    assert d_link.travel() == [9, 0]

    d_link.remove(9)
    assert d_link.travel() == [0]

    d_link.remove(0)
    assert d_link.is_empty()
