import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key = "084918df477d8c75a9d9ad00ee600388"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":"084918df477d8c75a9d9ad00ee600388"

}


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get("https://www.alphavantage.co/query", params=parameters)


print(response.status_code)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing = data_list[0]["4. close"]
day_before_yesterday_closing = data_list[1]["4. close"]
print(yesterday_closing)
print(day_before_yesterday_closing)
difference = float(yesterday_closing) - float(day_before_yesterday_closing)
percentage_increase = (abs(difference)/float(yesterday_closing))*100
print(round(percentage_increase,2))

if percentage_increase > 2:
    parameters_news = {
        "q": COMPANY_NAME,
        "from": "2022-07-01",
        "apikey": "398c0bbb255d4e02bab1b181e6228244"

    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=parameters_news)
    articles = news_response.json()["articles"]
    first_three_articles = articles[:3]
    print(first_three_articles)
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]




#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



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

