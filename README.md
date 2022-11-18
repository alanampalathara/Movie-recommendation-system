# Movie-recommendation-system
A movie recommendation system, also known as a movie recommender system, uses machine learning (ML) to predict or filter users' film preferences based on their prior decisions and actions.
Movie recommendation systems' main objective is to identify and forecast only those films that a corresponding user is most likely to be interested in watching. The user information from the system's database is used by the ML algorithms for these recommendation systems. Based on information from the past, this data is used to forecast the user in question's behaviour in the future.
### Aim of the project
To create a movie recommendation system using machine learning techniques and to create a graphical user interface through which users can access the model and be recommended movies based on their favourite movies.
### Dataset used
The dataset used for this project is called MovieLens 1M Dataset. It contains 1,000,209 anonymous ratings of approximately 3,900 movies 
made by 6,040 MovieLens users who joined MovieLens in 2000.
https://grouplens.org/datasets/movielens/1m/
### Modeling and Analysis
For the model, we have used cosine function and nearest neighbour function to determine which movies would be closely related to the movie selected by the user. The idea behind nearest neighbour approaches is to select a set number of training samples that are geographically closest to the new point and then estimate the label based on them. Regardless of the size of the documents, Cosine similarity is a metric used in NLP to evaluate how similar they are. The movies that have been previously selected by the user are saved into a list and a separate list of movies is also recommended from the history list.
### User Interface
A user interface is created using streamlit which is a framework for creating and deploying interactive data science dashboards and machine learning models that is open source and based on Python. 

![ui2](https://user-images.githubusercontent.com/39832668/202753257-43a6758a-b755-4505-af93-f3ec44306826.png)

The UI contains a drop box which contains all the names of the images from the movielens dataset from which the user can select a movie movie which he/she likes and then if they click on a "Recommend" button which is situated below the drop box, the model we created will run in the backend and 5 movie names related to the movie selected by the user will be displayed.

![ui1](https://user-images.githubusercontent.com/39832668/202753358-67881e6a-3639-4d6b-bd21-3e24827ad498.png)

After the user selects the second movie, the column named "Recommended movies from history" will show 5 different movies that are close to the movies that the user selected in the past.
