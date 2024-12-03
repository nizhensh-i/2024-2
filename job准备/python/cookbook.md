# collection.deque 

*class* collections.deque([*iterable*[, *maxlen*]])

本质是一个双端队列，在任意一边可进行append和pop，在两个方向上的大致性能均为 *O*(1)。

如果 `maxlen` 没有指定或者是 None，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。

应用：保存有限的历史记录（比如最后N个数据; 维护一个近期添加元素的序列）



# 找到最大或最小的N个元素

