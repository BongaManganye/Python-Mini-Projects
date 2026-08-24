#RAG Python
#How to Generate Text Summaries for Tables

from openai import OpenAI
import pandas as pd

def summarize_tables(row):
    summary_prompt = f"""You are an assistant tasked with summarizing tables. \
        Give a concise summary of the table. Table chunk: {row.table}"""

#Initialize the OpenAI API client and generate the table summary
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": summary_prompt}],
    temperature=0.7,
    max_tokens=150,
)

row["table_summary"] = response.choices[0].message.content

return row

#create a pandas dataframe from the tables
tables_df = pd.DataFrame(tables, columns=["table"])

#Add a column to the dataframe to store the summaries
tables_df = tables_df.apply(summarize_tables, axis=1 )
