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

# create a series with counts of how many times each value in the right column appears
unique_s = ordered_df['right'].value_counts()

# add a column to the dataframe for the count of how many times each left value appears on the right
ordered_df['counts'] = ordered_df['left'].map(lambda x: unique_s.get(x))

# replace null values with 0
ordered_df.fillna(0, inplace=True)

# the 'similarity score is: value * number of times that value appears in right list
# add a column for the similarity score

ordered_df['sim_score'] = ordered_df['left'] * ordered_df['counts']

# add the similarity scores and print the result
sum_of_sim_scores = ordered_df['sim_score'].sum()

print(sum_of_sim_scores)


