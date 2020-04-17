import sys 
from urllib.request import urlopen

#Fetchuju list slov z URL. URL je param.
def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


#Vyprintovat vsechny items of a list.
def print_items(items):
    for item in items:
        print(item)

#Cekam na zadani URL v CLI.
def main():
    url = str(input("Please type the URL:"))
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
   main()
