import boto3


def check_player_exists(player_name, table):
    response = table.get_item(Key={"PlayerName": player_name})
    return response.get('Item') is not None

def add_player(player_name, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('game')


    if check_player_exists(player_name, table):
        print("Player name already exists")
        return 0

    player = {
        "PlayerName": player_name,

        "info": {
            "score": [],
            "highest": 0
        }
    }

    print("Adding player:", player["PlayerName"])
    table.put_item(Item=player)

    return player_name

if __name__ == '__main__':
    name = input("enter name: ")
    add_player(name)