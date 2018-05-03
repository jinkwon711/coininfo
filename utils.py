from bs4 import BeautifulSoup
from time import sleep
from classes.coin import Coin
import requests

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
						item["MarketAssetCode"],
						item["BaseCurrencyCode"],
						str(item["Active"])
						)
					coinlist.append(coin)
	except:
		print("error occured",e)
	return coinlist

def add_github_info(coin):
	if coin.github == "":
	#no github info just return
		return
	html = requests.get(coin.github).text
	body = BeautifulSoup(html,"lxml").body
	numbers =[x.text.replace("\n","").strip() for x in body.find_all("span",{"class":"num text-emphasized"})]
	coin.set_github_info(*numbers)

	issue_url = coin.github+"/issues"
	html = requests.get(issue_url).text
	issue_body = BeautifulSoup(html,"lxml").body
	try:
		opened_and_closed_issues = [
			x.text.replace("\n","").split(" ")[6] 
			for x in issue_body
				.find("div",{"role":"main"})
				.find("div",{"class":"table-list-header"})
				.find_all("a")[:2]
		]
	except:
		opened_and_closed_issues = ["0","0"]
	coin.set_github_issue_info(*opened_and_closed_issues)
	return

def add_site_info(coin):
	if(coin.code=="BTC"):
		print(coin.code)
		return coin
	code = coin.code
	market = coin.market
	url = f"https://www.coinexchange.io/market/{code}/{market}"
	print(coin.name)
	print(url)
	html = requests.get(url).text
	soup = BeautifulSoup(html,"lxml")
	coinlinks = soup.find("div",{"class":"coinlinks"})
	if(coinlinks==None):
		return coin
	link_trs = coinlinks.table.find_all('tr')


	for link_tr in link_trs:
		tds = link_tr.find_all("td")

		site_name = tds[1].text.strip()
		site_link = tds[2].find("a",href=True).text
		if site_name == "Announcement":
			coin.set_announcement(site_link)
		elif site_name == "Github":
			coin.set_github(site_link)
		elif site_name == "Explorer1":
			coin.set_explore1(site_link)
		elif site_name == "explorer2":
			coin.set_explore2(site_link)
		elif site_name == "Forum":
			coin.set_forum(site_link)
		elif site_name == "Website":
			coin.set_website(site_link)
	return coin