MY_ALPHABET = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž0123456789.,-+?!AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"


def caesarWithNumberArray(shifts, text):
    output=""
    for i,char in enumerate(text):
        if char == " ":
            output+=" "
        else:
            output+=MY_ALPHABET[((MY_ALPHABET.index(char)) + shifts[i%len(shifts)]) % len(MY_ALPHABET)]
    return output

def decipherCaesarWithNumberArray(shifts, text):
    
    return caesarWithNumberArray([ -x for x in shifts ], text)

originalText="Ahojjj jak to jde??"

print(caesarWithNumberArray([1,54,45,24], originalText))

print(decipherCaesarWithNumberArray([1,54,45,24], caesarWithNumberArray([1,54,45,24], originalText)))

