def match_words(dictionary, sentence, n, m):
    mp = dict()
    for i in range(n):
        mp[dictionary[i]] = mp.get(dictionary[i], 0) + 1
    for i in range(m):
        if (mp[sentence[i]]):
            mp[sentence[i]] -= 1
        else:
            return False
    return True

dictionary = ["news", "paper", "chocolate", "chip", "lap",
              "top", "desk", "answers"]
 
n = len(dictionary)
 
sentence = ["newspaper", "laptop"]
m = len(sentence)

if (match_words(dictionary, sentence, n, m)):
    print("YES")
else:
    print("NO")
 