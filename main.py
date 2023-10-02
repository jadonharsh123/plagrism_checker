import re
from collections import Counter
import math

def get_cosine(vec1, vec2):
    intersection = set(vec1) & set(vec2)
    numerator = sum(vec1[x] * vec2[x] for x in intersection)

    sum1 = sum(vec1[x] ** 2 for x in vec1)
    sum2 = sum(vec2[x] ** 2 for x in vec2)
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = re.findall(r'\w+', text)
    return Counter(words)

def check_plagiarism(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine = get_cosine(vector1, vector2)
    return cosine

def main():
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    similarity = check_plagiarism(text1, text2)

    print(f"The similarity between the texts is: {similarity}")

if __name__ == "__main__":
    main()
