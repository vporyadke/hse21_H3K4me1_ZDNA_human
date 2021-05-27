import pandas as pd
import matplotlib.pyplot as plt

files = ["H3K4me1_K562.merge.hg19.bed"]
for filename in files:
    df = pd.read_table("data/" + filename, names=["chrom", "start", "end", "name", "score", "a", "b", "c", "d", "e"])
    lens = df["end"] - df["start"]
    df_filtered = df[lens < 5000]
    plt.hist(lens[lens < 5000])
    plt.savefig("images/" + filename[:-3] + "hist.png")
    plt.close()
    df_filtered[["chrom", "start", "end", "name", "score"]].to_csv("data/" + filename[:-3] + "filtered.bed", sep="\t")

