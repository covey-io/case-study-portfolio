import os
import json
import pandas as pd
import numpy as np
import datetime


def calculate_portfolio(address,startCash):
    tradingKey = pd.read_csv('tradingKey.csv')
    # percent = target percent, 0.05 means a 5% target position, 0 means they are closing a position, -0.05 means short 5% 
    # entry_price = price from prices.csv AFTER entry_date 
    # market_entry_date =  first date_time after entry_date from prices.csv
    # prior_portfolio = total_value from portfolio in the date_time before the trade 
    # target_position_value = prior_portfolio_value * percent 
    # post_cumulative_share_count = prior_cumulative_share_count + share_count 
    # target_position_value = prior_position_value + cash_used
    # realized_profit = profit realized whenever you change percent and add a new trade of the same symbol 

    onlyOneAddress = (tradingKey['address'] == address)
    tradingKeyOne = tradingKey.loc[onlyOneAddress] # focus on one address at a time 
    firstTrade = min(tradingKeyOne['entry_date']) # start portfolio math at firstTrade
    

    prices = pd.read_csv('prices.csv')
    prices.set_index('date_time',inplace=True)

    portfolio = pd.DataFrame(index = prices.index,columns=[ "address", "cash","position_value", "total_value",
                                      "inception_return"])
    # total_value = cash + position_value 
    ''' CALCULATE PORTFOLIO HERE from tradingKey and prices '''
    
    return tradingKey, prices, portfolio

tradingKey, prices, portfolio = calculate_portfolio('0x41da2035ac26e4308b624a84d3caebf80a4dccf1',10000)
tradingKey.to_csv('reviewTradingKey.csv')
portfolio.to_csv('reviewPortfolio.csv')