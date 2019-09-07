// Will print out all 26 decoded version of the message. 
// the message should only be an excerpt
// using these functions find the secret key that decodes the message and use it on the full message. 
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
message = "MEMYQ ZFADU ZAIGZ PQDEF MZPFT MFAZQ OMZEG OOQQP UZAGD BDARQ EEUAZ UZYMZ KIMKE EAYQE FGPQZ FEMDQ"

def map_alphabet(x):
   my_dict = {};
   for letter in alphabet:
        index = alphabet.find(letter);
        if (index - x < 0):
            index = 26 + (index - x);
        else:
            index = index - x;
        my_dict.update({letter : alphabet[index]});
   my_dict.update({' ':' '}); 
   return my_dict;

for x in range(1, 26):
    string = '';
    my_dict = map_alphabet(x);
    for letter in message:
        val = mydict[letter];
        string += val
    print(string);
    print("==================")
    string = '' 
