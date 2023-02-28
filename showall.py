import boto3

def showall(dynamodb=None):
    
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('game')

    response = table.scan()
    items = response['Items']

    for item in items:
        print(item['PlayerName'], item['info'])


if __name__ == '__main__':
    showall()
