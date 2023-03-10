import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def marks_prediction(marks):
    x=pd.read_csv("Student_Marks.csv")
    y=pd.read_csv("Student_Marks.csv")

    x=x.values
    y=y.values

    plt.scatter(x,y)
    plt.xlabel("Time study")
    plt.ylabel("Marks")
    plt.show()

    model=LinearRegression()

    model.fit(x,y)

    marks=2
    x_test=np.array(marks)
    x_test=x_test.reshape((1,-1))

    return model.predict(x)[0]



