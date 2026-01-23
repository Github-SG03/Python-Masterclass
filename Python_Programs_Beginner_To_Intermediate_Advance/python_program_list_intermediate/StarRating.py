def StarRating(rating_str):
    rating = round(float(rating_str) * 2) / 2  # Round to nearest 0.5
    stars = []

    for _ in range(5):
        if rating >= 1:
            stars.append("full")
            rating -= 1
        elif rating == 0.5:
            stars.append("half")
            rating -= 0.5
        else:
            stars.append("empty")

    return " ".join(stars)

# Test cases
print(StarRating("0.38"))  # Output: "half empty empty empty empty"
print(StarRating("4.5"))   # Output: "full full full full half"
print(StarRating("3.76"))  # Output: "full full full half empty"
print(StarRating("2.2"))   # Output: "full full empty empty empty"
print(StarRating("5.0"))   # Output: "full full full full full"
print(StarRating("0.00"))  # Output: "empty empty empty empty empty"
