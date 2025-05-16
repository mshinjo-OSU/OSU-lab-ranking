import streamlit as st
import random

# 研究室のリスト（表示順をシャッフル）
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

# セッションステートの初期化
if "labs" not in st.session_state:
    st.session_state.labs = labs
    st.session_state.stack = [[lab] for lab in labs]
    st.session_state.current_pair = None
    st.session_state.finished = False

# 比較処理を進める
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

# 現在の比較ペアを設定
def resolve_pair():
    stack = st.session_state.stack
    for i in range(len(stack)):
        if isinstance(stack[i], list) and len(stack[i]) == 2:
            left = stack[i][0]
            right = stack[i][1]
            if isinstance(left, list):
                left = left[0]
            if isinstance(right, list):
                right = right[0]
            st.session_state.current_pair = (i, left, right)
            return
    st.session_state.current_pair = None

# 比較を進める or 結果を表示
if not st.session_state.finished:
    resolve_pair()
    if st.session_state.current_pair:
        idx, lab1, lab2 = st.session_state.current_pair
        st.write("次のうち、どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {lab1}"):
                st.session_state.stack[idx] = [lab1]
                next_comparison()
        with col2:
            if st.button(f"🅱 {lab2}"):
                st.session_state.stack[idx] = [lab2]
                next_comparison()
else:
    # 最終的なリストを平坦化して表示
    flat_list = []
    def flatten(stack):
        for item in stack:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_list.append(item)
    flatten(st.session_state.stack)

    st.success("あなたの興味順ランキングはこちら！")
    for i, lab in enumerate(flat_list, 1):
        st.write(f"{i}位: {lab}")
