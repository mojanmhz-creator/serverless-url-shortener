import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("links-test")

def lambda_handler(event, context):
    code = event.get("code", "abc123")
    response = table.get_item(Key={"code": code})
    item = response.get("Item")
    if not item:
        return {"statusCode": 404, "body": json.dumps({"error": "not found"})}
    return {"statusCode": 200, "body": json.dumps({"url": item["url"]})}