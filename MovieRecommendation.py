
import pandas as pd

dataset=pd.read_csv("movies.csv")

dataset.head(4)

dataset.info()

meanvote=dataset['vote_average'].mean()
print(round(meanvote,2))

minimumvote=dataset['vote_count'].quantile(0.50)
print(round(minimumvote,2))

q_movies=dataset.copy().loc[dataset['vote_count']>=minimumvote]
q_movies.shape

def weighted_rating(x,minimumvote=minimumvote,meanvote=meanvote):
    voters=x['vote_count']
    avg_vote=x['vote_average']
    return(voters/(voters+minimumvote)*avg_vote + 
       (minimumvote/(minimumvote+voters)*meanvote))
       
       
q_movies['score']=q_movies.apply(weighted_rating,axis=1)
q_movies=q_movies.sort_values('score',ascending=False)

pd.set_option('precision',2)
q_movies[['title','vote_count','vote_average','score']].head(20)

