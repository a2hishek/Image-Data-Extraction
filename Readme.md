# 🧾 Image-to-Structured-Menu Data Extractor

This project is a Streamlit-based web app that performs **structured data extraction** from menu images using **Google Gemini (via LangChain)** and outputs a clean, downloadable CSV file. It detects food items, categories, types (Veg/Non-Veg), descriptions, prices, and add-ons from menu images.

---

## 📌 Features

* 🔍 Extracts **structured data** (restaurant, category, item, price, type, add-ons) from menu images.
* 📦 Uses **Google Gemini (Generative AI)** via LangChain with **structured output schema**.
* 🖼️ Supports image upload (JPG, PNG, JPEG).
* 📋 Displays extracted data as a table in the app.
* 💾 Exports the result as a **CSV file** for download.

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** – Web UI
* **LangChain** – LLM chaining and structured output
* **Google Gemini API** – Image understanding and extraction
* **Pydantic** – Schema validation for structured data
* **Pandas** – Dataframe manipulation
* **dotenv** – Environment variable handling

---

## 📁 Project Structure

```bash
.
├── app.py                  # Streamlit frontend
├── model.py                # Image processing, LLM calls, data transformation
├── schema.py               # Pydantic schema for structured output
├── .env                    # Contains GOOGLE_API_KEY
├── /data                   # Folder to save downloaded CSVs
├── /images                 # Folder of menu images
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/a2hishek/Image-Data-Extraction.git
cd image-menu-extractor
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
.\venv\Scripts\activate  # or source venv/bin/activate on Mac

pip install -r requirements.txt
```

### 3. Add your Google API Key

Create a `.env` file in the project root with the following content:

```
GOOGLE_API_KEY=your_google_genai_api_key
```

> Alternatively, the app will prompt you to enter the key when running.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. **Upload Image** – Menu image with food categories and items.
2. **Gemini LLM Prompting** – Image and context are sent to Gemini using LangChain with a `Pydantic` schema.
3. **Structured Response** – LLM returns a JSON conforming to the schema.
4. **Tabular View** – Parsed JSON is converted to a DataFrame.
5. **Download CSV** – Export and save results.

---

## ✅ Output Format

Each row in the CSV contains:

* Restaurant Name & Area
* Category ID & Name
* Item ID, Name, Description, Price, Type (Veg/Non-Veg)
* Add-on Name & Price (if any)

---

