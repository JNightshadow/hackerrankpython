from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self,tag,attrs):
        print(tag)
        for attr,values in attrs:
            print(f"-> {attr} > {values}")
    def handle_startendtag(self,tag,attrs):
        print(tag)
        for attr,values in attrs:
            print(f"-> {attr} > {values}")
    
if __name__ == "__main__":
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())
