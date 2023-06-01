import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load data
data = pd.read_csv('product_data.csv')

# Create a pivot table to represent user-product interactions
pivot = pd.pivot_table(data, values='rating', index='user_id', columns='product_id')

# Use k-NN to find the most similar users
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(pivot)

def recommend_products(user_id, k):
    distances, indices = model.kneighbors(pivot.loc[user_id].values.reshape(1, -1), n_neighbors=k+1)
    recommended = []
    for i in range(1, len(distances.flatten())):
        product_id = pivot.index[indices.flatten()[i]]
        rating = pivot.iloc[user_id][product_id]
        recommended.append((product_id, rating))
    return recommended

# Example usage
recommendations = recommend_products(1, 5)
print(recommendations)
