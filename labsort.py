import streamlit as st
import random

# 研究室リスト
labs = [
    "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
    "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
    "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
    "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
    "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
]
random.seed(42)
random.shuffle(labs)

st.title("研究室興味ランキング調査")

# 初期化
if "labs" not in st.session_state:
    st.session_state.labs = labs
    st.session_state.stack = [[lab] for lab in labs]
    st.session_state.current_pair = None
    st.session_state.finished = False

def next_comparison():
    if len(st.session_state.stack) == 1:
        st.session_state.finished = True
        return
    new_stack = []
    for i in range(0, len(st.session_state.stack), 2):
        if i + 1 == len(st.session_state.stack):
            new_stack.append(st.session_state.stack[i])
        else:
            new_stack.append([st.session_state.stack[i], st.session_state.stack[i + 1]])
    st.session_state.stack = new_stack

def resolve_pair():
