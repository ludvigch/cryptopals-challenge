import challenge3
def find_encrypted():
    read_strings = ""
    with open('4.txt', 'r') as f:
        read_strings = f.read()
    candidates = read_strings.split("\n")
    all_candidates = []
    for candidate in candidates:
        all_candidates += challenge3.crack(candidate)
    sorted_candidates = sorted(all_candidates, key=lambda entry: entry[0])
    return sorted_candidates

if __name__ == '__main__':
    meme = find_encrypted()
    for x in range(5):
        print(meme[x])
