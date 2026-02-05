# AHKU  Cafe – Amazon S3 Static Website Hosting Guide
Project Overview
This document describes the steps followed to host the AHKU Cafe static website using Amazon S3 Static Website Hosting as part of the AWS re/Start Portfolio Project.
Amazon S3 was selected as the hosting solution because it is cost-effective, highly available, scalable, and does not require server management—making it ideal for a small café business.

________________________________________
Prerequisites
Before starting, ensure you have:
-•	An active AWS Account
-•	A completed static website (HTML/CSS files)
-•	The main website file named index.html
________________________________________
Step 1: Log in to the AWS Management Console
1.	Open a browser and go to https://aws.amazon.com
2.	Click Sign in to the Console
3.	Log in using your AWS account credentials
________________________________________
Step 2: Access Amazon S3
1.	In the AWS Console search bar, type S3
2.	Select Amazon S3
3.	You will be redirected to the S3 dashboard




<img width="1319" height="842" alt="1" src="https://github.com/user-attachments/assets/1032d720-78ae-4f6e-bfbd-45ca1e5f1451" />




________________________________________
Step 3: Create an S3 Bucket
<img width="438" height="276" alt="2" src="https://github.com/user-attachments/assets/f0b250ee-bf1b-476c-825f-94dfdf703f04" />

1.	Click Create bucket

2.	Enter a globally unique bucket name (bucket name: Ahku-cafe-website)
3.	Select a Region ( Africa (Cape Town)
4.	Leave Object Ownership as default (ACLs disabled) 


<img width="1612" height="852" alt="3" src="https://github.com/user-attachments/assets/62c3a82d-c8dc-41e2-91fd-3c063aac4582" />

________________________________________
Step 4: Configure Public Access Settings
1.	Under Block Public Access settings, uncheck:
o	✅ Block all public access
2.	Acknowledge the warning by ticking the confirmation checkbox
3.	Leave Bucket Versioning disabled
4.	Leave Default Encryption enabled(SSE-S3 enabled)
5.	Click Create bucket

<img width="1839" height="623" alt="4" src="https://github.com/user-attachments/assets/1aa257ad-e403-4125-901e-9cd3be25a896" />

<img width="1267" height="572" alt="6" src="https://github.com/user-attachments/assets/00c7060d-c989-4207-a0f7-36a35444a9c5" />

________________________________________
Step 5: Upload Website Files
1.	Open the newly created bucket
2.	Click Upload
3.	Select Add files
4.	Upload index.html (and any additional files such as images, CSS, or JavaScript)
5.	Click Upload
<img width="1862" height="361" alt="7" src="https://github.com/user-attachments/assets/d9ba41b7-8af9-48eb-9dd7-ab699d7dcb70" />

<img width="1834" height="571" alt="8" src="https://github.com/user-attachments/assets/45f810c0-5560-4018-b069-0997f78e017b" />

<img width="1867" height="744" alt="9" src="https://github.com/user-attachments/assets/362fa802-565c-40fb-8db2-64744f261a0d" />

<img width="1860" height="667" alt="10" src="https://github.com/user-attachments/assets/255b41c3-78ec-4e0b-8e60-3e6856631e68" />

________________________________________
Step 6: Enable Static Website Hosting
1.	Go to the Properties tab of the bucket
<img width="1838" height="352" alt="16" src="https://github.com/user-attachments/assets/4d2b9923-346a-4ba6-9195-60680a850696" />
<img width="1051" height="82" alt="11" src="https://github.com/user-attachments/assets/f709997b-7c2f-4000-bcf7-02e25c042c93" />

2.	Scroll to Static website hosting
3.	Click Edit
4.	Select Enable
5.	Choose Host a static website
6.	Enter:
7.	Index document: index.html
8.	Click Save changes
<img width="1423" height="724" alt="14" src="https://github.com/user-attachments/assets/e9b7e926-3b8f-4265-8fb6-97b2005e7c64" />

________________________________________
Step 7: Configure Bucket Policy for Public Access
1.	Go to the Permissions tab
2.	Scroll to Bucket policy
3.	Click Edit
4.	Paste the following policy (replace the bucket name if necessary):
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::ahku-cafe-website/*"
    }
  ]
}
5.	Click Save changes
<img width="1863" height="535" alt="15" src="https://github.com/user-attachments/assets/510be419-e797-4375-b05d-c6a880fe1f98" />

________________________________________
Step 8: Access the Live Website
1.	Navigate back to the Properties tab
2.	Scroll to Static website hosting
3.	Copy the Bucket website endpoint
4.	Paste the URL into a web browser to view the live AHKU Cafe website
   <img width="1838" height="352" alt="16" src="https://github.com/user-attachments/assets/913dd66a-3786-4b17-918c-7f5cd921b52a" />


<img width="1893" height="967" alt="17" src="https://github.com/user-attachments/assets/99905753-4de6-4372-bef8-218fa555633c" />

________________________________________
Benefits of Hosting AHKU Cafe on Amazon S3
•	Low Cost: Pay only for storage and usage
•	High Availability: 99.99% availability
•	Scalability: Automatically handles traffic growth
•	No Server Management: AWS fully manages the infrastructure
•	Security: Supports encryption and IAM integration
________________________________________
Conclusion
By hosting the AHKU Cafe website on Amazon S3, the business gains a reliable, scalable, and affordable online presence. This solution removes the need for on-premises servers while improving accessibility and customer engagement.
________________________________________




