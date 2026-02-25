# 🎵 Introduction to Amazon DynamoDB

## 📌 Lab Overview

In this lab, I worked with **Amazon DynamoDB**, a fully managed NoSQL database service that provides single-digit millisecond performance at any scale.

The objective was to create and manage a DynamoDB table for a music library and explore how NoSQL databases handle flexible data models.

---

## 🎯 Objectives

- Create a DynamoDB table
- Add and manage items
- Modify existing data
- Perform Query and Scan operations
- Delete the table

---

## 🧱 Task 1 – Create a Table

Created a table named **Music** with:

- **Partition Key:** `Artist` (String)
- **Sort Key:** `Song` (String)

Used default settings for capacity and indexing.

This demonstrated how DynamoDB uses partition and sort keys to uniquely identify items.
![Screenshot_25-2-2026_211111_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/e924a30f-8e2a-4030-a85a-f53f832ed5cb)

---

## ➕ Task 2 – Add Data

Inserted multiple items into the `Music` table:

### Example Item
| Attribute | Value |
|------------|--------|
| Artist | Pink Floyd |
| Song | Money |
| Album | The Dark Side of the Moon |
| Year | 1973 |

Other entries included:
- John Lennon – *Imagine*
- Psy – *Gangnam Style*

Each item had different attributes, demonstrating DynamoDB’s **schema flexibility**.
![Screenshot_25-2-2026_211849_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/8bd54e66-efeb-470c-87ef-c9ea928fd7b7)

---

## ✏️ Task 3 – Modify an Item

Updated the item:

- Changed `Year` for *Gangnam Style* from **2011 → 2012**

This showed how DynamoDB allows easy item updates.
![Screenshot_25-2-2026_212017_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/1c8a42b0-8887-429f-a133-32a810e98c78)

---

## 🔍 Task 4 – Query vs Scan

### Query
Used primary key values:
- Artist: `Psy`
- Song: `Gangnam Style`

Result: Fast and efficient retrieval (indexed).

### Scan
Filtered by:
- Year = `1971`

Result: Retrieved matching item but less efficient.

### Key Difference
- **Query** → Fast, indexed search using primary key  
- **Scan** → Checks every item (slower for large tables)
![Screenshot_25-2-2026_212153_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/0d6fef11-9671-4272-81be-37194c80db72)

---

## 🗑 Task 5 – Delete Table

Deleted the `Music` table and confirmed removal.

---

## 🧠 Key Concepts Learned

- NoSQL data modeling
- Partition key & sort key design
- Schema flexibility in DynamoDB
- Query vs Scan performance differences
- CRUD operations in AWS

---


## ✅ Lab Outcome

✔ Created a DynamoDB table  
✔ Inserted structured & flexible data  
✔ Modified existing records  
✔ Queried and scanned data  
✔ Deleted the table  

---

