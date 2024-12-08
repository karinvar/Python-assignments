import os
import sys

def calculate_statistics(seq):
    # Initialize the counters
    stats = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    
    # Count the nucleotides
    for nucleotide in seq:
        if nucleotide in stats:
            stats[nucleotide] += 1
        else:
            stats["Unknown"] += 1
    
    # Calculate percentages
    total = len(seq)
    percentages = {key: (count / total) * 100 for key, count in stats.items()} if total > 0 else stats
    
    return stats, percentages, total

def process_file(file_name):
    if not os.path.exists(file_name):
        print(f"Error: File {file_name} not found.")
        return {}, 0
    
    with open(file_name, "r") as file:
        seq = file.read().strip()
        stats, percentages, total = calculate_statistics(seq)

    # Print results for the current file
    print(f"Results for {file_name}:")
    for nucleotide, count in stats.items():
        print(f"{nucleotide}: {count} {percentages[nucleotide]:.1f}%")
    print(f"Total: {total}")
    print("\n")
    return stats, total

def combine_statistics(all_stats):
    combined_stats = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    total = 0

    for stats, file_total in all_stats:
        for key in combined_stats:
            combined_stats[key] += stats.get(key, 0)
        total += file_total
    
    percentages = {key: (count / total) * 100 for key, count in combined_stats.items()} if total > 0 else combined_stats
    
    print("Combined Results:")
    for nucleotide, count in combined_stats.items():
        print(f"{nucleotide}: {count} {percentages[nucleotide]:.1f}%")
    print(f"Total: {total}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python seq.py <file1> [<file2> ...]")
        sys.exit(1)

    file_names = sys.argv[1:]
    all_stats = []

    for file_name in file_names:
        stats, total = process_file(file_name)
        if stats:
            all_stats.append((stats, total))
    
    if len(all_stats) > 1:
        combine_statistics(all_stats)

if __name__ == "__main__":
    main()
