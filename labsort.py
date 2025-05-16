import streamlit as st
import random

# --- 初期化 ---
def initialize():
    labs = [
        "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
        "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
        "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
        "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
        "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
    ]
    random.shuffle(labs)
    st.session_state.rounds = [[lab] for lab in labs]
    st.session_state.current_pairs = []
    st.session_state.current_index = 0
    st.session_state.next_round = []
    st.session_state.done = False
    st.session_state.phase = "compare"

# --- 初回起動 or リセット時 ---
if "phase" not in st.session_state or st.session_state.get("phase") == "reset":
    initialize()

# --- ペアを準備する ---
def prepare_pairs():
    pairs = []
    i = 0
    while i < len(st.session_state.rounds):
        if i + 1 < len(st.session_state.rounds):
            pairs.append((st.session_state.rounds[i], st.session_state.rounds[i+1]))
            i += 2
        else:
            st.session_state.next_round.append(st.session_state.rounds[i])
            i += 1
    st.session_state.current_pairs = pairs
    st.session_state.current_index = 0

# --- 比較ロジック ---
def compare_ui():
    pairs = st.session_state.current_pairs
    idx = st.session_state.current_index

    if idx < len(pairs):
        a = pairs[idx][0]
        b = pairs[idx][1]

        lab1 = a[0] if isinstance(a, list) else a
        lab2 = b[0] if isinstance(b, list) else b

        st.write("どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {lab1}"):
                st.session_state.next_round.append(a)
                st.session_state.current_index += 1
        with col2:
            if st.button(f"🅱 {lab2}"):
                st.session_state.next_round.append(b)
                st.session_state.current_index += 1
    else:
        # ラウンド終了
        st.session_state.rounds = st.session_state.next_round
        st.session_state.next_round = []
        if len(st.session_state.rounds) == 1:
            st.session_state.done = True
            st.session_state.phase = "done"
        else:
            prepare_pairs()

# --- 表示フェーズ ---
st.title("研究室興味ランキング調査")

if st.session_state.phase == "compare":
    if st.session_state.current_index == 0 and not st.session_state.current_pairs:
        prepare_pairs()
    compare_ui()

elif st.session_state.phase == "done":
    st.success("あなたの興味順ランキングはこちら！")
    final = st.session_state.rounds[0]
    for i, lab in enumerate(final, 1):
        st.write(f"{i}位: {lab}")

    if st.button("やり直す"):
        st.session_state.phase = "reset"
