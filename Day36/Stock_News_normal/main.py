import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = 'OJEHHA8T0380BU9G'
NEWS_API_KEY = '458fd7d330d747c5a141a153f7043a86'
TWILIO_SID = 'AC96ff8f1e4119a93e0b9f1473ba29abe4'
TWILIO_AUTH_TOKEN = '40c0f8e94aa194b31da4470f4f131d1c'

parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':STOCK_API_KEY
}

        ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
#Get yesterday's closing stock price.

response = requests.get(STOCK_ENDPOINT,params=parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
# print(yesterday_data)
yesterday_closing_price = yesterday_data['4. close']
#print(yesterday_closing_price)
# When stock price increase/decreases by 5% between yesterday and
# the day before yesterday then print("Get News").

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data['4. close']
#print(day_before_yesterday_closing_data)

#Find the positive difference between 1 and 2.
# e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_data))
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

#Work out the percentage difference in price between closing price yesterday
# and closing price the day before yesterday.
diff_percent = round((difference/float(yesterday_closing_price))*100)
print(diff_percent)

#If TODO4 percentage is greater than 5 then print("Get News").
     ## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 1:
    new_params = {
        'apikey': NEWS_API_KEY,
        'qInTitle':COMPANY_NAME,
    }
    new_response = requests.get(NEWS_ENDPOINT,params = new_params)
    articles = new_response.json()['articles']
    # Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article_list = [f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline:{article['title']}.\n Brief:{article['description']}" for article in three_articles]

    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_article_list:
        message = client.messages.create(body=article,
                                     from_='+12187182869',
                                         to='+905366458227')



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

