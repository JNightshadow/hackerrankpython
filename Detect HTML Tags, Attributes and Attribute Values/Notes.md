# Intoducing [HTML Parser](https://docs.python.org/3/library/html.parser.html)

- This class allows us to print out start tags, end tags, and data as they are encountered.

- We included it by:
`from html.parser import HTMLParser`
For the problem in [HackerRank](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true), we've been asked to output the HTML tags, attributes and attribute values in order of their occurrences.

  ## What we need to do:
1. In the code we must declare define a class say `MyHTMLParser` inheriting the built-in class `HTMLParser`.
  2. We override the methods `handle_starttag` and `handle_startendtag`
  3. We declare an object `parser` of our class `MyHTMLParser`.
  4. We feed the input using   `parser.feed(input())`
  5. The definitions we override will handle the printing. 
