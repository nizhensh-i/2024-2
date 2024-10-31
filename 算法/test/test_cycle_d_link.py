def test_travel(cycle_d_link):
    # assert cycle_d_link.travel() == [3,8,10,90]
    assert cycle_d_link.travel() == [20, 1, 2, 90]


def test_remove(cycle_d_link):
    cycle_d_link.remove(1)
    assert cycle_d_link.travel() == [20, 2, 90]

    cycle_d_link.remove(90)
    assert cycle_d_link.travel() == [20, 2]

    cycle_d_link.remove(20)
    assert cycle_d_link.travel() == [2]

    cycle_d_link.remove(2)
    assert cycle_d_link.is_empty()
