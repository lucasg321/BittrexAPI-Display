# BittrexAPI-Display
Made in Python

It became annoying to login to my Bittrex account (Bittrex is a cryptocurrency exchange) as it asks for a Google Authenticator code for every login attempt. The program I made solves this issue by using an API key and API secret linked to my account. Using this I can call Bittrex's API to retreive information about my account, such as my holdings and balances without having to login. I parse this data in the JSON format, and with the use of the tkinter toolkit for Python, display all pertinent information in a GUI. This way, I can check my holdings and balances with the click of a button. 

This will work for any account. Simply change the apikey and apisecret variables to your accounts api key and api secret.
