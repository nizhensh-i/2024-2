import pytest
from ds.link import LinkedList
from ds.cycle_link import CycleLinkedList
from ds.d_link import DLinkedList
from ds.cycle_d_link import CycleDLink
from ds.stack import Stack
from ds.share_stack import ShareStack
from ds.queue import Queue
from ds.d_queue import Deque

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


@pytest.fixture()
def stack():
    s = Stack()
    s.push(1)
    s.push(6)
    return s


@pytest.fixture()
def share_stack():
    share_stack = ShareStack()
    share_stack.push1(3)
    share_stack.push1(1)
    share_stack.push1(0)
    share_stack.push1(8)
    share_stack.push1(11)

    share_stack.push2(4)
    share_stack.push2(0)
    share_stack.push2(9)
    share_stack.push2(1)
    return share_stack


@pytest.fixture()
def queue():
    q = Queue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(9)
    q.enqueue(0)
    return q


@pytest.fixture()
def deque():
    q = Deque()
    q.enqueue_front(2)
    q.enqueue_front(7)
    q.enqueue_front(12)
    q.enqueue_rear(8)
    q.enqueue_rear(0)
    q.enqueue_rear(1)
    return q