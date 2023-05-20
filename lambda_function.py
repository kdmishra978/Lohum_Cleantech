import json
from bs4 import BeautifulSoup
import requests
def lambda_handler(event, context):
    # TODO implement
    ans = ''
    try:
      url = 'https://www.metal.com/Lithium-ion-Battery/202303240001'
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')
      label_span = soup.find('span', class_='label___NR96c')
      value_span = soup.find('span', class_='strong___1JlBD priceDown___2TbRQ')
      label = label_span.text.strip()
      value = value_span.text.strip()
      ans = str(value)
      # Assuming the value is in the format 'XX.XX'
      avg_price = float(value)
      print(label , avg_price)
    except:
      ans = 'Average price is not present'
      print('Average price is not present')
    return {
        'statusCode': 200,
        'body': json.dumps(ans)
    }