import requests

print("\nПервое задание:\n")
url_marvel = 'https://akabab.github.io/superhero-api/api//all.json'
response = requests.get(url_marvel)
intelligence_superheros = {}
for i in response.json():
    if i['name'] == 'Captain America' or i['name'] == 'Thanos' or i['name'] == 'Hulk':
        intelligence_superheros[i["name"]] = i["powerstats"]["intelligence"]

the_most_intelligence = {k:v for k, v in intelligence_superheros.items()
                         if v == max(intelligence_superheros.values())}
print(f'The most intelligence superhero is {list(the_most_intelligence.keys())[-1]}, '
      f'his intelligence is equal to {list(the_most_intelligence.values())[-1]}')

print("\nВторое задание:\n")


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        params = {'path': file_path.split("/")[-1]}
        headers = {'Authorization': self.token}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers, params=params)
        url_for_upload = response.json().get("href")
        with open(file_path, 'rb') as file:
            response1 = requests.put(url_for_upload, files={'file': file})
        print('cтатус кода -', response1.status_code)


if __name__ == '__main__':
    path_to_file = 'C:/Users/79995/Desktop/fighting.jpg'
    token = 'token'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)



