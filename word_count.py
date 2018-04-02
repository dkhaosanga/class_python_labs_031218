#
# def strip_words(emma_strip):
#     for space in emma_strip.strip()
#     return strip_words()
#
# def word_count(emma_string):
#     string_words = {}
#     for word in emma_string.split():
#         if word in string_words:
#             string_words[word] += 1
#         else:
#             string_words[word] = 1
#     return string_words
#
#
# with open('emma.txt', 'r') as fileinput:
#     for line in fileinput:
#         line = line.lower()
#         # line = line.replace('\n','')
#         line = line.strip()
#         print(word_count(line))

# def word_count(a_string):
#     string_dictionary = {}
#     for word in line.split():
#         if word in string_dictionary:
#             string_dictionary[word] += 1
#         else:
#             string_dictionary[word] = 1
#     return string_dictionary

string_words = {}

with open('emma.txt', 'r') as fileinput:
    data = fileinput.readlines()

for line in data:
    line = line.lower().strip().replace(',','').replace('.','').replace('"','').replace('-','').replace("'",'').replace('?','').replace('!','').replace('_','')
    words = line.split()
    for word in words:
        if word in string_words:
            string_words[word] += 1
        else:
            string_words[word] = 1

string_word_count = sorted(string_words.items(), key=lambda x: x[1], reverse=True)
for k,v in string_word_count[:10]:
    print(k,v)

# string_word_count = string_words.items()
#
# print (string_word_count [1:10])


    # print (word, string_words)
#     for word in fileinput.split():
#         if word in string_words:
#             string_words[word] += 1
#         else:
#             string_words[word] = 1
#


# string_word_count = sorted(string_words.items(), key=lambda x: x[1], reverse=True)
#
# for k,v in string_word_count[:10]:
#     print(k,v)
