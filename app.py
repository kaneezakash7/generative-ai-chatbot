import streamlit as st
from ollama import chat

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("📚 About")

    st.write(
        "KA-AI Study Assistant is a Generative AI chatbot "
        "built with Python, Streamlit, Ollama, and Gemma 3."
    )

    st.divider()

    st.subheader("🤖 Model")
    st.write("gemma3:1b")

    st.subheader("🔒 Privacy")
    st.write("The AI model runs locally using Ollama.")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# App Header
# -----------------------------
st.title("🤖 KA-AI Study Assistant")
st.write("Your local AI-powered learning companion.")
st.caption("Ask questions about Python, AI, programming, or your studies.")

# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input("Ask your study question...")

if question:

    # Add user's question to chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user's question
    with st.chat_message("user"):
        st.write(question)

    try:
        # Show loading indicator while AI is thinking
        with st.spinner("Thinking..."):

            # System instruction for the AI
            messages_for_ai = [
                {
                    "role": "system",
                    "content": (
                        "You are a friendly AI Study Assistant. "
                        "Help students understand Python, programming, "
                        "artificial intelligence, and general study topics. "
                        "Explain answers clearly and use simple examples."
                    )
                }
            ]

            # Add conversation history
            messages_for_ai.extend(st.session_state.messages)

            # Send request to Ollama
            response = chat(
                model="gemma3:1b",
                messages=messages_for_ai
            )

            answer = response.message.content

        # Save AI answer to chat history
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Display AI answer
        with st.chat_message("assistant"):
            st.write(answer)

    except Exception as error:
        st.error(f"Something went wrong: {error}")

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Built with Python • Streamlit • Ollama • Gemma 3")