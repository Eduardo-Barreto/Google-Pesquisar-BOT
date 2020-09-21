import pyshorteners

s = pyshorteners.Shortener()
print(s.tinyurl.short('http://www.g1.com.br'))