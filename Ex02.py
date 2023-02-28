import boto3
from boto3.dynamodb.conditions import Key

def query_movies(year, title, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year) &
                               Key('title').eq(title)
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1985
    query_title = 'After Hours'
    print(f"Movie detail:")
    movies = query_movies(query_year, query_title)
    for movie in movies:
        print(movie['year'], ":", movie['title'])
        print(movie['info'])
