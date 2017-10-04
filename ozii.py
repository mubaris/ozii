import os
import numpy as np
import matplotlib.pyplot as plt

alphabet = {
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
    'E': 2*10.0,
    'T': 2*9.62,
    'A': 2*9.23,
    'O': 2*8.85,
    'I': 2*8.46,
    'N': 2*8.08,
    'S': 2*7.69,
    'R': 2*7.31,
    'H': 2*6.92,
    'D': 2*6.54,
    'L': 2*6.15,
    'U': 2*5.77,
    'C': 2*5.34,
    'M': 2*5.00,
    'F': 2*4.62,
    'Y': 2*4.23,
    'W': 2*3.85,
    'G': 2*3.46,
    'P': 2*3.08,
    'B': 2*2.69,
    'V': 2*2.31,
    'K': 2*1.92,
    'X': 2*1.54,
    'Q': 2*1.15,
    'J': 2*0.77,
    'Z': 2*0.34,
    '.': 25,
    '?': 30,
    ' ': 0
}

def cos(x):
    return np.cos(180 * x / np.pi)

def sin(x):
    return np.sin(180 * x / np.pi)

def inverse(x):
    return 1/x

def transformer(x):
    y = cos(x)
    y = sin(y)
    y = inverse(y)
    return y

x = np.linspace(0, 1, 1001)
x = x[1:]

def transform(text):
    n = len(text)
    y = 0
    for i in range(len(text)):
        y += alphabet[text[i]] * (x ** (i+1))
    y = transformer(y)
    max_y = np.max(np.abs(y))
    y = (0.5/max_y) * y
    return y

def sentence_transformer(sentence):
    words = sentence.split()
    y = np.zeros(x.shape)
    for i, word in enumerate(words):
        y += transform(word)
    max_y = np.max(np.abs(y))
    y = (0.5/max_y) * y
    return y

def generate_image(sentence, pixels=500, dir="output"):
    y = sentence_transformer(sentence)
    size = pixels / 10
    fig = plt.figure(figsize=(10, 10))
    plt.plot(x, y, linewidth=1, c='k')
    plt.axis([0, 1, -0.5, 0.5])
    plt.axis('off')
    words = sentence.split()
    if not os.path.isdir(dir):
        os.makedirs(dir)
    filename = dir + "/" + sentence + ".png"
    plt.savefig(filename, dpi=size, bbox_inches='tight')