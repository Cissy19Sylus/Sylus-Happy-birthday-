import streamlit as st
st.title('秦彻生日快乐')
  if st.button("Send balloons!"):
    st.balloons()
st.badge("秦彻生日快乐！", color="red")
  if st.checkbox('秦彻生日快乐！'):
      video_file = open('./秦彻PV.mp4', 'rb')
      video_bytes = video_file.read()

      st.video(video_bytes)
      st.write('视频来自恋与深空官网')
    
