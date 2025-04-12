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

# 生日倒计时
st.markdown('<h3>⏳ 生日倒计时 ⏳</h3>', unsafe_allow_html=True)
st.markdown("距离秦彻的生日还有多少天？")

# 设置秦彻的生日日期（示例：2025年4月18日）
birthday_month = 4
birthday_day = 18

# 获取当前日期（只取日期部分，忽略时间）
now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# 计算今年的生日日期
current_year = now.year
birthday = datetime(current_year, birthday_month, birthday_day)

# 如果今年的生日已经过了，计算到明年的生日
if now > birthday:
    birthday = datetime(current_year + 1, birthday_month, birthday_day)

# 计算距离生日还有多少天
days_left = (birthday - now).days

st.markdown(
    f"""
    <div class="countdown">
        <h3>距离秦彻的生日还有 {days_left} 天！</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# 视频展示区
st.markdown('<h3>🎬 生日PV 🎬</h3>', unsafe_allow_html=True)


# 留言区
st.markdown('<h3>📝 留言区 📝</h3>', unsafe_allow_html=True)
st.markdown("在这里留下你对秦彻的生日祝福吧！")
st.markdown("**提示：只有公开留言才能留存下来，且公开留言不可删除（我就是想试一下结果删不掉了）**")

with st.form(key="birthday_wish"):
    name = st.text_input("你的名字：")
    wish = st.text_area("写下你的祝福：", height=100)
    is_public = st.checkbox("是否公开留言", value=True)  # 默认公开
    submit_button = st.form_submit_button(label="提交祝福")

# 保存和显示留言
if submit_button:
    if not os.path.exists("wishes.json"):
        with open("wishes.json", "w") as f:
            json.dump([], f)
    
    with open("wishes.json", "r") as f:
        wishes = json.load(f)
    
    new_wish = {
        "name": name,
        "wish": wish,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "is_public": is_public
    }
    
    wishes.append(new_wish)
    
    with open("wishes.json", "w") as f:
        json.dump(wishes, f)
    
    st.success("祝福已提交！")

if os.path.exists("wishes.json"):
    with open("wishes.json", "r") as f:
        wishes = json.load(f)
    
    if wishes:
        st.markdown('<h4>来自大家的祝福：</h4>', unsafe_allow_html=True)
        for wish in reversed(wishes):
            # 检查是否包含is_public键，如果没有，默认为True
            is_public = wish.get("is_public", True)
            if is_public:
                st.markdown(
                    f"""
                    <div class="message-card">
                        <strong>{wish['name']} 在 {wish['time'].split()[1]} 写道：</strong>
                        <p>{wish['wish']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# 幸运抽奖
st.markdown('<h3>🎮 幸运抽奖 🎮</h3>', unsafe_allow_html=True)
st.markdown("参与抽奖，赢取特别礼物！")

prizes = ["彻狸亲亲烧", "秦彻爽", "十连十金符", "幸运抽奖券"]
if st.button("参与抽奖"):
    prize = random.choice(prizes)
    st.balloons()
    st.markdown(
        f"""
        <div class="surprise">
            <h3>🎁 你获得了：{prize}！🎁</h3>
            <p>恭喜你！</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# 心情选择
st.markdown('<h3>😊 心情选择 😊</h3>', unsafe_allow_html=True)
st.markdown("选择你的心情，表达对秦彻的祝福！")

moods = ["❤️", "😍", "🎉", "🥳", "🌟", "🌈", "✨"]
selected_mood = st.selectbox("选择你的心情：", moods)

if st.button("提交心情"):
    if not os.path.exists("moods.json"):
        with open("moods.json", "w") as f:
            json.dump([], f)
    
    with open("moods.json", "r") as f:
        moods_data = json.load(f)
    
    new_mood = {
        "mood": selected_mood,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    moods_data.append(new_mood)
    
    with open("moods.json", "w") as f:
        json.dump(moods_data, f)
    
    st.success("心情已提交！")

if os.path.exists("moods.json"):
    with open("moods.json", "r") as f:
        moods_data = json.load(f)
    
    if moods_data:
        st.markdown('<h4>大家的心情：</h4>', unsafe_allow_html=True)
        for mood in reversed(moods_data):
            st.markdown(
                f"""
                <div class="message-card">
                    <p>{mood['mood']} - {mood['time'].split()[1]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# 特别惊喜
st.markdown('<h3>🎉 特别惊喜 🎉</h3>', unsafe_allow_html=True)
st.markdown("点击下方按钮，给秦彻一个特别的惊喜！")

if st.button("🎉 点击这里给秦彻一个惊喜 🎉"):
    st.balloons()
    st.markdown(
        """
        <div class="surprise">
            <h3>🎈 生日快乐，秦彻！🎈</h3>
            <p>愿你的每一天都充满光和希望！</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 页脚
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; color: #FF6347;">
        <p>祝秦彻生日快乐！愿你新的一岁平安喜乐，万事胜意！</p>
        <p>🎉 生日快乐，永远18岁！🎉</p>
    </div>
    """,
    unsafe_allow_html=True
)
