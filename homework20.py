import matplotlib as plt
import pandas as pd

df = pd.read_csv("sales.csv")

by_seller = df.groupby("seller")["total"].sum().sort_values(ascending=False)

by_seller.to_csv("sellers.csv")

by_seller.plot(
    kind="bar",
    title= "Income",
    rot=0
)

plt.ylabel("uah")
plt.tight_layout()

# 5. Зберігаємо графік у sellers.png
plt.savefig("sellers.png")
plt.show()