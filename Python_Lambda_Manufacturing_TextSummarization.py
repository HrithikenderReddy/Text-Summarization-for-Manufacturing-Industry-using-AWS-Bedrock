import json
import boto3
import base64

#2. Create client connection with bedrock 
client_bedrock=boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    
    #3. Store the input data (prompt) in a variable
    input_prompt=event['prompt']
    print(input_prompt)
    
    #4. Create a Request Syntax to access the Bedrock Service 
    client_bedrockrequest = client_bedrock.invoke_model(
        contentType='application/json', 
        accept='application/json',
        modelId='cohere.command-light-text-v14',
        body=json.dumps({
           
           
        "prompt": input_prompt,
        "temperature": 0.9,
        "p": 0.75,
        "k": 0,
        "max_tokens": 100 }))
    #print(client_bedrockrequest) 
    
    #5 Convert Streaming body to byte(.read method) and then Byte to string using json.loads
    
    client_bedrock_byte=client_bedrockrequest['body'].read()
    #print(client_bedrock_byte)
    #print(type(client_bedrock_byte))
    
    #6 Print the event and type , b . Store the input in a variable
    
    client_bedrock_string=json.loads(client_bedrock_byte)
    #print(client_bedrock_string)
    
    #7 Update the 'return' by changing the 'body'
    
    client_final_response= client_bedrock_string['generations'][0]['text']
    print(client_final_response)
    
    
    # TODO implement
    return {
        
        'statusCode': 200,
        'body': json.dumps(client_final_response)
    }
