import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 図全体の設定
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
plt.title("かぎ針編み サニタリーポーチ 修正版 編み図", fontsize=20, pad=20)

# 吹き出し風ボックスを描画する関数
def draw_box(ax, center_x, center_y, width, height, text, facecolor):
    box = patches.FancyBboxPatch(
        (center_x - width/2, center_y - height/2),
        width,
        height,
        boxstyle="round,pad=0.5",
        fc=facecolor,
        ec="black",
        lw=2
    )
    ax.add_patch(box)
    ax.text(center_x, center_y, text, ha="center", va="center", fontsize=12, wrap=True)

# 各パートのテキストと配置（上から下へ）
steps = [
    ("材料・ゲージ\n・コットン糸\n・4.0mmかぎ針\n・留め具", 0.88, "#FFEBEE"),
    ("パート1：\n【円形底部】\n魔法輪から\n6sc → 12sc → 18sc → 24sc", 0.72, "#E1F5FE"),
    ("パート2：\n【側面】\n底部からscを\n1ラウンドずつ編む\n(約10cm)", 0.56, "#FFF3E0"),
    ("パート3：\n【蓋（オプション）】\n方法A：別パート編み\nまたは\n方法B：内側折返し", 0.40, "#E8F5E9"),
    ("パート4：\n【仕上げ】\n糸端処理・ブロッキング\n・留め具調整", 0.24, "#F3E5F5")
]

box_width = 0.8
box_height = 0.12
for text, y, color in steps:
    draw_box(ax, 0.5, y, box_width, box_height, text, color)

# 各ボックス間を矢印で接続
arrow_positions = [
    ((0.5, 0.83), (0.5, 0.76)),
    ((0.5, 0.67), (0.5, 0.60)),
    ((0.5, 0.51), (0.5, 0.44)),
    ((0.5, 0.35), (0.5, 0.28))
]
for start, end in arrow_positions:
    arr = patches.FancyArrowPatch(
        start, end,
        arrowstyle='->,head_length=10,head_width=5',
        mutation_scale=20, color='black', lw=2)
    ax.add_patch(arr)

# タイトルをハートで装飾
ax.text(0.5, 0.96, "♡ かわいいサニタリーポーチ ♡", ha="center", va="center", fontsize=16, color="#FF4081", fontweight="bold")

plt.tight_layout()
plt.show()
