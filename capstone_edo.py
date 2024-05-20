data = {'Admin001': {'Email': 'admincarent@carent.com', 'Password': 'Admin123!'},
        'Super001': {'Email': 'superadmincarent@carent.com', 'Password': 'Super123!'}
        }

database = {'C001': {'brand': 'Toyota',
                      'model': 'Innova Zenix',
                      'year': 2023,
                      'license plate': 'B 1234 RFH',
                      'status': 'Under Repair'},
            'C002': {'brand': 'Toyota',
                      'model': 'Innova Reborn',
                      'year': 2021,
                      'license plate': 'B 5678 DEF',
                      'status': 'Rented'},
            'C003': {'brand': 'Hyundai',
                      'model': 'Ioniq 5',
                      'year': 2023,
                      'license plate': 'B 9876 HEV',
                      'status': 'Standby'}
            }

# Validation
## Primary Key
def validate_primary_key(primary_key):
    # Check length
    if len(primary_key) != 4:
        print('Wrong format')
        return False
    
    # Check first character is alphabet and the rest are digits
    if not primary_key[0].isalpha() or not primary_key[1:].isdigit():
        print('Wrong format')
        return False
    
    return True

## Brand
def validate_brand(brand):
    return True

## Model
def validate_model(model):
    return True

## Year
def validate_year(year):
    return isinstance (year,int)

## License Plate
def validate_license_plate(license_plate):
    if len(license_plate) > 12:
        return False
    components = license_plate.split()
    if len(components) != 2 and len(components) != 3:
        return False

    if len(components) == 2:
        first_component, second_component = components

    else:
        first_component, second_component, third_component = components

    if len(first_component) > 2 or len(third_component) > 3:
        return False
    
    if not (first_component.isalpha() and third_component.isalpha()):
        return False
    
    if not second_component.isdigit() or len(second_component) > 4:
        return False
    
    return True

## Status
def validate_status(status):
    return True

# Data Input
## Brand
def input_brand():
    global brand
    brand = input('Please Input The Brand : ')
    while not validate_brand(brand):
        print('Wrong Input : ')
        continue

## Model
def input_model():
    global model
    model = input('Please Input The Model : ')
    while not validate_model(model):
        print('Wrong Input')
        continue

## Year
def input_year():
    global year
    while True:
        try:
            year_input = input('Please Input The Year : ')
            # Try converting the input to an integer
            year = int(year_input)
            # Check if the year is valid
            if validate_year(year):
                break  # Exit the loop if the year is valid
            else:
                print('Invalid year! Please enter a valid year.')
        except ValueError:
            print('Invalid input! Please enter a valid year.')

## License Plate
def input_licenseplate():
    global license_plate
    while True:
        license_plate = input('Please Input The License Plate : ')
        if validate_license_plate(license_plate):
            break
        else:
            print('Wrong Format')
            continue

## Status
def input_status():
    global selected_status
    data_status = {
        1: 'Rented',
        2: 'Under Repair',
        3: 'Standby'
    }
    print('Status Code: \n1. Rented\n2. Under Repair\n3. Standby')
    while True:
        try:
            input_status_code = int(input('Please Input The Current Status: '))
            if input_status_code in data_status:
                selected_status = data_status[input_status_code]
                return selected_status
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input. Please enter a valid status code.')

