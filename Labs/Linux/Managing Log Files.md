# 🔐 Linux Log File Analysis (AWS EC2)

## 📌 Overview

This lab demonstrates my ability to analyze **Linux system logs** to identify authentication activity and potential security threats. The work was performed on an **AWS EC2 (Amazon Linux)** environment using standard command-line tools.

---

## 🎯 Objective

The goal of this lab was to:

* Review secure log files
* Analyze authentication attempts
* Identify failed logins and suspicious activity
* Use `lastlog` to check user login history

---

## 🛠️ Environment

* **Platform:** AWS EC2
* **Operating System:** Amazon Linux 2
* **Access Method:** SSH (PuTTY)

---

## ⚙️ Commands Used

```bash
pwd
cd companyA
sudo less /tmp/log/secure
sudo lastlog
```

---

## 📸 Proof of Work

### 🔹 Secure Log Analysis

<img width="1442" height="1140" alt="1" src="https://github.com/user-attachments/assets/8be8b227-4ef5-4c4e-949e-2f96da8294c5" />
<img width="1402" height="1132" alt="2" src="https://github.com/user-attachments/assets/2905655c-7576-41a8-ae85-ad1d2dffc6e3" />

---

## 🔍 Analysis of Secure Logs

From the log output, I observed:

* Multiple **failed login attempts**
* Invalid usernames such as:

  * `guest`
  * `admin2`
  * `root`
* Repeated authentication failures from IP addresses:

  * `193.201.224.218`
  * `218.65.30.123`
* SSH authentication errors including:

  * `Failed password`
  * `Invalid user`
  * `Too many authentication failures`

---

## 🚨 Security Interpretation

These logs indicate:

* Possible **brute-force attack attempts**
* Unauthorized users trying to access the system
* Repeated login failures from external IP addresses

---

## 📊 What Information Can Be Extracted

From the logs, the following useful data can be identified:

* Source IP addresses of login attempts
* Target usernames being attacked
* Number of failed login attempts
* Authentication status (success/failure)
* Time and date of each attempt
* SSH port activity

---

## 📚 What I Learned

* How to read and interpret Linux log files
* Identifying suspicious login patterns
* Understanding authentication failure messages
* Using Linux tools (`less`, `lastlog`) for system monitoring

---



## ✅ Conclusion

This lab strengthened my ability to:

* Analyze system logs for security insights
* Detect potential unauthorized access attempts
* Work confidently in a Linux command-line environment

---

