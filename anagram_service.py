from state_dao import StateDao
from utils import chunk_map_keys


class AnagramService:
    def __init__(self, state_dao: StateDao):
        print('initializing anagram service')
        self.state_dao = state_dao

    def process_input(self, word):
        final_dict = {}
        for char in word:
            code = ord(char)
            if code in final_dict:
                final_dict[code] = final_dict[code] + 1
            else:
                final_dict[code] = 1

        for key in final_dict.keys():
            self.state_dao.update_word_count(key, final_dict[key])

    def get_all_word(self):
        final_data = []
        resp = []
        for i in chunk_map_keys(list(range(0, 256)), 100):
            keys_list = list(i.keys())
            objects_list = self.state_dao.get_non_zero_word_count(keys_list)
            final_data.append(objects_list)

        for objects_list in final_data:
            for object_value in objects_list:
                resp.append(object_value)

        return resp

    def get_all_eligible_word(self):
        resp = self.get_all_word()
        final_dict = {}
        for object_dict in resp:
            if object_dict['b'] != 0:
                word_code = object_dict['a']
                char = chr(word_code)
                resp = {char: object_dict['b']}
                final_dict = {**final_dict, **resp}

        return final_dict
