from state_dao_test_impl import StateDaoTestImpl
from state_dao_dynamo_impl import StateDaoDynamoImpl
from anagram_service import AnagramService

state_dao = StateDaoDynamoImpl()
anagram_service = AnagramService(state_dao)
if __name__ == '__main__':

    anagram_service.process_input('kalpeshk')
    resp = anagram_service.get_all_eligible_word()
    print(resp)
