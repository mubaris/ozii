import os
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import argparse
#from scipy.sparse import csr_matrix
#from PIL import Image

def build_alphabet():
    alphabet = defaultdict(lambda: 0, {
        'e': 10.0,
        't': 9.62,
        'a': 9.23,
        'o': 8.85,
        'i': 8.46,
        'n': 8.08,
        's': 7.69,
        'r': 7.31,
        'h': 6.92,
        'd': 6.54,
        'l': 6.15,
        'u': 5.77,
        'c': 5.34,
        'm': 5.00,
        'f': 4.62,
        'y': 4.23,
        'w': 3.85,
        'g': 3.46,
        'p': 3.08,
        'b': 2.69,
        'v': 2.31,
        'k': 1.92,
        'x': 1.54,
        'q': 1.15,
        'j': 0.77,
        'z': 0.34,
        '.': 4.9e-7,
        '?': 5.1e-7,
        ' ': 0
    })
    for letter in [key for key in alphabet.keys() if key.isalpha()]:
        alphabet[letter.upper()] = alphabet[letter]+(1e-7)
    return alphabet

def cos(x):
    return np.cos(180 * x / np.pi)

def sin(x):
    return np.sin(180 * x / np.pi)

def inverse(x):
    return 1/x

def transformer(x):
    return inverse(sin(cos(x)))

def transform(x, alphabet, text):
    n = len(text)
    y = 0
    for i in range(len(text)):
        y += alphabet[text[i]] * (x ** (i+1))
    y = transformer(y)
    max_y = np.max(np.abs(y))
    y = (0.5/max_y) * y
    return y

def sentence_transformer(x, alphabet, sentence):
    words = sentence.split()
    y = np.zeros(x.shape)
    for i, word in enumerate(words):
        y += transform(x, alphabet, word)
    max_y = np.max(np.abs(y))
    y = (0.5/max_y) * y
    return y

def generate_image(sentence, pixels=500, dir="output"):
    alphabet = build_alphabet()
    x = np.linspace(0, 1, 1001)[1:]
    y = sentence_transformer(x, alphabet, sentence)
    size = pixels / 10
    fig = plt.figure(figsize=(10, 10))
    plt.plot(x, y, linewidth=1, c='k')
    plt.axis([0, 1, -0.5, 0.5])
    plt.axis('off')
    words = sentence.split()
    if not os.path.isdir(dir):
        os.makedirs(dir)
    filename = dir + "/" + sentence + ".png"
    plt.savefig(filename, dpi=size)
    plt.close('all')
    return filename

'''def vectorizer(sentence, pixels=500, dir="output", dense=False):
    filename = generate_image(sentence, pixels=pixels, dir=dir)
    img = Image.open(filename).convert('L')
    arr = np.array(img)
    arr = 255 - arr
    if dense:
        return arr
    csr = csr_matrix(arr)
    return csr'''

def main():
    # Check if arguments have been given a value
    # text is not checked because it is mandatory
    if args.size is None:
        parser.error('Invalid size')
    elif args.dir is None:
        parser.error('Invalid output directory')
    generate_image(args.text, args.size, args.dir)

if __name__ == '__main__':
    # Command line argument parsing only if the program is being executed directly
    parser = argparse.ArgumentParser(description='Generate PulseGraphs from Text data')
    parser.add_argument('-t','--text', help='Input sentence', required=True)
    parser.add_argument('-s','--size', help='Output image size in pixels', type=int, nargs='?', default=500)
    parser.add_argument('-d','--dir', help='Output directory', nargs='?', default='output')
    args = parser.parse_args()
    main()