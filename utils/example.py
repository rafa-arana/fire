

def create_csv():
    my_function(3.4)


def my_function(x):
    """
    We want x to get squared
    """
    if not isinstance(x, int) and not isinstance(x, float):
        print("got an error, oops, do nothing")
        return

    # comment
    new_x = x * x
    print(f"{x} became {new_x}")
    write_result_to_csv(new_x, x)

def write_result_to_csv(new_x, x):
    # create csv file, write to the same folder
    with open("my_new_file.csv", "w+") as file:
        file.write("original,new value,description,\n")
        file.write(f"{x},{new_x},it is squared!,\n")

def mytest():
    my_function(3)
    my_function(3.4)
    my_function("sarah")

if __name__ == "__main__":
    mytest()
    create_csv()
