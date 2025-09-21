import pandas as pd
import matplotlib.pyplot as plt

def mostrar_tabela(resultados):
    if not resultados:
        print("⚠️ Nenhuma opção disponível dentro das restrições.\n")
        return None
    df = pd.DataFrame(resultados)
    print("\nEstamos enviando uma tabela para que você possa visualizar melhor:\n")
    print(df.to_string(index=False))
    return df

def gerar_grafico(df):
    try:
        df_plot = df[df["Prazo (meses)"] != ""]
        labels = [f"{r['Prazo (meses)']}m - {r['Banco'].split()[1]}" for _, r in df_plot.iterrows()]
        parcelas = df_plot["Parcela (R$)"].astype(float).tolist()
        juros = df_plot["Juros (R$)"].astype(float).tolist()
        x = range(len(labels))
        largura = 0.35

        fig, ax = plt.subplots(figsize=(12,6))
        bar1 = ax.bar([i - largura/2 for i in x], parcelas, width=largura, label='Parcela (R$)', color='#4C72B0')
        bar2 = ax.bar([i + largura/2 for i in x], juros, width=largura, label='Juros (R$)', color='#DD8452')

        # Valores em cima das barras
        for bars in [bar1, bar2]:
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'R$ {height:,.0f}', xy=(bar.get_x() + bar.get_width()/2, height),
                            xytext=(0,3), textcoords="offset points", ha='center', fontsize=9)

        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, rotation=45)
        ax.set_title("Comparativo de Parcelas e Juros por Instituição", fontsize=14)
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico: {e}")
