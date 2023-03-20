import boto3

def show_score(player_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('game')

    response = table.get_item(Key={"PlayerName": player_name})
    if response.get('Item') is None:
        print("Player does not exist.")
        return

    player = response['Item']
    scores = player['info']['score']
    highest_score = player['info']['highest']

    print("highest: ", highest_score)
    print("history: ", scores)

    return highest_score, scores



if __name__ == '__main__':
    player_name = input("enter the player name: ")

    show_score(player_name)
