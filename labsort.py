import streamlit as st
import random

# --- 初期化 ---
def initialize_state():
    labs = [
        "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
        "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
        "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
        "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
        "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
    ]
    random.shuffle(labs)
    st.session_state.labs = [[lab] for lab in labs]
    st.session_state.phase = "compare"
    st.session_state.merged = []
    st.session_state.index = 0

# 初回起動またはリセット
if "phase" not in st.session_state or st.session_state.phase == "reset":
    initialize_state()

# マージ1ステップを生成する
def prepare_next_round():
    labs = st.session_state.labs
    merged = []
    i = 0
    while i < len(labs):
        if i + 1 < len(labs):
            merged.append([labs[i], labs[i + 1]])  # 比較対象ペア
        else:
            merged.append(labs[i])  # 端数をそのまま残す
        i += 2
    st.session_state.labs = merged
    st.session_state.index = 0
    st.session_state.merged = []

# 比較対象を探して flatten する
def flatten(lab):
    if isinstance(lab, str):
        return [lab]
    elif isinstance(lab, list):
        result = []
        for item in lab:
            result.extend(flatten(item))
        return result
    return []

# --- UI 表示 ---
st.title("研究室興味ランキング調査")

if st.session_state.phase == "compare":
    if isinstance(st.session_state.labs[0], str):
        st.session_state.phase = "done"

    elif st.session_state.index < len(st.session_state.labs):
        pair = st.session_state.labs[st.session_state.index]
        if isinstance(pair, list) and len(pair) == 2:
            left = flatten(pair[0])[0]
            right = flatten(pair[1])[0]

            st.write("どちらの研究室により興味がありますか？")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🅰 {left}", key=f"left_{st.session_state.index}"):
                    st.session_state.merged.append(pair)
                    st.session_state.index += 1
            with col2:
                if st.button(f"🅱 {right}", key=f"right_{st.session_state.index}"):
                    st.session_state.merged.append([pair[1], pair[0]])  # 順序を逆転して保存
                    st.session_state.index += 1
        else:
            st.session_state.merged.append(pair)
            st.session_state.index += 1
    else:
        st.session_state.labs = st.session_state.merged
        st.session_state.index = 0
        st.session_state.merged = []

# 結果表示
if st.session_state.phase == "done":
    st.success("あなたの興味順ランキングはこちら！")
    final = flatten(st.session_state.labs)
    for i, lab in enumerate(final, 1):
        st.write(f"{i}位: {lab}")

    if st.button("やり直す"):
        st.session_state.phase = "reset"
