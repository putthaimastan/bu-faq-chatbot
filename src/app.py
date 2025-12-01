import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="BU FAQ Chatbot",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS styling
st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }
    .user-message {
        background-color: #262730;
        justify-content: flex-end;
    }
    .bot-message {
        background-color: #000000;
    }
    .message-content {
        max-width: 80%;
    }
    .timestamp {
        font-size: 0.75rem;
        color: #999;
        margin-top: 0.25rem;
    }
    .user-message .message-content {
        margin-left: auto;
        text-align: right;
    }
    .user-message .timestamp {
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_url" not in st.session_state:
    st.session_state.api_url = "http://localhost:5000"

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Settings")
    
    api_url = st.text_input(
        "API URL",
        value=st.session_state.api_url,
        help="Enter API Endpoint URL",
        width="stretch"
    )
    st.session_state.api_url = api_url
    
    st.divider()
    
    st.markdown("""
    ### 🛠️ About ChatBot
    This is Bangkok University FAQ ChatBot:
    - **Backend:** FastAPI + Groq LLM
    - **Frontend:** Streamlit
    
    ### 🎯 Features
    - Real-time FAQ retrieval
    - Thai language support
    """)
    
    st.divider()
    
    if st.button("Clear Chat History", type="primary", width="stretch"):
        st.session_state.messages = []
        st.rerun()

# Main chat interface
st.markdown(
    """
    <h1 style='text-align: center;'>🎓 BU FAQ ChatBot</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>Ask any questions about Bangkok University</p>", unsafe_allow_html=True)

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-content">
                {message["content"]}
                    <div class="timestamp">{message["timestamp"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <div class="message-content">
                    {message["content"]}
                    <div class="timestamp">{message["timestamp"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Chat input
col1, col2 = st.columns([0.9, 0.1])

with col1:
    user_input = st.text_input(
        "Your question:",
        placeholder="Type your question here...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("", icon=":material/arrow_forward:", help="Send message", use_container_width=True)

# Handle message sending
if send_button and user_input.strip():
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": current_time
    })
    
    # Show loading state
    with st.spinner("Bot is thinking..."):
        try:
            # Call API
            response = requests.post(
                f"{st.session_state.api_url}/chat",
                json={"message": user_input},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                bot_reply = data.get("reply", "Error: No response from server")
            else:
                bot_reply = f"❌ Error: {response.status_code} - {response.text}"
        
        except requests.exceptions.ConnectionError:
            bot_reply = "❌ Error: Cannot connect to API. Make sure FastAPI is running on " + st.session_state.api_url
        except requests.exceptions.Timeout:
            bot_reply = "⏱️ Error: Request timeout. The server took too long to respond."
        except Exception as e:
            bot_reply = f"❌ Error: {str(e)}"
    
    # Add bot response to history
    response_time = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "bot",
        "content": bot_reply,
        "timestamp": response_time
    })
    
    # Rerun to display new messages
    st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #999; font-size: 0.85rem;'>
    <p>Copyright &copy; 2025 BU Faq Chat Bot Group</p>
</div>
""", unsafe_allow_html=True)