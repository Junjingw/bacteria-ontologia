import json

import requests

from nltk.metrics.distance import edit_distance

from bs4 import BeautifulSoup
from bs4.element import NavigableString

qualifiers_hashmap = dict()
def get_qualifier(name: str) -> str:
    '''
    Get the qualifier of a bacteria with a given name.  
    Connects to wikidata search and performs webscraping to get the best 
    possible qualifier based on the Levenshtein distance (edit distance) and 
    the height of the search result.
    
    Args:
        name (str): The name of a bacteria.
    Returns:
        str: The qualifier of that bacteria.
    '''
    
    if name in qualifiers_hashmap:
        return qualifiers_hashmap[name]
    
    html_content = requests.get(
        'https://www.wikidata.org/w/index.php'
        f'?search={name}',
    ).text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    search_results = soup.find_all(
        attrs={'class': 'mw-search-result mw-search-result-ns-0'}
    )
    
    label_index_qualifier_hashmap = dict()
    for i, search_result in enumerate(search_results):
        qualifier = search_result.find(
            attrs={'class': 'wb-itemlink-id'}
        ).contents[0][1:-1]
        
        label_html = search_result.find(
            attrs={'class': 'wb-itemlink-label'}
        )
        segments = []
        for content in label_html.contents:
            if isinstance(content, NavigableString):
                segment = content
            else:
                segment = content.contents[0]
            segments.append(segment)
            
        label = ''.join(segments)
        label_index_qualifier_hashmap[(label, i)] = qualifier
        
    label_index = min(
        label_index_qualifier_hashmap,
        key=lambda label_index: (edit_distance(label_index[0], name), label_index[1])
    )


    qualifier = label_index_qualifier_hashmap[label_index]
    
    qualifiers_hashmap[name] = qualifier
    return qualifier


signs_hashmap = dict()
def get_signs(qualifier: str) -> set[str]:
    '''
    Get the signs of a bacteria with a given qualifier. Connects to the sparql 
    endpoint of wikidata to query for the signs of the bacteria which are every 
    effect, symptom and cause of the bacteria.
    
    Args:
        qualifier (str): The qualifier of a bacteria.
    Returns:
        set: The signs of that bacteria.
    '''
    
    if qualifier in signs_hashmap:
        return signs_hashmap[qualifier]
    
    query_endpoint = 'https://query.wikidata.org/sparql'
    query = '''
    SELECT
        ?effectLabel
        ?dataLabel
    WHERE{
        wd:'''+qualifier+''' wdt:P1542 ?effect .
        OPTIONAL {?effect wdt:P780 ?data}
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    '''
    params = {'query': query, 'format': 'json'}
    result = json.loads(requests.get(query_endpoint, params=params).text)

    signs = set()
    for entry in result['results']['bindings']:
        signs.add(entry['effectLabel']['value'])
        if 'dataLabel' in entry:
            signs.add(entry['dataLabel']['value'])
            
    signs_hashmap[qualifier] = signs
    return signs


if __name__ == '__main__':
    bacteria = 'Campylobacter jejuni'
    qualifier = get_qualifier(bacteria)
    print(f'The qualifier of {bacteria} is {qualifier}')
    signs = get_signs(qualifier)
    print(f'The signs of {bacteria} are {signs}')