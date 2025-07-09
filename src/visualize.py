import pandas as pd
import matplotlib.pyplot as plt

def category_pie_chart(df):
    df.groupby('label').size().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.axis('equal')
    plt.show()