import numpy as np

1
###price change后一天-前一天
# prices=np.array([101,102,101,105])
# print(np.diff(prices))


2
###累计利润
# prices=np.array([101,-102,-101,105])
# print(np.cumsum(prices))


3
###where函数
# prices=np.array([101,102,101,105])
# print(np.where(prices > 102, 1, 0))#大于102显示1，小于102显示0


4
###small project
prices=np.array([100,
                 102,
                 101,
                 105,
                 108,
                 107,
                 110])
# print('Maximum price:', np.max(prices))
# print('Minimum price:', np.min(prices))
# print('Mean price:', np.mean(prices))
# print('Standard deviation:', np.std(prices))
# print('Price changes:', np.diff(prices))
# print('Recommendation:', np.where(prices>105, "buy", "sell"))#大于105显示buy，小于105显示sell

5
###stock analysis functions
def daily_return(prices):
    return np.diff(prices) / prices[:-1]

def volatility(prices):
    return np.std(daily_return(prices))

def sharpe_ratio(prices):
    return np.mean(daily_return(prices)) / volatility(prices)

def buy_or_sell(daliy_return):
    return np.where(daliy_return > 0.02 "buy", "sell")

def max_drawdown(prices):
    cumulative_max = np.maximum.accumulate(prices)#找到每一天之前的历史最高值
    drawdown = (cumulative_max - prices) / cumulative_max
    return np.max(drawdown)