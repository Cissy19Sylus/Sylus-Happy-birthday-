import streamlit as st
import json
import os
from datetime import datetime

# 设置页面配置
st.set_page_config(
    page_title="秦彻生日快乐",
    page_icon="🔥",
    layout="wide"
)

# 自定义CSS样式
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #FF0000;
        text-align: center;
        font-size: 48px;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #FF4500;
        text-align: center;
        font-size: 24px;
        margin-bottom: 40px;
    }
    .message-card {
        background-color: #2E2E2E;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-left: 4px solid #FF0000;
    }
    .quote-card {
        background-color: #2E2E2E;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-left: 4px solid #FF0000;
    }
    .photo-gallery {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
    }
    .photo {
        width: 200px;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        transition: transform 0.3s;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .photo:hover {
        transform: scale(1.05);
    }
    .birthday-cake {
        text-align: center;
        margin: 40px 0;
    }
    .surprise {
        text-align: center;
        margin: 40px 0;
        padding: 20px;
        background-color: #2E2E2E;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .crow {
        width: 100px;
        height: 100px;
        margin: 10px;
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 页面标题
st.markdown('<h1 class="title">🔥 秦彻生日快乐！🔥</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">愿你岁岁平安，万事胜意！</h2>', unsafe_allow_html=True)

# 秦彻语录
st.markdown('<h3>✨ 秦彻语录 ✨</h3>', unsafe_allow_html=True)
quotes = [
    "“看清楚了么？这才是你内心真正的欲望。”",
    "“别在这里倒下，因为你一旦在这里倒下，就不能回头了。”",
    "“你是我唯一的例外。”",
    "“即使世界崩塌，我也不会放手。”",
    "“你是我存在的意义。”",
    "“别怕，我会保护你。”",
    "“你是我唯一的答案。”",
]

random_quote = random.choice(quotes)
st.markdown(
    f"""
    <div class="quote-card">
        <p style="font-style: italic; font-size: 18px;">"{random_quote}"</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 留言区
st.markdown('<h3>📝 留言区 📝</h3>', unsafe_allow_html=True)
st.markdown("在这里留下你对秦彻的生日祝福吧！")

with st.form(key="birthday_wish"):
    name = st.text_input("你的名字：")
    wish = st.text_area("写下你的祝福：", height=100)
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
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            st.markdown(
                f"""
                <div class="message-card">
                    <strong>{wish['name']} 在 {wish['time'].split()[1]} 写道：</strong>
                    <p>{wish['wish']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# 秦彻乌鸦展示区
st.markdown('<h3>🐦 秦彻的乌鸦 🖤</h3>', unsafe_allow_html=True)

# 使用随机乌鸦图片
crows = [
    "https://cdn-icons-png.flaticon.com/512/1046/1046777.png",
    "https://cdn-icons-png.flaticon.com/512/1046/1046776.png",
    "https://cdn-icons-png.flaticon.com/512/1046/1046775.png",
]

st.markdown(
    """
    <div class="photo-gallery">
    """,
    unsafe_allow_html=True
)

for crow in crows:
    st.markdown(
        f"""
        <img src="{crow}" class="crow" alt="Crow">
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    </div>
    """,
    unsafe_allow_html=True
)

# 特别惊喜
st.markdown('<h3>🎉 特别惊喜 🎉</h3>', unsafe_allow_html=True)
st.markdown("点击下方按钮，给秦彻一个特别的惊喜！")

if st.button("🔥 点击这里给秦彻一个惊喜 🔥"):
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
    <div style="text-align: center; margin-top: 50px; color: #FF4500;">
        <p>祝秦彻生日快乐！愿你新的一岁平安喜乐，万事胜意！</p>
        <p>🔥 生日快乐，永远18岁！🔥</p>
    </div>
    """,
    unsafe_allow_html=True
)
