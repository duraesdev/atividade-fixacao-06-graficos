"""Boxplot: distribuição salarial por departamento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(BASE / "dados" / "dados_boxplot.csv")

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="departamento", y="salario", hue="departamento",
            palette="Set2", legend=False, ax=ax)

ax.set_title("Distribuição de salários por departamento", fontweight="bold")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", ".")))

plt.tight_layout()
fig.savefig(BASE / "imagens" / "02_boxplot.png", dpi=150)
plt.show()
