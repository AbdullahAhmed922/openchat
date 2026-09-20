import streamlit as st
import ollama

# Page configuration
st.set_page_config(page_title="Local AI Chatbot", page_icon="🤖")

st.title("🤖 Local AI Chatbot")
st.markdown("Chat with a local model running via [Ollama](https://ollama.com/)")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    # Let the user choose a model they have installed via Ollama
    model_name = st.text_input("Model Name", value="qwen2.5:3b")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.markdown("""
    ### Setup Instructions:
    1. Install [Ollama](https://ollama.com/)
    2. Make sure the model is installed: `ollama pull qwen2.5:3b`.
    3. Make sure the Ollama app is running in the background.
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is on your mind?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            # Call Ollama API with streaming enabled
            stream = ollama.chat(
                model=model_name,
                messages=st.session_state.messages,
                stream=True,
            )

            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Make sure Ollama is running and the specified model is installed, for example: `ollama pull qwen2.5:3b`.")