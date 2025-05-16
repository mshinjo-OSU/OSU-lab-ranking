import streamlit as st
import random

# --- アプリ初期化関数 ---
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
    st.session_state.reset_requested = False
    st.session_state.initialized = True

# --- セッション初期化ロジック ---
if st.session_state.get("reset_requested", False):
    st.session_state.initialized = False
    st.session_state.reset_requested = False

if not st.session_state.get("initialized", False):
    initialize_state()

# --- 比較対象のペアを探す ---
def find_pair(node):
    if isinstance(node, list) and len(node) == 2:
        left, right = node
        if isinstance(left, list):
            result = find_pair(left)
            if result:
                return result
        if isinstance(right, list):
            result = find_pair(right)
            if result:
                return result
        if isinstance(left, str) and isinstance(right, str):
            return node
    return None

# --- 構造をフラット化 ---
def flatten(node):
    if isinstance(node, str):
        return [node]
    elif isinstance(node, list):
        result = []
        for item in node:
            result.extend(flatten(item))
        return result
    return []

# --- UI表示部 ---
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
        st.session_state.result = flatten(st.session_state.stack)
        st.session_state.finished = True

# --- 結果表示部 ---
if st.session_state.finished:
    st.success("あなたの興味順ランキングはこちら！")
    for i, lab in enumerate(st.session_state.result, 1):
        st.write(f"{i}位: {lab}")

    if st.button("やり直す"):
        st.session_state.reset_requested = True
