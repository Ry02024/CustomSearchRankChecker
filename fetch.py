import requests

def fetch_search_results(keyword, api_key, cse_id, num_results=10, start=1):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': keyword,
        'key': api_key,
        'cx': cse_id,
        'num': min(num_results, 10),
        'start': start
    }

    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"検索に失敗しました。ステータスコード: {response.status_code}")
        print(f"エラーメッセージ: {response.text}")
        return None

def validate_api_key(api_key, cse_id):
    test_query = "test"
    response = fetch_search_results(test_query, api_key, cse_id, num_results=1)
    return response is not None
