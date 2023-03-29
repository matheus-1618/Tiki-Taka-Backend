import http.client
import json

class Request:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("transfermarket.p.rapidapi.com")
        self.headers = {'X-RapidAPI-Host': "transfermarket.p.rapidapi.com",
                        'X-RapidAPI-Key': "97167c7cc2mshbf62f83c1618b15p1d1cb2jsn097e721239cf"}
    
    def get_best_players(self):
        self.conn.request("GET", "/statistic/list-best-fifa-players", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))
    
    def get_golden_boot(self):
        self.conn.request("GET", "/statistic/list-golden-boot", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))
    
    def get_valuables_leagues(self):
        self.conn.request("GET", "/statistic/list-most-valuable-competitions", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))
    
    def get_valuable_clubs(self):
        self.conn.request("GET", "/statistic/list-most-valuable-clubs", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

    def get_player_profile(self,id):
        self.conn.request("GET", f"/players/get-profile?id={id}", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))
    
    def get_player_performace(self,id):
        self.conn.request("GET", f"/players/get-performance-summary?id={id}&seasonID=2021", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))
    
    def get_club_profile(self,id):
        self.conn.request("GET", f"/clubs/get-profile?id={id}", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

    def get_club_header(self,id):
        self.conn.request("GET", f"/clubs/get-header-info?id={id}", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))
    
    def get_league_table(self,id):
        self.conn.request("GET", f"/competitions/get-table?id={id}&seasonID=2022", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

    def get_squad(self,id):
        self.conn.request("GET", f"/clubs/get-squad?id={id}", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))