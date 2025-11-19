import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

#tagit kod från lektionen om konfidensintervall
def ci_plot(ax, lo, hi, mean, title, xlabel):
    ax.hlines(y=0, xmin=lo, xmax=hi, color="black")
    ax.plot(mean, 0, "o", color="red")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_yticks([])
    ax.grid(False)
    return ax

#tagit kod från lektionen om konfidensintervall
def bootstrap_hist(ax, boot_means, mean_x, lo, hi, title="Bootsrapfördelning av medel", bins=30):
    boot_means = _num_for_plot(boot_means)
    ax.hist(boot_means, bins=bins, edgecolor="black", alpha=0.7)
    ax.axvline(mean_x, color="green", linestyle="--", label="Stickprovsmedelvärde")
    ax.axvline(lo, color="red", linestyle="--", label="Nedre 95% gräns")
    ax.axvline(hi, color="red", linestyle="--", label="Övre 95% gräns")
    ax.set_title(title)
    ax.set_xlabel("Resamplade medelvärden")
    ax.set_ylabel("Frekvens")
    ax.grid(True, axis="y")
    ax.legend()
    return ax

def mean_compare(ax, smokers, non_smokers, title="Jämförelse av medelvärde: Rökare vs Icke-rökare", ylabel="Systolic BP"):
    smokers = _num_for_plot(smokers)
    non_smokers = _num_for_plot(non_smokers)
    data = [smokers, non_smokers]
    labels = ["Rökare", "Icke-rökare"]
    ax.boxplot(data, labels=labels)
    mean_s = np.mean(smokers)
    mean_n = np.mean(non_smokers)
    ax.plot(1, mean_s, "o", color="red", label=f"Medel rökare ({mean_s:.2f})")
    ax.plot(2, mean_n, "o", color="blue", label=f"Medel icke-rökare ({mean_n:.2f})")
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y")
    ax.legend()
    return ax
