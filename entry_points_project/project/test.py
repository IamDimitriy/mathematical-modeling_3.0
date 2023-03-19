import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

data = [[18, 19], [15, 17], [16, 17], [18, 18], [21, 19], [23, 20], [23, 22], [24, 24], [25, 26], [27, 27], [28, 28], [29, 28],
        [30, 28], [31, 28], [31, 28], [31, 29], [31, 31], [31, 31], [31, 33], [31, 33], [31, 32], [30, 32], [30, 32], [29, 33], [29, 33], [28, 33], [27, 33], [27, 33], [27, 33], [27, 33], [27, 34], [27, 33], [26, 32], [25, 33], [25, 32], [24, 32], [24, 31], [24, 31]]


def build_a_graph(df):
    matplotlib.rcParams['font.size'] = 18
    sns.set(style="darkgrid")
    matplotlib.rcParams['figure.dpi'] = 200
    fig = sns.lineplot(x=df.index, y=df['with CRISPR/Cas'], color="r")
    fig = sns.lineplot(x=df.index, y=df['no CRISPR/Cas'], color="b")
    plt.title('График численности популяций настоящего моделирования')
    plt.xlabel('t, секунды')
    plt.ylabel('количество')
    plt.tight_layout()
    plt.show()


# передача данных для построения графика
df = pd.DataFrame(data, columns=["with CRISPR/Cas", "no CRISPR/Cas"])
build_a_graph(df)
