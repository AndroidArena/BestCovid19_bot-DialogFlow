import requests
import json


class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "36626c56f2msh8580d29c47aca59p12a368jsnc74c1cdf1888"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases'), result.get('deaths'), result.get('tests')

    def makeApiRequestForIndianStates(self):
        url = "https://covid-193.p.rapidapi.com/history?country=india&day=2022-04-17"
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "36626c56f2msh8580d29c47aca59p12a368jsnc74c1cdf1888"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        # result = js.get('list')
        return js

    def makeApiWorldwide(self):
        url = "https://covid-193.p.rapidapi.com/countries"
        headers = {
            "x-rapidapi-host": "covid-193.p.rapidapi.com",
            "x-rapidapi-key": "36626c56f2msh8580d29c47aca59p12a368jsnc74c1cdf1888"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')
        return result
