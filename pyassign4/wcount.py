#!/usr/bin/env python3
"""tile.py: methods of brick paving
__author__ = "Liu Yuxin"
__pkuid__  = "1800011832"
__email__  = "1800011832@pku.edu.cn"
"""
import sys
import string
from urllib.request import urlopen
from urllib import error


def wcount(lines, topn=10):
    """Statistics of the occurrence of words in a text file and printing the top n"""
    dic = {}
    for i in lines:
        if i in string.punctuation:
            lines = lines.replace(i, " ")
    values = lines.split()
    for word in values:
        word = word.lower()
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    items = []
    for (x, y) in dic.items():
        items.append((y, x))
    item = sorted(items, reverse=True)
    if topn < len(item):
        order = item[:topn]
    else:
        order = item[:]
    for (x, y)in order:
        print(y, x)
        
        
def main():
    """main module"""
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        url = sys.argv[1]
        try:  # Capture of exception
            doc = urlopen(url)
        except error.HTTPError as err:
            print(err.code)
        except error.URLError as err:
            print(err.reason)
        except Exception as err:
            print(err)
        else:
            docstr = doc.read()
            doc.close()
            text = docstr.decode()
            if len(sys.argv) > 2:
                topn = int(sys.argv[2])
                wcount(text, topn)  
            else:
                wcount(text)


if __name__ == '__main__':
    main()
