# read files
from biopython import SeqIO
records = SeqIO.parse("data/reads_bkg.fa", "fasta")
for i, seq_record in enumerate(records):
    print("Sequence %d:" % i)
    print("Number of A's: %d" % seq_record.seq.count("A"))
    print("Number of C's: %d" % seq_record.seq.count("C"))
    print("Number of G's: %d" % seq_record.seq.count("G"))
    print("Number of T's: %d" % seq_record.seq.count("T"))
    print()