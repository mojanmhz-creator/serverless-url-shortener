import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("links")

def lambda_handler(event, context):
    code = (event.get("pathParameters") or {}).get("code", "")
    if not code:
        return {"statusCode": 400, "body": json.dumps({"error": "missing code"})}

    response = table.get_item(Key={"code": code})
    item = response.get("Item")
    if not item:
        return {"statusCode": 404, "body": json.dumps({"error": "not found"})}

    return {"statusCode": 302, "headers": {"Location": item["url"]}, "body": ""}