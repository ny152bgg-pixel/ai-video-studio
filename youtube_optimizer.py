from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def optimize_youtube(topic, script):
    prompt = f"""
    주제: {topic}
    대본: {script}

    1. 조회수 잘 나오는 제목
    2. 설명란 (해시태그 포함)
    3. 태그 10개
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
