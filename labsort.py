import streamlit as st
import random

# --- 初期化関数 ---
def initialize_state():
    labs = [
        "吉川研究室（データ価値創造基盤）", "小山田研究室（空気とAIの快適空間）", "原研究室（DSのビジネス応用）",
        "鎌原研究室（マルチメディア）", "笠原研究室（パターン認識-衛星・観光）", "杉山研究室（コンテンツ解析学）",
        "山西研究室（生体情報処理）", "劉研究室（計算工学）", "上岡研究室（情報数理科学）",
        "佐々木研究室（サイバーフィジカル）", "關戸研究室（計算・実験計画）","夏川研究室（時空間ビジュアル分析）",
        "山本研究室（メディカルデータ）", "上阪研究室（テキスト解析）", "新庄研究室（コンピュータ数理）"
    ]
    random.shuffle(labs)
    st.session_state.rounds = [[lab] for lab in labs]
    st.session_state.current_pairs = []
    st.session_state.current_index = 0
    st.session_state.next_round = []
    st.session_state.phase = "compare"

# --- 再帰的 flatten 関数（深さ無制限） ---
def flatten(node):
    if isinstance(node, str):
        return [node]
    elif isinstance(node, list):
        result = []
        for item in node:
            result.extend(flatten(item))
        return result
    else:
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
            st.session_state.current_pairs.append((st.session_state.rounds[i], st.session_state.rounds[i + 1]))
        else:
            st.session_state.next_round.append(st.session_state.rounds[i])
        i += 2
    st.session_state.current_index = 0

# --- 選択後の処理（勝敗順に保持） ---
def process_selection(winner, loser):
    st.session_state.next_round.append([winner, loser])  # 勝者が先
    st.session_state.current_index += 1

    if st.session_state.current_index >= len(st.session_state.current_pairs):
        st.session_state.rounds = st.session_state.next_round
        st.session_state.next_round = []
        if len(st.session_state.rounds) == 1:
            st.session_state.phase = "done"
        else:
            prepare_pairs()

# --- UI 描画 ---
st.title("研究室興味ランキング")

if st.session_state.phase == "compare":
    if not st.session_state.current_pairs:
        prepare_pairs()

    if st.session_state.current_index < len(st.session_state.current_pairs):
        a, b = st.session_state.current_pairs[st.session_state.current_index]
        lab1 = flatten(a)[0]
        lab2 = flatten(b)[0]

        st.write("どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {lab1}", key=f"btn1_{st.session_state.current_index}"):
                process_selection(a, b)
        with col2:
            if st.button(f"🅱 {lab2}", key=f"btn2_{st.session_state.current_index}"):
                process_selection(b, a)
        st.write("（ダブルクリックしてください。）")

elif st.session_state.phase == "done":
    st.success("あなたの興味ランキングはこちら！結果を参考にして、研究室配属希望調査にご回答ください")
    flat_result = flatten(st.session_state.rounds)
    for i, lab in enumerate(flat_result, 1):
        st.write(f"{i}位: {lab}")

    if st.button("やり直す"):
        st.session_state.phase = "reset"
    
    st.caption("このランキングは、1対1の比較を順に行う方式（トーナメント形式）で作成されています。すべての研究室を比較しているわけではないため、順位は参考程度とお考えください。")
