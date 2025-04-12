import streamlit as st
import json
import os
from datetime import datetime, timedelta
import random
import time

# 设置页面配置
st.set_page_config(
    page_title="秦彻生日快乐",
    page_icon="🎉",
    layout="wide"
)

# 自定义CSS样式
st.markdown(
    """
    <style>
    body {
        background-color: #FFF5E6;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #FF0000;
        text-align: center;
        font-size: 48px;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #FF6347;
        text-align: center;
        font-size: 24px;
        margin-bottom: 40px;
    }
    .message-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #FF0000;
    }
    .video-container {
        text-align: center;
        margin: 40px 0;
    }
    .surprise {
        text-align: center;
        margin: 40px 0;
        padding: 20px;
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .wish-bottle {
        text-align: center;
        margin: 40px 0;
        padding: 20px;
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .lottery {
        text-align: center;
        margin: 40px 0;
        padding: 20px;
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .countdown {
        text-align: center;
        margin: 40px 0;
        padding: 20px;
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .mood {
        text-align: center;
        margin: 40px 0;
        padding: 20px;
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 页面标题
st.markdown('<h1 class="title">🎉 秦彻生日快乐！ 🎉</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">愿你岁岁平安，万事胜意！</h2>', unsafe_allow_html=True)

# 视频展示区
st.markdown('<h3>🎬 秦彻视频 🎬</h3>', unsafe_allow_html=True)
st.markdown("在这里观看与秦彻相关的视频吧！")

# 添加一个视频（示例使用一个公开的视频链接）
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # 示例视频链接，请替换为实际的秦彻相关视频
st.video(video_url)

# 留言区
st.markdown('<h3>📝 留言区 📝</h3>', unsafe_allow_html=True)
st.markdown("在这里留下你对秦彻的生日祝福吧！")
st.markdown("**提示：只有公开留言才能留存下来，且公开留言不可删除。**")

with st.form(key="birthday_wish"):
    name = st.text_input("你的名字：")
    wish = st.text_area("写下你的祝福：", height=100)
    is_public = st.checkbox("是否
