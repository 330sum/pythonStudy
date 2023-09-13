import pandas as pd

t1 = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "left_val": ["a", "b", "c", "d", "e"]
})
print(t1)

t2 = pd.DataFrame({
    "id": [3, 4, 5, 6, 7],
    "right_val": ["q", "w", "e", "r", "t"]
})
print(t2)

print("========================================")
# merge()
print(pd.merge(t1, t2))
print(pd.merge(t1, t2, on="id"))
print(pd.merge(t1, t2, left_on="left_val", right_on="right_val"))
print(pd.merge(t1, t2, how='left'))
print(pd.merge(t1, t2, how='right'))
print(pd.merge(t1, t2, how='outer'))
