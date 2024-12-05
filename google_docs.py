import requests
from bs4 import BeautifulSoup

def extract_table_data_from_public_doc(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table_data = []
    table = soup.find('table')

    rows = table.find_all('tr')
    for i, row in enumerate(rows):
        if i == 0: # skip first row
            continue
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        table_data.append([int(cols[0]), cols[1], int(cols[2])])

    #print(table_data)
    return table_data

def generate_printable_data(table_data):

    # get the Maximum x,y coordinators to initialize the two-dimensional array for printable_data
    max_x = 0
    max_y = 0
    for row in table_data:
        if max_x < row[0]:
            max_x = row[0]
        if max_y < row[2]:
            max_y = row[2]

    printable_data = []
    tmp_row = []
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            tmp_row.append(" ") #Any positions in the grid that do not have a specified character should be filled with a space character.
        printable_data.append(tmp_row)
        tmp_row = []

    # fill in the printable_data with table_data
    for row in table_data:
        printable_data[max_y - row[2]][row[0]] = row[1]

    #print(printable_data)
    return printable_data

def print_graphic(printable_data):
    for row in printable_data:
        for char in row:
            print(char, end='')
        print()

def main():
    doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
    table_data = extract_table_data_from_public_doc(doc_url)
    printable_data = generate_printable_data(table_data)
    print_graphic(printable_data)

if __name__ == '__main__':
    main()
