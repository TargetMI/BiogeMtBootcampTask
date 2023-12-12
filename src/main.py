from os import path

import click
import pandas as pd
from Bio import SeqIO as IO

from counting import count_nucleotides

from statistics.statistics import get_descriptives, get_comparatives


@click.command()
@click.option('--background_fasta', help='The fasta file containing the background sequences to be parsed and included')
@click.option('--motif_fasta', help='The fasta file containing the motifs to be parsed and included')
@click.option('--output_directory', help='The output directory holding the result')
def main(background_fasta, motif_fasta, output_directory) -> None:
    """
    The main function which will action the pipeline
    :param background_fasta: the background fasta file
    :param motif_fasta: the motifs fasta file
    :param output_directory: the output directory holding the results
    :return: None
    """
    # add a check that the args are fasta
    if ((background_fasta is None or motif_fasta is None or output_directory is None)
            or not (background_fasta.endswith('.fa') or motif_fasta.endswith('.fa'))):
        raise ValueError('Not a valid format')
    background_seq = IO.to_dict(IO.parse(background_fasta, "fasta"))
    motif_seq = IO.to_dict(IO.parse(motif_fasta, "fasta"))
    background_counts = pd.DataFrame([count_nucleotides(value) for _, value in background_seq.items()])
    background_counts.to_csv(path.join(output_directory, 'background_counts.csv'), header=True)
    motif_counts = pd.DataFrame([count_nucleotides(value) for _, value in motif_seq.items()])
    motif_counts.to_csv(path.join(output_directory, 'motif_counts.csv'), header=True)

    wilcoxon_test = list(get_comparatives(background_counts, motif_counts))
    print(wilcoxon_test)

if __name__ == '__main__':
    main()
