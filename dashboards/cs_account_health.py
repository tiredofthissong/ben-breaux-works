import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/account_health.csv")
plt.figure(figsize=(9,5))
plt.bar(df["metric"], df["value"])
plt.title("Portfolio Health Snapshot")
plt.ylabel("Value")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("../screenshots/account_health_dashboard.png", dpi=200)
