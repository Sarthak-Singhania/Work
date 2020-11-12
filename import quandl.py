import quandl
quandl.ApiConfig.api_key='Ur4Nnmc1XjCBQ3aUCyzz'
df=quandl.get('BSE/BOM500180')
print(df)