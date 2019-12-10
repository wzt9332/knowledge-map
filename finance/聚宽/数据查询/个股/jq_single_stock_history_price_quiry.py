#############################################################################
# 获取股票名称对应的股票代码
#############################################################################
stock_name = '洋河股份'

# 查询指定股票名称对应的股票代码，用来调用其他函数获取数据
stocks_df = get_all_securities()
stock_code = stocks_df[stocks_df['display_name'] == stock_name].index.item()

#############################################################################
# 调用get_price()获取股价走势
#############################################################################
start_date = '2018-12-05'
end_date = '2019-12-05'
stock_price = get_price(stock_code, start_date, end_date, 'daily', 'close')
stock_price.plot(figsize=(20, 10))
