import pandas as pd
import numpy as np
import scipy.stats as stats

background_counts = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns = ["a", "t", "c", "g", "sum"])
motif_counts = pd.DataFrame(np.array([[10,11,12], [13,14,15], [16,17,18]]), columns = ["a", "t", "c", "g", "sum"])

def descriptives(background_counts, motif_counts):
    background = background_counts.describe()
    motif = motif_counts.describe()
    print(background)
    print(motif)

descriptives(background_counts, motif_counts)

def comparatives(background_counts, motif_counts): # Wilcoxon Test
    wilcoxon_a = stats.ranksums(background_counts["a"], motif_counts["a"])
    wilcoxon_t = stats.ranksums(background_counts["t"], motif_counts["t"])
    wilcoxon_c = stats.ranksums(background_counts["c"], motif_counts["c"])
    wilcoxon_g = stats.ranksums(background_counts["g"], motif_counts["g"])
    wilcoxon_sum = stats.ranksums(background_counts["sum"], motif_counts["sum"])
    print(wilcoxon_a)
    print(wilcoxon_t)
    print(wilcoxon_c)

comparatives(background_counts, motif_counts)