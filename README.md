# Caesars_Cipher
A tool to decode Caesar's cypher. The idea is a simple shifting of the keys back to decode a mesage. 

### Dev Env
The code was used on Juptyrs notebook. You don't need to run it there. 

### Approach
The code first create a map of the letter of the alphabet and then iterate over that by shifting 1-26 keys back on an _excerpt_ of the encoded message. If you notice a word on a certain key, decode the whole message using that key.
