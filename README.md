# DataWhisperer – Conversational Business Intelligence

DataWhisperer is a conversational analytics prototype that allows users to interact with business data using natural language. Instead of navigating complex dashboards, users can simply ask questions about their data and receive instant insights along with automated visualizations.

This project was developed as part of the **AI Product Manager Challenge**, demonstrating how conversational AI can transform traditional business intelligence workflows.

---

## Project Overview

Traditional BI tools such as PowerBI and Tableau require users to manually explore dashboards and filters to extract insights. This creates friction for business leaders who need quick answers for decision-making.

DataWhisperer introduces a **Conversational Query Layer** on top of enterprise data. Users upload a dataset and ask questions in natural language. The system uses an LLM to convert the question into a data query, analyze the dataset, and return a clear answer along with a visualization.

This demonstrates the "Magic Moment" where a 10-minute manual Excel analysis can be replaced with a 5-second conversation.

---

## Key Features

Conversational Data Queries
Users can ask natural language questions about their dataset.

LLM-Powered Query Generation
The system uses a Groq-hosted Llama model to convert questions into Pandas queries.

Automated Data Visualization
Charts are automatically generated based on query results.

Simple Web Interface
Built with Streamlit for rapid prototyping and easy deployment.

CSV Data Upload
Users can upload their own sales dataset and analyze it instantly.

---

## Example Interaction

User question:

```
Which region generated the highest revenue?
```

Generated query:

```
df.groupby("Region")["Revenue"].sum().idxmax()
```

Result:

```
West
```

The system can also automatically generate charts such as revenue distribution across regions.

---

## Tech Stack

Frontend / Interface
Streamlit

Data Processing
Pandas

Visualization
Matplotlib / Streamlit charts

LLM Integration
Groq API (Llama 3.1)

Deployment
Streamlit Cloud

---

## Project Structure

```
datawhisperer-mvp
│
├── app.py                 # Streamlit application
├── requirements.txt       # Python dependencies
├── sample_sales_data.csv  # Example dataset for testing
└── README.md              # Project documentation
```

---

## How It Works

1. User uploads a CSV dataset
2. User asks a natural language question
3. The Groq LLM converts the question into a Pandas query
4. The query runs against the dataset
5. The system returns the result and generates a visualization

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/talking-rabbitt-mvp.git
cd talking-rabbitt-mvp
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add Groq API Key

Create a Streamlit secrets file:

```
.streamlit/secrets.toml
```

Add:

```
GROQ_API_KEY="your_groq_api_key"
```

### 4. Run the application

```
streamlit run app.py
```

---

## Example Questions to Try

```
Which region generated the highest revenue?
Show revenue by region
Which product sold the most units?
What is the total revenue by product?
```

---

## Future Improvements

Improved natural language understanding for complex questions

Support for multiple datasets and joins

Predictive analytics and forecasting

Integration with business tools such as Slack or Microsoft Teams

Enterprise data warehouse integration

---

## License

This project was developed as a prototype for a product strategy exercise and is intended for demonstration and educational purposes.
