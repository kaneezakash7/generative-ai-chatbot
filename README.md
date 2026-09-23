\# 🤖 AI Study Assistant



AI Study Assistant is a simple Generative AI chatbot developed using Python, Streamlit, Ollama, and the Gemma 3 language model.



The chatbot runs locally on the computer and allows students to ask questions about Python, programming, artificial intelligence, and general study topics.



This project was created as part of my AI learning assignment to demonstrate how a Generative AI model can be connected with a Python-based web interface.



\---



\## 📌 Project Type



\*\*Generative AI Chatbot\*\*



\---



\## ✨ Features



\- 💬 Chat-based user interface

\- 🤖 AI-generated responses using Gemma 3

\- 🧠 Conversation history

\- 🗑️ Clear Chat option

\- 📚 Study Assistant system instructions

\- ⏳ Thinking indicator while generating responses

\- ⚠️ Basic error handling

\- 🔒 Local AI processing using Ollama

\- 🌐 Web interface built with Streamlit



\---



\## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Main programming language |

| uv | Python project and dependency management |

| Streamlit | Web-based chatbot interface |

| Ollama | Runs the AI model locally |

| Gemma 3 1B | Large Language Model used by the chatbot |

| Git | Version control |

| GitHub | Project repository and submission |



\---



\## 🧠 How It Works



The application follows this basic flow:



```text

User

&#x20; ↓

Streamlit Chat Interface

&#x20; ↓

Python

&#x20; ↓

Ollama

&#x20; ↓

Gemma 3 (gemma3:1b)

&#x20; ↓

AI Response

&#x20; ↓

Streamlit Chat Interface

```



The user enters a question through the Streamlit interface.



Python sends the conversation to Ollama, which runs the `gemma3:1b` model locally.



Gemma generates an answer, and the response is displayed back to the user through Streamlit.



\---



\## 📂 Project Structure



```text

generative-ai-chatbot/

│

├── app.py

├── test\_ollama.py

├── pyproject.toml

├── uv.lock

├── README.md

├── .gitignore

├── .python-version

└── .venv/

```



> The `.venv` directory contains the local Python virtual environment and should not be uploaded to GitHub.



\---



\## ⚙️ Requirements



Before running the project, install:



\- Python

\- uv

\- Ollama



You also need the Gemma 3 1B model installed in Ollama.



\---



\## 🚀 Installation



\### 1. Clone the repository



```bash

git clone https://github.com/kaneezakash7/generative-ai-chatbot

```



Move into the project directory:



```bash

cd generative-ai-chatbot

```



\### 2. Install project dependencies



Run:



```bash

uv sync

```



This installs the Python dependencies defined in the project.



\### 3. Download the AI model



Make sure Ollama is installed, then run:



```bash

ollama pull gemma3:1b

```



Check that the model is available:



```bash

ollama list

```



You should see:



```text

gemma3:1b

```



\---



\## ▶️ Running the Application



From the project directory, run:



```bash

uv run streamlit run app.py

```



Streamlit will start the application and normally provide a local address such as:



```text

http://localhost:8501

```



Open the address in your web browser.



\---



\## 💬 How to Use



1\. Start the Streamlit application.

2\. Enter a study question in the chat box.

3\. Press Enter.

4\. Wait while Gemma generates the response.

5\. Continue asking questions to maintain conversation history.

6\. Use \*\*Clear Chat\*\* from the sidebar to start a new conversation.



Example questions:



```text

What is a Python variable?



Explain artificial intelligence in simple words.



What is the difference between a list and a tuple in Python?



Give me a simple example of a Python loop.

```



\---



\## 🧪 Testing Ollama



The project includes `test\_ollama.py` to test the Python connection with Ollama.



Run:



```bash

uv run test\_ollama.py

```



If Ollama and Gemma are configured correctly, the AI model should generate a response in the terminal.



\---



\## 📸 Screenshots



\### Main Chatbot Interface



Add screenshot here.



\### Chat Conversation



Add screenshot here.



\---



\## 🔒 Privacy



The Gemma model runs locally through Ollama.



The chatbot does not require an external cloud AI API for generating responses.



\---



\## 🎯 Learning Outcomes



Through this project, I learned how to:



\- Create and manage a Python project using `uv`

\- Install and use Python packages

\- Run a local Large Language Model using Ollama

\- Communicate with an Ollama model from Python

\- Build a web interface using Streamlit

\- Store conversation history using Streamlit session state

\- Handle basic application errors

\- Build a simple Generative AI application



\---



\## 🔮 Future Improvements



Possible future improvements include:



\- Allow users to select different Ollama models

\- Add more study categories

\- Add document or PDF question answering

\- Add voice input

\- Add voice responses

\- Improve the user interface

\- Add chat export functionality



\---



\## 👩‍💻 Author



\*\*Kinza Akash\*\*



AI for Everyone — Generative AI Project



\---



\## 📄 Project



\*\*Project 1: Chatbot — Generative AI\*\*

