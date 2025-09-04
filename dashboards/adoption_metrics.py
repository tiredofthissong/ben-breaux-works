import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/adoption_metrics.csv")
plt.figure(figsize=(9,5))
plt.plot(df["month"], df["adoption_percent"], marker="o")
plt.title("Adoption Over Time")
plt.xlabel("Month")
plt.ylabel("Active Users (% of licenses)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../screenshots/adoption_dashboard.png", dpi=200)
