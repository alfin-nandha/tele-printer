### Contents
1. [Version](#1-version) <br/>
2. [Description](#2-description) <br/>
3. [Repository](#3-repository) <br/>
4. [Technology stack](#4-technology-stack) <br/>
5. [Architecture](#5-architecture) <br/>
6. [Flow diagram](#6-flow-diagram) <br/>
7. [Tools](#7-tools) <br/>
8. [Config](#8-config) <br/>
8. [Running Application](#9-running-application) <br/>
9. [Chatbot Command](#10-chatbot-command) <br/>



### 1. Version

| Date       | Version | Author        | Changelog |
|------------| --- |---------------| --- |
| 2024-12-30 | 1.0.0 | Alfin Pratama | Initial release |

[**Back to contents**](#contents)

### 2. Description

**Tele-Printer** is a service that integrate telegram with thermal-printer

[**Back to contents**](#contents)

### 3. Repository

You can access tele-printer repository [here](https://github.com/alfin-nandha/tele-printer).

[**Back to contents**](#contents)

### 4. Technology stack

- Python : Python version python3.8.0, link [here](https://www.python.org/downloads/release/python-380/).
- BotFather (telegram_bot) : Chat bot, link [here](https://telegram.me/BotFather).

[**Back to contents**](#contents)

### 5. Architecture
```mermaid
flowchart LR
    S[Server];
    P[Thermal Printer]
    T[Telegram]
    

    S-->P
    S-->T
    T-->S
```

[**Back to contents**](#contents)


### 6. Flow diagram

N/A

[**Back to contents**](#contents)

### 7. Tools

- [VsCode](https://code.visualstudio.com/) as IDE code for Go

[**Back to contents**](#contents)

### 8. Config

- TELEGRAM_BOT_TOKEN = "12345:TOKEN" -> Obtained from BotFather to authenticate the bot.
- CHAT_ID = "1234567" -> Chat ID for a specific user to send messages.
- PRINTER_PORT = "/dev/usb/lp0" -> Defines the printer port to be used.

[**Back to contents**](#contents)

### 9. Running application

#### Install Dependencies:
```
pip3 install -r requirements.txt
```
#### Run the Application:
```

python3 main.py
```

[**Back to contents**](#contents)

### 10. Chatbot Command

#### /health
Checks the server status:
- If the system is running normally, it prints "sistem OK" on the thermal printer and sends "alhamdulillah sehat" in the chat.
- If there's an issue, it prints the problem on the thermal printer or sends a message via the chatbot.

#### /poweroff
- Safely shuts down the server.
  
#### receipt format
```
tokopedia           -> platform/ecomerce
john doe            -> customerName/receiverAddress
jnt                 -> courier
TKJNT-000007FW3NN   -> resi
1 salak A 500g      -> item 1
1 nangka A 500g     -> item 2
```

#### [plain]
- Use this prefix to print plain text on the thermal printer (no special formatting). The printer will print the content exactly as entered after the prefix.

[**Back to contents**](#contents)
