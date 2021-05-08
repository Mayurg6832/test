class CompanyMaster:
    def __init__(self, data):
        self.dataset = data

    def histogram_auth_cap(self):
        auth_cap = [int(float(i[8])) for i in self.dataset]
        for i in range(len(auth_cap)):
            if auth_cap[i] <= 100000:
                auth_cap[i] = 1
            elif auth_cap[i] > 100000 and auth_cap[i] <= 1000000:
                auth_cap[i] = 2
            elif auth_cap[i] > 1000000 and auth_cap[i] <= 10000000:
                auth_cap[i] = 3
            elif auth_cap[i] > 10000000 and auth_cap[i] <= 100000000:
                auth_cap[i] = 4
            elif auth_cap[i] > 10000000:
                auth_cap[i] = 5
        return auth_cap

    def barplot_by_year(self):
        years = self.convert_years()
        frist_20 = dict(list(years.items())[:20])
        frist_20 = dict(sorted(frist_20.items()))
        years = list(frist_20.keys())
        year_count = list(frist_20.values())
        return (years, year_count)

    def top_registrations(self):
        pba = {}
        for i in self.dataset:
            if i[6].split("-")[-1] == '2015':
                if i[11] in pba:
                    pba[i[11]] += 1
                else:
                    pba[i[11]] = 1
        sorted_pba = dict(
            sorted(pba.items(), key=lambda x: x[1], reverse=True))
        top_10 = dict(list(sorted_pba.items())[:10])
        pba = list(top_10.keys())
        word1 = pba[4].split()[:8]
        word2 = pba[4].split()[11:]
        pba[4] = " ".join(word1+word2)
        pba_count = list(top_10.values())
        return (pba, pba_count)

    def grouped_bar(self):
        grup_pba = {}
        for i in self.dataset:
            if i[11] in grup_pba:
                grup_pba[i[11]] += 1
            else:
                grup_pba[i[11]] = 1
        del grup_pba['NA']
        years = self.convert_years()
        sorted_pba = dict(
            sorted(grup_pba.items(), key=lambda x: x[1], reverse=True))
        first_17 = dict(list(years.items())[:17])
        year_y = list(first_17.values())
        year_x = [i-(0.35/2) for i in range(17)]
        pba_y = list(sorted_pba.values())
        pba_x = [i+(0.35/2) for i in range(17)]
        return (year_x, year_y, pba_x, pba_y)

    def convert_years(self):
        years = {}
        for i in self.dataset:
            year = i[6].split("-")[-1]
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
        del years["NA"]
        del years["5600"]
        sorted_years = dict(sorted(years.items(), reverse=True))
        return sorted_years
