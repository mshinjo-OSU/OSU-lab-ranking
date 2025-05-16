import streamlit as st
import random

# ---------------- 初期化 ----------------

def init_app():
    labs = [
        "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
        "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
        "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
        "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
        "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
    ]
    random.seed(42)
    random.shuffle(labs)
    st.session_state.stack = [[lab] for lab in labs]
    st.session_state.finished = False
    st.session_state.ranked = []
    st.session_state.reset_requested = False

if "stack" not in st.session_state or st.session_state.reset_requested:
    init_app()
    st.session_state.reset_requested = False

# ---------------- 比較処理 ----------------

def merge_pairs(pairs):
    new_stack = []
    i = 0
    while i < len(pairs):
        if i + 1 == len(pairs):
            new_stack.append(pairs[i])
            break
        new_stack.append([pairs[i], pairs[i + 1]])
        i += 2
    return new_stack

def flatten(structure):
    if isinstance(structure, str):
        return [structure]
    elif isinstance(structure, list):
        result = []
        for item in structure:
            result.extend(flatten(item))
        return result
    return []

# ---------------- UI ----------------

st.title("研究室興味ランキング調査")

if not st.session_state.finished:
    # 深さ優先で次の比較対象を探索
    def find_next_comparison(node):
        if isinstance(node, list) and len(node) == 2:
            left, right = node
            if isinstance(left, list):
                result = find_next_comparison(left)
                if result:
                    return result
            if isinstance(right, list):
                result = find_next_comparison(right)
                if result:
                    return result
            if isinstance(left, str) and isinstance(right, str):
                return node
        return None

    pair = find_next_comparison(st.session_state.stack)

    if pair:
        lab1, lab2 = pair
        st.write("次のうち、どちらの研究室により興味がありますか？")
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
        # 比較終了 → flattenして表示
        st.session_state.finished = True
        st.session_state.ranked = flatten(st.session_state.stack)

# ---------------- 結果表示 ----------------

if st.session_state.finished:
    st.success("あなたの興味順ランキングはこちら！")
    for i, lab in enumerate(st.session_state.ranked, 1):
        st.write(f"{i}位: {lab}")

    if st.button("やり直す"):
        st.session_state.reset_requested = True
