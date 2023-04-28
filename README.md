# DataFoundry
Scheduled Parameterised Data Extraction from Coin Gecko Public API into S3 bucket using AWS Lambda Function.

The Read.me file provides the high-level overview of the total project dynamics:

Project Overview:

The project aims to ingest the data from coingecko public api endpoint into AWS S3 storage using Lambda Function. The language used in Lambda Function was Python. The Lambda function was then triggered on every minute cadence using EventBridge. The event logs can then be monitored using CloudWatch. 

Please note, its the first project that I completed using cloud platform other than Azure. Therefore, there is a big room for improvement.


Usage:

There were 3 AWS infrastructure components used for the deployment of solution i.e.AWS S3, AWS Lambda, and AWS EventBridge and one component for the monitoring of the lambda function i.e. AWS CloudWatch. Additionally, AWS CloudFormation was also used to test the infrastructure-as-a-code configuration file. The my_deployment.zip file contains the python script along with all the dependencies required to execute the script in Lambda runtime environment. Just for the explanation purpose, I assume that all the resources required have been provisioned using InfraStructure_as_a_Code.yaml with all the required permission policies attached, hence, my_deployment.zip can be uploaded into Lambda and testing it would create an output.txt file in s3 bucket. The file will contain the selected parameters of top 50 crypto coins with proper indexing and the current timestamp at the top. EventBridge is then used to assign the rule on the lambda function that would trigger the function every minute. I used such a short time window so that I could monitor and debug the function by reducing the wait time for not having to wait for the trigger to start. At the time of my writing, Lambda function has been triggered 978 times and the coin_data.txt has been appended accordingly and it has also been uploaded in this repository.


Final Comments:
I hope this read.me file explains how the project works and how the solution can be deployed into the configured infrastructure. It should be noted that there are many other important details as well which can not be covered in this high-level description but are worth for discussion if I was given the opportunity.






