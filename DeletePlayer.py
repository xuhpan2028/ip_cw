import boto3

def delete_player(player_name, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    
    table = dynamodb.Table('game')
    response = table.delete_item(

        Key={
            'PlayerName': player_name
        }
    )
         
    return response

if __name__ == '__main__':
    name = input("enter name: ")
    delete_player(name)
    print("deteted")