# Updating
def update_data(primary_key):
    if primary_key in database:
        print('Data found!')
        confirm = input('Are you sure you want to update this data? (y/n): ')
        if confirm.lower() == 'y':
            print('Enter the new values. Leave blank if you do not want to update a specific field.')
            new_brand = input('Enter new brand: ')
            new_model = input('Enter new model: ')
            new_year = input('Enter new year: ')
            new_license_plate = input('Enter new license plate: ')
            new_status = input_status()  # Call input_status() to get the new status

            # Check if status is provided
            if new_status == '':
                print('Status must be provided. Update canceled.')
                return  # Exit the function if status is not provided

            # Update values if not blank
            if new_brand:
                database[primary_key]['brand'] = new_brand
            if new_model:
                database[primary_key]['model'] = new_model
            if new_year:
                try:
                    database[primary_key]['year'] = int(new_year)
                except ValueError:
                    print('Invalid year format. Year should be a number.')
            if new_license_plate:
                if validate_license_plate(new_license_plate):
                    database[primary_key]['license plate'] = new_license_plate
                else:
                    print('Invalid license plate format.')

            # Update status
            database[primary_key]['status'] = new_status

            confirm_update = input('Do you want to proceed with the update? (y/n): ')
            if confirm_update.lower() == 'y':
                print('Data updated successfully.')
            elif confirm_update.lower() == 'n':
                print('Update canceled.')
            else:
                print('Invalid input! Please enter either "y" or "n".')
        elif confirm.lower() == 'n':
            print('Update canceled.')
    else:
        print('Data does not exist.')

# Login Page
def Login():
    global data
    global id_input

    try_log_in = 0
    try_limit = 5

    while try_log_in < try_limit:
        print('=' * 50)
        id_input = input('Username: ')
        pass_input = input('Password: ')
        print('=' * 50, '\n')

        if id_input not in data:
            print(f'Username not registered! You can try {try_limit - try_log_in - 1} times more\n')
            try_log_in += 1
        elif pass_input != data[id_input]['Password']:
            print(f'Wrong Password, You can try {try_limit - try_log_in - 1} times more\n')
            try_log_in += 1
        else:
            print('Welcome\n')
            print('=' * 50)
            if id_input == 'Admin001':
                Landing_Page_Admin()
            elif id_input == 'Super001':
                Landing_Page_Super_Admin()
            return id_input
    print('Login Try Limit.\n')

# Landing Page Super Admin
def Landing_Page_Super_Admin():
    landing_option = {
        1: 'Car Database',
        2: 'Input New Car Data',
        3: 'Modify Existing Car Data',
        4: 'Delete Car Data',
        5: 'Exit'
    }
    while True:
        print('#### Welcome to Carent App ####')
        print('=' * 50)
        for key, value in landing_option.items():
            print(f'{key}. {value}')
        input_landing = input('Input: ')
        if input_landing.isnumeric():
            input_landing = int(input_landing)
            if input_landing in landing_option:
                if input_landing == 1:
                    print('=' * 50, '\n')
                    print('Accessing.............')
                    print('=' * 9, landing_option[1], '=' * 8, '\n')
                    Read_Menu()
                elif input_landing == 2:
                    print('=' * 50, '\n')
                    print('Inputting.............')
                    print('=' * 9, landing_option[2], '=' * 8, '\n')
                    Create_Menu()
                elif input_landing == 3:
                    print('=' * 50, '\n')
                    print('Modifying..............')
                    print('=' * 9, landing_option[3], '=' * 8, '\n')
                    Update_Menu()
                elif input_landing == 4:
                    print('=' * 50, '\n')
                    print('Deleting...............')
                    print('=' * 7, landing_option[4], '=' * 8, '\n')
                    Delete_Menu()
                elif input_landing == 5:
                    print('=' * 50, '\n')
                    print('Exiting................')
                    print('=' * 8, landing_option[5], '=' * 9, '\n')
                    break
            else:
                print('Please Select The Correct Menu!')
                print('=' * 50, '\n')
        else:
            print('Invalid Input! Please enter a number.')
            print('=' * 50, '\n')

