#WAF that accepts a list of marks & returns the average, highest and lowest marks
def lom(m):
    avg = sum(m) / len(m)
    high = max(m)
    low = min(m)
    return avg, high, low

avg, high, low = lom([45, 67, 89, 23, 78])
print("Average:", avg, "Highest:", high, "Lowest:", low)