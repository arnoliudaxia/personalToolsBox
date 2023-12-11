import pandas as pd
import streamlit as st
from PIL import Image
from pillow_lut import load_cube_file, amplify_lut


@st.cache_data
def load_lut(path):
    return load_cube_file(path)


"LUT加载工具"

uploaded_file = st.file_uploader("选择一张图片", type=["jpg", "jpeg", "png"])
lutCatcategory = st.tabs(["自然系"])
#TODO 这里填写所有的预制LUT
lutExampleImgSetting={
    "自然系": [("assets/LUTs/MIX_小清新.png","自然小清新")],
}
lutPath={
    "自然小清新":"assets/LUTs/MIX_小清新.cube",
}
ColumeNumberOfEachCategory = 2

for idx, (cat, imgs) in enumerate(lutExampleImgSetting.items()):
    with lutCatcategory[idx]:
        threeExampleCol=st.columns(ColumeNumberOfEachCategory)
        for img,cap in imgs:
            threeExampleCol[idx % ColumeNumberOfEachCategory].image(Image.open(img), caption=cap, use_column_width=True)

st.text_input(label="想要使用的LUT的名称", key="lutName")

if st.session_state["lutName"] in lutPath:
    loadingText=st.empty()
    loadingText.text("正在加载LUT")
    lut = load_lut(lutPath[st.session_state["lutName"]])
    # 用户上传图片
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        loadingText.image(image, caption='原图', use_column_width=True)
        amplify = st.slider("LUT强度", 0.0, 1.0, 0.3)
        st.image(image.filter(amplify_lut(lut, amplify)), caption='LUT', use_column_width=True)
