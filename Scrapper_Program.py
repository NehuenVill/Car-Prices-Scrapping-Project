from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

BaseUrl = 'https://www.cars.com/shopping/results/?'

#function that prepares the URL with the parameters given by
#the client

def Preparator(BaseUrl, MinPrice, MaxPrice, brand, status):

    Url =  BaseUrl + 'page=1&&list_price_max=%s&list_price_min=%s&page_size=100&sort=list_price_desc&stock_type=%s&makes[]=%s' % (MaxPrice, MinPrice, status, brand)

    print(Url)

    return Url


AllCarsOutput = []

#Function to get the Cars' data, one by one and then store each
#one of them in the "AllCarsOutput" variable. 

def GetData(Url):

    url = Url

    while True:

        Req = requests.get(url).text
        Soup = BeautifulSoup(Req, 'html.parser')

        CarList = Soup.find_all('div', class_ = 'vehicle-details')
        LastNextPageBtn = Soup.find('button', id = 'next_paginate')

        NextPageBtn = Soup.find('a', class_ = '')


        for i in range(len(CarList)):

            CarListOutput = {

                'Number': i,
                'Title': CarList[i].find('h2', class_ = 'title').text,
                'Price': CarList[i].find('span', class_ = 'primary-price').text,

            }

            AllCarsOutput.append(CarListOutput)
            print(CarListOutput)
            print(NextPageBtn)

        url = NextPageBtn['href']

        if LastNextPageBtn:

            break

        else:

            pass

#Function to export all the retrieved data into an .xls file.

def SaveData(OP):

    df = pd.DataFrame(OP, columns=['Number', 'Title', 'Price'])
    df.to_excel('Cars List.xls', index=True, columns=['Number', 'Title', 'Price'])


#Run the whole process given certain parameters:

FUrl = Preparator(BaseUrl, 1500, 100000, 'audi', 'new')

GetData(FUrl)

SaveData(AllCarsOutput)