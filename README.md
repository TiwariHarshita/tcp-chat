Absolutely! Here’s the full README text you can directly copy and paste into your README.md file:

# TCP Chat Application

A **multi-client TCP chat application** built in Python that allows users to connect with a username, send and receive messages in real-time, and see server-side logs of all activity. Perfect for demonstrating **network programming, socket handling, and multithreading** skills.

---

## Features
- Supports **multiple clients** simultaneously.
- Users can join with a **custom username**.
- **Real-time message broadcasting** to all connected clients.
- Server logs all messages and user activity.
- Graceful handling of **disconnects**.

---

## Folder Structure

tcp-chat/
│── server.py        # The main server script
│── client.py        # The client script with username support
│── README.md        # Project documentation

---

## Requirements
- Python 3.x
- No external libraries required (uses built-in `socket` and `threading` modules).

---

## Step-by-Step Setup and Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/tcp-chat.git
cd tcp-chat

2️⃣ Start the Server

Open a terminal and run:

python3 server.py

	•	The server will start on 127.0.0.1:5010.
	•	It will log all incoming messages and connections.

Server Output Example:

[STARTING] Server is running on 127.0.0.1:5010
[NEW USER] Harshita connected from ('127.0.0.1', 50432)
[Harshita] Hello everyone!

3️⃣ Start Clients

Open one or more new terminal windows and run:

python3 client.py

	•	Enter a username when prompted.
	•	Start sending messages — they will appear for all connected clients.

Client Output Example:

Enter your username: Harshita
✅ Connected to chat! Start typing...
🔔 Shreya has joined the chat!
[Shreya] Hi Harshita!
[Harshita] Hello!

4️⃣ Send Messages
	•	Type your message and press Enter.
	•	Messages are broadcast to all connected clients.

5️⃣ Disconnect
	•	Type /quit to safely disconnect from the chat.
	•	Other users will see a notification when someone leaves.

⸻

How it Works
	1.	Server uses Python socket to listen for incoming client connections.
	2.	Each client connection is handled in a separate thread (threading.Thread) to support multiple clients.
	3.	Server maintains a dictionary of clients with usernames.
	4.	Messages are broadcast to all clients except the sender.
	5.	Graceful disconnects ensure server and clients do not crash.

⸻

Tech Stack
	•	Language: Python 3
	•	Concepts: Sockets, TCP/IP networking, Multithreading, Terminal I/O
	•	Skills Demonstrated: Backend development, real-time communication, problem-solving, debugging

⸻


⸻

Demo
	•	Terminal-based chat working with multiple users.

⸻

Author

Harshita Tiwari
	•	GitHub: https://github.com/TiwariHarshita
	•	LinkedIn: https://linkedin.com/in/tiwariharshita12

---
