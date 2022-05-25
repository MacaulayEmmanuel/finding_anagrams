def find_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)
print(find_anagrams("restful", "fluster"))