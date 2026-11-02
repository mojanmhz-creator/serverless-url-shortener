import json
import secrets
import string
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("links")

ALPHABET = string.ascii_letters + string.digits

def make_code(length=6):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))

def lambda_handler(event, context):
    body = event.get("body", event)
    if isinstance(body, str):
        body = json.loads(body)

    url = body.get("url", "")
    if not url.startswith(("http://", "https://")):
        return {"statusCode": 400, "body": json.dumps({"error": "url must start with http:// or https://"})}

    code = make_code()
    table.put_item(Item={"code": code, "url": url}, ConditionExpression="attribute_not_exists(code)")

    return {"statusCode": 200, "body": json.dumps({"code": code, "url": url})}