months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def get_input():
    data = input("Enter 12 numbers:")
    return data

def check_data(data):
    numbers = data.split()
    
    if len(numbers) > 12:
        print("You need enter 12 numbers")
        return None

    rainfall=[]

    for i in numbers:
        try:
            rainfall.append(float(i))
        except:
            print("You need enter numbers")
            return None
        
    return rainfall

def calculate(rainfall):
    total = sum(rainfall)
    avarage = total / 12
    max_value = max(rainfall)
    min_value = min(rainfall)
    max_index = rainfall.index(max_value)
    min_index = rainfall.index(min_value)

    return (total, avarage, (max_value, months[max_index]),(min_value, months[min_index]))

def output(result):
    print(result)


def main():
    info = get_input()
    rainfall = check_data(info)

    result = calculate(rainfall)
    output(result)

def output(result):
    print(result)

main()