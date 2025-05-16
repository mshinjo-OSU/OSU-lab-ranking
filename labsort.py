import streamlit as st
import random

# ラボリスト
labs = [
    "吉川研究室（プライバシー保護技術）", "小山田研究室（可視化情報学）", "原研究室（イノベーション・マネジメント）",
    "鎌原研究室（インターネットアプリケーション）", "笠原研究室（観光情報学）", "杉山研究室（情報検索・自然言語処理）",
    "山西研究室（生体情報学）", "劉研究室（CAE：計算機援用工学）", "上岡研究室（数え上げ組合せ論）",
    "佐々木研究室（ヒューマンコンピュータインタラクション）", "關戸研究室（実験計画法）",
    "夏川研究室（情報可視化・スポーツデータ科学）", "上阪研究室（計量文献学）", "新庄研究室（コンピュータ数学）"
]
random.seed(42)
random.shuffle(labs)

# 初期化
if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.sorted_labs = None
    st.session_state.merged = None
    st.session_state.phase = "sorting"

# マージソート + 比較UI構築
def merge_sort_with_state(data):
    # 長さ1ならそのまま返す
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort_with_state(data[:mid])
    right = merge_sort_with_state(data[mid:])
    return [left, right]

def get_next_comparison(structure):
    # 再帰的に構造の中の比較対象を探す
    if isinstance(structure, list) and len(structure) == 2:
        a, b = structure
        if isinstance(a, list):
            a_result = get_next_comparison(a)
            if a_result:
                return a_result
        if isinstance(b, list):
            b_result = get_next_comparison(b)
            if b_result:
                return b_result
        if isinstance(a, str) and isinstance(b, str):
            return (structure, a, b)
    return None

def apply_choice(structure, chosen):
    # ユーザー選択に応じて構造を更新
    if isinstance(structure, list) and len(structure) == 2:
        a, b = structure
        if isinstance(a, list):
            apply_choice(a, chosen)
        elif isinstance(b, list):
            apply_choice(b, chosen)
        elif isinstance(a, str) and isinstance(b, str):
            if chosen == a:
                structure.clear()
                structure.append(a)
                return True
            elif chosen == b:
                structure.clear()
                structure.append(b)
                return True
    return False

# フェーズ管理
if st.session_state.phase == "sorting":
    if st.session_state.merged is None:
        st.session_state.merged = merge_sort_with_state(labs)

    result = get_next_comparison(st.session_state.merged)
    if result:
        struct, lab1, lab2 = result
        st.write("次のうち、どちらの研究室により興味がありますか？")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🅰 {lab1}"):
                apply_choice(struct, lab1)
        with col2:
            if st.button(f"🅱 {lab2}"):
                apply_choice(struct, lab2)
    else:
        # 完了時に構造を平坦化して表示
        flat_list = []
        def flatten(x):
            if isinstance(x, str):
                flat_list.append(x)
            elif isinstance(x, list):
                for item in x:
                    flatten(item)
        flatten(st.session_state.merged)
        st.session_state.sorted_labs = flat_list
        st.session_state.phase = "done"

# 完了時表示
if st.session_state.phase == "done":
    st.success("あなたの興味順ランキングはこちら！")
    for i, lab in enumerate(st.session_state.sorted_labs, 1):
        st.write(f"{i}位: {lab}")
    if st.button("やり直す"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
