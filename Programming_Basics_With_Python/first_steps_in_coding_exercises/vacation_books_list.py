pagesCount = int(input())
pagesPH = int(input())
readingDays = int(input())
hours = int((pagesCount / pagesPH) // readingDays)
print(hours)