import boto3

def add_score(player_name, new_score, dynamodb=None):
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

    scores.append(new_score)
    highest_score = max(scores)

    table.update_item(
        Key={
            'PlayerName': player_name,
        },
        UpdateExpression='SET info.score = :s, info.highest = :h',
        ExpressionAttributeValues={
            ':s': scores,
            ':h': highest_score
        }
    )

    print("Score added for player:", player_name)


if __name__ == '__main__':
    player_name = input("enter the player name: ")
    new_score = input("enter the new score: ")

    add_score(player_name, new_score, dynamodb=None)
