# InstagramInfluencerFakeFollowerProportion
Project dedicated to determine the "fake" follower proportion of any given Instagram influencer.

## The idea:

Social network influencers tend to have "fake" followers, accounts created solely to add to follower counts without engaging with said influencers.
Some influencers pay directly for such followers to a specialized service, while others do not and still end up with them (see https://www.youtube.com/watch?v=oVfHeWTKjag).
In either case, the result is the same: a significant number of the influencer's followers do not consume said influencer's content, making them less effective brand advocates.

I aim to create a classification tool able to give the proportion of these "fake" followers, for any given Instagram influencer, by replicating and adapting the process made by journalists of the swiss media group SRF (https://srfdata.github.io/2017-10-instagram-influencers/).
I will be using different tools than them, mainly because I will develop my program in Python, while they used the R programming language.


## The plan:

1. Scrap and process data from public and private Instagram accounts.
2. Extract data from 500 accounts and manually label them real or fake.
   * The number "500" was arbitrarily chosen, and might not be enough to provide good results. But manual labeling being time-consuming, the number couldn't be too high.
3. Train a classification ML algorithm to detect fake accounts. Tweak hyperparameters for optimal results.
4. Repeat for multiple other classification algorithms, and keep the best performing.
5. Determine the fake follower proportion of a few Instagram influencers. Compare the obtained values with data from articles found online (such as this one: https://www.meltwater.com/uk/blog/influencer-fraud/).
6. If needed, wrap all this in one easy-to-use program.
