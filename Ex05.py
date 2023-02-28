from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_old_movie(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression="#yr < :year",
        ExpressionAttributeValues={
            ":year": year
        },
        ExpressionAttributeNames={
            "#yr": "year"
        }
    )
    items = response["Items"]
    with table.batch_writer() as batch:
        for item in items:
            batch.delete_item(Key={"year": item["year"], "title": item["title"]})

if __name__ == '__main__':
    print("Attempting a conditional delete...")
    delete_response = delete_old_movie(2000)
    if delete_response:
        print("Delete movie succeeded:")
        pprint(delete_response)
