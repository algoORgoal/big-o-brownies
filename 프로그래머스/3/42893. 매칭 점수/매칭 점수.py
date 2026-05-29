import re
from functools import cmp_to_key

def comparator(page1, page2):
    return page2['score'] - page1['score']

def solution(word, pages):
    page_table = {}
    
    for index, page in enumerate(pages):
        base_score = 0 
        for token in re.split(r'[^a-zA-Z]', page):
            if token.lower() == word.lower():
                base_score += 1
        
        id = re.findall(r'<meta property="og:url" content="(https.*?)"/>', page)[0]
                
                
        external_links = re.findall(r'<a href="(https.*?)">', page)
        page_table[id] = {
            'base_score': base_score,
            'external_links': external_links,
            'score': base_score,
            'index': index,
        }
            
    
    for url, page in page_table.items():
        if len(page['external_links']) == 0:
            continue
            
        matching_score = page['base_score'] / len(page['external_links'])
        for external_link in page['external_links']:
            if external_link in page_table:
                page_table[external_link]['score'] += matching_score    
            
    return sorted([ page for page in page_table.values()], key=cmp_to_key(comparator))[0]['index']

# 기본점수
# 외부 링크 수
# 매칭점수

# 기본점수: 웹페이지 텍스트 중 검색어가 등장하는 횟수
#   - 대소문자 구별 안 함
#   - 단어는 알파벳을 제외한 다른 모든 문자로 구분
# page의 id인 본인의 url은 <meta property="og:url" content=""/>와 같이 표현된다.

# 외부링크 수: 외부 페이지로 연결된 링크의 개수
# 링크점수: 기본점수 + 본 웹페이지로 링크가 걸린 다른 (웹페이지의 기본점수 / 외부링크 수)의 총합
