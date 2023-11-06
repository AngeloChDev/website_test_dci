import requests
url='https://angelochdev.github.io/website_test_dci/games.html'
page = requests.get(url)
re = page.request
if re.method == 'POST':
      with open('re.txt', 'w') as f:
            f.write('hghggj')
            f.close()
      print('oi')
