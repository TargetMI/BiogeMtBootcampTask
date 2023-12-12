from collections import Counter

with open('C:/Users/nickc/BiogeMtBootcampTask/data/reads_bkg.fa', 'r') as f:
    seq_name, d = '', ''
    total_count = 0  # Initialize the total count variable
    for line in f:
        if line.startswith('>'):
            if seq_name:  # Check if seq_name is not empty
                print(seq_name, d, "Total count:", total_count)  # Print total count for the previous sequence
            seq_name = line.rstrip('\n')
            d = Counter()
            total_count = 0  # Reset the total count for the new sequence
        else:
            for i in line.rstrip('\n'):
                d[i] += 1
                total_count += 1  # Update the total count for each nucleotide
    if seq_name:  # Print the counts for the last sequence
        print(seq_name, d, "Total count:", total_count)