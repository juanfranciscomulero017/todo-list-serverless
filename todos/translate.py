import boto3
import json
import os

from todos import decimalencoder

translate = boto3.client('translate')




dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }
    
    cadena1_traducida = translate.translate_text(Text=response,
                                          SourceLanguageCode="auto",
                                                                            TargetLanguageCode="en")

    lenguaje = input(cadena1_traducida["TranslatedText"])

    return lenguaje