import streamlit as st
import json
import random
import time
import os
from datetime import datetime
import base64

# 设置页面标题和图标
st.set_page_config(page_title="秦彻生日快乐", page_icon="🎉", layout="wide")

# 自定义CSS样式
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #FFF5E6;
    }
    .stApp {
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #FF6B6B;
        text-align: center;
        font-size: 48px;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #4A90E2;
        text-align: center;
        font-size: 24px;
        margin-bottom: 40px;
    }
    .birthday-cake {
        text-align: center;
        margin: 40px 0;
    }
    .gift {
        width: 100px;
        height: 100px;
        margin: 10px;
        display: inline-block;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .gift:hover {
        transform: scale(1.1);
    }
    .message-card {
        background-color: #FFF;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .balloon {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin: 10px;
        display: inline-block;
        cursor: pointer;
        animation: float 3s infinite ease-in-out;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .confetti {
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: #f00;
        opacity: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 页面标题
st.markdown('<h1 class="title">🎉 秦彻生日快乐！ 🎉</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">愿你岁岁平安，万事胜意！</h2>', unsafe_allow_html=True)

# 生日蛋糕动画
st.markdown(
    """
    <div class="birthday-cake">
        <img src="https://cdn-icons-png.flaticon.com/512/2423/2423241.png" width="300">
    </div>
    """,
    unsafe_allow_html=True,
)

# 生日祝福区
st.markdown('<h3>🎂 生日祝福区 🎂</h3>', unsafe_allow_html=True)
with st.form(key="birthday_wish"):
    name = st.text_input("你的名字：")
    wish = st.text_area("写下你的祝福：", height=100)
    submit_button = st.form_submit_button(label="提交祝福")

# 保存和显示祝福
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

# 生日小游戏
st.markdown('<h3>🎮 生日小游戏 🎮</h3>', unsafe_allow_html=True)
st.markdown("点击气球，看看你能戳破多少个！")

# 气球游戏
balloon_colors = ["#FF5252", "#FF4081", "#E040FB", "#7C4DFF", "#536DFE", "#448AFF", "#40C4FF", "#18FFFF", "#64FFDA", "#69F0AE"]
balloons = []

if "balloon_count" not in st.session_state:
    st.session_state.balloon_count = 0

def create_balloon():
    color = random.choice(balloon_colors)
    left = random.randint(0, 800)
    top = random.randint(100, 400)
    balloon_id = f"balloon_{len(balloons)}"
    balloons.append({
        "id": balloon_id,
        "color": color,
        "left": left,
        "top": top
    })
    return balloon_id

def pop_balloon(balloon_id):
    global balloons
    balloons = [balloon for balloon in balloons if balloon["id"] != balloon_id]
    st.session_state.balloon_count += 1

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if not st.session_state.game_started:
    if st.button("开始游戏"):
        st.session_state.game_started = True
        for _ in range(10):
            create_balloon()

if st.session_state.game_started:
    for balloon in balloons:
        st.markdown(
            f"""
            <div style="position: relative; width: 100%; height: 500px;">
                <div class="balloon" id="{balloon['id']}" style="background-color: {balloon['color']}; position: absolute; left: {balloon['left']}px; top: {balloon['top']}px;" onclick="popBalloon('{balloon['id']}')"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown(f"已戳破气球：{st.session_state.balloon_count} 个")
    
    if st.button("再加10个气球"):
        for _ in range(10):
            create_balloon()

# 礼物展示区
st.markdown('<h3>🎁 礼物展示区 🎁</h3>', unsafe_allow_html=True)
st.markdown("点击礼物，给秦彻送上你的祝福！")

gifts = [
    {"name": "蛋糕", "image": "https://cdn-icons-png.flaticon.com/512/1049/1049249.png"},
    {"name": "礼物盒", "image": "https://cdn-icons-png.flaticon.com/512/2423/2423241.png"},
    {"name": "蜡烛", "image": "https://cdn-icons-png.flaticon.com/512/4125/4125831.png"},
    {"name": "气球", "image": "https://cdn-icons-png.flaticon.com/512/1864/1864519.png"},
    {"name": "彩带", "image": "https://cdn-icons-png.flaticon.com/512/2423/2423241.png"},
]

gift_col1, gift_col2, gift_col3, gift_col4, gift_col5 = st.columns(5)

with gift_col1:
    st.image(gifts[0]["image"], width=100)
    if st.button(gifts[0]["name"]):
        st.balloons()
        st.success(f"你送出了一个{gifts[0]['name']}！")

with gift_col2:
    st.image(gifts[1]["image"], width=100)
    if st.button(gifts[1]["name"]):
        st.balloons()
        st.success(f"你送出了一个{gifts[1]['name']}！")

with gift_col3:
    st.image(gifts[2]["image"], width=100)
    if st.button(gifts[2]["name"]):
        st.balloons()
        st.success(f"你送出了一个{gifts[2]['name']}！")

with gift_col4:
    st.image(gifts[3]["image"], width=100)
    if st.button(gifts[3]["name"]):
        st.balloons()
        st.success(f"你送出了一个{gifts[3]['name']}！")

with gift_col5:
    st.image(gifts[4]["image"], width=100)
    if st.button(gifts[4]["name"]):
        st.balloons()
        st.success(f"你送出了一个{gifts[4]['name']}！")

# 添加JavaScript代码
st.markdown(
    """
    <script>
    function popBalloon(balloonId) {
        var balloon = document.getElementById(balloonId);
        balloon.style.opacity = '0';
        balloon.style.transform = 'scale(1.5)';
        balloon.style.transition = 'all 0.3s ease-out';
        
        setTimeout(function() {
            balloon.remove();
        }, 300);
        
        // 更新Streamlit状态
        var params = new URLSearchParams();
        params.append('balloon_count', window.parent.stSessionState.balloon_count + 1);
        var url = window.location.href.split('?')[0] + '?' + params.toString();
        window.parent.location.href = url;
    }
    </script>
    """,
    unsafe_allow_html=True
)

# 页脚
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; color: #777;">
        <p>愿你，灵魂永不消散</p>
        <p>🎈 秦彻，生日快乐！🎈</p>
    </div>
    """,
    unsafe_allow_html=True
)
