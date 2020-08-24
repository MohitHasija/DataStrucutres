from __future__ import print_function



class PriorityQueue(object):
    MOST_PRIORITY = 1

    def __init__(self, priority_converter=None):
        self._queue = []
        self._priority_converter = priority_converter

    def convert_priority_to_integer(self, priority):
        if not self._priority_converter:
            return priority
        else:
            return self._priority_converter(priority)

    def push(self, element, priority):
        if self.convert_priority_to_integer(priority) == PriorityQueue.MOST_PRIORITY:
            self._queue.insert(PriorityQueue.MOST_PRIORITY-1, tuple([element, PriorityQueue.MOST_PRIORITY]))
            return
        element_priority = self.convert_priority_to_integer(priority)
        index = 0
        while True:
            try:
                _, priority = self._queue[index]
            except IndexError:
                self._queue.append(tuple([element, element_priority]))
                break

            if priority >= element_priority:
                self._queue.insert(index, tuple([element, element_priority]))
                break
            index += 1

    def pop(self):
        element, _ = self._queue.pop(0)
        return element
