import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas.csv")

print("\n📊 Estadísticas:")
print("Total meses:", len(df))
print("Ventas totales:", df["ventas"].sum())
print("Promedio:", df["ventas"].mean())
print("Máximo:", df["ventas"].max())
print("Mínimo:", df["ventas"].min())

df.plot(x="mes", y="ventas", kind="bar", color="orange", title="Ventas mensuales", legend=False)
plt.ylabel("Ventas")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
