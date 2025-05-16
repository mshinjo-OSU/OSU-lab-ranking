import streamlit as st
import random

# ===== 初期化関数 =====
def initialize_state():
    labs = [
        "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
        "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
        "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
        "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
        "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
    ]
    random.shuffle(labs)
    st.session_state.stack = [[lab] for lab in labs]
    st.session_state.finished = False
    st.session_state.result = None
    st.session_state.initialized = True

# ===== 初期化判定 =====
if "initialized" not in st.session_state:
    initialize_state()

# ===== マージ構造の比較探索 =====
def find_pair(node):
    if isinstance(node, list) and len(node) == 2:
        left, right = node
        if isinstance(left, list):
            pair = find_pair(left)
            if pair:
                return pair
        if isinstance(right, list):
            pair = find_pair(right)
            if pair:
                return pair
        if isinstance(left, str) and isinstance(right, str):
            return node
    return None

# ===== フラット化 =====
def flatten(node):
    if isinstance(node, str):
        return [node]
    elif isinstance(node, list):
        result = []
        for item in node:
            result.extend(flatten(item))
        return result
    return []

# ===== 表示開始 =====
st.title("研究室興味ランキング調査")

if not st.session_state.finished:
    pair = find_pair(st.session_state.stack)
    if pair:
        lab1, lab2 = pair
        st.write("どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {lab1}"):
                pair.clear()
                pair.append(lab1)
        with col2:
            if st.button(f"🅱 {lab2}"):
                pair.clear()
                pair.append(lab2)
    else:
        st.session_state.finished = True
        st.session_state.result = flatten(st.session_state.stack)

# ===== 結果表示 =====
if st.session_state.finished:
    st.success("あなたの興味順ランキングはこちら！")
    for i, lab in enumerate(st.session_state.result, 1):
        st.write(f"{i}位: {lab}")
    
    if st.button("やり直す"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
