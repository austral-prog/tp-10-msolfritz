def find_max_value(dict):
    a = ""
    max = 0
    for keys ,values in dict.items():
        if  values > max :
            max = values
            a = keys
    return a
print(find_max_value({"juan": 85, "emma": 95, "sophia":55}))

def reverse_dict(dict):
    a = {}
    for k, v in dict.items():
        if v in a:
            a[v] += k
        else:
            a[v]=k
    return a 
print(reverse_dict({"a":1, "b":2, "c":3, "d":3, "e":2}))


def word_freq_counter(string):
    d= dict()
    for word in string:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
print(word_freq_counter(["apple", "banana", "apple", "orange", "banana", "apple"]))


def find_biggest_expense(dict):
    answer=('', 0) 
    for key, value in dict.items():
        average=0
        for i in value:
            average +=i
        average= average/len(value)             
        if answer[1] < average:                     
            answer=(key, average)                
    return answer[0]                              

print(find_biggest_expense({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]}))


def sum_of_expenses(dic):
    a = {}
    for clave,valor in dic.items():
        suma=0
        for nro in valor:
            suma+= nro
            a[clave]=suma
    return a
print(sum_of_expenses({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]}))


def sum_of_expenses_by_type(dict):
    ans={}
    for k, v in dict.items():
        for type, expense in v:
            if type in ans:
                ans[type]+= expense
            else:
                ans[type]= expense

    return ans
print(sum_of_expenses_by_type({'Food': [("A", 60), ("B", 100), ("A", 20)], 'Transport': [("A", 10), ("B", 50), ("C", 5)], 'Games': [("A", 6), ("B", 24), ("C", 99)]}))
