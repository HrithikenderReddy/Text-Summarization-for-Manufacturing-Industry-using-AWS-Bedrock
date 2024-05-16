# Text-Summarization-for-Manufacturing-Industry-using-AWS-Bedrock

**UseCase: ** : **Text Summarization is very much essential for faster processing to improve productivity of technicians for understanding and resolving the issue in lesser time. That's the reason we are summarizing the problem using the AWS Bedrock. In AWS Bedrock Cohera model is used for text summarization purpose.**

**Architecture:**

The User sends the POST request that is a prompt nothing but the (expanded) problem through API Gateway in a form of REST API when a prompt acts as a event for invoking the lambda function then then the function invokes the AWS Bedrock where the prompt is sent to the AWS Bedrock and in which the Cohera model is used to summarize the given prompt and sends back the summarized prompt back to the lambda as the response and to the user where user can view the summarized prompt/output prompt and can easily know about the issue and resolve it faster.

The REST API is tested using the **POSTMAN API** .

Here the AWS services used for this use case are API Gateway, Lambda and AWS Bedrock
