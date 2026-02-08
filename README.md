# Simple File Integrity Monitor (FIM)

A lightweight cybersecurity tool written in Python that monitors a specific folder for unauthorized changes. It calculates SHA-256 hashes of files to detect modifications, deletions, and new file creations in real-time.

## 🚀 Features
* **SHA-256 Hashing:** Uses secure cryptographic hashing to "fingerprint" files.
* **Baseline Creation:** Takes a snapshot of the target folder state.
* **Continuous Monitoring:** Compares current file states against the baseline.
* **Alerts:** Notifies the user about:
    * File Modifications (Content changed).
    * File Deletions.
    * New File Creations.

## 🛠️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/Adham504/simple-fim.git](https://github.com/Adham504/simple-fim.git)
cd simple-fim
