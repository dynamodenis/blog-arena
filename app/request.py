import urllib.request,json
from .models import Quotes

api_url=None

def create_configuration(app):
    global api_url
    api_url=app.config['RANDOM_API']

#create an api request
def get_quote():
    api_url=api_url
    with urllib.request.urlopen(api_url) as url:
        read_content=url.read()
        convert_json=json.loads(read_content)

        source_result=None

        if convert_json:
            source_result=process_result(convert_json)
    return source_result

def process_result(quote_list):
   source_result=[] 
   for quote in quote_list:
       id=quote.get('id')
       author=quote.get('author')
       quote=quote.get('quote')
       if quote:
           new_quote=Quotes(id=id,author=author,quote=quote)
           source_result.append(new_quote)
    return source_result

