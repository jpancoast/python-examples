import requests


class test_class():

    def __init__(self, first_key, second_key, debug=False):
        self.first_key = first_key
        self.second_key = second_key
        self.debug = debug
        self.response = None
        self.map = {}
        self.list = []

        self.create_map()
        self.create_list()

        if debug:
            print("Debug mode enabled")
            print("DEBUG First Key: " + self.first_key)
            print("DEBUG Second Key: " + self.second_key)

    def create_map(self):
        self.map["key1"] = "value1"

    def work_map(self):
        print(self.map)

        for key, value in sorted(self.map.items()):
            print(f"{key}: {value}")

    def create_list(self):
        self.list.append("item1")
        self.list.append("item2")

    def work_list(self):
        print(self.list)

        for index, item in enumerate(sorted(self.list)):
            print(f"{index}: {item}")

    def print_something(self):
        print("First Key: " + self.first_key)
        print("Second Key: " + self.second_key)

    def run_get(self, url, params=None, timeout=10):
        """Send a GET request to url and store the response."""
        self.response = requests.get(url, params=params, timeout=timeout)

        if self.debug:
            print(f"DEBUG GET {self.response.url} -> {self.response.status_code}")

        self.response.raise_for_status()
        return self.response.status_code

    def get_content(self):
        """Return the body of the last GET response as text."""
        if self.response is None:
            raise RuntimeError("No request has been made yet; call run_get() first.")
        return self.response.text
