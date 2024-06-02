from fetch import fetch_search_results

def check_rankings(keywords, target_url, api_key, cse_id, max_results=30):
    rankings = []
    for keyword in keywords:
        results = []
        for start in range(1, max_results + 1, 10):
            batch_results = fetch_search_results(keyword, api_key, cse_id, num_results=10, start=start)
            if batch_results and 'items' in batch_results:
                results.extend(batch_results['items'])
                if len(batch_results['items']) < 10:
                    break
            else:
                break

        if results:
            found = False
            for index, item in enumerate(results):
                link = item.get('link')
                if target_url in link:
                    rankings.append({
                        "keyword": keyword,
                        "rank": index + 1,
                        "title": item.get('title'),
                        "snippet": item.get('snippet'),
                        "url": link
                    })
                    found = True
                    break
            if not found:
                rankings.append({
                    "keyword": keyword,
                    "rank": None,
                    "title": None,
                    "snippet": None,
                    "url": None
                })
        else:
            rankings.append({
                "keyword": keyword,
                "rank": None,
                "title": None,
                "snippet": None,
                "url": None
            })
    return rankings
