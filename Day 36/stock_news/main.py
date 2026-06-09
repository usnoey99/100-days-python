import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEW_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "your_stock_api_key" # example
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"


## STEP 1:
# i. get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


# ii. Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


# iii. Find the positive difference between i and ii.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# iv. Work out the value of 1% of yesterday's closing price.
diff_percent = round((difference/float(yesterday_closing_price)) * 100)


# v. If iv is true then print("Get News")
if abs(diff_percent) > 1:
    # print("Get News")


## STEP 2:
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_param = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEW_ENDPOINT, params=news_param)
    articles = news_response.json()["articles"]


    # vi. Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]


    ## STEP 3:
    # vii. Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down} {diff_percent}%\n"
        f"Headline: {article['title']}.\n"
        f"Brief: {article['description']}"
        for article in three_articles
    ]


    # viii. Send each article as a separate message via Twilio
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for formatted_article in formatted_articles:
        message = client.messages.create(
            body = formatted_article,
            from_ = "+1234567890",
            to = "+1234567890"
        )
        print(message.status)



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