# Landing Page Admin
def Landing_Page_Admin():
    landing_option = {
        1: 'Car Database',
        2: 'Input New Car Data',
        3: 'Modify Existing Car Data',
        4: 'Delete Car Data',
        5: 'Exit'
    }
    while True:
        print('#### Welcome to Carent App ####')
        print('=' * 50)
        for key, value in landing_option.items():
            print(f'{key}. {value}')
        input_landing = input('Input: ')
        if input_landing.isnumeric():
            input_landing = int(input_landing)
            if input_landing in landing_option:
                if input_landing == 1:
                    print('=' * 50, '\n')
                    print('=' * 20, landing_option[1], '=' * 20, '\n')
                    Read_Menu()
                elif input_landing == 2:
                    print('=' * 50, '\n')
                    print('Restricted Access, Only Super Admin can access\n')
                    print('=' * 20, landing_option[5], '=' * 20, '\n')
                elif input_landing == 3:
                    print('=' * 50, '\n')
                    print('Modifying..............')
                    print('=' * 9, landing_option[3], '=' * 10, '\n')
                    Update_Menu()
                elif input_landing == 4:
                    print('=' * 50, '\n')
                    print('Restricted Access, Only Super Admin can access\n')
                    print('=' * 20, landing_option[5], '=' * 20, '\n')
                elif input_landing == 5:
                    print('=' * 50, '\n')
                    print('Exiting.................')
                    print('=' * 11, landing_option[5], '=' * 14, '\n')
                    break
            else:
                print('Please Select The Correct Menu!')
                print('=' * 50, '\n')
        else:
            print('Invalid Input! Please enter a number.')
            print('=' * 50, '\n')

def Read_Menu():
    read_option = {
        1: 'Show All',
        2: 'Search Data',
        3: 'Back to Main Menu',
    }
    while True:
        print('#### Read Data Menu ####')
        print('=' * 40)
        for key, value in read_option.items():
            print(f'{key}. {value}')
        input_read = input('Input: ')
        if input_read.isnumeric():
            input_read = int(input_read)
            if input_read in read_option:
                if input_read == 1:
                    print('=' * 40)
                    print('Accessing.............\n')
                    print("ID".ljust(5), "Brand".ljust(10), "Model".ljust(15), "Year".ljust(6), "License Plate".ljust(15), "Status")
                    print('-' * 70)
                    if database:
                        for car_id, car_info in database.items():
                            brand = car_info.get('brand', '')
                            model = car_info.get('model', '')
                            year = str(car_info.get('year', ''))
                            license_plate = car_info.get('license plate', '')
                            status = car_info.get('status', '')
                            print(car_id.ljust(5), brand.ljust(10), model.ljust(15), year.ljust(6), license_plate.ljust(15), status)
                    else:
                        print("Data does not exist.")
                    print('-' * 70, '\n')
                elif input_read == 2:
                    primary_key = input('Please enter the primary key: ').title()
                    if primary_key in database:
                        print('=' * 40)
                        print(f"Data for {primary_key}:")
                        car_info = database[primary_key]
                        print("ID".ljust(5), "Brand".ljust(10), "Model".ljust(15), "Year".ljust(6), "License Plate".ljust(15), "Status")
                        print('-' * 70)
                        brand = car_info.get('brand', '')
                        model = car_info.get('model', '')
                        year = str(car_info.get('year', ''))
                        license_plate = car_info.get('license plate', '')
                        status = car_info.get('status', '')
                        print(primary_key.ljust(5), brand.ljust(10), model.ljust(15), year.ljust(6), license_plate.ljust(15), status)
                        print('-' * 70, '\n')
                    else:
                        print("Data does not exist.")
                        print('-' * 70, '\n')
                elif input_read == 3:
                    print('=' * 11, read_option[3], '=' * 14, '\n')
                    break
            else:
                print('Please Select The Correct Menu!')
                print('=' * 40, '\n')
        else:
            print('Invalid Input! Please enter a number.')
            print('=' * 40, '\n')

