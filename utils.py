from wit import Wit 
from gnewsclient import gnewsclient

access_token = "ENTER YOU WIT.AI ACCESS TOKEN"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	categories = {'newstype':None, 'location':None}

	
	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']
	# print(entities)
	return categories


def get_news_elements(categories):
	# query = None
	if categories['newstype'] != None:
		query == categories['newstype'] + ' '

	if categories['location'] != None:
		query == categories['location']
	# print(query)
	news_client = gnewsclient.NewsClient(topic="coronavirus", location="india")
	news_items = news_client.get_news()

	elements = []
	# print(news_items)
	for item in news_items:
		element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "Read more",
								'url': item['link']
					}],
					'image_url': item['media']		
		}
		elements.append(element)
	# print(elements)
	return elements
# print(get_news_elements(wit_response("i live in india")))
