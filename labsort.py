def compare_labs(lab1, lab2):
    """ユーザーに2つの研究室を比較させて、どちらが上かを返す。"""
    while True:
        print(f"\nどちらの研究室により興味がありますか？")
        print(f"1: {lab1}")
        print(f"2: {lab2}")
        choice = input("選択肢（1 or 2）: ")
        if choice == "1":
            return lab1
        elif choice == "2":
            return lab2
        else:
            print("無効な入力です。1 か 2 を入力してください。")

def merge_sort_with_user(labs):
    """ユーザーの比較に基づいて研究室をソートする。"""
    if len(labs) <= 1:
        return labs

    mid = len(labs) // 2
    left = merge_sort_with_user(labs[:mid])
    right = merge_sort_with_user(labs[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        winner = compare_labs(left[i], right[j])
        if winner == left[i]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 研究室のリスト（シャッフルしておくと偏りが減る？）
import random
labs = [
    "吉川研究室（プライバシー保護技術）",
    "小山田研究室（可視化情報学）", 
    "原研究室（イノベーション・マネジメント）", 
    "鎌原研究室（インターネットアプリケーション）",
    "笠原研究室（観光情報学）",
    "杉山研究室（情報検索・自然言語処理）",
    "山西研究室（生体情報学）",
    "劉研究室（CAE：計算機援用工学）", 
    "上岡研究室（数え上げ組合せ論）", 
    "佐々木研究室（ヒューマンコンピュータインタラクション）", 
    "關戸研究室（実験計画法）", 
    "夏川研究室（情報可視化・スポーツデータ科学）", 
    "上阪研究室（計量文献学）", 
    "新庄研究室（コンピュータ数学）"
]
random.shuffle(labs)

# ソート開始
print("=== 研究室興味度ランキング調査 ===")
sorted_labs = merge_sort_with_user(labs)

# 結果表示
print("\n=== あなたの興味順ランキング ===")
for i, lab in enumerate(sorted_labs, 1):
    print(f"{i}位: {lab}")
