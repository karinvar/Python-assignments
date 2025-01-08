import argparse

def parse_fasta(file_path):
    """Parse a FASTA file and yield record ID and sequence."""
    with open(file_path, "r") as file:
        record_id = None
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if record_id:
                    yield record_id, "".join(sequence)
                record_id = line[1:]  # Remove ">" from the header line
                sequence = []
            else:
                sequence.append(line)
        if record_id:
            yield record_id, "".join(sequence)

def find_longest_duplicate(sequence):
    """Find the longest subsequence that repeats itself."""
    n = len(sequence)
    longest = ""
    for i in range(n):
        for j in range(i + 1, n):
            length = 0
            while j + length < n and sequence[i + length] == sequence[j + length]:
                length += 1
            if length > len(longest):
                longest = sequence[i:i + length]
    return longest

def gc_content(sequence):
    """Calculate GC content as a percentage."""
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    return (g_count + c_count) / len(sequence) * 100 if sequence else 0

def analyze_file(file_path, duplicate, blabla):
    """Perform the selected analyses on the input file."""
    for record_id, sequence in parse_fasta(file_path):
        print(f"Analyzing sequence: {record_id}")
        if duplicate:
            longest_dup = find_longest_duplicate(sequence)
            print(f"Longest duplicate subsequence: {longest_dup}")
        if blabla:
            gc = gc_content(sequence)
            print(f"GC content: {gc:.2f}%")

def main():
    parser = argparse.ArgumentParser(description="Analyze sequences from a FASTA file.")
    parser.add_argument("file", type=str, help="Path to the input file.")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest duplicate subsequence.")
    parser.add_argument("--blabla", action="store_true", help="Calculate GC content.")
    args = parser.parse_args()

    if not args.duplicate and not args.blabla:
        print("Please select at least one analysis option (--duplicate or --blabla).")
        return

    analyze_file(args.file, args.duplicate, args.blabla)

if __name__ == "__main__":
    main()
