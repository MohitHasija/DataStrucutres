from priority_queue import PriorityQueue
import unittest



class PriorityQueueTests(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()

    def test_add_two_elements_in_queue(self):
        self.queue.push("Random 1", 34)
        self.queue.push("Random 2", 1)
        assert "Random 2" == self.queue.pop()

    def test_add_then_pop_then_add_in_queue(self):
        self.queue.push("Random 1", 34)
        self.queue.push("Random 2", 1)
        self.queue.push("Random 5", 12)
        assert "Random 2" == self.queue.pop()
        assert "Random 5" == self.queue.pop()

        self.queue.push("Random3", 23)
        assert "Random3" == self.queue.pop()

    def test_priority_converter_in_queue(self):



if __name__=='__main__':
    unittest.main()