import boto3
import json
import sys

if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

textract = boto3.client('textract', 'us-east-2')
with open(sys.argv[1], 'rb') as file:
    result = textract.analyze_document(
        Document={'Bytes': file.read()},
        FeatureTypes=['TABLES', 'FORMS'])
    print(json.dumps(result, indent=4))
