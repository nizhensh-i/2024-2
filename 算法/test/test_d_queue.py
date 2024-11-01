def test_dequeue_front(deque):
    assert deque.dequeue_front() == 12
    assert deque.dequeue_front() == 7
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_front()
    assert not deque.dequeue_front()

def test_dequeue_rear(deque):
    assert deque.dequeue_rear() == 1
    assert deque.dequeue_rear() == 0
    deque.dequeue_rear()
    deque.dequeue_rear()
    deque.dequeue_rear()
    deque.dequeue_rear()
    assert not deque.dequeue_rear()

def test_is_empty(deque):
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_front()
    assert deque.is_empty()

def test_size(deque):
    assert deque.size() == 6
