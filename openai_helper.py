import re
import pandas as pd
import dotenv
import os
from openai import OpenAI,RateLimitError
dotenv.load_dotenv()
import json
client = OpenAI(api_key=os.getenv("api_key"))

def extract_json(content):
  try:
    match = re.search(r'\{.*\}', content, re.DOTALL)
    if match:
      return json.loads(match.group())
  except:
    pass
  return None


def fallback_extraction(text):
  # Simple regex fallback (no API needed)
  revenue = re.search(r'revenue of ([\d\.]+\s*billion)', text, re.I)
  profit = re.search(r'([\d\.]+\s*billion)\s*\$\s*profit', text, re.I)
  eps = re.search(r'earnings per share.*?([\d\.]+\s*\$)', text, re.I)

  return {
    "Company Name": "Amazon" if "amazon" in text.lower() else "",
    "Stock Symbol": "AMZN" if "amazon" in text.lower() else "",
    "Revenue": revenue.group(1) + " $" if revenue else "",
    "Net Income": profit.group(1) + " $" if profit else "",
    "EPS": eps.group(1) if eps else ""
  }

def extract_financial_data(text):
  prompt = get_prompt_financial() + text

  try:
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content
    data = extract_json(content)

    if data:
      return pd.DataFrame(data.items(), columns=["Measure", "Value"])

  except RateLimitError:
    print("⚠️ API quota exceeded. Using fallback...")
    data = fallback_extraction(text)
    return pd.DataFrame(data.items(), columns=["Measure", "Value"])

  except Exception as e:
    print(f"Unexpected error: {e}")

    # final safe fallback
  return pd.DataFrame({
    "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
    "Value": ["", "", "", "", ""]
  })


def get_prompt_financial():
  return '''Please retrieve company name, revenue, net income and earnings per share(a.k.a. EPS)
  from the following news article. If you can't find the information from this article 
  then return "". Do not make things up.    
  Then retrieve a stock symbol corresponding to that company. For this you can use
  your general knowledge (it doesn't have to be from this article). Always return your
  response as a valid JSON string. The format of that string should be this, 
  {
    "Company Name": "Walmart",
    "Stock Symbol": "WMT",
    "Revenue": "12.34 million",
    "Net Income": "34.78 million",
    "EPS": "2.1 $"
  }
  News Article:
  ============

  '''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  text = '''
    Tesla's Earning news in text format: Tesla's earning this quarter blew all theestimates. They reported 4.5 billion $ profit against a revenue of 30 billion $.Their earnings per share was 2.3 $
  '''
  df = extract_financial_data(text)

  print(df.to_string())