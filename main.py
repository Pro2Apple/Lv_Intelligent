import streamlit as st
from click import password_option
from streamlit import video, divider

from utils import script_master


st.title("🎬 视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入 OpenAI_API 密钥🔑：", type = "password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

subject = st.text_input("💡 请输入视频的主题：")
st.divider()
video_length = st.number_input("⌚⏱️ 请输入视频的大致时常（单位：秒）：", min_value=10, max_value = 180, step = 10)
st.divider()
creativity = st.slider("🪄 请输入视频脚本的创造力（数字越小创造性越低，内容越严谨；数字大创造性越高，容易产生幻觉)", value = 1.0, min_value=0.1, max_value=1.2, step=0.05)
st.divider()

submit = st.button("开始生成")
if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()

if submit and not subject:
    st.info("请输入视频的主题！")
    st.stop()

if submit:
    with st.spinner("AI正在绞尽脑汁创作中，请稍等..."):
        search_result, title, script = script_master(subject, video_length, creativity, openai_api_key)
    st.success("视频脚本已经生成！✅")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("🗒️ 脚本：")
    st.write(script)
    with st.expander("维基百科搜索结果 🔍："):
        st.info(search_result)