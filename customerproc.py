import PersonClass as p

def main():
    person = p.Person("jane doe", "1 Bear Pl", "806-335-6987")
    person.print_person()
    customer = p.Customer("806-335-6987", True ,"jane doe", "1 Bear Pl",1 )

    print()
    customer.print_person()

main()
