from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def scan_movies(actor, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')

    #scan and get the first page of results
    response = table.scan(FilterExpression="contains(info.actors, :actor)",
                              ExpressionAttributeValues={":actor": actor}
                              );
    data = response['Items']
    display_movies(data)

    #continue while there are more pages of results
    while 'LastEvaluatedKey' in response:
        response = table.scan(FilterExpression="contains(info.actors, :actor)",
                              ExpressionAttributeValues={":actor": actor},
                              ExclusiveStartKey=response['LastEvaluatedKey']
                              )
        data.extend(response['Items'])
        display_movies(data)

    return data

if __name__ == '__main__':
    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}")
            #pprint(movie['info'])
            #pprint(movie)

    query_name = "Tom Hanks"
    print(f"Scanning for movies starred {query_name}...")
    scan_movies(query_name, print_movies)
