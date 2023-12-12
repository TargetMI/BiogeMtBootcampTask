import click
from Bio import SeqIO as IO
from counting import count_seq


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
    background_counts = [count_seq(seq) for seq in background_seq]
    motif_counts = [count_seq(seq) for seq in motif_seq]


if __name__ == '__main__':
    main()
