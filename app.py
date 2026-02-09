import streamlit as st
from ai_topic import get_topic
from ai_script import generate_script
from video_renderer import render_video
from youtube_optimizer import optimize_youtube

st.set_page_config(page_title="AI 올인원 영상 제작기", layout="centered")

st.title("🎬 AI 올인원 영상 제작기 (TTS 제외)")

category = st.selectbox("카테고리", ["부동산", "경제", "전쟁", "역사"])
duration = st.selectbox("영상 길이(초)", [30, 60])

if st.button("🚀 전체 자동 제작"):
    with st.spinner("주제 선정 중..."):
        topic = get_topic(category)
        st.write("📌 주제:", topic)

    with st.spinner("대본 생성 중..."):
        script = generate_script(topic, duration)
        st.write("📝 대본:", script)

    with st.spinner("영상 렌더링 중..."):
        video_path = render_video(script)
        st.video(video_path)

    with st.spinner("유튜브 최적화 중..."):
        yt = optimize_youtube(topic, script)
        st.text_area("📈 유튜브 업로드 정보", yt, height=300)
