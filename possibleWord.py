
def words(string, word=''):
    string or print(word)
    for character in string:
        words(string - {character}, word + character)


List = ['a', 'e', 'i', 'o', 'u']

words(set(''.join(List)))
