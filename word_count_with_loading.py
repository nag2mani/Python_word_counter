def wordcount(fname):
    """
    Returns a dictionary with the individual word count of fname

    This function opens the specified text file and creates
    a dictionary from it. The keys of the dictionaries are 
    words (i.e. adjacent letters with no spaces or
    punctuation). For example, in the sring 'Who are you?',
    the words are 'who', 'are' and 'you'. The values are
    the number of times that word (paying atention to 
    capitalization) appears in the file.

    Parameter fname: The file name
    Precondition: fname is a string and the name of a text file
    """

    file = open(fname)
    text = file.read()
    file.close()

    counts = {}           # Store the word count
    word = ''             # Accumulator to build word
    for pos in range(len(text)):
        # yield every 10%
        if pos%(len(text)//10) == 0:
            # indicate the amount of progress made.
            yield round(100*pos/len(text))

        x = text[pos]
        if x.isalpha():
            word = word+x
        else:
            if word != '':
                add_word(word,counts)
            word = ''

    if word != '':
        add_word(word,counts)
    return counts


def add_word(word,counts):
    if word not in counts.keys():
        counts[word] = 1
    else:
        counts[word] += 1


def loadfile(fname):
    """
    Creates a word-count dictionary for fname and prints
    its size.

    The size of the word-count dict is the number of
    distinct words in the file.

    Parameter fname: The file name
    Precondition: fname is a string and the name of a text file
    """
    loader = wordcount(fname)

    # keep going as long as loader is not None.
    while not loader is None:
        try:
            amount = next(loader)
            print('Loaded '+str(amount)+'% of '+repr(fname))
        except StopIteration as e:
            result = e.args[0]
            loader = None

    print('Read a total of '+str(len(result))+' words.')

if __name__ == '__main__':
    loadfile('gandhi10.txt')


