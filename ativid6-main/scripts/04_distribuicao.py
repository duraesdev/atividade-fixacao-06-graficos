"""Histograma com curva de densidade: distribuição de idade dos clientes."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(BASE / "dados" / "dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df["idade"], bins=15, kde=True, color="#2c7fb8", edgecolor="white", ax=ax)

media, mediana = df["idade"].mean(), df["idade"].median()
ax.axvline(media, color="red", linestyle="--", label=f"Média: {media:.1f}")
ax.axvline(mediana, color="green", linestyle="-.", label=f"Mediana: {mediana:.1f}")

ax.set_title("Distribuição de idade dos clientes", fontweight="bold")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend()

plt.tight_layout()
fig.savefig(BASE / "imagens" / "04_distribuicao.png", dpi=150)
plt.show()
