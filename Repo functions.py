import pandas as pd


def normalized(data):
    """Calculates the z score between two data sets"""
    mean = data.mean()
    sd = data.std()
    score = (data - mean) / sd
    return score


def column_scaler(data):
    """
    Scales each column in the dataset
    """
    new_data = pd.DataFrame()
    for value in data.columns:
        column_data = data[value]
        new_data[value] = normalized(column_data)
    return new_data


def correlation(dataset, threshold):
    """
    Remove columns that do exceeed correlation threshold
    """
    col_corr = set()  # Set of all the names of deleted columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j] >= threshold) and (corr_matrix.columns[j] not in col_corr):
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
                if colname in dataset.columns:
                    del dataset[colname]  # deleting the column from the dataset
    return dataset


def PCA_Col_names(count):
    colname = []
    rowname = 1
    while rowname <= count:
        colname.append(f'Principle Component {rowname}')
        rowname += 1
    return (colname)


# consolidate outlier
def consolodate_outliers(labels, threshold):
    new_labels = []
    for i in labels:
        if i == threshold:
            new_labels.append('Normal')
        else:
            new_labels.append('Outlier')

    count = np.unique(new_labels, return_counts = True)
    return new_labels, pd.DataFrame(count)
