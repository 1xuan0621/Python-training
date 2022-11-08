import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = 'AC0458b97cd21ffecc79446b73d2f304ca'
auth_token = 'c8aed3cb5a8c483f598aafccb4083fa9'
stock_api = 'U5U1UJM17QE3XL4L'
news_api = '8755cd8c92654dbf836fba5e22b993d2'
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parametes = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TSLA',
    'apikey': stock_api
}

stock_responese = requests.get(url='https://www.alphavantage.co/query', params=stock_parametes)
stock_data = stock_responese.json()
stock_list = [float(value['4. close']) for key, value in stock_data['Time Series (Daily)'].items()]

print(stock_list[:2])
if 0.99999 > stock_list[0]/stock_list[1] or stock_list[0]/stock_list[1] > 1.00001 :
    news_parameters = {
        "apiKey": news_api,
        'qInTitle': "Tesla Inc",
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
    news_data = news_response.json()
    articles = news_data['articles'][:3]

    formatted_articles = [f'Headline: {article["title"]}. \nBrief: {article["description"]}' for article in articles]
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                body=article,
                from_='+14345054642',
                to='+886983839151'
            )
    print(message.status)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

