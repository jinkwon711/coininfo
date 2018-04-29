import bs4
import requests


class Coin():
	def __init__(self,name,code,market,active):
		self.name = name
		self.code = code
		self.market = market
		self.active = active

	def url_item(self):
		return f"{self.code}/{self.market}"

def get_html(url):
	response = requests.get(url)
	return response.text



def get_coinlist(market="ALL"):
	if market not in ["BTC","ETH","DOGE","ETC","LTC","ALL"]:
		print(f"{market} market does not exist")
	coinlist= []
	response = requests.get("https://www.coinexchange.io/api/v1/getmarkets")
	json_data = response.json()
	try:
		if json_data["message"]=="":
			for item in json_data["result"]:
				if item["BaseCurrencyCode"] in [market,"ALL"]:
					coin = Coin(
						item["MarketAssetName"],
						item["BaseCurrencyCode"],
						item["BaseCurrencyCode"],
						item["Active"]
						)
					coinlist.append(coin)
	except e:
		print("error occured",e)
	return coinlist


