import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/gonggong xiangmu_chengguo.csv")
categories = df["xiangmu"].tolist()
before = df["gailiang qian"].tolist()
after = df["gailiang hou"].tolist()

x = np.arange(len(categories))
width = 0.35
plt.figure(figsize=(10,5))
plt.bar(x - width/2, before, width, label="gailiang qian")
plt.bar(x + width/2, after, width, label="gailiang hou")
plt.title("gonggong weisheng xiangmu chengguo (pinyin)")
plt.xticks(x, categories, rotation=20, ha="right")
plt.ylabel("zhi")
plt.legend()
plt.tight_layout()
plt.savefig("../screenshots/public_sector_dashboard.png", dpi=200)
