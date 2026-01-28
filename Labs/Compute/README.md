# EC2 Instance Setup Lab

## Objective
To provision and configure an Amazon EC2 instance and understand the fundamentals of compute resources in AWS.

## Key Concepts Covered
- EC2 instance creation
- Instance types and sizing
- Key pairs and security groups
- Connecting to an EC2 instance

## Outcome
Successfully launched and accessed an EC2 instance, demonstrating foundational cloud compute knowledge.
# Lab: Launching and Managing an EC2 Instance  
This lab demonstrates how to launch, configure, secure, monitor, resize, and terminate an Amazon EC2 instance. It includes enabling termination protection and deploying a simple web server using a User Data script.
 Task 1: Launch an EC2 Instance
### 1. Open EC2 Console  
- Navigate to **Services → EC2 → EC2 Dashboard**  
- Select **Launch instance**
### 2. Name Your Instance  
- Name: **Web Server**
### 3. Choose an AMI  
- Keep default: **Amazon Linux 2023**
 ![Screenshot_28-1-2026_21530_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/3f2223f7-c360-44af-b207-4d20c80d9f0d)

### 4. Choose Instance Type  
- Select: **t3.micro**  
  - 2 vCPU  
  - 1 GiB RAM
![Screenshot_28-1-2026_2166_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/c0898705-5e6a-4635-a84a-e8ae235ae264)

### 5. Key Pair  
- Select: **Proceed without a key pair** (lab requirement)
![Screenshot_28-1-2026_21634_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/a76c8200-697b-4a79-a566-8a83aeb46025)

### 6. Configure Network Settings  
- VPC: **Lab VPC**  
- Security Group:  
  - Name: *Web Server security group*  
  - Description: *Security group for my web server*  
- Remove SSH inbound rule (improves security)
![Screenshot_28-1-2026_21952_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/783f3663-0079-4137-b094-e06a1efa0425)

### 7. Storage  
- Keep default: **8 GiB EBS**

### 8. Advanced Details  
- Enable **Termination Protection**  
- Add User Data script:
 ![Screenshot_28-1-2026_22232_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/63ba8178-6651-4fbd-be42-91ac09df3a73)
9. Launch Instance
Wait for:
Instance State: Running
Status Checks: 2/2 passed
Resize Instance & EBS Volume
10. Stop Instance
Instance state → Stop instance
![Screenshot_26-1-2026_145032_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/367acc48-f615-4a84-93f9-2718b4648fe5)

Change Instance Type
Actions → Instance Settings → Change instance type
New type: t3.small
Resize EBS Volume
Volumes → Modify Volume
Change size: 8 GiB → 10 GiB
Restart Instance
Instance state → Start instance
![Screenshot_26-1-2026_143957_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/cd761282-4802-43fe-b8c9-6b582b2f3dfc)


##  Lab Completed

You successfully:

- Launched and configured an EC2 instance  
- Deployed a web server  
- Modified security groups  
- Monitored instance health  
- Resized compute and storage  
- Tested termination protection  
- Terminated the instance safely  
