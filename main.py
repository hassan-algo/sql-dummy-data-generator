from random import seed
from random import randint
import uuid

# seed random number generator
seed(1)


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random strin


table = input("Enter the table name: ")
numberOfRows = int(input("Enter the number of row you want: "))
numberOfColumn = int(input("Enter number of columns you want: "))
column = []
columntype = []
for i in range(numberOfColumn):
    columnname = str(input(f"Enter {i + 1} column name: "))
    column.append(columnname)
    type = str(input(f"Enter the type of '{column[i]}' str/guid/int or s/g/i"))
    columntype.append(type)
file = open(r"./output.txt", "w+")
for i in range(numberOfRows):
    str1 = f"INSERT INTO {table} ("
    for j in range(numberOfColumn):
        str1 += f"{column[j]}, "
    str1 = str1[:-2]
    str1 += ") VALUES ("
    for j in range(numberOfColumn):
        if columntype[j] == "str" or columntype[j] == "s":
            str1 += f"'{my_random_string(6)}', "
        elif columntype[j] == "guid" or columntype[j] == "g":
            str1 += f"'{str(uuid.uuid4())}', "
        else:
            str1 += f"'{randint(1, 100)}', "
    str1 = str1[:-2]
    str1 += ");\n"
    file.write(str1)

file.close()
