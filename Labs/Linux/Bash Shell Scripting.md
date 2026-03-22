

# 🚀 Bash File Generator Automation Script

## 📌 Overview

This project demonstrates my ability to automate tasks using **Bash scripting on a Linux (Amazon EC2) environment**. The script dynamically creates batches of files while maintaining continuous numbering across multiple executions.

---

## 🧾 Challenge Objective

The goal of this lab was to:

* Create **25 empty (0 KB) files**
* Use naming format: `SINDISIWE<number>`
* Automatically detect the **highest existing number**
* Continue numbering without duplication
* Avoid hardcoding values using **automation**
* Verify output using `ls -l`

---

## 🛠️ What I Did

* Connected to an **AWS EC2 instance (Amazon Linux 2)** using SSH (PuTTY)
* Wrote Bash commands to:

  * Extract existing file numbers
  * Identify the highest number
  * Generate the next sequence dynamically
* Used a loop to create 25 files per run
* Validated results using a long directory listing

---

## ⚙️ Commands & Logic Used

* `touch` → create files
* `ls -l` → list directory contents
* `grep` → filter filenames
* `awk` → extract filename column
* `sed` → isolate numbers
* `sort -n` → sort numerically
* `tail -1` → get highest value
* `seq` → generate number range

---

## 💻 Script Logic (Executed in Terminal)

```bash
NAME="SINDISIWE"

MAX_NUMBER=$(ls -l | grep "$NAME" | awk '{print $9}' | sed 's/[^0-9]//g' | sort -n | tail -1)

if [ -z "$MAX_NUMBER" ]; then
  MAX_NUMBER=0
fi

for i in $(seq 1 25); do
  touch "${NAME}$((MAX_NUMBER + i))"
done
```

---

## ▶️ Execution Steps

```bash
chmod +x file_generator.sh
./file_generator.sh
ls -l
```

---

## 📸 Proof of Work

### 🔹 EC2 Login & Environment

<img width="1600" height="773" alt="image" src="https://github.com/user-attachments/assets/953470dd-abd3-4078-bf92-64bc06888fd4" />


### 🔹 Script Execution & File Creation


<img width="1600" height="930" alt="image" src="https://github.com/user-attachments/assets/33368725-04f5-4590-b780-e2ed050dfc69" />

---

## 📊 Results

* Successfully generated **25 files**
* Files named sequentially from:

  * `SINDISIWE1` → `SINDISIWE25`
* Verified:

  * All files are **0 KB**
  * No duplication
  * Correct numbering sequence

---

## 📚 Key Learnings

* Practical use of **Bash scripting for automation**
* Working in a **Linux cloud environment (AWS EC2)**
* Extracting and processing command-line data
* Writing **dynamic scripts (no hardcoding)**
* Validating outputs using Linux commands


---

## ✅ Conclusion

This lab strengthened my ability to:

* Work confidently in a Linux terminal
* Automate repetitive processes using Bash
* Build scalable and reusable scripts
* Apply problem-solving in a real cloud environment

---





