import pandas as pd
import matplotlib.pyplot as plt

files = ["ENCFF540NGG.bed",  "ENCFF540NGG.hg19.bed", "ENCFF759NWD.bed",  "ENCFF759NWD.hg19.bed"]
for filename in files:
    df = pd.read_table(filename, names=["chrom", "start", "end", "name", "score", "a", "b", "c", "d", "e"])
    lens = df["end"] - df["start"]
    df_filtered = df[lens < 5000]
    plt.hist(lens[lens < 5000])
    plt.savefig(filename[:-3] + "hist.png")
    plt.close()
    df_filtered[["chrom", "start", "end", "name", "score"]].to_csv(filename[:-3] + "filtered.bed", sep="\t")

