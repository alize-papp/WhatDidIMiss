# WhatDidIMiss
A movie recommender by year: didn't go a lot to the movies in 2012? Check here what you could have liked!

Some years are busier than others and sometimes at the end of the year, I notice I didn't see a lot of movies. My goal here is to create a movie recommender that recommends movie based on what you liked the other years.

## TODO:
- [X] Find dataset
- [X] Create a general purpose movie recommender on small dataset
- [X] Test movie recommender and select evaluation metrics (MAP@K, RMSE, MAE...)
- [ ] Add a filter to recommend only movies of a given year
- [ ] Adapt to new user: from notebook, ask if the user liked a bunch of movies and return recommendation
- [ ] Implement best sampling strategy to ask which movies the user saw and how they rate it
- [ ] Fine tune recommender using adapted metrics
- [ ] [Optional] Develop Dash app to use the movie recommender
- [ ] [Optional] Use PySpark to run the SVD on the large dataset
- [ ] [Optional] Interprete SVD with proper visualizations

## Resources
- Data: [https://grouplens.org/datasets/movielens/latest/](https://grouplens.org/datasets/movielens/latest/)