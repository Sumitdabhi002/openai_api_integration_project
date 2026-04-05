# 📊 Financial Data Extraction Tool

A simple and intelligent web app that extracts key financial metrics from unstructured news articles using AI + fallback logic.

---

## 🚀 Features

* ✅ Extracts:

  * Company Name
  * Stock Symbol
  * Revenue
  * Net Income
  * Earnings Per Share (EPS)

* ✅ Handles messy real-world text

* ✅ Uses OpenAI for intelligent extraction

* ✅ Includes regex fallback (works even without API)

* ✅ Clean UI built with Streamlit

* ✅ Production-safe error handling

---

## 🧠 How It Works

1. User inputs a financial news article
2. App sends the text to an LLM (OpenAI)
3. Extracts structured JSON data
4. If API fails → fallback to regex-based extraction
5. Displays results in a clean table

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* Pandas
* Regex (re)

---

## 📂 Project Structure

```
project/
│── main.py                 # Streamlit UI
│── openai_helper.py        # Extraction logic
│── requirements.txt
│── Procfile                # For deployment (Railway)
│── .env                    # Local environment variables
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Set environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the app

```
streamlit run main.py
```

---

## 🌐 Deployment (Railway)

1. Push code to GitHub
2. Go to https://railway.app
3. Create new project → Deploy from GitHub
4. Add environment variable:

```
OPENAI_API_KEY=your_api_key_here
```

5. Done 🎉

---

## ⚠️ Error Handling

The app gracefully handles:

* API quota errors
* Invalid JSON responses
* Missing data

If the API fails, it automatically switches to a **regex-based fallback system**.

---

## 🧪 Example Input

```
Amazon's earning this quarter exceeded market expectations. 
They reported 6.2 billion $ profit against a revenue of 42 billion $. 
Their earnings per share was 3.1 $.
```

---

## 📊 Example Output

| Measure      | Value         |
| ------------ | ------------- |
| Company Name | Amazon        |
| Stock Symbol | AMZN          |
| Revenue      | 42 billion $  |
| Net Income   | 6.2 billion $ |
| EPS          | 3.1 $         |

---


## 👨‍💻 Author

**Sumit Dabhi**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub — it helps!

---
