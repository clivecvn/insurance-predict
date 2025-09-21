import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import joblib


def main():
    data = pd.read_csv("insurance.csv")
    data.dropna(inplace=True)
    data = pd.get_dummies(data)
    data.info()
    X = data.drop(["charges"], axis=1)
    y = data["charges"]
    forest = RandomForestRegressor()
    param_grid = {
        "n_estimators": [3, 10, 30],
        "max_features": [2, 4, 6, 8],
    }
    grid_search = GridSearchCV(forest, param_grid, cv=5, return_train_score=True)
    grid_search.fit(X, y)
    print(
        grid_search.predict(
            [[18, 33.75, 1, False, True, True, False, False, False, True, False]]
        )
    )
    joblib.dump(grid_search, "forest.pkl")


if __name__ == "__main__":
    main()
