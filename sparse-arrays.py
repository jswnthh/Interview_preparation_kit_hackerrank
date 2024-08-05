# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries

def matchingStrings(strings, queries):
    #create frequency dictionary
    freq_dict = {}
    for string in strings:
        if string in freq_dict:
            print("counting string", string)
            freq_dict[string] += 1
        else:
            print("adding string....", string)
            freq_dict[string] = 1
    
    #count occurences and get result
    result = []
    for query in queries:
        count = freq_dict.get(query, 0)
        result.append(count)
        print("appending result.... ", result)

    return result


strings = []
queries = []
size_strings = int(input())
for i in range(size_strings):
    a = input()
    strings.append(a)

query_strings = int(input())
for i in range(query_strings):
    b = input()
    queries.append(b)


counts = matchingStrings(strings, queries)
print(counts)