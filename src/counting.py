from collections import Counter


def count_nucleotides(sequence) -> dict:
    """
    A function to count the nucleotides in a sequence
    :param sequence: the sequence
    :return: the dictionary of nucleotide counts
    """
    sum_sequence = 0
    counter = Counter()
    for nucleotide in sequence:
        counter[nucleotide] += 1
        sum_sequence += 1  # Update the total count for each nucleotide
    counter = dict(counter)
    counter['sum'] = sum_sequence
    return counter
