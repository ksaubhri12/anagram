from state_dao import StateDao


class StateDaoTestImpl(StateDao):

    def update_word_count(self, word_code: int, word_count: int):
        return True

    def get_non_zero_word_count(self, keys: [int]):
        object_list = [{'a': 67, 'b': 5}, {'a': 68, 'b': 9}, {'a': 88, 'b': 0}]
        return object_list
