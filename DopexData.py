"""
DOPEX API // decentralized option data // https://www.dopex.io/
https://github.com/dopex-io/dopex-api/blob/master/docs/v1/ENDPOINTS.md
@author: adam fisher
"""

# import modules
import pandas as pd
import requests
# import time
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.offline import plot
# import numpy as np
import datetime as dt
import json

"""
GET SSOV DATA // API V2
"""

# build url for SSOVs 
url = 'https://api.dopex.io/api/v2/ssov'

# make get request
res = requests.get(url)

# convert to dataframe // the column name is the chainId
dfSSOV = pd.read_json(res.text)

# expand dictionaries to columns
dfSSOV = dfSSOV[dfSSOV.columns[0]].apply(pd.Series)

# review columns 
print(dfSSOV.columns)

# review values
for i in dfSSOV.columns:
    print(i)
    print('- ' * 9)
    print(dfSSOV[i])
    print('- ' * 9)

# review assets that SSOVs are available for
symbols = list(dfSSOV.symbol)
print(symbols)

# SSOV contract address (???)
print(dfSSOV.address)

# navigating rewards
print(dfSSOV.rewards)
print(dfSSOV.rewards[0])
print(dfSSOV.rewards[0][0])
print(dfSSOV.rewards[0][0]['amount'])
print(dfSSOV.rewards[0][0]['amount']['hex'])

# navigating epoch times
print(dfSSOV.epochTimes)
print(dfSSOV.epochTimes[0])
print(dfSSOV.epochTimes[0]['expiry'])
dtStart = dt.datetime.fromtimestamp(int(dfSSOV.epochTimes[0]['expiry']))
print(dtStart)

# # duration of vault epoch
# print(dfSSOV.duration)

# # is vault retired
# print(dfSSOV.retired)

# # SSOV contract address (???)
# print(dfSSOV.address)

# # total value locked per SSOV
# print(dfSSOV.tvl)

# # get APY metric 
# print(dfSSOV.apy)

# # underlying prices
# print(dfSSOV.underlyingPrice)

"""
GET APY DATA // API V2
"""

# assign SSOV symbol
ssovSymbol = dfSSOV.symbol[0]

# build url for APYs with option type
url = f'https://api.dopex.io/api/v2/ssov/apy?symbol={ssovSymbol}'
# make get request
res = requests.get(url)

# convert response to dictionary
apyData = json.loads(res.text)

#review keys
print(apyData['apy'])

"""
GET IR VAULT DATA // API V2 // NO DICE
"""

# build url for APYs with option type
url = 'https://api.dopex.io/api/v2/rateVaults'

# make get request
res = requests.get(url)

"""
GET STRADDLE DATA // API V2
"""

# build url for APYs
url = 'https://api.dopex.io/api/v2/straddles'

# make get request
res = requests.get(url)

# convert response to dictionary
straddleData = json.loads(res.text)

#review keys // navigating data structure
straddleData.keys()
list(straddleData.keys())[0]
straddleData[list(straddleData.keys())[0]]
straddleData[list(straddleData.keys())[0]][0]

"""
GET FARM TVL DATA // API V2
"""

farmName = 'dpx-weth' # 'rdpx-weth'

# build url for Farm TVL per pool
url = f'https://api.dopex.io/api/v2/farms?pool={farmName}'
    
# make get request
res = requests.get(url)

# convert to dataframe 
farmTVL = json.loads(res.text)

print(farmTVL)

"""
GET AVAILABLE TOKENS FOR PRICE DATA // API V2
"""

# build url for current token price
url = 'https://api.dopex.io/api/v2/price'
    
# make get request
res = requests.get(url)

# convert to dataframe 
availableTokens = json.loads(res.text)
tokenData = pd.DataFrame(availableTokens['supportedTokens'])

"""
GET TOKEN PRICE DATA // API V2
"""

# assign token
token = tokenData.symbol[0]

# build url for current token price
url = f'https://api.dopex.io/v2/price/{token}'
    
# make get request
res = requests.get(url)

# prices + oracle type
print(json.loads(res.text))

"""
GET TOKEN SUPPLY DATA // API V1
"""

# dpx
assetSymbol = dfSSOV.underlyingSymbol[0]

# build url for current token supply
url = f'https://api.dopex.io/api/v1/{assetSymbol.lower()}/supply'
    
# make get request
res = requests.get(url)

# convert to dataframe 
tokenSupply = json.loads(res.text)

print(tokenSupply)

"""
GET TOKEN MARKET CAP DATA // API V1
"""

# build url for current token mkt cap
url = f'https://api.dopex.io/api/v1/{assetSymbol.lower()}/market-cap'
    
# make get request
res = requests.get(url)

# convert to dataframe 
mktCap = json.loads(res.text)

print(mktCap)

"""
GET DEPOSIT DATA // API V1 // EMPTY
"""

# dpx
assetSymbol = dfSSOV.underlyingSymbol[0]

# assign option type
optionType = 'CALL' # 'PUT'

# build url for SSOV deposits 
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'deposits?asset={assetSymbol}&type={optionType}'
)    

# make get request
res = requests.get(url)

# convert to dataframe
deposits = pd.read_json(res.text)

print(deposits)

"""
GET OPTION PRICE DATA // API V1 // EMPTY
"""

# build url for SSOV option prices
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'options/prices?asset={assetSymbol}&type={optionType}'
)    

# make get request
res = requests.get(url)

# convert to dataframe 
optionPrices = pd.read_json(res.text)

print(optionPrices)

"""
GET OPTION USAGE DATA // API V1 // EMPTY
"""

# build url for SSOV option usage
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'options/usage?asset={assetSymbol}&type={optionType}'
)    

# make get request
res = requests.get(url)

# convert to dataframe 
optionUsage = pd.read_json(res.text)

print(optionUsage)

"""
GET TVL DATA // API V1 // EMPTY
"""

# build url for TVL
url = 'https://api.dopex.io/api/v1/tvl'
# url = 'https://api.dopex.io/api/v1/tvl?include=dpx-ssov,eth-ssov'
# url = (
    # f'https://api.dopex.io/api/v1/tvl?'
    # f'include=dpx-farm,rdpx-farm,dpx-weth-farm,'
    # f'rdpx-weth-farm,dpx-ssov,rdpx-ssov'
# )
    
# make get request
res = requests.get(url)

# convert to dataframe 
allTVL = json.loads(res.text)

print(allTVL)
