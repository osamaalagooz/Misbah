import streamlit as st
import pandas as pd
from core_ai import PandasAI
from core_ai.llm.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from core_ai.middlewares import StreamlitMiddleware
from PIL import Image

df = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [21400000, 2940000, 2830000, 3870000, 2160000, 1350000, 1780000, 1320000, 516000, 14000000],
    "happiness_index": [7.3, 7.2, 6.5, 7.0, 6.0, 6.3, 7.3, 7.3, 5.9, 5.0]
})


OPENAI_API_KEY = "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"
llm = OpenAI(api_token=OPENAI_API_KEY, streaming=True)

pandas_ai = PandasAI(llm,verbose=True, save_charts=True, save_charts_path="./images")
res = pandas_ai.run(df, prompt="What are the 5 happiest countries", show_code=True)
image_path = f"/images/exports/charts/{pandas_ai._prompt_id}/chart.png"

print(res)
