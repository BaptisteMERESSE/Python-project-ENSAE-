import pandas as pd

data = pd.DataFrame({
    "A": [1,2,3],
    "B": ["a","b","c"]
})

data2 = pd.DataFrame({
    "A": [1,2,3],
    "C": ["e","f","g"]
})

data3 = pd.concat([data,data2], ignore_index=True)

print(data3)