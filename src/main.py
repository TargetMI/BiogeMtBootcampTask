import click
from Bio import SeqIO as IO
from counting import count_seq


@click.command()
@click.option('--background_fasta', help='The fasta file containing the background sequences to be parsed and included')
@click.option('--motif_fasta', help='The fasta file containing the motifs to be parsed and included')
def main(background_fasta, motif_fasta):
    background_seq = IO.to_dict(IO.parse(background_fasta, "fasta"))
    motif_seq = IO.to_dict(IO.parse(motif_fasta, "fasta"))
    background_counts = [count_seq(seq) for seq in background_seq]
    motif_counts = [count_seq(seq) for seq in motif_seq]
    pass


if __name__ == '__main__':
    main()
