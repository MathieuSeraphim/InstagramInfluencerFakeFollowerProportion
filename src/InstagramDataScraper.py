# Adapted from https://www.promptcloud.com/blog/how-to-scrape-instagram-data-using-python/
# Implementation is a bit ugly - relies on analysing source code rather than using a third party scraper or an API
# A consequence of that is that while I can get the profile picture URL from said source code, I can't easily tell if
# it's the default picture or not.
# This implementation is dependant on the structure of the Instagram source code, as of June 2019.

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl


class InstagramDataScraper:

    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    # Returns an array of Instagram user characteristics. See code for more details.
    # they are estimations.
    def getInfo(self, id):

        url = 'https://www.instagram.com/' + id + '/?hl=en'

        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        data = soup.find_all('meta', attrs={'property': 'og:description'})[0].get('content').split()
        accountIsPrivate = str(soup.find_all('script')).find('"is_private":true')

        if accountIsPrivate == -1:
            accountIsPrivate = False
        else:
            accountIsPrivate = True

        numbers = [data[0], data[2], data[4]]

        multiplier = 1
        for i in range(len(numbers)):
            multiplier = 1
            numbers[i] = numbers[i].replace(',', '')
            if numbers[i][-1] == 'm':
                numbers[i] = numbers[i][:-1]
                multiplier = 1000000
            elif numbers[i][-1] == 'k':
                numbers[i] = numbers[i][:-1]
                multiplier = 1000
            numbers[i] = int(float(numbers[i]) * multiplier)

        nbOfFollowers = numbers[0]
        nbOfFollowing = numbers[1]
        nbOfPosts = numbers[2]

        idHasNumber = any(char.isdigit() for char in id)
        idHasNumberAtEnd = id[-1].isdigit()

        letterCounter = 0
        for i in range(len(id)):
            letterCounter += id[i].isalpha()
        idLetterRatio = float(letterCounter) / len(id)

        if nbOfFollowers == 0:
            followingFollowerRatio = float('Inf')
        else:
            followingFollowerRatio = float(nbOfFollowing) / nbOfFollowers
        if nbOfPosts == 0:
            followerPostRatio = float('Inf')  # still inf even if no followers
            followingPostRatio = float('Inf')
        else:
            followingPostRatio = float(nbOfFollowing) / nbOfPosts
            followerPostRatio = float(nbOfFollowers) / nbOfPosts

        return [id, nbOfFollowers, nbOfFollowing, nbOfPosts, accountIsPrivate, idHasNumber, idHasNumberAtEnd,
                idLetterRatio, followingFollowerRatio, followingPostRatio, followerPostRatio]
