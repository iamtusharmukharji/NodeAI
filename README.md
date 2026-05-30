# NodeAI

AI Powered IoT Automation using Generative AI, FastAPI, MQTT, and ESP8266.

---

## Overview

NodeAI is a Generative AI based smart automation system that enables users to control real-world IoT devices using natural language prompts.

The system uses Gemini API for intelligent command understanding, FastAPI as the backend server, MQTT for real-time communication, and NodeMCU/ESP8266 for hardware-level execution.

The hardware setup currently includes:

* 5 Relay-controlled appliances
* RGB LED control
* DHT11 temperature & humidity sensor

---


## User Interface

NodeAI provides a modern AI-powered interface for controlling real-world IoT devices using natural language commands. The frontend includes an interactive chat assistant, real-time device communication, quick command actions, and live sensor-aware responses powered by Gemini AI, FastAPI, MQTT, and NodeMCU.

<img width="1914" height="1042" alt="NodeAI Web_1" src="https://github.com/user-attachments/assets/c9a61296-7e68-49d8-a7cf-c7b82158bfad" />
<img width="2000" height="1128" alt="NodeAI Web_2" src="https://github.com/user-attachments/assets/dbc4fea9-7633-4578-8ca0-b8d85f30b173" />



---

## Features

* Natural language based device control
* AI-powered command interpretation
* Real-time MQTT communication
* Multi-relay appliance automation
* RGB LED color control
* Live temperature & humidity monitoring
* FastAPI backend architecture
* React-based frontend
* Scalable IoT communication system

---

## Example Commands

```text id="v8fhzt"
Turn on relay 1
Turn off all switches
Set RGB light to blue
Blink RGB light in red
What is the room temperature?
Show humidity level
```

---

## Tech Stack

| Layer         | Technology        |
| ------------- | ----------------- |
| Frontend      | React.js          |
| Backend       | FastAPI           |
| AI Engine     | Gemini API        |
| Communication | MQTT              |
| Hardware      | NodeMCU / ESP8266 |
| Sensors       | DHT11             |
| Embedded Code | Arduino C++       |

---

## Hardware Components

* NodeMCU / ESP8266
* 5-Channel Relay Module
* RGB LED
* DHT11 Sensor
* MQTT Broker

---

## Hardware Setup (NodeAI Device)

<img width="3807" height="3149" alt="Hardware" src="https://github.com/user-attachments/assets/4641d2cf-06ac-485c-a171-7052fd579900" />

---
---

## Architecture

<img width="1536" height="1024" alt="SystemArch" src="https://github.com/user-attachments/assets/80348b71-3ea3-4155-b4b9-b5332d6017ef" />

---

## Project Workflow

1. User enters a natural language command from the React application.
2. FastAPI receives the request.
3. Gemini API processes the prompt using predefined system instructions.
4. The backend converts the AI response into structured MQTT commands.
5. MQTT messages are published to NodeMCU topics.
6. NodeMCU executes hardware actions in real time.
7. Sensor data can also be sent back to the backend/frontend.

---

## Folder Structure

```bash
NodeAI/
│
├── frontend/          # React frontend
├── backend/           # FastAPI backend
├── firmware/          # NodeMCU Arduino code
└── README.md
```

---

## Future Improvements

* Voice command support
* Mobile application
* Device scheduling
* Authentication & user management
* Smart automation workflows
* Sensor-based AI actions
* Local/offline LLM integration
* Home dashboard analytics

---

## Potential Use Cases

* Smart room automation
* AI-based appliance control
* GenAI + IoT experimentation
* Educational embedded systems projects
* Smart environmental monitoring

---

## Author

Built by Tushar Mukharji

A Curious Learner
