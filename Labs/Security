# 🛡  280-[SF] LAB: Malware Protection Using AWS Network Firewall

### 📌 Lab Overview

This lab demonstrates how to mitigate malware threats using **AWS Network Firewall**.

Malware (malicious software) includes:

* Viruses
* Worms
* Trojan horses
* Spyware
* Adware
* Ransomware

The goal was to prevent users from downloading malicious files by strengthening the company’s network perimeter.

---

### 🏢 Scenario

**AnyCompany** experienced users accidentally downloading malware from specific websites.

As a Security Engineer, I was tasked with:

* Hardening the firewall
* Blocking known malicious URLs
* Verifying that access is denied

---

### 🎯 Objectives

After completing this lab, I was able to:

* Update a Network Firewall policy
* Create a Stateful Rule Group
* Implement Suricata IPS rules
* Attach rule groups to a firewall
* Validate that malicious sites are blocked

---

### 🧪 Lab Environment

* Amazon EC2 (TestInstance)
* AWS Network Firewall
* VPC (Perimeter zone)
* Pre-configured IAM roles and services

The EC2 instance was used to simulate user traffic.

---

## 🔎 Task 1 – Confirm Reachability

From EC2, tested access using:
![Screenshot_25-2-2026_13156_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/e5459506-a80a-4557-8609-19a3b666d4a1)

```bash
wget http://malware.wicar.org/data/js_crypto_miner.html
wget http://malware.wicar.org/data/java_jre17_exec.html
```

* Received `200 OK`
* Malware files downloaded successfully
* Confirmed firewall was not blocking traffic
![Screenshot_25-2-2026_131856_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/6810ea66-4cb8-4f77-8e01-76749bf24ea7)

---

## 🔍 Task 2 – Update Firewall Policy

Modified firewall policy:

* Forward stateless traffic to stateful rule groups
* Enabled deep packet inspection

This ensures advanced traffic inspection instead of basic packet filtering.
![Screenshot_25-2-2026_132038_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/eab0ef1f-32a9-41a9-95a2-244df55bb50e)

---

## 🧱 Task 3 – Create Stateful Rule Group

Created a **Stateful Rule Group** using Suricata rule syntax:

```bash
drop http $HOME_NET any -> $EXTERNAL_NET 80 (msg:"MALWARE custom solution"; flow: to_server,established; classtype:trojan-activity; sid:2002001; content:"/data/js_crypto_miner.html"; http_uri; rev:1;)

drop http $HOME_NET any -> $EXTERNAL_NET 80 (msg:"MALWARE custom solution"; flow: to_server,established; classtype:trojan-activity; sid:2002002; content:"/data/java_jre17_exec.html"; http_uri; rev:1;)
```

These rules block access to malicious file paths.
![Screenshot_25-2-2026_13311_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/401a44d3-d543-4af2-a2a8-297fed6eff35)


---

## 🔗 Task 4 – Attach Rule Group

* Attached `StatefulRuleGroup` to `LabFirewallPolicy`
* Applied policy to the Network Firewall
* Confirmed successful update
![Screenshot_25-2-2026_13311_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/81aa8742-9f41-4b63-9515-d8d08305fd73)

---

## ✅ Task 5 – Validate the Solution

Re-tested access from EC2:

```bash
wget http://malware.wicar.org/data/js_crypto_miner.html
```

Result:

```
HTTP request sent, awaiting response...
```

Connection stalled — access successfully blocked.
![Screenshot_25-2-2026_133744_us-west-2 console aws amazon com](https://github.com/user-attachments/assets/9e16ecd0-f15b-46d8-a474-5617abaf9a35)

---

## 🏁 Final Outcome

✔ Firewall policy updated
✔ Stateful inspection enabled
✔ Malicious URLs blocked
✔ Solution validated

