"""Gráfico de linhas: evolução diária das vendas (com média móvel de 7 dias)."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(BASE / "dados" / "dados_linhas.csv", parse_dates=["data"]).sort_values("data")
df["media_movel_7d"] = df["vendas"].rolling(7, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["data"], df["vendas"], color="lightgray", linewidth=1.5, zorder=1)
sns.scatterplot(data=df, x="data", y="vendas", hue="loja", palette="Set1", s=50, ax=ax, zorder=2)
ax.plot(df["data"], df["media_movel_7d"], color="black", linewidth=2.5, label="Média móvel (7 dias)", zorder=3)

ax.set_title("Evolução diária das vendas", fontweight="bold")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend(title="Legenda", fontsize=11)
fig.autofmt_xdate()

plt.tight_layout()
fig.savefig(BASE / "imagens" / "07_linhas.png", dpi=150)
plt.show()
