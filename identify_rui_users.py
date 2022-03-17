import requests

def main():

    # first, let's get the most recent data
    # To get TOKEN for viewing unpublished data, go to EUI, log in, then view source, then copy token from browser
    TOKEN = "AgE1lb133P2DNnVb8VPyGDzpxOrM2eV51OXkVd9N4NMmn9gr2bIwCEp0p4zgmpnY4bMGo9rDDzlKnncyE63r5cN390"
    endpoint = "https://ccf-api.hubmapconsortium.org/v1/hubmap/rui_locations.jsonld"
    headers = {"Authorization": "Bearer " + TOKEN}
    data = requests.get(endpoint, headers=headers).json()

    # identify unique creators
    iris = set()
    for item in data['@graph']:
        for sample in item['samples']:
            iris.add(sample['rui_location']['creator'])

    print(f'''
Unique creators: {iris}
''')

# driver code
if __name__ == '__main__':
    main()
