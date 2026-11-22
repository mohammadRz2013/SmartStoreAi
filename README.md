
# 🛍️ SmartStore AI

### Your Personal AI Shopping Assistant

SmartStore AI is an intelligent shopping platform powered by Artificial Intelligence.

Instead of searching through hundreds of products manually, simply tell the AI what you're looking for.

The AI understands your needs, searches through the available products, recommends the most relevant options, and explains why each product might be the right choice for you.

**Shopping is no longer just searching. It's a conversation.**

---

## ✨ Features

- 🤖 **AI Shopping Assistant** — Talk to an AI to find the products you need.
- 🔎 **Semantic Product Search** — Find products based on their meaning, not just exact keywords.
- 🎯 **Smart Recommendations** — Get relevant products based on your requirements.
- 📦 **Product Information** — Receive detailed explanations about recommended products.
- 💬 **Natural Language Interaction** — Describe what you want using everyday language.

---

## 🧠 How It Works

SmartStore AI combines Artificial Intelligence with Vector Search to provide a smarter shopping experience.

1. **User Input:** Describe the product you're looking for.
2. **AI Processing:** The AI understands your request.
3. **Semantic Search:** The system searches the product database using vector embeddings.
4. **Product Retrieval:** Relevant products are retrieved from the database.
5. **AI Response:** The AI presents the products and explains why they match your needs.

---

## 🛠️ Technologies

- Python
- OpenAI-compatible AI API
- Rag
- Embedding Models
- Qdrant Vector Database
- Docker
- PostgreSQL

---

## 🚀 Getting Started

Follow these steps to run SmartStore AI locally.

### 1. Clone the Repository

```bash
git clone MY_REPOSITORY_URL
```

```bash
cd SmartStore-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r req.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your API credentials and configuration.

```env
embaikey=Your_AvalAI_key
aikey=Your_apiKey_from_gen.pollinations.ai
aiurl='https://gen.pollinations.ai/v1/chat/completions'
embaiurl="https://api.avalai.ir/v1"
qdranturl="http://localhost:7000"
```

### 5. Start Docker Services

Make sure Docker Desktop or Docker Engine is running.

```bash
docker compose up -d
```

### 6. Run the Application

```bash
python main.py
```
it's in the src folder

That's it! Your SmartStore AI assistant is ready.

---

## 📁 Project Structure

```text
SmartStore-AI/
│
├── src
├────  test_ai.py
├────  main.py
├
├── venv
├── .env
├── Readme.md
├── req.txt
└── ...
```

---

## 🎯 Project Goal

The goal of SmartStore AI is to make online shopping more intelligent, convenient, and personalized.

Traditional online stores require users to search, filter, and compare products manually.

SmartStore AI changes this experience by allowing users to communicate their needs naturally and receive intelligent product recommendations.

---

### 📫 Contact Me

- instagram: https://www.instagram.com/mohammadreza_sj2931/
- telegram: https://t.me/MrRobot_m
- email: mohammadsj9231@gmail.com
---

<p align="center">
  **SmartStore AI — Find What You Need, Just by Asking.**
</p>
