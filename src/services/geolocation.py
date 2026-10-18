import requests

API_URL = "http://ip-api.com/json/"

def get_ip_geolocation(ip):
    url = f"{API_URL}{ip}"
    params = {
        "fields": "status,message,query,country,countryCode,regionName,city,lat,lon",
        "lang": "es",
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except (requests.RequestException, ValueError) as error:
        return {
            "status": "fail",
            "query": ip,
            "message": str(error),
        }
def enrich_ips(ips):
    results = {}
    for ip in sorted(set(ips)):
        results[ip] = get_ip_geolocation(ip)
    return results
