import Bio.SeqIO as IO
import pandas as pd
import argparse

def get_fasta_lengths(fasta_file,output_file):

    record_dict = IO.to_dict(IO.parse(fasta_file, "fasta"))

    # create dict to collect lengths 

    fasta_len_dict = {}

    for key in record_dict.items():

        fasta_len_dict[key[0]] = [key[1].seq, len(key[1].seq)]


    len_counts_df =  pd.DataFrame.from_dict(fasta_len_dict,orient='index')

    len_counts_df = len_counts_df.reset_index()

    len_counts_df.columns = ["Name","Sequence","Length"]

    len_counts_df.to_csv(output_file,index=False)

    
def main():

    #print("System Path", sys.path)

    parser = argparse.ArgumentParser(prog='Get fasta lengths',
                                     description='Generates the lengths of sequences in a fasta file.',
                                     epilog='Have a good day!')
    parser.add_argument('fasta_file', help='Path to the input fasta file')
    parser.add_argument('output_file', help='Path to the output fasta file')

    args = parser.parse_args()

    print("Starting to calculate")
 
    get_fasta_lengths(args.fasta_file,args.output_file)

if __name__ == "__main__":
    main()