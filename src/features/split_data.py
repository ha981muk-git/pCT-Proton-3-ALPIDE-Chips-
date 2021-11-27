
def get_df_of_plane(df: object, plane: int) -> object:
    result_df = df[df['id_plane'] == plane]

    return result_df

#returns a df of all hits on a single plane