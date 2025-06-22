import pandas as pd
import random

def generate_bin_data():
    bins = []
    for i in range(10):
        bins.append({
            'bin_id': f'Bin-{i+1}',
            'lat': 12.9 + random.uniform(0.01, 0.05),
            'lon': 77.6 + random.uniform(0.01, 0.05),
            'fill_level': random.randint(20, 100)
        })
    return pd.DataFrame(bins)
