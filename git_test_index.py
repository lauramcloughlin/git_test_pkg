import pandas as pd

# Read file into pandas using a relative path and set column names
def read_data(path):
    data = pd.read_csv(path, header=None, names=['text', 'label'], sep='\t', encoding = 'unicode_escape')
    return data

# Function to identify labels values
def get_label_values(label_column):
    label_values = label_column.unique()
    return label_values

# Function to set label if label does not already contain 0 and 1
# Depending on the dataset - score is either 1(for positive) or 0 (for negative)
def set_label(data):
    # convert label to a numerical variable
    label_values = get_label_values(data['label'])
    binary_labels = [0,1]
    if (all(i in binary_labels for i in label_values)) == False:
        data['label_name'] = data['label']
        data['label'] = data.label.map({label_values.item(0): 0, label_values.item(1): 1})
    return data

# Prompts user to enter path to data
def input_data_path():
    datafile_path = input('Enter the relative path to data?: ')
    return datafile_path

def main():
    print("Welcome to Text Misclassification Analysis")
    print("Please enter valid input (or default values will be used)")
    path = input_data_path()
    data = read_data(path)
    data = set_label(data)
    print(data)