def overlapping_ranges(range1, range2, X):
    # Extract range start and end points
    start1, end1 = range1
    start2, end2 = range2

    # Find the overlapping range
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)

    # Count the number of overlapping elements
    overlap_count = max(0, overlap_end - overlap_start + 1)

    # Return True if overlap meets or exceeds X
    return overlap_count >= X

# Example Usage
print(overlapping_ranges([4, 10], [6, 15], 3))  # ✅ True (Overlap = {6,7,8,9,10})
print(overlapping_ranges([1, 5], [6, 10], 2))   # ❌ False (No overlap)
print(overlapping_ranges([2, 8], [5, 12], 4))   # ✅ True (Overlap = {5,6,7,8})
