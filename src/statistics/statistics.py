import pandas as pd
import numpy as np
import scipy.stats as stats

def get_descriptives(background_counts, motif_counts):
    background = background_counts.describe()
    motif = motif_counts.describe()
    return background, motif

def get_comparatives(background_counts, motif_counts): # Wilcoxon Test
    for column in background_counts.columns:
        yield stats.ranksums(background_counts[column], motif_counts[column])

