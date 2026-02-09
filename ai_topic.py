from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_topic(category):
    prompt = f"""
    유튜브 {category} 분야에서
    최근 조회수 잘 나올 만한 쇼츠 주제 1개만 추천해줘.
    자극적이지만 과장하지 말 것.
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content.strip()
