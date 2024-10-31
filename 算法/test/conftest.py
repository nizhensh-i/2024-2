import pytest
from ds.link import LinkedList
from ds.cycle_link import CycleLinkedList
from ds.d_link import DLinkedList
from ds.cycle_d_link import CycleDLink


@pytest.fixture()
def link():
    link = LinkedList()
    link.tail_add(1)
    link.tail_add(10)
    link.tail_add(11)
    link.tail_add(6)
    return link


@pytest.fixture()
def cycle_link():
    cycle_link = CycleLinkedList()
    cycle_link.tail_add(1)
    cycle_link.tail_add(20)
    cycle_link.tail_add(8)
    cycle_link.tail_add(90)

    # cycle_link.head_add(1)
    # cycle_link.head_add(20)
    # cycle_link.head_add(8)
    # cycle_link.head_add(90)
    return cycle_link


@pytest.fixture()
def d_link():
    d_link = DLinkedList()
    # d_link.head_add(1)
    # d_link.head_add(8)
    # d_link.head_add(0)
    # d_link.head_add(2)

    d_link.tail_add(9)
    d_link.tail_add(0)
    d_link.tail_add(1)
    d_link.tail_add(23)

    return d_link


@pytest.fixture()
def cycle_d_link():
    cycle_d_link = CycleDLink()
    # cycle_d_link.tail_add(3)
    # cycle_d_link.tail_add(8)
    # cycle_d_link.tail_add(10)
    # cycle_d_link.tail_add(90)

    cycle_d_link.head_add(90)
    cycle_d_link.head_add(2)
    cycle_d_link.head_add(1)
    cycle_d_link.head_add(20)
    return cycle_d_link
