from faker import Faker

fake = Faker()


def get_registered_user():
    return {
        "employee_id" : fake.unique.random_number(digits=5),
        "first_name" : fake.first_name(),
        "last_name" : fake.last_name(),
        "email" : fake.email(),
        "phone_number" : fake.phone_number()

    }


if __name__ == "__main__":
    print(get_registered_user())