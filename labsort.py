import streamlit as st
import random

# 研究室リスト（シャッフル）
labs = [
    "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
    "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
    "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
    "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
    "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
]
random.seed(42)
random.shuffle(labs)

# タイトル
st.title("研究室興味ランキング調査")

# セッション初期化
if "comparisons" not in st.session_state:
    st.session_state.comparisons = []
    st.session_state.index = 0
    st.session_state.scores = {lab: 0 for lab in labs}
    st.session_state.pairs = [
        (a, b) for i, a in enumerate(labs) for b in labs[i+1:]
    ]
    random.shuffle(st.session_state.pairs)
    st.session_state.finished = False

# メインロジック
if not st.session_state.finished and st.session_state.index < len(st.session_state.pairs):
    lab1, lab2 = st.session_state.pairs[st.session_state.index]
    st.write("次のうち、どちらの研究室により興味がありますか？")

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"🅰 {lab1}", key=f"btn1_{st.session_state.index}"):
            st.session_state.scores[lab1] += 1
            st.session_state.index += 1
    with col2:
        if st.button(f"🅱 {lab2}", key=f"btn2_{st.session_state.index}"):
            st.session_state.scores[lab2] += 1
            st.session_state.index += 1
else:
    if not st.session_state.finished:
        st.session_state.finished = True
        # スコア順に並び替え
        st.session_state.ranked_labs = sorted(
            st.session_state.scores.items(), key=lambda x: x[1], reverse=True
        )

    st.success("あなたの興味順ランキングはこちら！")
    for i, (lab, score) in enumerate(st.session_state.ranked_labs, 1):
        st.write(f"{i}位: {lab}（スコア: {score}）")

    if st.button("やり直す"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
