from state_dao import StateDao
import boto3


class StateDaoDynamoImpl(StateDao):

    def __init__(self):
        print('initializing state dao dynamo')
        self.table_name = 'anagrams'
        self.resources = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id='AKIAT56UZRYZNCGR2R5A',
                                        aws_secret_access_key='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')
        self.word = 'kalpesh'
        self.table = self.resources.Table(self.table_name)

    def update_word_count(self, word_code: int, word_count: int):
        self.table.update_item(
            Key={
                'a': word_code
            },
            UpdateExpression="ADD b:val",
            ExpressionAttributeValues={
                ":val": 1
            },
            ReturnValues='ALL_NEW'
        )
        return True

    def get_non_zero_word_count(self, keys: [int]):
        lookup_key_index = []
        for key in keys:
            data = {'a': key}
            lookup_key_index.append(data)

        resp = self.resources.batch_get_item(
            RequestItems={
                self.table_name: {
                    'Keys': lookup_key_index
                }
            }
        )
        items = resp['Responses'][self.table_name]
        object_dict_list = []
        for item in items:
            char_code_decimal = int(item['a'])
            char_code_count = int(item['b'])
            object_dict = {'a': char_code_decimal, 'b': char_code_count}
            object_dict_list.append(object_dict)

        return object_dict_list
