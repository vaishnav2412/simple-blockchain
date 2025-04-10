# 🧱 Simple Blockchain in Python

This is a basic simulation of a blockchain implemented in Python, intended for educational purposes and as part of an internship assignment.

## 📌 Features

- Block structure with:
  - Index
  - Timestamp
  - Transactions
  - Previous Hash
  - Nonce
  - Current Hash
- Blockchain class to:
  - Create the genesis block
  - Add new blocks
  - Validate the chain
- Proof-of-Work (PoW) mechanism
- Tamper detection and chain validation
- Dockerized for easy setup

---

## 📂 Project Structure
Blockchain/ ├── blockchain.py # Main blockchain implementation ├── requirements.txt # Python dependencies ├── Dockerfile # Docker image setup └── README.md # Project documentation

---

## 🚀 How It Works

Each block in the blockchain contains data, a nonce (used for mining), and the hash of the previous block. The proof-of-work algorithm ensures that generating a block takes computational effort.

When a block's hash meets a specific difficulty (e.g., starts with "0000"), it's added to the chain.

We then simulate tampering by modifying one block’s data and checking if the blockchain still validates.

---

## 🛠️ How to Run

### ▶️ Run Locally (Without Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/vaishnav2412/simple-blockchain.git
   cd simple-blockchain



Run with Docker:
Make sure Docker is installed and running.

Build the Docker image:
docker build -t simple-blockchain .

Run the container:
docker run --rm simple-blockchain

This project demonstrates:

An understanding of blockchain fundamentals

Ability to write and structure clean Python code

Basic usage of Docker for software containerization

Awareness of tamper detection and cryptographic integrity






