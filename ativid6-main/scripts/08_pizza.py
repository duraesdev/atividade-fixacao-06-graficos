"""Gráfico de pizza: participação de cada canal no faturamento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(BASE / "dados" / "dados_pizza.csv").sort_values("faturamento", ascending=False)

fig, ax = plt.subplots(figsize=(9, 9))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%", startangle=90,
       counterclock=False, colors=sns.color_palette("pastel"),
       wedgeprops={"edgecolor": "white", "linewidth": 2}, textprops={"fontsize": 14})

ax.set_title("Participação dos canais de venda no faturamento", fontweight="bold")

plt.tight_layout()
fig.savefig(BASE / "imagens" / "08_pizza.png", dpi=150)
plt.show()
