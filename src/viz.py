import matplotlib.pyplot as plt
import pandas as pd

#Tog denna kod från EDA projektet. Den fyller eventuella tomma "celler" med 0.
def _num_for_plot(s):
    try:
        return pd.to_numeric(s, errors="coerce").fillna(0)
    except Exception:
        return s


def histogram(ax, values, title, xlabel, ylabel="Antal", bins=30, grid=True):
    values = _num_for_plot(values)
    ax.hist(values, bins=bins, edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax

def box_h(ax, values, title, xlabel, grid: bool = True):
    values = _num_for_plot(values)
    ax.boxplot(values, vert=False)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(grid, axis="x")
    return ax

def bar_chart(ax, values, title, xlabel, ylabel="Andel (%)", grid: bool = True):
    values = _num_for_plot(values)
    ax.bar(values.index, values.values, edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax


def ci_plot(ax, lo, hi, mean, title, xlabel):
    ax.hlines(y=0, xmin=lo, xmax=hi, color="black")
    ax.plot(mean, 0, "o", color="red")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_yticks([])
    ax.grid(False)
    return ax