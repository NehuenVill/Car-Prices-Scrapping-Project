# **Car Prices scrapping program**


## Goal of the project

Extract information about the price of all the cars that present certain features such as the brand, minimum and maximum price, and state of usage. All these parameters may change according to the client, ==which can be simply changed in only one function on the code.==

## Technologies ussed

* **Python**.
* **Beautiful Soup 4.**
* **Excel Spreadsheets.**
* **Pandas library.**

## Description of the scrapping process

All the Parameters are given by the client to the *Preparator* function (The base URL, Minimum and maximum price, brand, and status), this function gets all the data together in a single URL and returns it as a string.

The output of the *Preparator* is given to the *GetData* function, which retrieves the title and price of each car on the page and when done, starts with the next one until there're no more cars available. All the information is stored in the *AllCarsOutput* variable.

Finally, the *SaveData* function is called and given the *AllCarsOutput* variable as the only parameter. This function uses the **Pandas library** to Export all the data stored in the *AllCarsOutput* variable to an **Excel sheet** called *Cars List.xls*, finishing the scrapping process.