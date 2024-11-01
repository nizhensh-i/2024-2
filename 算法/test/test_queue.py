def test_enqueue(queue):
    assert queue.enqueue(9)
    queue.enqueue(0)
    queue.enqueue(7)
    assert not queue.enqueue(1)


def test_dequeue(queue):
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    queue.dequeue()
    queue.dequeue()
    assert not queue.dequeue()


def test_is_empty(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()


def test_is_full(queue):
    queue.enqueue(0)
    queue.enqueue(0)
    queue.enqueue(2)
    assert queue.is_full()


def test_size(queue):
    assert queue.size() == 4
