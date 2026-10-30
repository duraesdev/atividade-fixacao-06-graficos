"""Gráfico de frequência: quantidade de chamados por tipo de atendimento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(BASE / "dados" / "dados_frequencia.csv")

ordem = df["tipo_atendimento"].value_counts().index  # do mais ao menos frequente

fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x="tipo_atendimento", order=ordem, hue="tipo_atendimento",
              palette="mako", legend=False, ax=ax)

total = len(df)
for c in ax.containers:
    ax.bar_label(c, labels=[f"{int(v.get_height())} ({v.get_height() / total:.0%})" for v in c],
                 padding=3, fontsize=11)

ax.set_title("Frequência de chamados por tipo de atendimento", fontweight="bold")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Quantidade de chamados")
ax.set_ylim(0, ax.get_ylim()[1] * 1.1)

plt.tight_layout()
fig.savefig(BASE / "imagens" / "05_frequencia.png", dpi=150)
plt.show()
