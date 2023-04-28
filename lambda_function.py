import boto3
import requests
import json
import datetime

def lambda_handler(event, context):

    # Set the required parameters for the API endpoint
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1,
        'sparkline': False
    }

    # Make the request and get the response
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params=params)

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract only the required parameters
    current_time=datetime.datetime.now()
    index=0
    output = ""
    output += current_time.strftime("%d %B %Y ---- %H:%M:%S") + '\n' +'\n'
    for item in data:
        index+=1
        filtered_item = {
            'id': item['id'],
            'symbol': item['symbol'],
            'name': item['name'],
            'current_price': item['current_price'],
            'market_cap': item['market_cap']
        }

        output += str(index) + "..." + str(filtered_item) + '\n\n\n'

    # Retrieve existing object from S3
    s3 = boto3.client('s3')
    try:
        existing_object = s3.get_object(Bucket='datafoundry.adilashfaq', Key='coin_data.txt')
        existing_data = existing_object['Body'].read().decode('utf-8')
    except s3.exceptions.NoSuchKey:
        existing_data = ""

    # Concatenate new data to existing data
    updated_data = existing_data + output

    # Write the updated data to S3
    s3.put_object(
        Bucket='datafoundry.adilashfaq',
        Key='coin_data.txt',
        Body=updated_data.encode('utf-8')
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Prices retrieved successfully.')
    }
