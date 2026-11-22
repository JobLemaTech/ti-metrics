import requests

API_URL = "http://ip-api.com/json/"

class GeolocationClient:
    def get_ip_geolocation(self, ip):
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
    def enrich_ips(self, ips):
        results = {}
        for ip in sorted(set(ips)):
            results[ip] = self.get_ip_geolocation(ip)
        return results
