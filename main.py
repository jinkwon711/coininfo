# 3rd party
import pickle
# my module
from utils import get_coinlist,add_site_info,add_github_info





coin_list = get_coinlist("BTC")[:5]

new_coin_list = []
for coin in coin_list:
	new_coin_list.append(add_site_info(coin))

for coin in new_coin_list:
    add_github_info(coin)

for coin in new_coin_list:
    print(coin)

# new_coin_list = []
# for coin in coin_list:
# 	new_coin_list.append(add_site_info(coin))


#save coin data as binary
# with open("./coinlist.pickle","wb") as save_f:
# 	pickle.dump(new_coin_list,save_f,protocol=pickle.HIGHEST_PROTOCOL)

# load coin data
# with open('./coinlist.pickle','rb') as load_f:
# 	data = pickle.load(load_f)










