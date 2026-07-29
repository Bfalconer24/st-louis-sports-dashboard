import os
import sqlite3
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

connection = sqlite3.connect("sports.db")
cursor = connection.cursor()

cursor.execute("""
SELECT player_name, team_name, position, nationality
FROM Players
LIMIT 1
""")

player = cursor.fetchone()

connection.close()

prompt = f"""
Write a professional soccer scout report in under 150 words.

Player: {player[0]}
Club: {player[1]}
Position: {player[2]}
Nationality: {player[3]}

Format:

Strengths:
- 3 bullet points

Weaknesses:
- 2 bullet points

Overall Evaluation:
One short paragraph.

Keep the report concise and suitable for a GitHub portfolio.
"""

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print(response.output_text)