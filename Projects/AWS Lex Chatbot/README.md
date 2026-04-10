# 🚀 AWS Learning Assistant Chatbot
### Serverless Conversational AI using Amazon Lex

An interactive serverless chatbot built on AWS that provides FAQ responses and conducts real-time quizzes to help users learn cloud concepts.

---

## 📌 Overview
This project implements a cloud-native conversational chatbot using AWS services. The system leverages **Amazon Lex** for natural language interaction and integrates with serverless backend services to deliver dynamic responses and quiz functionality.

**The chatbot enables users to:**
* Ask questions about AWS services
* Take interactive quizzes
* Receive instant feedback
* Learn through conversation

---

## 🏗 Architecture

### Serverless Architecture Diagram
<img width="1600" height="871" alt="image" src="https://github.com/user-attachments/assets/acfd64ee-2be7-43f0-a4a4-94e582c03e32" />


### Architecture Flow
* 1.  **User** interacts with the chatbot interface.
* 2.  **Amazon Lex** processes input using Natural Language Understanding (NLU).
* 3.  **Request** is passed to **AWS Lambda** for fulfillment.
* 4.  **Lambda** executes quiz logic and business rules.
* 5.  **Data** is retrieved/stored in **Amazon DynamoDB**.
* 6.  **Logs** and static content are handled via **Amazon S3**.
* 7.  **Response** is formatted and returned to the user.

---

## ☁️ AWS Services Used

* **🟩 Amazon Lex:** Conversational AI engine; handles intents, utterances, and NLU processing.
* **🟧 AWS Lambda:** Serverless compute layer; executes quiz logic and evaluates user answers.
* **🟦 Amazon DynamoDB:** NoSQL database; stores quiz questions, FAQ data, and state.
* **🟩 Amazon S3:** Stores logs, documentation, and static chatbot resources.
* **📊 Amazon CloudWatch:** Monitoring and logging; tracks chatbot performance and interactions.

---

## ✨ Features
* 🤖 **Natural Language Interface:** Intuitive chatbot interactions.
* 📚 **AWS FAQ System:** Instant responses to common cloud queries.
* 🧠 **Interactive Quizzes:** Gamified learning experience.
* ✅ **Real-time Validation:** Immediate feedback on quiz answers.
* ⚡ **Serverless Design:** Scalable, cost-effective, and highly available.

---

## 💬 Example Interaction

> **User:** Start quiz
> 
> **Bot:** What does S3 stand for?
> *A) Simple Storage Service*
> *B) Secure Server Storage*
> *C) Smart Storage System*
>
> **User:** A
> 
> **Bot:** ✅ Correct! S3 stands for Simple Storage Service.

---

## 🧪 Testing & Validation
The chatbot underwent testing to ensure production-grade reliability:

* **Intent Recognition:** Verified multiple utterance variations for "Quiz" and "Help" triggers to ensure high NLU accuracy.
* **Logic Flow:** Confirmed **AWS Lambda** correctly identifies right/wrong answers and maintains session state.
* **Error Handling:** Implemented **Fallback Intents** and custom error messages for unrecognized user input.

---

# 📸 Screenshots
- Chatbot Setup
<img width="969" height="557" alt="image" src="https://github.com/user-attachments/assets/9f6bbff2-1a65-4490-89de-be59fe83d8f3" />

<img width="969" height="574" alt="image" src="https://github.com/user-attachments/assets/c6f6ef4d-7fd8-424b-8e39-4317d1a5892d" />

- Intent Configuration
<img width="950" height="417" alt="image" src="https://github.com/user-attachments/assets/fa88cedb-25e0-4394-9527-4ecc083fecf4" />

- Quiz Interaction
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/0482c67d-0366-47c6-928f-17b86431ba12" />

---


## 🎓 Learning Outcomes
* **Conversational AI:** Architected a full-stack AI interface using **Amazon Lex**.
* **Serverless Compute:** Developed **Python/Node.js** Lambda functions for backend fulfillment and API integration.
* **Database Management:** Managed **NoSQL data schemas** in DynamoDB for educational content and quiz questions.
* **Security & IAM:** Applied **AWS Best Practices** by configuring granular IAM roles and resource-based policies.

---

## 🔮 Future Roadmap
- [ ] **Voice Integration:** Enable **Amazon Polly** for voice-to-text learning capabilities.
- [ ] **Web Frontend:** Deploy a **React-based** UI to provide a more polished, branded user experience.
- [ ] **Leaderboards:** Track and store user high scores in DynamoDB to gamify the learning process.
- [ ] **Advanced Categories:** Expand quiz modules to include **VPC Networking**, **IAM Security**, and **EC2 Fleet Management**.

---

## 👩‍💻 Author
**Sindisiwe Maseko** 

---

## 🏷 Topics
`aws` `amazon-lex` `serverless` `chatbot` `cloud-computing` `aws-lambda` `dynamodb`
