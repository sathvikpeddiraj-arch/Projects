# 🍽️ Smart Menu System

A simple, interactive restaurant menu and billing application built with **Python** and **Streamlit**. Browse menu items, filter by category, select quantities, and generate an itemized bill with an automatically calculated total.

## ✨ Features

- 📋 **Menu Display** — View available menu items, their categories, and prices.
- 🔎 **Category Filtering** — Filter menu items by category.
- 🛒 **Quantity Selection** — Choose quantities for individual items.
- 🧾 **Automatic Billing** — Generate an itemized bill with subtotals.
- 💰 **Total Calculation** — Calculate the grand total automatically.
- ✅ **Order Confirmation** — Confirm an order through an interactive interface.
- 📂 **JSON Data Handling** — Load menu information from a JSON file.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| JSON | Menu data storage |

## 📁 Project Structure

```text
smart-menu-system/
├── app.py
├── menu.json
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python 3.9 or later
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/sathvikpeddiraj-arch/Projects.git
```

Navigate into the project directory:

```bash
cd Projects
```

> **Note:** The repository is named `Projects`. If the application is inside a `smart-menu-system` subfolder, navigate into that folder before continuing.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 🎯 Project Objective

This project was built to practice Python programming and develop a practical, interactive application using Streamlit. It demonstrates JSON data handling, category-based filtering, quantity management, session state, and basic billing logic.

## 🔮 Future Improvements

- Add a search function for menu items.
- Improve input validation and error handling.
- Store confirmed orders persistently.
- Add order history and sales summaries.
- Improve the user interface with menu images and a more polished layout.

## 👨‍💻 Author

**Sathvik Peddiraj**

A Python project created as part of my journey in application development and problem-solving.

## 📄 License

See the [LICENSE](LICENSE) file for the licensing terms of this project.
