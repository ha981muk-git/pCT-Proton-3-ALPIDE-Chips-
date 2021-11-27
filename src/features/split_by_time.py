
def split_df(df: object) -> list:

    different_timestamps = df['i_time_stamp'].unique()
    list_of_df = list()
    for val in different_timestamps:
        list_of_df.append(df[df['i_time_stamp'] == val])

    return list_of_df


#creates a list of df that contains the hits split by timestamp