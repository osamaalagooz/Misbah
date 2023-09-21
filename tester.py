import streamlit as st
import pandas as pd
from core_ai import Misbah
from core_ai.llm.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from PIL import Image

df = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [21400000, 2940000, 2830000, 3870000, 2160000, 1350000, 1780000, 1320000, 516000, 14000000],
    "happiness_index": [7.3, 7.2, 6.5, 7.0, 6.0, 6.3, 7.3, 7.3, 5.9, 5.0]
})


OPENAI_API_KEY = "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"
llm = OpenAI(api_token=OPENAI_API_KEY, streaming=True)

misbah_ai = Misbah(llm,verbose=True, save_charts=True, save_charts_path="./images")
res = misbah_ai.run(df, prompt="What are the 5 happiest countries")
image_path = f"/images/exports/charts/{misbah_ai._prompt_id}/chart.png"

print(res)
