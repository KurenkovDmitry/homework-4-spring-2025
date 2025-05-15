import json

def save_session(driver, cookies_file='cookies.json', localstorage_file='localstorage.json'):
    # Сохранение cookies
    with open(cookies_file, 'w') as f:
        json.dump(driver.get_cookies(), f)

    # Сохранение localStorage
    localstorage = driver.execute_script("return window.localStorage;")
    with open(localstorage_file, 'w') as f:
        json.dump(localstorage, f)

def load_session(driver, cookies_file='cookies.json', localstorage_file='localstorage.json', base_url='http://example.com'):
    # Загрузка базового URL
    driver.get(base_url)

    # Загрузка cookies
    try:
        with open(cookies_file, 'r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                # Убедитесь, что cookie не содержит поля 'domain' или оно совпадает с текущим доменом
                if 'domain' in cookie:
                    del cookie['domain']
                driver.add_cookie(cookie)
    except FileNotFoundError:
        print("Cookies file not found, skipping cookies restoration.")

    # Загрузка localStorage
    try:
        with open(localstorage_file, 'r') as f:
            localstorage = json.load(f)
            for key, value in localstorage.items():
                driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
    except FileNotFoundError:
        print("LocalStorage file not found, skipping localStorage restoration.")