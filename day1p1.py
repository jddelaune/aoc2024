# import dependencies
import pandas as pd

# read the input file and store it as a dataframe
input_df = pd.read_csv('day1input.txt', engine='python', sep='   ',
                       header=None, names=['left', 'right'])

# create a series for each column, sorted ascending by value
left_s = input_df.sort_values(by='left', ignore_index=True)['left']
right_s = input_df.sort_values(by='right', ignore_index=True)['right']

# create a dataframe from the two series
ordered_df = pd.concat([left_s, right_s], axis=1)

# add a column for absolute value of the difference between each pair
ordered_df['difference'] = abs(ordered_df['left'] - ordered_df['right'])

# sum the differences and print the total
sum_of_diffs = ordered_df['difference'].sum()

print(sum_of_diffs)