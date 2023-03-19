import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


def build_a_graph(df):
    matplotlib.rcParams['font.size'] = 18
    sns.set(style="darkgrid")
    matplotlib.rcParams['figure.dpi'] = 200
    fig = sns.lineplot(x=df.index, y=df['no CRISPR/Cas'], color="r")
    fig = sns.lineplot(x=df.index,  y=df['with CRISPR/Cas'], color="b")
    plt.title('График численности популяций настоящего моделирования')
    plt.xlabel('t, секунды')
    plt.ylabel('Количество')
    plt.tight_layout()
    plt.show()
