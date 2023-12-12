import click
import pandas as pd
from Bio import SeqIO as IO
from counting import count_nucleotides


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
    if not (background_fasta.endswith('.fa') or motif_fasta.endswith('.fa')):
        raise ValueError('Not a valid format')
    background_seq = IO.to_dict(IO.parse(background_fasta, "fasta"))
    motif_seq = IO.to_dict(IO.parse(motif_fasta, "fasta"))
    background_counts = pd.DataFrame([count_nucleotides(value) for _, value in background_seq.items()])
    motif_counts = pd.DataFrame([count_nucleotides(value) for _, value in motif_seq.items()])


if __name__ == '__main__':
    main()
