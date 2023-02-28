import boto3

def check_player_exists(player_name, table):
    response = table.get_item(Key={"PlayerName": player_name})
    return response.get('Item') is not None

def add_player(dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('game')

    while True:
        player_name = input("Enter player name: ")
        if check_player_exists(player_name, table):
            print("Player name already exists. Please enter a different name.")
        else:
            break

    player = {
        "PlayerName": player_name,

        "info": {
            "score": [],
            "highest": 0
        }
    }

    print("Adding player:", player["PlayerName"])
    table.put_item(Item=player)

if __name__ == '__main__':
    add_player(dynamodb=None)