"""Regressão linear: gasto mensal em função da renda mensal."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

from scipy import stats

df = pd.read_csv(BASE / "dados" / "dados_regressao.csv")

res = stats.linregress(df["renda_mensal"], df["gasto_mensal"])

fig, ax = plt.subplots(figsize=(10, 7))
sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", ci=95,
            scatter_kws={"alpha": 0.7, "s": 60}, line_kws={"color": "red"}, ax=ax)

texto = f"y = {res.slope:.3f}x + {res.intercept:.1f}\nR² = {res.rvalue ** 2:.3f}"
ax.text(0.05, 0.95, texto, transform=ax.transAxes, fontsize=14, va="top",
        bbox={"boxstyle": "round", "facecolor": "white", "edgecolor": "gray"})

ax.set_title("Regressão linear: renda x gasto mensal", fontweight="bold")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")

plt.tight_layout()
fig.savefig(BASE / "imagens" / "09_regressao.png", dpi=150)
plt.show()
