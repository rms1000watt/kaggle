# Playing with https://www.kaggle.com/zlatankr/titanic/titanic-random-forest-82-78

import os
import ryan
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ignore: 1
def main():
    # Import data
    test = pd.read_csv(os.path.join(FILE_DIR, 'test.csv'))
    train = pd.read_csv(os.path.join(FILE_DIR, 'train.csv'))

    # View data
    # print train.info()
    # print train.head()
    print train['Survived'].value_counts(normalize=True)

    # Plot survivors
    sns.countplot(train['Survived'])

# Ignore: 2
if __name__ == '__main__':
    main()
