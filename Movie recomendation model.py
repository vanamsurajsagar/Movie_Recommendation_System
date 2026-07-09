import numpy as np

# User input
print("Enter your preferences (scale -5 to +5)")
action = int(input("Action: "))
comedy = int(input("Comedy: "))
suspense = int(input("Suspense: "))

user = np.array([action, comedy, suspense])

# Movie database
movies = {
    "Movie 1": np.array([2,1,3]),
    "Movie 2": np.array([5,1,4]),
    "Movie 3": np.array([1,2,1]),
    "Movie 4": np.array([-1,2,-2]),
    "Movie 5": np.array([2,4,2])
}

# Find closest movie using Euclidean distance
best_movie = None
min_distance = float('inf')

for name, vector in movies.items():
    distance = np.linalg.norm(user - vector)
    print(f"{name} distance: {distance:.2f}")
    
    if distance < min_distance:
        min_distance = distance
        best_movie = name

print("\nRecommended Movie:", best_movie)
