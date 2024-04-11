class FlatIterator:
    def __init__(self, list_of_list):
        self.current_list = list_of_list
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.current_list):
            raise StopIteration

        while not isinstance(self.current_list[self.current_index], list) or len(self.current_list[self.current_index]) == 0:
            if self.current_index < len(self.current_list) - 1:
                self.current_index += 1
            else:
                raise StopIteration

        item = self.current_list[self.current_index].pop(0)

        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
