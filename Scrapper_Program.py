from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

BaseUrl = 'https://www.cars.com/shopping/results/?'

def Preparator(BaseUrl, MinPrice, MaxPrice, brand, status):

    Url =  BaseUrl + '&list_price_max=%s&list_price_min=%s&page_size=100&sort=list_price_desc&stock_type=%s&makes[]=%s' % (MaxPrice, MinPrice, status, brand)

    print(Url)

    return Url



AllCarsOutput = []



def GetData(Url):

    while True:

        Req = requests.get(Url).text
        Soup = BeautifulSoup(Req, 'html.parser')

        CarList = Soup.find_all('div', class_ = 'vehicle-details')
        time.sleep(0.5)
        NextPageBtns = Soup.find_all('a', class_ = 'sds-button sds-button--secondary sds-pagination__control')

        for i in CarList:

            CarListOutput = {

                'Number': i,
                'Title': CarList.find('h2', class_ = 'title').text,
                'Price': CarList.find('span', class_ = 'primary-price').text,

            }

            AllCarsOutput.append(CarListOutput)
        
        print(NextPageBtns)

        if NextPageBtn['aria-disabled'] == 'true':

            break

        else:

            pass

def SaveData(OP):

    df = pd.DataFrame(OP, columns=['Number', 'Title', 'Price'])
    df.to_excel('Cars List.xls', index=True, columns=['Number', 'Title', 'Price'])

FUrl = Preparator(BaseUrl, 15000, 35000, 'audi', 'new')

GetData(FUrl)

SaveData(AllCarsOutput)