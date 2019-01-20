from colorama import Fore


def hello(event, context):
    response = {
        "statusCode": 200,
        "body": "{}HELLO".format(Fore.RED)
    }

    return response
