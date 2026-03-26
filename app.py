import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq

st.set_page_config(page_title="DataWhisperer", layout="wide")

st.title("💬 DataWhisperer")
st.subheader("Conversational Intelligence for Business Data")

# Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

uploaded_file = st.file_uploader("Upload your sales CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about your data")

    if question:

        prompt = f"""
        You are a data analyst.

        The dataframe is called df.

        Columns:
        {df.columns.tolist()}

        Convert the user's question into a valid pandas expression.

        Only return the python expression.

        Example:
        df.groupby("Region")["Revenue"].sum()

        Question:
        {question}
        """

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You write pandas queries."},
                    {"role": "user", "content": prompt}
                ]
            )

        query = response.choices[0].message.content.strip()

        st.subheader("Generated Query")
        st.code(query)

        try:

            result = eval(query)

            st.subheader("Result")
            st.write(result)

            if isinstance(result, pd.Series):
                st.subheader("Visualization")
                st.bar_chart(result)

        except Exception as e:
            st.error("Could not run generated query.")
            st.write(e)