def hello(event, context):
    body = {
        "message": "Hello world!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
