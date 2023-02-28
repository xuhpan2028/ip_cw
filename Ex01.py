from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')
    print(f"Get title")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="#yr, title",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=
            Key('year').eq(year)

    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1994

    print(f"Get movies from {query_year}")
    movies = query_and_project_movies(query_year)
    for movie in movies:
        print(f"\n {movie['title']}")
