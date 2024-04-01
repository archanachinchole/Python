def calculate_fd_maturity_amount():
    try:
        depo_amt = float(input("Enter the deposit amount (in INR): "))
        if depo_amt > 10000000:  # Check if deposit amount is greater than 1 crore
            raise ValueError("Deposit amount cannot be greater than 1 crore.")
        
        int_rate = float(input("Enter the interest rate (in percentage): "))
        if int_rate < 6 or int_rate > 8.5:  # Check if interest rate is between 6% and 8.5%
            raise ValueError("Interest rate should be between 6% and 8.5%.")

        mat_amt = depo_amt + (int_rate / 100 * depo_amt)
        print("Maturity amount: {:.2f} INR".format(mat_amt))
    
    except ValueError as e:
        print("Error:", e)

# Call the function to calculate FD maturity amount
calculate_fd_maturity_amount()


# if we but wrong value then say again put it 
def calculate_fd_maturity_amount():
    while True:
        try:
            depo_amt = float(input("Enter the deposit amount (in INR): "))
            if depo_amt > 10000000:  # Check if deposit amount is greater than 1 crore
                raise ValueError("Deposit amount cannot be greater than 1 crore.")
            
            int_rate = float(input("Enter the interest rate (in percentage): "))
            if int_rate < 6 or int_rate > 8.5:  # Check if interest rate is between 6% and 8.5%
                raise ValueError("Interest rate should be between 6% and 8.5%.")

            mat_amt = depo_amt + (int_rate / 100 * depo_amt)
            print("Maturity amount: {:.2f} INR".format(mat_amt))
            break  # Exit the loop if calculation is successful
        
        except ValueError as e:
            print("Error:", e)
            print("Please try again.")

# Call the function to calculate FD maturity amount
calculate_fd_maturity_amount()
