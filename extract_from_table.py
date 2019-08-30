# Extract data from html table where data is not consistently held in single class type.
# Hacky so requires reworking for each use & checking output
# Requires saving table html via e.g. Developer Tools in Chrome

from bs4 import BeautifulSoup as BS
import pandas as pd
html = open(r'usr\path\file.html')
dir = (r'usr\path\'')
soup = BS(html,"html.parser")
tables =  soup.find_all("table")
i=1

for table in tables:
    headings = [th.get_text() for th in table.find("tr").find_all("th")] 
    rows = table.findAll('tr')
    table_deets = [headings]
    row_deets = []
    for row in rows[1:]:
        cols = row.find_all('td')
        for col in cols:
               spans = col.find_all('span')
               for span in spans:
                   if span.has_attr('class') and span['class'][0] == 'yes': 
                       row_deets.append("Yes")
                   elif span.has_attr('class') and span['class'][0] == 'no': 
                       row_deets.append("No")#ok
                   elif span.has_attr('class') and span['class'][0] == 'tablesaw-cell-content':
                       if  span.get_text() != '':
                           row_deets.append(span.get_text())
        table_deets.append(row_deets)
        row_deets = []
    df=pd.DataFrame(table_deets)
    df.to_csv(dir+table['id']+'.csv')
