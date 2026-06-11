import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

import stores


#TODO: Potentially implement "cities" where locations are clustered and similar brands aren't in the same city
    #TODO: Maybe include a markup per city in addition to or in place of locational markups

def main():
    num_stores = 1000
    brands = ["Brand A", "Brand B", "Brand C"]
    brand_markups = {}
    stores_list = []
    regions = 10

    mean_individual_markup = 2
    std_individual_markup = 1

    min_store_markup = 15

    # Generate brank markups
    for i in range(len(brands)):
        brand_markups[brands[i]] = np.random.lognormal(mean_individual_markup, std_individual_markup)




    # Generate stores
    for i in range(num_stores):
        # Old Location generation, uniformly random
        location = (random.uniform(0, 1), random.uniform(0, 1))

        # New location generation random with clustering
       




        brand = random.choice(brands)
        individual_markup = np.random.lognormal(mean_individual_markup, std_individual_markup) + min_store_markup
        store = stores.retail_store(location, brand, individual_markup)
        stores_list.append(store)

    '''
    # Visualize markups
    X = []
    Y = []
    for store_place in stores_list:
        X.append(store_place.location[0])
        Y.append(store_place.location[1])
    '''
        


    # Generate 4 clusters of 50 points each
    X, y = make_blobs(n_samples=num_stores, centers=regions, n_features=2, cluster_std=0.05, center_box=(0,1))
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.title("Randomly Generated Clusters")
    plt.show()



if __name__ == "__main__":
    main()