print("question 1")
import pandas as pd

data = {'Name': ['Aarushi', 'Rubal', 'Sanju'], 'Age': [19, 20, 21],
        'mail_id': ['Aarushi048@gmail.com', 'rubal34@gmail.com', 'sanyogitasingh@gmail.com'],
        'phone_no': [8284826399, 9689564369, 9876542309]}
df = pd.DataFrame(data, index=[1, 2, 3])
print(df)

# Q2
print("question 2")
a = pd.read_csv("test.csv")
df = pd.DataFrame(a)
# a.
print("part a")
print(df.head(5))

# b.
print("part b")
print(df.head(10))

# c.
print("part c")
print(df.axes)
print(df.T)

# d.
print("part d")
print(df.tail(5))


# e.
b = pd.read_csv("test.csv")
df = pd.DataFrame(b, index=[1])
print(df.head)
print(df.axes)
print(df.shape)
print(df['MinTemp'].head)
print(df['MinTemp'].dtypes)
print(df['MinTemp'].shape)