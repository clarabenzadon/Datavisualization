from matplotlib import pylab as plt
import pandas


df1 = pandas.read_csv("Apple.csv")
print(df1.head())
df1['Date'] = pandas.to_datetime(df2.Date)

df2 = pandas.read_csv("Google.csv")
print(df2.head())
df2['Date'] = pandas.to_datetime(df2.Date)

plt.title("Stock Comparison: Apple vs Google")


plt.plot(df1.Date, df1.Open, "b:", label="Apple", linewidth=0.5, ms=0.5)
plt.plot(df2.Date, df2.Open, "y:", label="Google", linewidth=0.5, ms=0.5)
plt.legend(loc="upper left")
plt.xlabel("Year")
plt.ylabel("Price in US Dollars")
plt.show()
