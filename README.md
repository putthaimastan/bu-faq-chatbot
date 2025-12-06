# BU FAQ Chatbot

A conversational AI chatbot for answering frequently asked questions about Bangkok University, built with FastAPI backend and Streamlit frontend.

## Features

- **Real-time FAQ retrieval** - Instant answers from Bangkok University knowledge base
- **Thai language support** - Fully supports Thai language queries and responses
- **Modern UI** - Clean and responsive chat interface
- **RESTful API** - Backend API built with FastAPI
- **LLM-powered** - Uses Groq's Llama 3.3 70B model for intelligent responses

## Project Structure

```
bu-faq-chatbot/
├── main.py                 # FastAPI backend server
├── src/
│   └── app.py             # Streamlit frontend
├── bu_faq_data.json       # FAQ knowledge base
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md             
```

## 🔧 Prerequisites

- Python
- Groq API key (get it from https://console.groq.com)

## Installation

1. **Clone the repository** (or download the files)

   ```bash
   git clone https://github.com/putthaimastan/bu-faq-chatbot.git
   cd bu-faq-chatbot
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Prepare FAQ data**

   Ensure `bu_faq_data.json` exists in the project root with the following structure:

   ```json
   [
     {
       "id": 1,
       "category": "หมวดหมู่",
       "question": "คำถาม",
       "answer": "คำตอบ",
       "keywords": ["คีย์เวิร์ด1", "คีย์เวิร์ด2"]
     }
   ]
   ```

## Running the Application

### Option 1: Run Both Servers Separately

**Step 1: Start the FastAPI Backend**

Open a terminal and run:

```bash
uvicorn main:app --reload --port 5000
```

The API will be available at `http://localhost:5000`

**Step 2: Start the Streamlit Frontend**

Open a **new terminal** (keep the first one running) and run:

```bash
streamlit run src/app.py
```

The web interface will automatically open at `http://localhost:8501`

## Usage

1. Open your browser to `http://localhost:8501` (Streamlit interface)
2. Type your question about Bangkok University in Thai
3. Click the send button or press Enter
4. The chatbot will respond with relevant information from the FAQ database

### Example Questions

- "มหาวิทยาลัยกรุงเทพตั้งอยู่ที่ไหน?"
- "สมัครเรียนต้องทำอย่างไร?"
- "มีคณะอะไรบ้าง?"

## API Endpoints

### GET `/`

Health check endpoint

```bash
curl http://localhost:5000/
```

Response:

```json
{
  "message": "BU FAQ Chatbot API is running!"
}
```

### POST `/chat`

Send a question to the chatbot

Request:

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "มหาวิทยาลัยกรุงเทพตั้งอยู่ที่ไหน?"}'
```

Response:

```json
{
  "reply": "มหาวิทยาลัยกรุงเทพตั้งอยู่ที่..."
}
```

## Configuration

### Backend Configuration (main.py)

- **Port**: Default 5000 (change with `--port` flag)
- **Model**: `llama-3.3-70b-versatile`

### Frontend Configuration (src/app.py)

- **API URL**: Configure in sidebar (default: `http://localhost:5000`)
- **Page Title**: "BU FAQ Chatbot"

## Troubleshooting

### "Cannot connect to API" error

- Ensure FastAPI server is running on port 5000
- Check if the API URL in Streamlit sidebar is correct

### "No response from server"

- Check your Groq API key in `.env` file
- Verify internet connection (required for Groq API)
- Check Groq API rate limits

### Import errors

- Ensure all dependencies are installed: `pip install -r requirements.txt`
