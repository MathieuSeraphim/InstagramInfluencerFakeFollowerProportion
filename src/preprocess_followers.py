import pandas as pd
from os import listdir
from os.path import isfile, join
from InstagramDataScraper import InstagramDataScraper


fileList = [f for f in listdir('./extracted_data') if isfile(join('./extracted_data', f))]

scraper = InstagramDataScraper()

for fileName in fileList:

    data = pd.read_csv('./extracted_data/' + fileName)
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

    followerData.to_csv('./processed_data/' + fileName)
    print('File ' + fileName + " successfully processed.")
