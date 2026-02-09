from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_script(topic, duration):
    prompt = f"""
    주제: {topic}
    영상 길이: {duration}초

    쇼츠용 대본을
    1. 훅
    2. 핵심
    3. 인사이트
    4. 마무리

    자막용으로 짧은 문장 위주로 작성
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return [line for line in res.choices[0].message.content.split("\n") if line.strip()]
