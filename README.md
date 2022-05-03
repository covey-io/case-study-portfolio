# Case Study Intro

The purpose of this case study is build a portfolio calculator by completing the function on portfolio.py: 

calculate_portfolio(address,10000)

For the following addresses
0x41da2035ac26e4308b624a84d3caebf80a4dccf1
0x211fe601e24ce89cb443356f687c67fbf7708412


# Setup

-   Run `pip install`
-   Create virtual env `python3 -m venv env`
-   Activate virtual env `source env/bin/activate`
-   Should get an (env) in terminal
-   Then `pip install -r requirements.txt`
-   Then in the command line `python portfolio.py`

# Assumptions 
  a) For trade data use tradingKey.csv. Percent is the target percent position size. A 0 percent means closing a position. A negative percent means short. You can use leverage (i.e. 110%), ignore borrow cost and leverage costs. 
  b) For price data use prices = pd.read_csv('prices.csv')
  c) Ignore corporate actions 
  e) startCash = $10,000
  f) entry price is the next price after the entry_date associated with the trade.

# Output 
4) The output will use the pre-set columns to produce two CSVs: 
  a) CSV for trade table using pre-set columns. Don't add columns, everything you need is here.
  b) CSV for a portfolio table calculated at the same date_time intervals as prices.csv. Again, don't add columns. 
