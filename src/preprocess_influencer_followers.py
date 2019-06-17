import pandas as pd
from InstagramDataScraper import InstagramDataScraper
import sys
from time import sleep


if len(sys.argv) != 2:
    print("There must be ONE argument: the name of a .csv file in the influencer_data folder..")
    sys.exit()

fileName = sys.argv[1]

scraper = InstagramDataScraper()


data = pd.read_csv('./influencer_data/' + fileName)
usernames = data['username']
columns = ['ID', 'Followers', 'Following', 'Posts', 'Is private', 'ID has number', 'ID has number at end',
           'ID letter ratio', 'Following/follower ratio', 'Following/post ratio', 'Follower/post ratio']
followerData = pd.DataFrame(columns=columns)
for username in usernames:
    try:
        entry = scraper.getInfo(username)
        followerData.loc[len(followerData)] = entry
    except Exception:
        print("Error for ", username)
        sleep(120)  # Sometimes, there will be multiple errors in a row. This seems to fix it.

followerData.to_csv('./data_ready_for_analysis.csv')
print('File ' + fileName + " successfully processed.")
