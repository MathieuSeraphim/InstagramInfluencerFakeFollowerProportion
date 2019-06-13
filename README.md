# InstagramInfluencerFakeFollowerProportion
Project dedicated to determine the "fake" follower proportion of any given Instagram influencer.

This program is primarily an exercise, not a serious project. As such, the different parts of this README will correspond to chronological steps, and a method used in a specific step may be found to have been less than optimal in a later step.
All this will be reported in the "chronological step" where it was discovered

## The idea:

Social network influencers tend to have "fake" followers, accounts created solely to add to follower counts without engaging with said influencers.
Some influencers pay directly for such followers to a specialized service, while others do not and still end up with them (see https://www.youtube.com/watch?v=oVfHeWTKjag).
In either case, the result is the same: a significant number of the influencer's followers do not consume said influencer's content, making them less effective brand advocates.

I aim to create a classification tool able to give the proportion of these "fake" followers, for any given Instagram influencer, by replicating and adapting the process made by journalists of the swiss media group SRF (https://srfdata.github.io/2017-10-instagram-influencers/).
I will be using different tools than them, mainly because I will develop my program in Python, while they used the R programming language.

## The original plan:

1. Scrape and process data from public and private Instagram accounts.
2. Extract data from 500 accounts and manually label them real or fake.
   * The number "500" was arbitrarily chosen, and might not be enough to provide good results. But manual labeling being time-consuming, the number couldn't be too high.
3. Train a classification ML algorithm to detect fake accounts. Tweak hyperparameters for optimal results.
4. Repeat for multiple other classification algorithms, and keep the best performing.
5. Determine the fake follower proportion of a few Instagram influencers. Compare the obtained values with data from articles found online (such as this one: https://www.meltwater.com/uk/blog/influencer-fraud/).
6. If needed, wrap all this in one easy-to-use program.

## The collection of Instagram data

This part is divided into multiple classes:

### Scraping the metadata of a given Instagram account, public or private

This is done using the InstagramDataScraper class of the scraper module.

Given an instagram user's ID, the getInfo method returns an array of information on said user.
The array contains:
* The Instagram user's ID (again) - String
* The number of followers the user has - Integer, approximation if the number is big (>10000)
* The number of other users the user's following - Integer, approximation if the number is big
* The total number of posts from the user* The total number of posts from the user - Integer, approximation if the number is big
* If the user's account is private - Boolean
* If the user's ID contains a number - Boolean
* If the user's account countains a number specifically at the end of the string  - Boolean
* The user's ID's letter ratio (number of alphabetical symbols / total number of symbols in the string) - Floating point number
* The user's following-to-follower ratio - Floating point number, may be infinite
* The user's following-to-number of posts ratio - Floating point number, may be infinite
* The user's follower-to-number of posts ratio - Floating point number, may be infinite

The data is obtained by parsing the Instagram source code. If the source code format changes significantly compared to the current format at the time of writing, this class may not function anymore.

### Collecting and processing follower data

To extract a list of Instagram followers for a given public account, I used the Google Chrome extension "Helper Tools for Instagram" (HTfI, https://chrome.google.com/webstore/detail/helper-tools-for-instagra/hcdbfckhdcpepllecbkaaojfgipnpbpb).

This extension needs an Instagram account to function, and is only usable through the browser, limiting automation. It can, however, provide all the information that is scraped through the InstagramDaraScraper class, rendering it mostly useless.

I have decided to not extract too much data with the HTfI extension, and to keep using the InstagramDataScraper class for most of the work. If this project is to be integrated into a real product, I would advise to find an alternative to both these tools usable through Python, or another programming language.

The extracted data can be found in the extracted_data folder, and through execution of the preprocess_followers.py script, new .csv files will appear in the processed_data folder..