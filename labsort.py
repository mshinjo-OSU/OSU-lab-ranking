import streamlit as st
import random

# --- 初期化関数 ---
def initialize_state():
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

def flatten(node):
    if isinstance(node, str):
        return [node]
    elif isinstance(node, list):
        result = []
        for item in node:
            result.extend(flatten(item))
        return result
    return []

# --- 再起動 or 初回 ---
if "phase" not in st.session_state or st.session_state.get("phase") == "reset":
    initialize_state()

# --- ペア準備 ---
def prepare_pairs():
    st.session_state.current_pairs = []
    i = 0
    while i < len(st.session_state.rounds):
        if i + 1 < len(st.session_state.rounds):
            st.session_state.current_pairs.append((st.session_state.rounds[i], st.session_state.rounds[i+1]))
        else:
            st.session_state.next_round.append(st.session_state.rounds[i])
        i += 2
    st.session_state.current_index = 0

# --- 選択の後処理 ---
def process_selection(winner):
    st.session_state.next_round.append(winner)
    st.session_state.current_index += 1

    if st.session_state.current_index >= len(st.session_state.current_pairs):
        # ラウンド終了
        st.session_state.rounds = st.session_state.next_round
        st.session_state.next_round = []
        if len(st.session_state.rounds) == 1:
            st.session_state.phase = "done"
        else:
            prepare_pairs()

# --- UI 描画 ---
st.title("研究室興味ランキング調査")

if st.session_state.phase == "compare":
    if not st.session_state.current_pairs:
        prepare_pairs()

    if st.session_state.current_index < len(st.session_state.current_pairs):
        a, b = st.session_state.current_pairs[st.session_state.current_index]
        lab1 = a[0] if isinstance(a, list) else a
        lab2 = b[0] if isinstance(b, list) else b

        st.write("どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {lab1}", key=f"btn1_{st.session_state.current_index}"):
                process_selection(a)
        with col2:
            if st.button(f"🅱 {lab2}", key=f"btn2_{st.session_state.current_index}"):
                process_selection(b)

elif st.session_state.phase == "done":
    st.success("あなたの興味順ランキングはこちら！")
    final = flatten(st.session_state.rounds)
    for i, lab in enumerate(final, 1):
        st.write(f"{i}位: {lab}")

    if st.button("やり直す"):
        st.session_state.phase = "reset"
