
class Validate_Location:

    def location_val(self,loc):
        location = loc.lower().strip()
        tier1 = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune']
        tier1 = [ele.lower() for ele in tier1]

        if location in tier1:
            return(True)
        else:
            pass

        import requests
        import bs4

        c = requests.get('https://en.wikipedia.org/wiki/Classification_of_Indian_cities')
        soup = bs4.BeautifulSoup(c.text,'html5lib')
        data = soup.find_all(name = 'table',attrs = {'class':'wikitable'})
        string = data[0].text
        stri = string[113:1058]
        #stri.split()
        # stri
        tier2 = [ele.strip(',') for ele in stri.split()]
        tier2.remove('and')
        tier2 = [ele.lower() for ele in tier2]
        #li
        
        if location in tier2:
            return(True)
        else:
            return(False)
        





