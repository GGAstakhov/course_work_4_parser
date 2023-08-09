from functions import hh_ru_vacancies, sj_ru_vacancies, minimum_salary, add_vacancies_to_json

PATH = 'data_vacancies.json'


def main():
    while True:
        user_choice = input(
            'Select site:\n'
            '1)superjob.ru\n'
            '2)hh.ru\n'
            '3)exit\n'
        )

        if user_choice == "1":
            user_find_key = input('Enter a query by keyword: \n')
            list_vacancies = sj_ru_vacancies(user_find_key)
        elif user_choice == "2":
            user_find_key = input('Enter a query by keyword: \n')
            list_vacancies = hh_ru_vacancies(user_find_key)
        elif user_choice == "3":
            break
        else:
            print('No such site, please select one of the options')
            continue

        user_sorted_data_choice = input(
            'Sort data:\n'
            '1)Ascending\n'
            '2)Descending\n'
            '3)Show salary not less than the specified amount\n'
            '4)Exit\n'
        )

        if user_sorted_data_choice == "1":
            list_vacancies.sort()
            for item in list_vacancies:
                format_salary = item.salary_formatting()
                format_description = item.description_formatting()
                print(f'{item.title}, {item.url}, {format_salary}, {format_description}')
                add_vacancies_to_json(PATH, list_vacancies)

        elif user_sorted_data_choice == "2":
            list_vacancies.sort(reverse=True)
            for item in list_vacancies:
                format_salary = item.salary_formatting()
                format_description = item.description_formatting()
                print(f'{item.title}, {item.url}, {format_salary}, {format_description}')
                add_vacancies_to_json(PATH, list_vacancies)

        elif user_sorted_data_choice == "3":
            user_minimum_salary = int(input('Enter the minimum wage in numbers: '))
            desire = minimum_salary(list_vacancies, user_minimum_salary)
            if not desire:
                print("There are no such vacancies")
                add_vacancies_to_json(PATH, list_vacancies)
            else:
                for item in desire:
                    format_salary = item.salary_formatting()
                    format_description = item.description_formatting()
                    print(f'{item.title}, {item.url}, {format_salary}, {format_description}')
                    add_vacancies_to_json(PATH, list_vacancies)

        elif user_sorted_data_choice == "4":
            break

        else:
            print("Wrong item, please select one item from the options")
            continue


if __name__ == '__main__':
    main()
