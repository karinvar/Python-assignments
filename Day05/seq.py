import os

def calculate_statistics(seq):
    # Initialize the counters
    stats = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    
    # Count the nucleotides
    for nucleotide in seq:
        if nucleotide == "A":
            stats["A"] += 1
        elif nucleotide == "C":
            stats["C"] += 1
        elif nucleotide == "G":
            stats["G"] += 1
        elif nucleotide == "T":
            stats["T"] += 1
        else:
            stats["Unknown"] += 1
    
    # Calculate percentages
    total = len(seq)
    percentages = {key: (count / total) * 100 for key, count in stats.items()}
    
    return stats, percentages, total

def process_file(file_name):
    if not os.path.exists(file_name):
        print(f"Error: File {file_name} not found.")
        return
    
    with open(file_name, "r") as file:
        seq = file.read().strip()
        stats, percentages, total = calculate_statistics(seq)

    # Print results for the current file
    print(f"Results for {file_name}:")
    for nucleotide, count in stats.items():
        print(f"{nucleotide}: {count} {percentages[nucleotide]:.1f}%")
    print(f"Total: {total}")
    print("\n")

def test_calculate_statistics():
    seq = "ACGTNNNN"
    stats, percentages, total = calculate_statistics(seq)
    assert stats == {"A": 1, "C": 1, "G": 1, "T": 1, "Unknown": 4}
    assert round(percentages["A"], 1) == 12.5
    assert total == 8
    print("Test passed.")

def main():
    file_names_input = input("Enter file names (file1.txt,file2.txt): ")
    file_names = file_names_input.split(",")
    
    for file_name in file_names:
        file_name = file_name.strip()
        process_file(file_name)
    
    # Run the test function
    test_calculate_statistics()

if __name__ == "__main__":
    main()
