def get_optimized_route(df):
    high_fill_bins = df[df['fill_level'] > 80].sort_values(by='fill_level', ascending=False)
    return high_fill_bins['bin_id'].tolist()
