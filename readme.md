# Google Docs

There are two types of Google Docs, private and public shared.
- For private docs we need to authenticate first to get access to the doc.
- For public shared docs we can use HTTP request to get the content.

In order to use HTTP request, we need to install `requests` package.
In order by parse HTML content, we need to install `beautifulsoup4` package.

In the example code, you are given a Google Doc like [this one](https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub) that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

- The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.
- The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.
- Any positions in the grid that do not have a specified character should be filled with a space character.