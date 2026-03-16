# 🚀 AWS Learning Assistant Bot (Amazon Lex Chatbot)

An interactive cloud learning chatbot built with Amazon Lex that answers AWS service questions and provides an educational quiz for learners.

This project demonstrates how conversational AI can be built using AWS services to create an interactive assistant for cloud education.

# 📌 Project Overview

The goal of this project was to design and implement a chatbot capable of:

Answering common questions about AWS services

Running an interactive quiz on cloud concepts

Providing feedback on correct and incorrect answers

Demonstrating conversational AI using Amazon Lex

The chatbot acts as a cloud learning assistant that helps users understand AWS services in an interactive way.

# 🏗 Architecture

The chatbot architecture follows a simple conversational flow:

User
  │
  ▼
Amazon Lex Bot
(Chatbot Engine)
  │
  ▼
Intent Recognition
(Understand User Input)
  │
  ▼
Response / Quiz Logic
- FAQ Answers
- Quiz Questions
- Correct / Incorrect Feedback
  │
  ▼
Response Returned to User
# ☁️ AWS Services Used
### 🤖 Amazon Lex

Amazon Lex is used to build the conversational chatbot interface.
It processes user input and determines the correct response based on intents and utterances.

### ⚡ AWS Lambda

Lambda can be used to extend chatbot logic, validate quiz answers, and control conversation flow.

###  🗄 Amazon DynamoDB

DynamoDB can store quiz questions, correct answers, and user scores.

### 📊 Amazon CloudWatch

CloudWatch can monitor chatbot logs and track conversation events.

### 📦 Amazon S3

S3 can store project documentation, screenshots, and architecture diagrams.

# ✨ Features

- AWS service information chatbot

- Interactive cloud knowledge quiz

- Multiple-choice questions

- Correct and incorrect answer feedback

- Simple conversational user interface

# 💬 Example FAQ Interaction
User Input
What is Amazon S3?
Bot Response
Amazon S3 (Simple Storage Service) is an AWS cloud storage service that allows users to store and retrieve data from anywhere.
🧠 Example Quiz Interaction
Bot asks
What does S3 stand for?

A) Simple Storage Service
B) Secure Server Storage
C) Smart Storage System
User response
A
Bot reply
Correct! S3 stands for Simple Storage Service.
## 📂 File Structure
AWS Lex Chatbot
│
├── README.md
│
├── architecture diagram.png
│
├── screenshots
│   ├── bot-created.png
│   ├── intent-configuration.png
│   ├── quiz-intent.png
│   ├── chatbot-test-correct.png
│   └── chatbot-test-incorrect.png
│
├── AWS_Lex_Chatbot_Report.pdf
│
└── AWS_Lex_Chatbot_Presentation.pptx
# 📸 Screenshots
- Chatbot Setup

(Add screenshot of Lex bot creation)

- Intent Configuration

(Add screenshot of FAQ intent)

- Quiz Interaction

(Add screenshot of quiz interaction)

# 🎓 Learning Outcomes

Through this project I learned:

- How conversational chatbots are built using Amazon Lex

- How intents and utterances work in natural language processing

- How chatbot conversation flows are structured

- How AWS services can be integrated into a chatbot solution


# 🔮 Future Improvements

Possible improvements for this project include:

- Adding voice interaction

- Expanding the quiz with more AWS services

- Building a web interface for the chatbot

- Tracking user scores and progress

- Deploying the bot as a learning assistant for cloud training

# 👩‍💻 Author

Sindisiwe Maseko
Cloud & AWS Learner
