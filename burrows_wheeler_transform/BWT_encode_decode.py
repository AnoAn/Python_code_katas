def encode(s):
    '''
    Compresses a string via the Burrows-Wheeler Transformation
    
    Input: string s to encode
    Output: string of same length w BWTransform
    '''

    if s=="":
        return [""]
    
    # create encoding matrix w cyclic char shifting
    encode_l = []
    for i in range(len(s)):
        comb = s[-i:]+s[:-i]
        encode_l.append(comb)
    
    # sort matrix
    encode_l.sort()
    
    # return last col of encoded matrix and index of input string
    return (''.join(x[-1:] for x in encode_l), encode_l.index(s))

def decode(s, n):
    '''
    Decodes string compressed via the Burrows-Wheeler Transform
    
    Input: BWT string s and index n of last character
    Output: original string
    '''

    # define Last and First columns of encoded matrix
    L = s
    F = sorted(L)
    
    # set initial idx defined by n
    idx = n

    string = []
    for l in range(len(s)):
        # pick char w idx from last col
        curr_char = L[idx]
        # append it
        string.append(curr_char)
        
        # count char occurrences up to its idx
        occurrence = 0
        for x in L[:idx+1]:
            if x == curr_char:
                occurrence += 1
        
        # in first col find index of char w same occurrence
        inner_c = 0
        for i, x in enumerate(F):
            if x == curr_char:
                inner_c += 1
                if inner_c == occurrence:
                    idx = i
                    break

    return ''.join(reversed(string))
  
  
  if __name__ == "__main__":
    assert encode("bananabar") == ("nnbbraaaa", 4)
    assert decode("nnbbraaaa", 4) == "bananabar"
