def Censored(someString, addLetters):
    return someString.replace('*', '{}').format(*addLetters)


String = 'W*o Di* I*?'
Letters = 'hdt'

print(Censored(String, Letters))
