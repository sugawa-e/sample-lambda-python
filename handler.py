def hello(event, context):
    body = {
        "message": "Hello from Lambda!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
