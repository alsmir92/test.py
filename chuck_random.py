import requests


class Test_new_joke():

    def __init__(self):
        pass

    def test_create_new_joke(self):
        category = 'sport'
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Status code: " + str(result.status_code))
        assert 200 == result.status_code
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get('categories')
        print(check_info)
        assert check_info == ['sport']
        print("Correct category")


sport_joke = Test_new_joke()
sport_joke.test_create_new_joke()
