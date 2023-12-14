from os import path

import click
import pandas as pd
from Bio import SeqIO as IO
from counting import count_nucleotides
from plotting import plot_functions

FASTA_FORMATS = ['.fasta', '.fas', '.fa', '.fna', '.ffn', '.faa', '.mpfa', '.frn']


def check_fasta(fasta_file):
    if not path.isfile(fasta_file) and path.splitext(fasta_file) not in FASTA_FORMATS:
        raise ValueError(f'Not a valid fasta format. Accepted: {",".join(FASTA_FORMATS)}')
    return True

from statistics.statistics import output_statistics


@click.command()
@click.option('-b', '--background_fasta', type=str, help='The fasta file containing the background'
                                                         ' sequences to be parsed and included', prompt=True)
@click.option('-m', '--motif_fasta', type=str, help='The fasta file containing the'
                                                    ' motifs to be parsed and included', prompt=True)
@click.option('-o', '--output_directory', help='The output directory for the results', prompt=True)
def main(background_fasta, motif_fasta, output_directory) -> None:
    """
    The main function which will action the pipeline
    :param background_fasta: the background fasta file
    :param motif_fasta: the motifs fasta file
    :param output_directory: the output directory holding the results
    :return: None
    """
    # add a check that the args are fasta
    if not (check_fasta(motif_fasta) and check_fasta(background_fasta)):
        raise ValueError('Not a valid format')
    background_seq = IO.to_dict(IO.parse(background_fasta, "fasta"))
    motif_seq = IO.to_dict(IO.parse(motif_fasta, "fasta"))
    click.echo('Parsed background and motif files')
    background_counts = pd.DataFrame([count_nucleotides(value) for _, value in background_seq.items()])
    motif_counts = pd.DataFrame([count_nucleotides(value) for _, value in motif_seq.items()])
    click.echo(f'Generated Counts. logging counts in {output_directory}')
    motif_counts.to_csv(path.join(output_directory, 'motif_counts.csv'), header=True)
    background_counts.to_csv(path.join(output_directory, 'background_counts.csv'), header=True)

    plot_functions(background_counts, motif_counts, output_directory)

    output_statistics(background_counts, motif_counts)


if __name__ == '__main__':
    main()
