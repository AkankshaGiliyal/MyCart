def format_test_cases(test_cases):
    max_test_case_length = max(len(str(case_number)) for case_number in range(1, len(test_cases) + 1))
    max_input_length = max(len(str(case['input'])) for case in test_cases)
    max_output_length = max(len(str(case['expected_output'])) for case in test_cases)
    max_result_length = max(len(str(case['result'])) for case in test_cases)

    header = f"| {'Test Case':<{max_test_case_length}} | {'Input':<{max_input_length}} | {'Expected Output':<{max_output_length}} |{'Result':<{max_result_length}} |\n"
    separator = f"|{'-' * (max_test_case_length + 2)}|{'-' * (max_input_length + 2)}|{'-' * (max_output_length + 2)}|{'-' * (max_result_length + 2)}|\n"
    rows = ''

    for case_number, case in enumerate(test_cases, start=1):
        test_case = f"{case_number:<{max_test_case_length}}"
        input_data = f"{str(case['input']):<{max_input_length}}"
        expected_output = f"{str(case['expected_output']):<{max_output_length}}"
        recieved_result = f"{str(case['result']):<{max_result_length}}"
        row = f"| {test_case} | {input_data} | {expected_output} |{recieved_result} |\n"
        rows += row

    return f"{header}{separator}{rows}"


# Example test cases
test_cases = [
    {
        'input': 'Registering a new user',
        'expected_output': 'User "sponge" is successfully registered in the database.',
        'result': 'Pass',
    },
    {
        'input': 'Setting a user as an admin',
        'expected_output': 'User "akanksha" is successfully set as an admin in the database.',
        'result': 'Pass',
    },
    {
        'input': 'Adding a new category ',
        'expected_output': 'Category "Bath Products" is successfully added to the database',
        'result': 'Pass',

    },
     {
        'input': 'Adding a new product',
        'expected_output': ' Product "Body Wash" is successfully added to the database..',
        'result': 'Pass',

    },
     {
        'input': 'Viewing all categories',
        'expected_output': 'The list of all categories available in the database is displayed.',
        'result': 'Pass',

    },
     {
        'input': 'Viewing all products',
        'expected_output': 'The list of all products available in the database is displayed.',
        'result': 'Pass',

    },
     {
        'input': 'Viewing product details',
        'expected_output': 'The details of the "Body Wash" product are displayed.',
        'result': 'Pass',

    },
     {
        'input': 'Adding a product to the cart',
        'expected_output': 'The "Body Wash" product is successfully added to the cart of user "sponge".',
        'result': 'Pass',

    },
     {
        'input': 'Removing a product from the cart',
        'expected_output': 'The "Body Wash" product is successfully removed from the cart of user "sponge".',
        'result': 'Pass',

    },
     {
        'input': 'Checking out the cart  ',
        'expected_output': 'The contents of the cart for user "sponge" are displayed, along with the total bill amount and any applicable discounts.',
        'result': 'Pass',

    },
     
]

formatted_test_cases = format_test_cases(test_cases)
print(formatted_test_cases)