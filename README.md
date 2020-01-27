# Football Hypothesis Testing

Goals
* Create four hypotheses based on our research on the football myths
* Collect relevant data based on our hypothesis
* Conduct data cleaning and exploratory data analysis
* Sampling the data and perform appropriate t-tests to the data samples 
* Analyse t-test results and make decisions on the null hypothesis 
* Make conclusions and create a presention on our findings

Summary of files

data_cleaning.py: Includes functions that perform the following tasks;
* Deleting rows with null values and duplicated rows
* Deleting brackts from the object columns 
* Changing column names in lowercase and deleting white spaces  

hypothesis_test.py: Includes functions that perform the following tasks;
* Creates random samples from data set 
* Creates a visualisation of a t-distribution, with lines for t-statistic and critical t-value
* Calculates the degrees of freedom that go into a welch's t-test
* Calculates Cohen's d 

hypothesis_testing.ipynb: Includes the examining of the four hypotheses based on the most common myths surrounding the results of football matches

visualizations.py: Includes functions that perform the following tasks;
* Creates a visualisation of a overlapping density plot
* Creates a boxplot 

Premier League 2018.pdf: Powerpoint on the statistical results from the hypothesis testing

Football_players_age_and_minutes.csv: Includes the columns with the values about players age and played minutes on the field, used for the second hypothesis.

Football_players_by_nationality_and_goals.csv: Includes the columns about players nationality, number of goals and their position on the field, used for the 4th hypothesis.



This repo contains:
* Description of the project in a PDF
* Three python starter files
* Three test files
* A starter jupyter notebook
* Our main anaylisis takes place in the hypothesis_testing.ipynb

Datasets used:
* https://www.football-data.org/documentation/api - Football Data API for information about premier league matches 2018/2019
* https://footystats.org/ - The free version of the footystats API for player information for the premier 2018/2018 season
* https://datahub.io/sports-data/english-premier-league - Additional match information pulled from csv

Hypotheses to be tested:

1. Is a team more likely to win playing at home?
    * $H_0$: There is no relationship between the team's home and away match performance.
    * $H_1$: A team is significantly more likely to win if they play at home.
  
2. Is there a relationship between the age of a player and the minutes that the player plays?
    * $H_0$: There is no relationship between a player's age and the minutes that a player plays in a season.
    * $H_1$: A player is significantly more likely to play more minutes if they are older.

3. If there are more cards in a game, are there more goals scored?
    * We create a ratio for each match between the goals scored and the number of cards in a match.
    * $H_0$: There is no significant reltationship between the number of cards in a game and the number of goals scored. 
    * $H_1$: If the if there are more cards in a game, it significantly more probable that there will be more goals.
    * $h_2$: If there are more cards in a game, it is significantly less probably that there will be more goals. 

4. If a team is winning at half time are they more likely to win at full-time
    * $H_0$: A team is no more likely to win the game if they are leading at half time.
    * $H_1$: A team is more likely to win the game outright if they are leading at half time.
    * $H_2$: A team is less likely to win the game outright if they are leading at half time.
