# BittrexAPI-Display
Made in Python

It became annoying to login to my Bittrex account (Bittrex is a cryptocurrency exchange) as it asks for a Google Authecnticator code for every login. The program I made solves this by using an API key and API secret linked to my account. Using this I can call Bittrex's API to retreive information about my account, such as my holdings and balances. Next I parse this data in the JSON format and use the tkinter toolkit for Python to display all pertinent information to a GUI. This way, I can check my holdings and balances with the click of a button instead of having to login manually. 

This will work for any account. Simply change the apikey and apisecret variables to your accounts api key and api secret.
