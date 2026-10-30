"""Gráfico de barras agrupadas: vendas médias por categoria e região."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(BASE / "dados" / "dados_barras.csv")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao", palette="viridis", ax=ax)

ax.set_title("Vendas médias por categoria e região", fontweight="bold")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.legend(title="Região", loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=11, title_fontsize=12)
for c in ax.containers:
    ax.bar_label(c, fmt="%.0f", fontsize=9, padding=2)

plt.tight_layout()
fig.savefig(BASE / "imagens" / "01_barras.png", dpi=150)
plt.show()
