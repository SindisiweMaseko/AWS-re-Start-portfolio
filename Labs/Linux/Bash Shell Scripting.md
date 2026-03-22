# 🚀 Challenge Lab: Bash Shell Scripting Exercise


## The objective of this challenge was to create a Bash script that:

- Creates 25 empty (0 KB) files
- Uses a naming format: yourName<number> (e.g., Sindisiwe1, Sindisiwe2, …)
- Automatically determines the next starting number based on existing files
- Avoids hardcoding values (must use automation)
- Can be run multiple times, generating the next batch of files each time
- Verifies results using a long directory listing (ls -l)
## 🛠️ What I Did
- Created a Bash script that:
- Checks existing files in the directory
- Extracts the highest number already used
- Calculates the next starting number dynamically
- Uses a loop to generate 25 new files
- Used commands like:
touch → to create files
ls, grep, sort, tail → to determine the latest file number
for loop → to automate file creation
- Tested the script multiple times to confirm: Files are created correctly & Numbering continues without duplication
## 📸 Screenshots


<img width="1600" height="773" alt="image" src="https://github.com/user-attachments/assets/9e5e6296-17dd-4a27-91c6-6c1e2ec7e9d8" />

<img width="1600" height="930" alt="image" src="https://github.com/user-attachments/assets/d4170626-2265-4259-84ef-85cfcb98912a" />

## 📚 What I Learned
- How to write and execute Bash scripts
- Automating repetitive tasks using loops
- Extracting and processing data from command-line output
- Avoiding hardcoding by using dynamic scripting techniques
- Importance of testing scripts for consistency and scalability
