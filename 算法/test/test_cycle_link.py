from ds.cycle_link import CycleLinkedList


def test_travel(cycle_link):
    assert cycle_link.travel() == [1, 20, 8, 90]
    # assert cycle_link.travel() == [90,8,20,1]


def test_is_empty():
    cycle_link = CycleLinkedList()
    assert cycle_link.is_empty()

    cycle_link.tail_add(45)
    assert not cycle_link.is_empty()


def test_length():
    cycle_link = CycleLinkedList()
    assert cycle_link.length() == 0

    cycle_link.head_add(12)
    assert cycle_link.length() == 1
