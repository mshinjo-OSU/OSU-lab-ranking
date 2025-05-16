import streamlit as st
import random

# --- 初期化関数 ---
def initialize():
    labs = [
        "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
        "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
        "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
        "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
        "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
    ]
    random.shuffle(labs)
    st.session_state.items = [[lab] for lab in labs]
    st.session_state.stack = [(0, len(st.session_state.items))]
    st.session_state.merges = []
    st.session_state.left = []
    st.session_state.right = []
    st.session_state.result = []
    st.session_state.i = 0
    st.session_state.j = 0
    st.session_state.k = 0
    st.session_state.phase = "sorting"

# --- 初回のみ初期化 ---
if "phase" not in st.session_state or st.session_state.phase == "reset":
    initialize()

# --- UIタイトル ---
st.title("研究室興味ランキング調査")

# --- 比較フェーズ ---
if st.session_state.phase == "sorting":
    # 比較中
    if st.session_state.left and st.session_state.i < len(st.session_state.left) and st.session_state.j < len(st.session_state.right):
        a = st.session_state.left[st.session_state.i][0]
        b = st.session_state.right[st.session_state.j][0]
        st.write("どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {a}"):
                st.session_state.result.append(st.session_state.left[st.session_state.i])
                st.session_state.i += 1
        with col2:
            if st.button(f"🅱 {b}"):
                st.session_state.result.append(st.session_state.right[st.session_state.j])
                st.session_state.j += 1

    # 比較終了 → 残りを追加
    elif st.session_state.left:
        st.session_state.result.extend(st.session_state.left[st.session_state.i:])
        st.session_state.result.extend(st.session_state.right[st.session_state.j:])
        st.session_state.items[st.session_state.k[0]:st.session_state.k[2]] = st.session_state.result
        st.session_state.left = []
        st.session_state.right = []
        st.session_state.result = []
        st.session_state.i = 0
        st.session_state.j = 0

    # 次のマージを準備
    elif st.session_state.merges:
        start, mid, end = st.session_state.merges.pop()
        st.session_state.left = st.session_state.items[start:mid]
        st.session_state.right = st.session_state.items[mid:end]
        st.session_state.k = (start, mid, end)

    # スタックから分割・マージ指示を作成
    elif st.session_state.stack:
        start, end = st.session_state.stack.pop()
        if end - start <= 1:
            pass  # 要素1つはソート済み
        else:
            mid = (start + end) // 2
            st.session_state.stack.append((start, mid))
            st.session_state.stack.append((mid, end))
            st.session_state.merges.append((start, mid, end))

    # 完了
    else:
        st.session_state.phase = "done"

# --- ランキング表示 ---
elif st.session_state.phase == "done":
    st.success("あなたの興味順ランキングはこちら！")
    for i, lab in enumerate([x[0] for x in st.session_state.items], 1):
        st.write(f"{i}位: {lab}")
    if st.button("やり直す"):
        st.session_state.phase = "reset"
