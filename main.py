# 3rd party
import pickle
# my module
from utils import get_coinlist, add_site_info, add_github_info


coin_list = get_coinlist("BTC")[:5]
attr = ["name", "code", "market", "active", "github", "website", "explorer1", "explorer2", "forum",
        "announcement", "commits", "branchs", "releases", "contributors", "opened_issues", "closed_issues"]
with open('./coinlist.csv', 'w') as f:
    f.write(",".join(attr) + "\n")
    new_coin_list = []
    for coin in coin_list:
        add_site_info(coin)
        if coin.active == "True":
            add_github_info(coin)
            f.write(str(coin) + "\n")


# save coin data as binary
# with open("./coinlist.pickle","wb") as save_f:
# 	pickle.dump(new_coin_list,save_f,protocol=pickle.HIGHEST_PROTOCOL)

# load coin data
# with open('./coinlist.pickle','rb') as load_f:
# 	data = pickle.load(load_f)
