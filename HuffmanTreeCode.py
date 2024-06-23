class Nodes:
    """calculate the Huffman code for a given data.\n
        huffman with data as dictionary of items and their frequencies """  
    def __init__(self, probability, symbol, left=None, right=None):  
        # probability of the symbol  
        self.probability = probability  
  
        # the symbol  
        self.symbol = symbol  
  
        # the left node  
        self.left = left  
  
        # the right node  
        self.right = right  
  
        # the tree direction (0 or 1)  
        self.code = ''  


""" A supporting function in order to calculate the probabilities of symbols in specified data """  
def CalculateProbability(symbol_frequency):  
    the_symbols = dict()  
    for symbol, frequency in symbol_frequency.items():  
        if the_symbols.get(symbol) == None:  
            the_symbols[symbol] = frequency  
        else:   
            the_symbols[symbol] += frequency       
    return the_symbols  


""" A supporting function in order to print the codes of symbols by travelling a Huffman Tree """  
the_codes = dict()  
  
def CalculateCodes(node, value=''):  
    # a huffman code for current node  
    newValue = value + str(node.code)  
  
    if(node.left):  
        CalculateCodes(node.left, newValue)  
    if(node.right):  
        CalculateCodes(node.right, newValue)  
  
    if(not node.left and not node.right):  
        the_codes[node.symbol] = newValue  
           
    return the_codes  


""" A supporting function in order to get the encoded result """  
def OutputEncoded(the_data, coding):  
    encodingOutput = []  
    for element in the_data:  
        print(coding[element], end='')  
        encodingOutput.append(coding[element])  
          
    the_string = ''.join([str(item) for item in encodingOutput])      
    return the_string  


""" A supporting function in order to calculate the space difference between compressed and non-compressed data"""      
def TotalGain(the_data, coding):  
    # total bit space to store the data before compression  
    beforeCompression = sum(the_data.values()) * 8  
    afterCompression = 0  
    the_symbols = coding.keys()  
    for symbol in the_symbols:  
        the_count = the_data[symbol]  
        # calculating how many bits are required for that symbol in total  
        afterCompression += the_count * len(coding[symbol])  
    print("Space usage before compression (in bits):", beforeCompression)  
    print("Space usage after compression (in bits):",  afterCompression)


def HuffmanEncoding(symbol_frequency):  
    symbolWithProbs = CalculateProbability(symbol_frequency)  
    the_symbols = symbolWithProbs.keys()  
    the_probabilities = symbolWithProbs.values()  
    print("symbols: ", the_symbols)  
    print("probabilities: ", the_probabilities)  
    
    the_nodes = []  
    
    # converting symbols and probabilities into huffman tree nodes  
    for symbol in the_symbols:  
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))  
    
    while len(the_nodes) > 1:  
        # sorting all the nodes in ascending order based on their probability  
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)  
    
        # picking two smallest nodes  
        right = the_nodes[0]  
        left = the_nodes[1]  
    
        left.code = 0  
        right.code = 1  
    
        # combining the 2 smallest nodes to create a new node  
        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right)  
    
        the_nodes.remove(left)  
        the_nodes.remove(right)  
        the_nodes.append(newNode)  
              
    huffmanEncoding = CalculateCodes(the_nodes[0])  
    print("symbols with codes", huffmanEncoding)  
    TotalGain(symbol_frequency, huffmanEncoding)  
    encoded_output = OutputEncoded(symbol_frequency, huffmanEncoding)  
    return encoded_output, the_nodes[0] 


def HuffmanDecoding(encodedData, huffmanTree):  
    treeHead = huffmanTree  
    decodedOutput = []  
    for x in encodedData:  
        if x == '1':  
            huffmanTree = huffmanTree.right     
        elif x == '0':  
            huffmanTree = huffmanTree.left  
        try:  
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:  
                pass  
        except AttributeError:  
            decodedOutput.append(huffmanTree.symbol)  
            huffmanTree = treeHead  
          
    string = ''.join([str(item) for item in decodedOutput])  
    return string  

symbol_frequency = {"b": 90, "c": 15, "d": 40, "f": 30,"g":125,"h":35}

import sys
#Optional CLI input syntax: python HuffmanTreeCode table="<char> <frequency>, <char> <frequency>, ..."
#Example: python HuffmanTreeCode.py table="a 10, b 15, c 12, d 3, e 4, f 13, g 1"
if __name__ == "__main__": 
    for arg in sys.argv:
        if arg.startswith("table="):
            table_data = arg.split("=")[1].replace("\"", "").split(",")
            newDict = {}
            for item in table_data:
                key, value = item.strip().split(" ")
                try:
                    newDict[key] = int(value)
                except ValueError:
                    print(f"Invalid input for key {key} with value {value}")
                    sys.exit(0)
            symbol_frequency = newDict

print("Symbol Frequency:", symbol_frequency)  
encoding, the_tree = HuffmanEncoding(symbol_frequency)  
print("Encoded output:", encoding)  
print("Decoded Output:", HuffmanDecoding(encoding, the_tree))