# Create menu
def Create_Menu():
    create_option = {
        1: 'Add Data',
        2: 'Back To Main Menu'
    }
    while True:
        header = print('#### Add Data Menu ####')
        print('=' * 40)
        for Keys, Values in create_option.items():
            print(f'{Keys}.{Values}')
        input_landing = input('Input : ')
        if input_landing.isnumeric():
            input_landing = int(input_landing)
            if input_landing in create_option:
                if input_landing == 1:
                    print('=' * 40)
                    primary_key = input('Please enter the primary key: ').title()
                    if validate_primary_key(primary_key):
                        if primary_key in database:
                            print('Data Already Exist')
                        else:
                            input_brand()
                            input_model()
                            input_year()
                            input_licenseplate()
                            input_status()
                            print('=' * 40)
                            confirm_save = input('Do you want to save this data? (y/n): ').lower()
                            if confirm_save == 'y':
                                database.update({primary_key : {'brand': brand,
                                                                'model': model,
                                                                'year': year,
                                                                'license plate': license_plate,
                                                                'status': selected_status
                                                                }
                                                })
                                print('Data saved.\n')
                            elif confirm_save == 'n':
                                print('Data not saved.\n')
                            else:
                                print('Invalid input! Please enter either "y" or "n".')
                elif input_landing == 2:
                    print('=' * 17, create_option[2], '=' * 23, '\n')
                    break
            else:
                print('Please Select The Correct Menu !')
                print('=' * 40, '\n')
        else:
            print('Invalid Input ! Please enter a number.')
            print('='*40, '\n')

# Update menu
def Update_Menu():
    update_option = {
        1: 'Modify Data',
        2: 'Back To Main Menu'
    }
    while True:
        header = print('#### Modify Data Menu ####')
        print('=' * 40)
        for Keys, Values in update_option.items():
            print(f'{Keys}.{Values}')
        input_update = input('Input : ')
        if input_update.isnumeric():
            input_update = int(input_update)
            if input_update in update_option:
                if input_update == 1:
                    print('=' * 40)
                    primary_key = input("Enter the primary key of the data to update: ").title()
                    if validate_primary_key(primary_key):
                        update_data(primary_key)
                    else:
                        print('Invalid primary key format. Please enter a valid primary key.')
                    continue
                elif input_update == 2:
                    print('=' * 11, update_option[2], '=' * 14, '\n')
                    break
            else:
                print('Please Select The Correct Menu !')
                print('=' * 40, '\n')
        else:
            print('Invalid Input ! Please enter a number.')
            print('=' * 40, '\n')

# Delete_menu
def Delete_Menu():
    delete_option = {
        1 : 'Delete Data',
        2 : 'Back To Main Menu'
    }
    while True:
        header = print('#### Delete Data Menu ####')
        print('=' * 40)
        for Keys, Values in delete_option.items():
            print(f'{Keys}.{Values}')
        input_landing = input('Input : ')
        if input_landing.isnumeric():
            input_landing = int(input_landing)
            if input_landing in delete_option:
                if input_landing == 1:
                    print('=' * 40)
                    primary_key = input("Enter the primary key of the data to delete: ").title()
                    # Validate primary key format
                    if validate_primary_key(primary_key):
                        if primary_key in database:
                            print('Data found!')
                            confirm = input('Are you sure you want to delete this data? (y/n): ')
                            if confirm.lower() == 'y':
                                del database[primary_key]
                                print('Deleting...........................')
                                print('=' * 40)
                                print('Data has been successfully deleted.')
                            elif confirm.lower() == 'n':
                                print('Deletion cancelled.\n')
                            else:
                                print('Invalid input! Please enter either "y" or "n".\n')
                        else:
                            print('Data does not exist.\n')
                    else:
                        print('Invalid primary key format. Please enter a valid primary key.\n')
                    continue
                    continue              
                elif input_landing == 2:
                    print('=' * 11, delete_option[2], '=' * 14, '\n')
                    break
            else:
                print('Please Select The Correct Menu !')
                print('=' * 40, '\n')
        else:
            print('Invalid Input ! Please enter a number.')
            print('=' * 40, '\n')

Login()