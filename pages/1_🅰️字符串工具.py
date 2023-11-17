import streamlit as st
import re


"ChatGPT相关工具"

Convert2Notion, tab2, tab3 = st.tabs(["Convert2Notion", "Dog", "Owl"])


with Convert2Notion:
    "说明：将chatgpt中复制的内容的格式适配notion"

    output=""

    chatgptOutput=st.text_area("chatgpt输出")
    if chatgptOutput!="":
        ss=re.split(r'\\\(|\\\)', chatgptOutput)
        # 所有的公式是奇数索引处
        for i in range(len(ss)):
            if i%2==0:
                output+=ss[i]
            else:
                output+="$"+ss[i]+"$"

        st.text_area("chatgptConvert2notionOuput",value=output)
