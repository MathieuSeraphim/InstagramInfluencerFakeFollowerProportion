import pandas as pd
from os import listdir
from os.path import isfile, join

fileList = [f for f in listdir('./processed_data') if isfile(join('./processed_data', f))]

resultingData = pd.DataFrame(columns=['ID', 'Followers', 'Following', 'Posts', 'Is private', 'ID has number',
                                      'ID has number at end', 'ID letter ratio', 'Following/follower ratio',
                                      'Following/post ratio', 'Follower/post ratio', 'IsFake'])

for fileName in fileList:

    data = pd.read_csv('./processed_data/' + fileName)
    data['IsFake'] = False
    data.drop(['Unnamed: 0'], axis=1, inplace=True)

    print("\nFor file " + fileName + ":\n")

    for i in range(data.shape[0]):

        isFake = False
        answer = input("Is " + data['ID'][i] + " a fake account? (y/n) ")
        while answer != 'y' and answer != 'n':
            answer = input("Please input y or n: ")
        if answer == 'y':
            isFake = True

        data.at[i, 'IsFake'] = isFake
        resultingData = resultingData.append(data.loc[i], ignore_index=True)

resultingData.to_csv("./labeled_data.csv")
