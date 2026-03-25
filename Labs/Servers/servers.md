# AWS Lambda Sales Analysis Lab

## 📌 Overview
This lab demonstrates the configuration and testing of AWS Lambda functions, IAM roles, and supporting services for a sales analysis reporting system.

---

## ✅ Task 1: IAM Role Configuration

Two IAM roles were analyzed to understand permissions required for Lambda functions.

### Key Observations:
- **salesAnalysisReportRole**
  - Trusted entity: `lambda.amazonaws.com`
  - Permissions:
    - AmazonSNSFullAccess
    - AmazonSSMReadOnlyAccess
    - AWSLambdaBasicExecutionRole
    - AWSLambdaRole
<img width="1398" height="917" alt="1A" src="https://github.com/user-attachments/assets/f3ca0065-32ff-4110-a87d-5b19a4b23834" />


- **salesAnalysisReportDERole**
  - Trusted entity: `lambda.amazonaws.com`
  - Permissions:
    - AWSLambdaBasicExecutionRole
    - AWSLambdaVPCAccessExecutionRole

<img width="1410" height="935" alt="1B" src="https://github.com/user-attachments/assets/e5eb5867-4161-4e01-9386-35ccbd506507" />



---

## ✅ Task 2: Lambda Layer and Function Setup

### Lambda Layer:
- Name: `pymysqlLibrary`
- Runtime: Python 3.9
- Purpose: Provide PyMySQL library for database connectivity


<img width="1401" height="868" alt="1C" src="https://github.com/user-attachments/assets/ab1c6bf5-0c00-424e-852e-2aadfa397cfe" />

### Lambda Function:
- Name: `salesAnalysisReportDataExtractor`
- Runtime: Python 3.9
- Role: `salesAnalysisReportDERole`
- Layer attached successfully


<img width="1390" height="877" alt="1D" src="https://github.com/user-attachments/assets/03cac87a-4068-4430-a4d5-a413349e0952" />

<img width="1523" height="565" alt="1E" src="https://github.com/user-attachments/assets/fcdbfcdf-5469-4fdb-b43e-6e6197157448" />

---

## ⚠️ Task 3: Function Testing and Issue Identified

### Test Execution Result:
- Status: ❌ Failed
- Error: Timeout after 3 seconds

<img width="1867" height="922" alt="1H" src="https://github.com/user-attachments/assets/c87a751c-68f0-48ac-9598-f025667810d6" />


### Root Cause:
The Lambda function attempts to connect to a MySQL database hosted on an EC2 instance.

- MySQL uses **port 3306**
- The security group did **not allow inbound traffic on port 3306**
- This prevented the Lambda function from establishing a database connection


<img width="1887" height="642" alt="1G" src="https://github.com/user-attachments/assets/265d7e41-cbeb-4be0-8054-0f6228951751" />


### Resolution (Identified):
To fix the issue:
- Add an inbound rule in the security group:
  - Type: MySQL/Aurora
  - Port: 3306
  - Source: Appropriate Lambda/VPC security group



---

## 🚧 Current Status

✔ IAM roles configured correctly  
✔ Lambda layer created and attached  
✔ Lambda function deployed  
✔ Initial test executed  
✔ Issue identified and analyzed  


---

## 🧠 Key Learning Outcomes

- Understanding IAM roles and permissions for Lambda
- Using Lambda layers for dependency management
- Configuring Lambda functions within a VPC
- Troubleshooting network-related Lambda timeouts
- Identifying security group misconfigurations

---

## 📌 Conclusion

This lab successfully demonstrates the setup and partial testing of a serverless data extraction workflow.  
The failure encountered provided valuable insight into AWS networking and security configurations, particularly the importance of correctly configuring security group rules for database connectivity.
