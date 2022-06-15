def check_prime(number):

    """

    Prints out if the number is prime or not

    """

    flag = False

    if number == 0 or number == 1 or number < 0:

        print(f"{number} is not prime number")

    else:

        for check_number in range(2, 1+number//2):

            if number % check_number == 0:

                print(f"{number} is not prime number")
                flag = True

                break

 

        if not flag:

            print(f"{number} is prime number")
			
			
		
check_prime(31)

