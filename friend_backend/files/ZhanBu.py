import datetime
import time

class BaziPaipan(object): #  计算八字排盘

    def __init__(self,y,m,d,h):

        self.stardard_day = datetime.datetime(1970,2,4,23)
        # self.input_data = datetime.datetime(self.year,self.month,self.day_num,self.time)
        self.__Jie = [datetime.datetime(1970, 2, 4, 0, 0), datetime.datetime(1970, 3, 6, 0, 0),
                      datetime.datetime(1970, 4, 5, 0, 0),
                      datetime.datetime(1970, 5, 6, 0, 0), datetime.datetime(1970, 6, 6, 0, 0),
                      datetime.datetime(1970, 7, 7, 0, 0),
                      datetime.datetime(1970, 8, 8, 0, 0), datetime.datetime(1970, 9, 8, 0, 0),
                      datetime.datetime(1970, 10, 9, 0, 0),
                      datetime.datetime(1970, 11, 8, 0, 0), datetime.datetime(1970, 12, 7, 0, 0),
                      datetime.datetime(1971, 1, 6, 0, 0),
                      datetime.datetime(1971, 2, 4, 0, 0), datetime.datetime(1971, 3, 6, 0, 0),
                      datetime.datetime(1971, 4, 5, 0, 0),
                      datetime.datetime(1971, 5, 6, 0, 0), datetime.datetime(1971, 6, 6, 0, 0),
                      datetime.datetime(1971, 7, 8, 0, 0),
                      datetime.datetime(1971, 8, 8, 0, 0), datetime.datetime(1971, 9, 8, 0, 0),
                      datetime.datetime(1971, 10, 9, 0, 0),
                      datetime.datetime(1971, 11, 8, 0, 0), datetime.datetime(1971, 12, 8, 0, 0),
                      datetime.datetime(1972, 1, 6, 0, 0),
                      datetime.datetime(1972, 2, 5, 0, 0), datetime.datetime(1972, 3, 5, 0, 0),
                      datetime.datetime(1972, 4, 5, 0, 0),
                      datetime.datetime(1972, 5, 5, 0, 0), datetime.datetime(1972, 6, 5, 0, 0),
                      datetime.datetime(1972, 7, 7, 0, 0),
                      datetime.datetime(1972, 8, 7, 0, 0), datetime.datetime(1972, 9, 7, 0, 0),
                      datetime.datetime(1972, 10, 8, 0, 0),
                      datetime.datetime(1972, 11, 7, 0, 0), datetime.datetime(1972, 12, 7, 0, 0),
                      datetime.datetime(1973, 1, 6, 0, 0),
                      datetime.datetime(1973, 2, 4, 0, 0), datetime.datetime(1973, 3, 6, 0, 0),
                      datetime.datetime(1973, 4, 5, 0, 0),
                      datetime.datetime(1973, 5, 5, 0, 0), datetime.datetime(1973, 6, 6, 0, 0),
                      datetime.datetime(1973, 7, 7, 0, 0),
                      datetime.datetime(1973, 8, 8, 0, 0), datetime.datetime(1973, 9, 8, 0, 0),
                      datetime.datetime(1973, 10, 8, 0, 0),
                      datetime.datetime(1973, 11, 7, 0, 0), datetime.datetime(1973, 12, 7, 0, 0),
                      datetime.datetime(1974, 1, 5, 0, 0),
                      datetime.datetime(1974, 2, 4, 0, 0), datetime.datetime(1974, 3, 6, 0, 0),
                      datetime.datetime(1974, 4, 5, 0, 0),
                      datetime.datetime(1974, 5, 6, 0, 0), datetime.datetime(1974, 6, 6, 0, 0),
                      datetime.datetime(1974, 7, 7, 0, 0),
                      datetime.datetime(1974, 8, 8, 0, 0), datetime.datetime(1974, 9, 8, 0, 0),
                      datetime.datetime(1974, 10, 9, 0, 0),
                      datetime.datetime(1974, 11, 8, 0, 0), datetime.datetime(1974, 12, 7, 0, 0),
                      datetime.datetime(1975, 1, 6, 0, 0),
                      datetime.datetime(1975, 2, 4, 0, 0), datetime.datetime(1975, 3, 6, 0, 0),
                      datetime.datetime(1975, 4, 5, 0, 0),
                      datetime.datetime(1975, 5, 6, 0, 0), datetime.datetime(1975, 6, 6, 0, 0),
                      datetime.datetime(1975, 7, 8, 0, 0),
                      datetime.datetime(1975, 8, 8, 0, 0), datetime.datetime(1975, 9, 8, 0, 0),
                      datetime.datetime(1975, 10, 9, 0, 0),
                      datetime.datetime(1975, 11, 8, 0, 0), datetime.datetime(1975, 12, 8, 0, 0),
                      datetime.datetime(1976, 1, 6, 0, 0),
                      datetime.datetime(1976, 2, 5, 0, 0), datetime.datetime(1976, 3, 5, 0, 0),
                      datetime.datetime(1976, 4, 4, 0, 0),
                      datetime.datetime(1976, 5, 5, 0, 0), datetime.datetime(1976, 6, 5, 0, 0),
                      datetime.datetime(1976, 7, 7, 0, 0),
                      datetime.datetime(1976, 8, 7, 0, 0), datetime.datetime(1976, 9, 7, 0, 0),
                      datetime.datetime(1976, 10, 8, 0, 0),
                      datetime.datetime(1976, 11, 7, 0, 0), datetime.datetime(1976, 12, 7, 0, 0),
                      datetime.datetime(1977, 1, 6, 0, 0),
                      datetime.datetime(1977, 2, 4, 0, 0), datetime.datetime(1977, 3, 6, 0, 0),
                      datetime.datetime(1977, 4, 5, 0, 0),
                      datetime.datetime(1977, 5, 5, 0, 0), datetime.datetime(1977, 6, 6, 0, 0),
                      datetime.datetime(1977, 7, 7, 0, 0),
                      datetime.datetime(1977, 8, 7, 0, 0), datetime.datetime(1977, 9, 8, 0, 0),
                      datetime.datetime(1977, 10, 8, 0, 0),
                      datetime.datetime(1977, 11, 7, 0, 0), datetime.datetime(1977, 12, 7, 0, 0),
                      datetime.datetime(1978, 1, 5, 0, 0),
                      datetime.datetime(1978, 2, 4, 0, 0), datetime.datetime(1978, 3, 6, 0, 0),
                      datetime.datetime(1978, 4, 5, 0, 0),
                      datetime.datetime(1978, 5, 6, 0, 0), datetime.datetime(1978, 6, 6, 0, 0),
                      datetime.datetime(1978, 7, 7, 0, 0),
                      datetime.datetime(1978, 8, 8, 0, 0), datetime.datetime(1978, 9, 8, 0, 0),
                      datetime.datetime(1978, 10, 8, 0, 0),
                      datetime.datetime(1978, 11, 8, 0, 0), datetime.datetime(1978, 12, 7, 0, 0),
                      datetime.datetime(1979, 1, 6, 0, 0),
                      datetime.datetime(1979, 2, 4, 0, 0), datetime.datetime(1979, 3, 6, 0, 0),
                      datetime.datetime(1979, 4, 5, 0, 0),
                      datetime.datetime(1979, 5, 6, 0, 0), datetime.datetime(1979, 6, 6, 0, 0),
                      datetime.datetime(1979, 7, 8, 0, 0),
                      datetime.datetime(1979, 8, 8, 0, 0), datetime.datetime(1979, 9, 8, 0, 0),
                      datetime.datetime(1979, 10, 9, 0, 0),
                      datetime.datetime(1979, 11, 8, 0, 0), datetime.datetime(1979, 12, 8, 0, 0),
                      datetime.datetime(1980, 1, 6, 0, 0),
                      datetime.datetime(1980, 2, 5, 0, 0), datetime.datetime(1980, 3, 5, 0, 0),
                      datetime.datetime(1980, 4, 4, 0, 0),
                      datetime.datetime(1980, 5, 5, 0, 0), datetime.datetime(1980, 6, 5, 0, 0),
                      datetime.datetime(1980, 7, 7, 0, 0),
                      datetime.datetime(1980, 8, 7, 0, 0), datetime.datetime(1980, 9, 7, 0, 0),
                      datetime.datetime(1980, 10, 8, 0, 0),
                      datetime.datetime(1980, 11, 7, 0, 0), datetime.datetime(1980, 12, 7, 0, 0),
                      datetime.datetime(1981, 1, 6, 0, 0),
                      datetime.datetime(1981, 2, 4, 0, 0), datetime.datetime(1981, 3, 6, 0, 0),
                      datetime.datetime(1981, 4, 5, 0, 0),
                      datetime.datetime(1981, 5, 5, 0, 0), datetime.datetime(1981, 6, 6, 0, 0),
                      datetime.datetime(1981, 7, 7, 0, 0),
                      datetime.datetime(1981, 8, 7, 0, 0), datetime.datetime(1981, 9, 8, 0, 0),
                      datetime.datetime(1981, 10, 8, 0, 0),
                      datetime.datetime(1981, 11, 7, 0, 0), datetime.datetime(1981, 12, 7, 0, 0),
                      datetime.datetime(1982, 1, 5, 0, 0),
                      datetime.datetime(1982, 2, 4, 0, 0), datetime.datetime(1982, 3, 6, 0, 0),
                      datetime.datetime(1982, 4, 5, 0, 0),
                      datetime.datetime(1982, 5, 6, 0, 0), datetime.datetime(1982, 6, 6, 0, 0),
                      datetime.datetime(1982, 7, 7, 0, 0),
                      datetime.datetime(1982, 8, 8, 0, 0), datetime.datetime(1982, 9, 8, 0, 0),
                      datetime.datetime(1982, 10, 8, 0, 0),
                      datetime.datetime(1982, 11, 8, 0, 0), datetime.datetime(1982, 12, 7, 0, 0),
                      datetime.datetime(1983, 1, 6, 0, 0),
                      datetime.datetime(1983, 2, 4, 0, 0), datetime.datetime(1983, 3, 6, 0, 0),
                      datetime.datetime(1983, 4, 5, 0, 0),
                      datetime.datetime(1983, 5, 6, 0, 0), datetime.datetime(1983, 6, 6, 0, 0),
                      datetime.datetime(1983, 7, 8, 0, 0),
                      datetime.datetime(1983, 8, 8, 0, 0), datetime.datetime(1983, 9, 8, 0, 0),
                      datetime.datetime(1983, 10, 9, 0, 0),
                      datetime.datetime(1983, 11, 8, 0, 0), datetime.datetime(1983, 12, 8, 0, 0),
                      datetime.datetime(1984, 1, 6, 0, 0),
                      datetime.datetime(1984, 2, 4, 0, 0), datetime.datetime(1984, 3, 5, 0, 0),
                      datetime.datetime(1984, 4, 4, 0, 0),
                      datetime.datetime(1984, 5, 5, 0, 0), datetime.datetime(1984, 6, 5, 0, 0),
                      datetime.datetime(1984, 7, 7, 0, 0),
                      datetime.datetime(1984, 8, 7, 0, 0), datetime.datetime(1984, 9, 7, 0, 0),
                      datetime.datetime(1984, 10, 8, 0, 0),
                      datetime.datetime(1984, 11, 7, 0, 0), datetime.datetime(1984, 12, 7, 0, 0),
                      datetime.datetime(1985, 1, 6, 0, 0),
                      datetime.datetime(1985, 2, 4, 0, 0), datetime.datetime(1985, 3, 5, 0, 0),
                      datetime.datetime(1985, 4, 5, 0, 0),
                      datetime.datetime(1985, 5, 5, 0, 0), datetime.datetime(1985, 6, 6, 0, 0),
                      datetime.datetime(1985, 7, 7, 0, 0),
                      datetime.datetime(1985, 8, 7, 0, 0), datetime.datetime(1985, 9, 8, 0, 0),
                      datetime.datetime(1985, 10, 8, 0, 0),
                      datetime.datetime(1985, 11, 7, 0, 0), datetime.datetime(1985, 12, 7, 0, 0),
                      datetime.datetime(1986, 1, 5, 0, 0),
                      datetime.datetime(1986, 2, 4, 0, 0), datetime.datetime(1986, 3, 6, 0, 0),
                      datetime.datetime(1986, 4, 5, 0, 0),
                      datetime.datetime(1986, 5, 6, 0, 0), datetime.datetime(1986, 6, 6, 0, 0),
                      datetime.datetime(1986, 7, 7, 0, 0),
                      datetime.datetime(1986, 8, 8, 0, 0), datetime.datetime(1986, 9, 8, 0, 0),
                      datetime.datetime(1986, 10, 8, 0, 0),
                      datetime.datetime(1986, 11, 8, 0, 0), datetime.datetime(1986, 12, 7, 0, 0),
                      datetime.datetime(1987, 1, 5, 0, 0),
                      datetime.datetime(1987, 2, 4, 0, 0), datetime.datetime(1987, 3, 6, 0, 0),
                      datetime.datetime(1987, 4, 5, 0, 0),
                      datetime.datetime(1987, 5, 6, 0, 0), datetime.datetime(1987, 6, 6, 0, 0),
                      datetime.datetime(1987, 7, 7, 0, 0),
                      datetime.datetime(1987, 8, 8, 0, 0), datetime.datetime(1987, 9, 8, 0, 0),
                      datetime.datetime(1987, 10, 9, 0, 0),
                      datetime.datetime(1987, 11, 8, 0, 0), datetime.datetime(1987, 12, 7, 0, 0),
                      datetime.datetime(1988, 1, 6, 0, 0),
                      datetime.datetime(1988, 2, 4, 0, 0), datetime.datetime(1988, 3, 5, 0, 0),
                      datetime.datetime(1988, 4, 4, 0, 0),
                      datetime.datetime(1988, 5, 5, 0, 0), datetime.datetime(1988, 6, 5, 0, 0),
                      datetime.datetime(1988, 7, 7, 0, 0),
                      datetime.datetime(1988, 8, 7, 0, 0), datetime.datetime(1988, 9, 7, 0, 0),
                      datetime.datetime(1988, 10, 8, 0, 0),
                      datetime.datetime(1988, 11, 7, 0, 0), datetime.datetime(1988, 12, 7, 0, 0),
                      datetime.datetime(1989, 1, 6, 0, 0),
                      datetime.datetime(1989, 2, 4, 0, 0), datetime.datetime(1989, 3, 5, 0, 0),
                      datetime.datetime(1989, 4, 5, 0, 0),
                      datetime.datetime(1989, 5, 5, 0, 0), datetime.datetime(1989, 6, 6, 0, 0),
                      datetime.datetime(1989, 7, 7, 0, 0),
                      datetime.datetime(1989, 8, 7, 0, 0), datetime.datetime(1989, 9, 7, 0, 0),
                      datetime.datetime(1989, 10, 8, 0, 0),
                      datetime.datetime(1989, 11, 7, 0, 0), datetime.datetime(1989, 12, 7, 0, 0),
                      datetime.datetime(1990, 1, 5, 0, 0),
                      datetime.datetime(1990, 2, 4, 0, 0), datetime.datetime(1990, 3, 6, 0, 0),
                      datetime.datetime(1990, 4, 5, 0, 0),
                      datetime.datetime(1990, 5, 6, 0, 0), datetime.datetime(1990, 6, 6, 0, 0),
                      datetime.datetime(1990, 7, 7, 0, 0),
                      datetime.datetime(1990, 8, 8, 0, 0), datetime.datetime(1990, 9, 8, 0, 0),
                      datetime.datetime(1990, 10, 8, 0, 0),
                      datetime.datetime(1990, 11, 8, 0, 0), datetime.datetime(1990, 12, 7, 0, 0),
                      datetime.datetime(1991, 1, 5, 0, 0),
                      datetime.datetime(1991, 2, 4, 0, 0), datetime.datetime(1991, 3, 6, 0, 0),
                      datetime.datetime(1991, 4, 5, 0, 0),
                      datetime.datetime(1991, 5, 6, 0, 0), datetime.datetime(1991, 6, 6, 0, 0),
                      datetime.datetime(1991, 7, 7, 0, 0),
                      datetime.datetime(1991, 8, 8, 0, 0), datetime.datetime(1991, 9, 8, 0, 0),
                      datetime.datetime(1991, 10, 9, 0, 0),
                      datetime.datetime(1991, 11, 8, 0, 0), datetime.datetime(1991, 12, 7, 0, 0),
                      datetime.datetime(1992, 1, 6, 0, 0),
                      datetime.datetime(1992, 2, 4, 0, 0), datetime.datetime(1992, 3, 5, 0, 0),
                      datetime.datetime(1992, 4, 4, 0, 0),
                      datetime.datetime(1992, 5, 5, 0, 0), datetime.datetime(1992, 6, 5, 0, 0),
                      datetime.datetime(1992, 7, 7, 0, 0),
                      datetime.datetime(1992, 8, 7, 0, 0), datetime.datetime(1992, 9, 7, 0, 0),
                      datetime.datetime(1992, 10, 8, 0, 0),
                      datetime.datetime(1992, 11, 7, 0, 0), datetime.datetime(1992, 12, 7, 0, 0),
                      datetime.datetime(1993, 1, 6, 0, 0),
                      datetime.datetime(1993, 2, 4, 0, 0), datetime.datetime(1993, 3, 5, 0, 0),
                      datetime.datetime(1993, 4, 5, 0, 0),
                      datetime.datetime(1993, 5, 5, 0, 0), datetime.datetime(1993, 6, 6, 0, 0),
                      datetime.datetime(1993, 7, 7, 0, 0),
                      datetime.datetime(1993, 8, 7, 0, 0), datetime.datetime(1993, 9, 7, 0, 0),
                      datetime.datetime(1993, 10, 8, 0, 0),
                      datetime.datetime(1993, 11, 7, 0, 0), datetime.datetime(1993, 12, 7, 0, 0),
                      datetime.datetime(1994, 1, 5, 0, 0),
                      datetime.datetime(1994, 2, 4, 0, 0), datetime.datetime(1994, 3, 6, 0, 0),
                      datetime.datetime(1994, 4, 5, 0, 0),
                      datetime.datetime(1994, 5, 6, 0, 0), datetime.datetime(1994, 6, 6, 0, 0),
                      datetime.datetime(1994, 7, 7, 0, 0),
                      datetime.datetime(1994, 8, 8, 0, 0), datetime.datetime(1994, 9, 8, 0, 0),
                      datetime.datetime(1994, 10, 8, 0, 0),
                      datetime.datetime(1994, 11, 7, 0, 0), datetime.datetime(1994, 12, 7, 0, 0),
                      datetime.datetime(1995, 1, 5, 0, 0),
                      datetime.datetime(1995, 2, 4, 0, 0), datetime.datetime(1995, 3, 6, 0, 0),
                      datetime.datetime(1995, 4, 5, 0, 0),
                      datetime.datetime(1995, 5, 6, 0, 0), datetime.datetime(1995, 6, 6, 0, 0),
                      datetime.datetime(1995, 7, 7, 0, 0),
                      datetime.datetime(1995, 8, 8, 0, 0), datetime.datetime(1995, 9, 8, 0, 0),
                      datetime.datetime(1995, 10, 9, 0, 0),
                      datetime.datetime(1995, 11, 8, 0, 0), datetime.datetime(1995, 12, 7, 0, 0),
                      datetime.datetime(1996, 1, 6, 0, 0),
                      datetime.datetime(1996, 2, 4, 0, 0), datetime.datetime(1996, 3, 5, 0, 0),
                      datetime.datetime(1996, 4, 4, 0, 0),
                      datetime.datetime(1996, 5, 5, 0, 0), datetime.datetime(1996, 6, 5, 0, 0),
                      datetime.datetime(1996, 7, 7, 0, 0),
                      datetime.datetime(1996, 8, 7, 0, 0), datetime.datetime(1996, 9, 7, 0, 0),
                      datetime.datetime(1996, 10, 8, 0, 0),
                      datetime.datetime(1996, 11, 7, 0, 0), datetime.datetime(1996, 12, 7, 0, 0),
                      datetime.datetime(1997, 1, 6, 0, 0),
                      datetime.datetime(1997, 2, 4, 0, 0), datetime.datetime(1997, 3, 5, 0, 0),
                      datetime.datetime(1997, 4, 5, 0, 0),
                      datetime.datetime(1997, 5, 5, 0, 0), datetime.datetime(1997, 6, 5, 0, 0),
                      datetime.datetime(1997, 7, 7, 0, 0),
                      datetime.datetime(1997, 8, 7, 0, 0), datetime.datetime(1997, 9, 7, 0, 0),
                      datetime.datetime(1997, 10, 8, 0, 0),
                      datetime.datetime(1997, 11, 7, 0, 0), datetime.datetime(1997, 12, 7, 0, 0),
                      datetime.datetime(1998, 1, 5, 0, 0),
                      datetime.datetime(1998, 2, 4, 0, 0), datetime.datetime(1998, 3, 6, 0, 0),
                      datetime.datetime(1998, 4, 5, 0, 0),
                      datetime.datetime(1998, 5, 6, 0, 0), datetime.datetime(1998, 6, 6, 0, 0),
                      datetime.datetime(1998, 7, 7, 0, 0),
                      datetime.datetime(1998, 8, 8, 0, 0), datetime.datetime(1998, 9, 8, 0, 0),
                      datetime.datetime(1998, 10, 8, 0, 0),
                      datetime.datetime(1998, 11, 7, 0, 0), datetime.datetime(1998, 12, 7, 0, 0),
                      datetime.datetime(1999, 1, 5, 0, 0),
                      datetime.datetime(1999, 2, 4, 0, 0), datetime.datetime(1999, 3, 6, 0, 0),
                      datetime.datetime(1999, 4, 5, 0, 0),
                      datetime.datetime(1999, 5, 6, 0, 0), datetime.datetime(1999, 6, 6, 0, 0),
                      datetime.datetime(1999, 7, 7, 0, 0),
                      datetime.datetime(1999, 8, 8, 0, 0), datetime.datetime(1999, 9, 8, 0, 0),
                      datetime.datetime(1999, 10, 9, 0, 0),
                      datetime.datetime(1999, 11, 8, 0, 0), datetime.datetime(1999, 12, 7, 0, 0),
                      datetime.datetime(2000, 1, 6, 0, 0),
                      datetime.datetime(2000, 2, 4, 0, 0), datetime.datetime(2000, 3, 5, 0, 0),
                      datetime.datetime(2000, 4, 4, 0, 0),
                      datetime.datetime(2000, 5, 5, 0, 0), datetime.datetime(2000, 6, 5, 0, 0),
                      datetime.datetime(2000, 7, 7, 0, 0),
                      datetime.datetime(2000, 8, 7, 0, 0), datetime.datetime(2000, 9, 7, 0, 0),
                      datetime.datetime(2000, 10, 8, 0, 0),
                      datetime.datetime(2000, 11, 7, 0, 0), datetime.datetime(2000, 12, 7, 0, 0),
                      datetime.datetime(2001, 1, 6, 0, 0),
                      datetime.datetime(2001, 2, 4, 0, 0), datetime.datetime(2001, 3, 5, 0, 0),
                      datetime.datetime(2001, 4, 5, 0, 0),
                      datetime.datetime(2001, 5, 5, 0, 0), datetime.datetime(2001, 6, 5, 0, 0),
                      datetime.datetime(2001, 7, 7, 0, 0),
                      datetime.datetime(2001, 8, 7, 0, 0), datetime.datetime(2001, 9, 7, 0, 0),
                      datetime.datetime(2001, 10, 8, 0, 0),
                      datetime.datetime(2001, 11, 7, 0, 0), datetime.datetime(2001, 12, 7, 0, 0),
                      datetime.datetime(2002, 1, 5, 0, 0),
                      datetime.datetime(2002, 2, 4, 0, 0), datetime.datetime(2002, 3, 6, 0, 0),
                      datetime.datetime(2002, 4, 5, 0, 0),
                      datetime.datetime(2002, 5, 6, 0, 0), datetime.datetime(2002, 6, 6, 0, 0),
                      datetime.datetime(2002, 7, 7, 0, 0),
                      datetime.datetime(2002, 8, 8, 0, 0), datetime.datetime(2002, 9, 8, 0, 0),
                      datetime.datetime(2002, 10, 8, 0, 0),
                      datetime.datetime(2002, 11, 7, 0, 0), datetime.datetime(2002, 12, 7, 0, 0),
                      datetime.datetime(2003, 1, 5, 0, 0),
                      datetime.datetime(2003, 2, 4, 0, 0), datetime.datetime(2003, 3, 6, 0, 0),
                      datetime.datetime(2003, 4, 5, 0, 0),
                      datetime.datetime(2003, 5, 6, 0, 0), datetime.datetime(2003, 6, 6, 0, 0),
                      datetime.datetime(2003, 7, 7, 0, 0),
                      datetime.datetime(2003, 8, 8, 0, 0), datetime.datetime(2003, 9, 8, 0, 0),
                      datetime.datetime(2003, 10, 9, 0, 0),
                      datetime.datetime(2003, 11, 8, 0, 0), datetime.datetime(2003, 12, 7, 0, 0),
                      datetime.datetime(2004, 1, 6, 0, 0),
                      datetime.datetime(2004, 2, 4, 0, 0), datetime.datetime(2004, 3, 5, 0, 0),
                      datetime.datetime(2004, 4, 4, 0, 0),
                      datetime.datetime(2004, 5, 5, 0, 0), datetime.datetime(2004, 6, 5, 0, 0),
                      datetime.datetime(2004, 7, 7, 0, 0),
                      datetime.datetime(2004, 8, 7, 0, 0), datetime.datetime(2004, 9, 7, 0, 0),
                      datetime.datetime(2004, 10, 8, 0, 0),
                      datetime.datetime(2004, 11, 7, 0, 0), datetime.datetime(2004, 12, 7, 0, 0),
                      datetime.datetime(2005, 1, 6, 0, 0),
                      datetime.datetime(2005, 2, 4, 0, 0), datetime.datetime(2005, 3, 5, 0, 0),
                      datetime.datetime(2005, 4, 5, 0, 0),
                      datetime.datetime(2005, 5, 5, 0, 0), datetime.datetime(2005, 6, 5, 0, 0),
                      datetime.datetime(2005, 7, 7, 0, 0),
                      datetime.datetime(2005, 8, 7, 0, 0), datetime.datetime(2005, 9, 7, 0, 0),
                      datetime.datetime(2005, 10, 8, 0, 0),
                      datetime.datetime(2005, 11, 7, 0, 0), datetime.datetime(2005, 12, 7, 0, 0),
                      datetime.datetime(2006, 1, 5, 0, 0),
                      datetime.datetime(2006, 2, 4, 0, 0), datetime.datetime(2006, 3, 6, 0, 0),
                      datetime.datetime(2006, 4, 5, 0, 0),
                      datetime.datetime(2006, 5, 5, 0, 0), datetime.datetime(2006, 6, 6, 0, 0),
                      datetime.datetime(2006, 7, 7, 0, 0),
                      datetime.datetime(2006, 8, 7, 0, 0), datetime.datetime(2006, 9, 8, 0, 0),
                      datetime.datetime(2006, 10, 8, 0, 0),
                      datetime.datetime(2006, 11, 7, 0, 0), datetime.datetime(2006, 12, 7, 0, 0),
                      datetime.datetime(2007, 1, 5, 0, 0),
                      datetime.datetime(2007, 2, 4, 0, 0), datetime.datetime(2007, 3, 6, 0, 0),
                      datetime.datetime(2007, 4, 5, 0, 0),
                      datetime.datetime(2007, 5, 6, 0, 0), datetime.datetime(2007, 6, 6, 0, 0),
                      datetime.datetime(2007, 7, 7, 0, 0),
                      datetime.datetime(2007, 8, 8, 0, 0), datetime.datetime(2007, 9, 8, 0, 0),
                      datetime.datetime(2007, 10, 9, 0, 0),
                      datetime.datetime(2007, 11, 8, 0, 0), datetime.datetime(2007, 12, 7, 0, 0),
                      datetime.datetime(2008, 1, 6, 0, 0),
                      datetime.datetime(2008, 2, 4, 0, 0), datetime.datetime(2008, 3, 5, 0, 0),
                      datetime.datetime(2008, 4, 4, 0, 0),
                      datetime.datetime(2008, 5, 5, 0, 0), datetime.datetime(2008, 6, 5, 0, 0),
                      datetime.datetime(2008, 7, 7, 0, 0),
                      datetime.datetime(2008, 8, 7, 0, 0), datetime.datetime(2008, 9, 7, 0, 0),
                      datetime.datetime(2008, 10, 8, 0, 0),
                      datetime.datetime(2008, 11, 7, 0, 0), datetime.datetime(2008, 12, 7, 0, 0),
                      datetime.datetime(2009, 1, 6, 0, 0),
                      datetime.datetime(2009, 2, 4, 0, 0), datetime.datetime(2009, 3, 5, 0, 0),
                      datetime.datetime(2009, 4, 4, 0, 0),
                      datetime.datetime(2009, 5, 5, 0, 0), datetime.datetime(2009, 6, 5, 0, 0),
                      datetime.datetime(2009, 7, 7, 0, 0),
                      datetime.datetime(2009, 8, 7, 0, 0), datetime.datetime(2009, 9, 7, 0, 0),
                      datetime.datetime(2009, 10, 8, 0, 0),
                      datetime.datetime(2009, 11, 7, 0, 0), datetime.datetime(2009, 12, 7, 0, 0),
                      datetime.datetime(2010, 1, 5, 0, 0),
                      datetime.datetime(2010, 2, 4, 0, 0), datetime.datetime(2010, 3, 6, 0, 0),
                      datetime.datetime(2010, 4, 5, 0, 0),
                      datetime.datetime(2010, 5, 5, 0, 0), datetime.datetime(2010, 6, 6, 0, 0),
                      datetime.datetime(2010, 7, 7, 0, 0),
                      datetime.datetime(2010, 8, 7, 0, 0), datetime.datetime(2010, 9, 8, 0, 0),
                      datetime.datetime(2010, 10, 8, 0, 0),
                      datetime.datetime(2010, 11, 7, 0, 0), datetime.datetime(2010, 12, 7, 0, 0),
                      datetime.datetime(2011, 1, 5, 0, 0),
                      datetime.datetime(2011, 2, 4, 0, 0), datetime.datetime(2011, 3, 6, 0, 0),
                      datetime.datetime(2011, 4, 5, 0, 0),
                      datetime.datetime(2011, 5, 6, 0, 0), datetime.datetime(2011, 6, 6, 0, 0),
                      datetime.datetime(2011, 7, 7, 0, 0),
                      datetime.datetime(2011, 8, 8, 0, 0), datetime.datetime(2011, 9, 8, 0, 0),
                      datetime.datetime(2011, 10, 8, 0, 0),
                      datetime.datetime(2011, 11, 8, 0, 0), datetime.datetime(2011, 12, 7, 0, 0),
                      datetime.datetime(2012, 1, 6, 0, 0),
                      datetime.datetime(2012, 2, 4, 0, 0), datetime.datetime(2012, 3, 5, 0, 0),
                      datetime.datetime(2012, 4, 4, 0, 0),
                      datetime.datetime(2012, 5, 5, 0, 0), datetime.datetime(2012, 6, 5, 0, 0),
                      datetime.datetime(2012, 7, 7, 0, 0),
                      datetime.datetime(2012, 8, 7, 0, 0), datetime.datetime(2012, 9, 7, 0, 0),
                      datetime.datetime(2012, 10, 8, 0, 0),
                      datetime.datetime(2012, 11, 7, 0, 0), datetime.datetime(2012, 12, 7, 0, 0),
                      datetime.datetime(2013, 1, 6, 0, 0),
                      datetime.datetime(2013, 2, 4, 0, 0), datetime.datetime(2013, 3, 5, 0, 0),
                      datetime.datetime(2013, 4, 4, 0, 0),
                      datetime.datetime(2013, 5, 5, 0, 0), datetime.datetime(2013, 6, 5, 0, 0),
                      datetime.datetime(2013, 7, 7, 0, 0),
                      datetime.datetime(2013, 8, 7, 0, 0), datetime.datetime(2013, 9, 7, 0, 0),
                      datetime.datetime(2013, 10, 8, 0, 0),
                      datetime.datetime(2013, 11, 7, 0, 0), datetime.datetime(2013, 12, 7, 0, 0),
                      datetime.datetime(2014, 1, 5, 0, 0),
                      datetime.datetime(2014, 2, 4, 0, 0), datetime.datetime(2014, 3, 6, 0, 0),
                      datetime.datetime(2014, 4, 5, 0, 0),
                      datetime.datetime(2014, 5, 5, 0, 0), datetime.datetime(2014, 6, 6, 0, 0),
                      datetime.datetime(2014, 7, 7, 0, 0),
                      datetime.datetime(2014, 8, 7, 0, 0), datetime.datetime(2014, 9, 8, 0, 0),
                      datetime.datetime(2014, 10, 8, 0, 0),
                      datetime.datetime(2014, 11, 7, 0, 0), datetime.datetime(2014, 12, 7, 0, 0),
                      datetime.datetime(2015, 1, 5, 0, 0),
                      datetime.datetime(2015, 2, 4, 0, 0), datetime.datetime(2015, 3, 6, 0, 0),
                      datetime.datetime(2015, 4, 5, 0, 0),
                      datetime.datetime(2015, 5, 6, 0, 0), datetime.datetime(2015, 6, 6, 0, 0),
                      datetime.datetime(2015, 7, 7, 0, 0),
                      datetime.datetime(2015, 8, 8, 0, 0), datetime.datetime(2015, 9, 8, 0, 0),
                      datetime.datetime(2015, 10, 8, 0, 0),
                      datetime.datetime(2015, 11, 8, 0, 0), datetime.datetime(2015, 12, 7, 0, 0),
                      datetime.datetime(2016, 1, 6, 0, 0),
                      datetime.datetime(2016, 2, 4, 0, 0), datetime.datetime(2016, 3, 5, 0, 0),
                      datetime.datetime(2016, 4, 4, 0, 0),
                      datetime.datetime(2016, 5, 5, 0, 0), datetime.datetime(2016, 6, 5, 0, 0),
                      datetime.datetime(2016, 7, 7, 0, 0),
                      datetime.datetime(2016, 8, 7, 0, 0), datetime.datetime(2016, 9, 7, 0, 0),
                      datetime.datetime(2016, 10, 8, 0, 0),
                      datetime.datetime(2016, 11, 7, 0, 0), datetime.datetime(2016, 12, 7, 0, 0),
                      datetime.datetime(2017, 1, 6, 0, 0),
                      datetime.datetime(2017, 2, 3, 0, 0), datetime.datetime(2017, 3, 5, 0, 0),
                      datetime.datetime(2017, 4, 4, 0, 0),
                      datetime.datetime(2017, 5, 5, 0, 0), datetime.datetime(2017, 6, 5, 0, 0),
                      datetime.datetime(2017, 7, 7, 0, 0),
                      datetime.datetime(2017, 8, 7, 0, 0), datetime.datetime(2017, 9, 7, 0, 0),
                      datetime.datetime(2017, 10, 8, 0, 0),
                      datetime.datetime(2017, 11, 7, 0, 0), datetime.datetime(2017, 12, 7, 0, 0),
                      datetime.datetime(2018, 1, 5, 0, 0),
                      datetime.datetime(2018, 2, 4, 0, 0), datetime.datetime(2018, 3, 5, 0, 0),
                      datetime.datetime(2018, 4, 5, 0, 0),
                      datetime.datetime(2018, 5, 5, 0, 0), datetime.datetime(2018, 6, 6, 0, 0),
                      datetime.datetime(2018, 7, 7, 0, 0),
                      datetime.datetime(2018, 8, 7, 0, 0), datetime.datetime(2018, 9, 8, 0, 0),
                      datetime.datetime(2018, 10, 8, 0, 0),
                      datetime.datetime(2018, 11, 7, 0, 0), datetime.datetime(2018, 12, 7, 0, 0),
                      datetime.datetime(2019, 1, 5, 0, 0),
                      datetime.datetime(2019, 2, 4, 0, 0), datetime.datetime(2019, 3, 6, 0, 0),
                      datetime.datetime(2019, 4, 5, 0, 0),
                      datetime.datetime(2019, 5, 6, 0, 0), datetime.datetime(2019, 6, 6, 0, 0),
                      datetime.datetime(2019, 7, 7, 0, 0),
                      datetime.datetime(2019, 8, 8, 0, 0), datetime.datetime(2019, 9, 8, 0, 0),
                      datetime.datetime(2019, 10, 8, 0, 0),
                      datetime.datetime(2019, 11, 8, 0, 0), datetime.datetime(2019, 12, 7, 0, 0),
                      datetime.datetime(2020, 1, 5, 0, 0),
                      datetime.datetime(2020, 2, 4, 0, 0), datetime.datetime(2020, 3, 5, 0, 0),
                      datetime.datetime(2020, 4, 4, 0, 0),
                      datetime.datetime(2020, 5, 5, 0, 0), datetime.datetime(2020, 6, 5, 0, 0),
                      datetime.datetime(2020, 7, 6, 0, 0),
                      datetime.datetime(2020, 8, 7, 0, 0), datetime.datetime(2020, 9, 7, 0, 0),
                      datetime.datetime(2020, 10, 8, 0, 0),
                      datetime.datetime(2020, 11, 7, 0, 0), datetime.datetime(2020, 12, 7, 0, 0),
                      datetime.datetime(2021, 1, 6, 0, 0),
                      datetime.datetime(2021, 2, 3, 0, 0), datetime.datetime(2021, 3, 5, 0, 0),
                      datetime.datetime(2021, 4, 4, 0, 0),
                      datetime.datetime(2021, 5, 5, 0, 0), datetime.datetime(2021, 6, 5, 0, 0),
                      datetime.datetime(2021, 7, 7, 0, 0),
                      datetime.datetime(2021, 8, 7, 0, 0), datetime.datetime(2021, 9, 7, 0, 0),
                      datetime.datetime(2021, 10, 8, 0, 0),
                      datetime.datetime(2021, 11, 7, 0, 0), datetime.datetime(2021, 12, 7, 0, 0),
                      datetime.datetime(2022, 1, 5, 0, 0),
                      datetime.datetime(2022, 2, 4, 0, 0), datetime.datetime(2022, 3, 5, 0, 0),
                      datetime.datetime(2022, 4, 5, 0, 0),
                      datetime.datetime(2022, 5, 5, 0, 0), datetime.datetime(2022, 6, 6, 0, 0),
                      datetime.datetime(2022, 7, 7, 0, 0),
                      datetime.datetime(2022, 8, 7, 0, 0), datetime.datetime(2022, 9, 7, 0, 0),
                      datetime.datetime(2022, 10, 8, 0, 0),
                      datetime.datetime(2022, 11, 7, 0, 0), datetime.datetime(2022, 12, 7, 0, 0),
                      datetime.datetime(2023, 1, 5, 0, 0),
                      datetime.datetime(2023, 2, 4, 0, 0), datetime.datetime(2023, 3, 6, 0, 0),
                      datetime.datetime(2023, 4, 5, 0, 0),
                      datetime.datetime(2023, 5, 6, 0, 0), datetime.datetime(2023, 6, 6, 0, 0),
                      datetime.datetime(2023, 7, 7, 0, 0),
                      datetime.datetime(2023, 8, 8, 0, 0), datetime.datetime(2023, 9, 8, 0, 0),
                      datetime.datetime(2023, 10, 8, 0, 0),
                      datetime.datetime(2023, 11, 8, 0, 0), datetime.datetime(2023, 12, 7, 0, 0),
                      datetime.datetime(2024, 1, 5, 0, 0),
                      datetime.datetime(2024, 2, 4, 0, 0), datetime.datetime(2024, 3, 5, 0, 0),
                      datetime.datetime(2024, 4, 4, 0, 0),
                      datetime.datetime(2024, 5, 5, 0, 0), datetime.datetime(2024, 6, 5, 0, 0),
                      datetime.datetime(2024, 7, 6, 0, 0),
                      datetime.datetime(2024, 8, 7, 0, 0), datetime.datetime(2024, 9, 7, 0, 0),
                      datetime.datetime(2024, 10, 8, 0, 0),
                      datetime.datetime(2024, 11, 7, 0, 0), datetime.datetime(2024, 12, 6, 0, 0),
                      datetime.datetime(2025, 1, 6, 0, 0),
                      datetime.datetime(2025, 2, 3, 0, 0), datetime.datetime(2025, 3, 5, 0, 0),
                      datetime.datetime(2025, 4, 4, 0, 0),
                      datetime.datetime(2025, 5, 5, 0, 0), datetime.datetime(2025, 6, 5, 0, 0),
                      datetime.datetime(2025, 7, 7, 0, 0),
                      datetime.datetime(2025, 8, 7, 0, 0), datetime.datetime(2025, 9, 7, 0, 0),
                      datetime.datetime(2025, 10, 8, 0, 0),
                      datetime.datetime(2025, 11, 7, 0, 0), datetime.datetime(2025, 12, 7, 0, 0),
                      datetime.datetime(2026, 1, 5, 0, 0),
                      datetime.datetime(2026, 2, 4, 0, 0), datetime.datetime(2026, 3, 5, 0, 0),
                      datetime.datetime(2026, 4, 5, 0, 0),
                      datetime.datetime(2026, 5, 5, 0, 0), datetime.datetime(2026, 6, 5, 0, 0),
                      datetime.datetime(2026, 7, 7, 0, 0),
                      datetime.datetime(2026, 8, 7, 0, 0), datetime.datetime(2026, 9, 7, 0, 0),
                      datetime.datetime(2026, 10, 8, 0, 0),
                      datetime.datetime(2026, 11, 7, 0, 0), datetime.datetime(2026, 12, 7, 0, 0),
                      datetime.datetime(2027, 1, 5, 0, 0),
                      datetime.datetime(2027, 2, 4, 0, 0), datetime.datetime(2027, 3, 6, 0, 0),
                      datetime.datetime(2027, 4, 5, 0, 0),
                      datetime.datetime(2027, 5, 6, 0, 0), datetime.datetime(2027, 6, 6, 0, 0),
                      datetime.datetime(2027, 7, 7, 0, 0),
                      datetime.datetime(2027, 8, 8, 0, 0), datetime.datetime(2027, 9, 8, 0, 0),
                      datetime.datetime(2027, 10, 8, 0, 0),
                      datetime.datetime(2027, 11, 7, 0, 0), datetime.datetime(2027, 12, 7, 0, 0),
                      datetime.datetime(2028, 1, 5, 0, 0),
                      datetime.datetime(2028, 2, 4, 0, 0), datetime.datetime(2028, 3, 5, 0, 0),
                      datetime.datetime(2028, 4, 4, 0, 0),
                      datetime.datetime(2028, 5, 5, 0, 0), datetime.datetime(2028, 6, 5, 0, 0),
                      datetime.datetime(2028, 7, 6, 0, 0),
                      datetime.datetime(2028, 8, 7, 0, 0), datetime.datetime(2028, 9, 7, 0, 0),
                      datetime.datetime(2028, 10, 8, 0, 0),
                      datetime.datetime(2028, 11, 7, 0, 0), datetime.datetime(2028, 12, 6, 0, 0),
                      datetime.datetime(2029, 1, 6, 0, 0),
                      datetime.datetime(2029, 2, 3, 0, 0), datetime.datetime(2029, 3, 5, 0, 0),
                      datetime.datetime(2029, 4, 4, 0, 0),
                      datetime.datetime(2029, 5, 5, 0, 0), datetime.datetime(2029, 6, 5, 0, 0),
                      datetime.datetime(2029, 7, 7, 0, 0),
                      datetime.datetime(2029, 8, 7, 0, 0), datetime.datetime(2029, 9, 7, 0, 0),
                      datetime.datetime(2029, 10, 8, 0, 0),
                      datetime.datetime(2029, 11, 7, 0, 0), datetime.datetime(2029, 12, 7, 0, 0),
                      datetime.datetime(2030, 1, 5, 0, 0),
                      datetime.datetime(2030, 2, 4, 0, 0), datetime.datetime(2030, 3, 5, 0, 0),
                      datetime.datetime(2030, 4, 5, 0, 0),
                      datetime.datetime(2030, 5, 5, 0, 0), datetime.datetime(2030, 6, 5, 0, 0),
                      datetime.datetime(2030, 7, 7, 0, 0),
                      datetime.datetime(2030, 8, 7, 0, 0), datetime.datetime(2030, 9, 7, 0, 0),
                      datetime.datetime(2030, 10, 8, 0, 0),
                      datetime.datetime(2030, 11, 7, 0, 0), datetime.datetime(2030, 12, 7, 0, 0),
                      datetime.datetime(2030, 1, 5, 0, 0)]

        self.__Tian_Gan = {0: '甲', 1: '乙', 2: '丙', 3: '丁', 4: '戊', 5: '己', 6: '庚', 7: '辛', 8: '壬', 9: '癸'}

        self.__Di_Zhi = {0: '寅', 1: '卯', 2: '辰', 3: '巳', 4: '午', 5: '未', 6: '申', 7: '酉', 8: '戌', 9: '亥', 10: '子', 11: '丑', }

        self.__Hour_Dz = {1: '子', 2: '丑',3: '寅', 4: '卯', 5: '辰', 6: '巳', 7: '午', 8: '未', 9: '申', 10: '酉', 11: '戌', 0: '亥'}

        self.__kongwang = {1: '子', 2: '丑',3: '寅', 4: '卯', 5: '辰', 6: '巳', 7: '午', 8: '未', 9: '申', 10: '酉', 11: '戌', 0: '亥'}

        self.__Sex = ['女', '男']

        self.__SixtyJZ = ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉", "甲戌", "乙亥",
                     "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未", "甲申", "乙酉", "丙戌", "丁亥", "戊子",
                     "己丑", "庚寅", "辛卯", "壬辰", "癸巳", "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑",
                     "壬寅", "癸卯", "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑", "甲寅",
                     "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]

        self.year = y
        self.month = m
        self.day = d
        self.hour = h
        self.input_day = datetime.datetime(self.year, self.month, self.day, self.hour)
        self.hour_num = self.input_day - self.stardard_day

    def Time(self):  #  八字排盘主程序，元祖序列[0]为八字，排列为年干，年支，月干，月支，日干，日支，时干，时支。元祖序列[1]为空亡
    # def Year(self):

        """把输入的时间插入时间列表"""
        self.list_num = datetime.datetime(self.year, self.month, self.day)

        if self.list_num in self.__Jie:
            self.__Jie.append(self.list_num)
            self.__Jie.sort()
            self.mid_num = self.__Jie.index(self.list_num) + 1  # self.mid_num是插入的年份在列表中的位置
            # print(self.__Jie[self.mid_num-1],self.__Jie[self.mid_num],self.__Jie[self.mid_num+1])
        elif self.list_num not in self.__Jie:
            self.__Jie.append(self.list_num)
            self.__Jie.sort()
            self.mid_num = self.__Jie.index(self.list_num)  # mid_num代表输入时间在时间列表中的位置
            # print("midnum: ",self.mid_num)
            # print(self.__Jie[self.mid_num - 1], self.__Jie[self.mid_num], self.__Jie[self.mid_num + 1])
        if self.mid_num % 12 == 0:
            self.year_num = (self.mid_num - 1) // 12
        else:
            self.year_num = self.mid_num // 12

        self.tiangan_y = (self.year_num + 6) % 10  # 1970年是庚戌年，
        self.dizhi_y = (self.year_num + 8) % 12
        # print(self.mid_num%12,self.year_num,self.tiangan_y,self.dizhi_y)
        self.tiangan_year = self.__Tian_Gan[self.tiangan_y]
        self.dizhi_year = self.__Di_Zhi[self.dizhi_y]

        #     return self.tiangan_year, self.dizhi_year
        #
    # def Month(self):

        self.month_num = self.mid_num % 12 + 1
        self.dizhi_m = (self.month_num + 10) % 12  # 算出月柱地支

        if self.tiangan_y == 0 or self.tiangan_y == 5:
            self.tiangan_mid = 2
        elif self.tiangan_y == 1 or self.tiangan_y == 6:
            self.tiangan_mid = 4
        elif self.tiangan_y == 2 or self.tiangan_y == 7:
            self.tiangan_mid = 6
        elif self.tiangan_y == 3 or self.tiangan_y == 8:
            self.tiangan_mid = 8
        elif self.tiangan_y == 4 or self.tiangan_y == 9:
            self.tiangan_mid = 0

        self.tiangan_m = (self.tiangan_mid + self.dizhi_m) % 10
        self.tiangan_month = self.__Tian_Gan[self.tiangan_m]
        self.dizhi_month = self.__Di_Zhi[self.dizhi_m]
        # print(self.tiangan_month,self.dizhi_month)
        #     return self.tiangan_month, self.dizhi_month
        #
    # def Day(self):

        self.date_num = int((datetime.datetime(self.year, self.month, self.day) - self.stardard_day).days)
        self.day_num = self.date_num % 60
        # print("day number:",self.day_num)
        self.day_tg = (self.day_num + 2) % 10
        self.day_dz = (self.day_num + 2) % 12
        self.tiangan_day = self.__Tian_Gan[self.day_tg]
        self.dizhi_day = self.__Di_Zhi[self.day_dz]
        self.hour_num = (datetime.datetime(self.year, self.month, self.day, self.hour) - self.stardard_day).seconds
        if self.hour_num == 0:
            self.day_tg = self.day_tg + 1
            self.day_dz = self.day_dz + 1
            self.tiangan_day = self.__Tian_Gan[(self.day_tg) % 10]
            self.dizhi_day = self.__Di_Zhi[(self.day_dz) % 12]
        # print(self.tiangan_day , self.dizhi_day)
        #     return self.tiangan_day , self.dizhi_day
        #
    # def Hour(self):

        self.hour_num = (int(
            (datetime.datetime(self.year, self.month, self.day, self.hour) - self.stardard_day).seconds / 3600)) // 2
        self.hour_dz = self.hour_num + 1

        if self.day_tg % 10 == 0 or self.day_tg % 10 == 5:
            self.hour_tg = 0
        elif self.day_tg % 10 == 1 or self.day_tg % 10 == 6:
            self.hour_tg = 2
        elif self.day_tg % 10 == 2 or self.day_tg % 10 == 7:
            self.hour_tg = 4
        elif self.day_tg % 10 == 3 or self.day_tg % 10 == 8:
            self.hour_tg = 6
        elif self.day_tg % 10 == 4 or self.day_tg % 10 == 9:
            self.hour_tg = 8

        self.tiangan_h = (self.hour_tg + self.hour_dz - 1) % 10

        self.tiangan_hour = self.__Tian_Gan[self.tiangan_h]
        self.dizhi_hour = self.__Hour_Dz[self.hour_dz % 12]

        # return self.tiangan_hour, self.dizhi_hour, self.hour_dz, self.hour_tg

    # def KongWang(self):
        self.new_day_tg = self.day_tg + 1
        self.new_day_dz = (self.day_dz + 3) % 12

        self.kw_1 = (self.new_day_dz - self.new_day_tg + 12) % 12
        self.kw_2 = (self.kw_1 - 1 + 12) % 12
        self.kongwang1 = self.__kongwang[self.kw_1 % 12]
        self.kongwang2 = self.__kongwang[self.kw_2 % 12]
        # return self.kongwang1, self.kongwang2, self.kongwang, self.kongwang_previous   #  空亡

    def QiYun(self,sex):  #  sex:男为1，女为0  此为排大运主程序，输出元祖[0]为字典形式大运，元祖[1]为起运年份
        self.Time()
        self.dayun_list = []
        if sex == "男":
            self.sex = 1
        elif sex == "女":
            self.sex = 0

        mid_num = 0
        if (self.sex == 1 and self.tiangan_y % 2 == 0) or (self.sex == 0 and self.tiangan_y % 2 == 1):
            if (self.sex == 1 and self.tiangan_y % 2 == 0) or (self.sex == 0 and self.tiangan_y % 2 == 1):  # 阳男阴女顺排
                """mid_num，即这个时间所在列表的位置已经确定"""
                if self.list_num in self.__Jie:
                    mid_num = self.mid_num + 1
                self.jie_num = mid_num
                self.jie = self.__Jie[self.jie_num]
                self.qiyun_num = ((self.jie - datetime.datetime(self.year, self.month, self.day)).days) // 3
                self.qiyun_year = str(self.year + self.qiyun_num)

            qiyun = str(self.tiangan_month + self.dizhi_month)
            qiyun_num = self.__SixtyJZ.index(qiyun)
            for i in range(1,8):
                dayun_num = (qiyun_num + i) % 60
                self.dayun = self.__SixtyJZ[dayun_num]
                self.dayun_year = int(self.qiyun_year) + i * 10
                self.dayun_list.append((self.dayun,self.dayun_year))
                # self.dayun_dict[self.dayun] = self.dayun_year
                # print(self.dayun_dict)

        elif (self.sex == 1 and self.tiangan_y % 2 == 1) or (self.sex == 0 and self.tiangan_y % 2 == 0):
            if self.list_num in self.__Jie:
                mid_num = self.mid_num - 1

            self.jie_num = mid_num - 1
            self.jie = self.__Jie[self.jie_num]
            self.qiyun_num = ((datetime.datetime(self.year,self.month, self.day) - self.jie).days) // 3  # 和上一个节相差的天数除以3取整
            self.qiyun_year = str(self.year + self.qiyun_num)
            qiyun = str(self.tiangan_month + self.dizhi_month)
            qiyun_num = self.__SixtyJZ.index(qiyun)
            for i in range(1, 8):
                dayun_num = (qiyun_num - i + 60) % 60
                self.dayun = self.__SixtyJZ[dayun_num]
                self.dayun_year = int(self.qiyun_year) + i * 10
                self.dayun_list.append((self.dayun, self.dayun_year))
                # self.dayun_dict[self.dayun] = self.dayun_year
                # print(self.dayun_dict)
        # print(self.sex, type(self.sex))
        return self.dayun_list, self.qiyun_year



    def pre_Bazi_words(self):   #  输出文字版八字程序，元祖序列[0]为八字，排列为年干，年支，月干，月支，日干，日支，时
        # 干，时支。元祖序列[1]为空亡
        self.Time()
        res = [self.tiangan_year , self.dizhi_year , self.tiangan_month , self.dizhi_month , self.tiangan_day ,\
              self.dizhi_day , self.tiangan_hour , self.dizhi_hour]
        res_kw = [self.kongwang2 , self.kongwang1]
        # print(type(self.tiangan_year))
        return res , res_kw


class Bazi_Number(BaziPaipan):  #   输出数字版八字程序，元祖序列[0]为八字，排列为年干，年支，月干，月支，日干，日支，时
        # 干，时支。元祖序列[1]为空亡

    __tgdz = ["占","甲","乙","丙","丁","戊","己","庚","辛","壬","癸","子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

    def Bazi_Num(self):   #   输出数字版八字程序
        super().Time()
        super().pre_Bazi_words()
        res = [self.__tgdz.index(self.tiangan_year) , self.__tgdz.index(self.dizhi_year) , self.__tgdz.index(self.tiangan_month) , self.__tgdz.index(self.dizhi_month) , self.__tgdz.index(self.tiangan_day) , \
              self.__tgdz.index(self.dizhi_day) , self.__tgdz.index(self.tiangan_hour) , self.__tgdz.index(self.dizhi_hour)]
        res_kw = [self.__tgdz.index(self.kongwang1) , self.__tgdz.index(self.kongwang2)]

        return res , res_kw


class TenGods(object):   # 输出十神，十神为文字版和数字版，"比肩","劫财","食神","伤官","偏财","正财","偏官","正官","偏印","正印"分别为0-9

    __TGDZ = {
        "甲":1,"乙":1,"丙":2,"丁":2,"戊":3,"己":3,"庚":4,"辛":4,"壬":0,"癸":0,"子":0,"丑":3,"寅":1,"卯":1,"辰":3,"巳":2,"午":2,"未":3,"申":4,"酉":4,"戌":3,"亥":0
    }

    __TGDZ_Num = {
        "甲": 1, "乙": 2, "丙": 3, "丁": 4, "戊": 5, "己": 6, "庚": 7, "辛": 8, "壬": 9, "癸": 10,
        "子": 1, "丑": 2, "寅": 3, "卯": 4, "辰": 5, "巳": 6, "午": 7, "未": 8, "申": 9, "酉": 10, "戌": 11, "亥": 12
    }

    __Tengods = [("比肩","劫财"),("食神","伤官"),("偏财","正财"),("偏官","正官"),("偏印","正印")]

    def __init__(self):

        self.teng_list = []

    def Tengods(self,dayself, *args):
        self.dayself = dayself
        self.tengs = args
        self.zhengpian = 0
        for item in self.tengs:
            self.fivegods = self.__TGDZ[item] - self.__TGDZ[self.dayself]
            if self.fivegods < 0:
                self.fivegods = self.fivegods + 5

            if self.__TGDZ_Num[self.dayself] % 2 == self.__TGDZ_Num[item] % 2:
                self.zhengpian = 0
            else:
                self.zhengpian = 1

            self.teng_list.append(self.__Tengods[self.fivegods][self.zhengpian])

        return self.teng_list

"""
    def __init__(self,dayself, *args):

        self.dayself = dayself
        self.args = args
        self.__tengod = [("比肩","劫财"),("食神","伤官"),("偏财","正财"),("偏官","正官"),("偏印","正印")]
        self.__tengod_num = ["比肩","劫财","食神","伤官","偏财","正财","偏官","正官","偏印","正印"]
        # self.__tgdz = ["占","甲","乙","丙","丁","戊","己","庚","辛","壬","癸","子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
        self.__tiangandizhi = {"1":2,"2":2,"13":2,"14":2,"3":3,"4":3,"16":3,"17":3,"7":5,"8":5,"19":5,"20":5,"9":1,"10":1,"22":1,"11":1,"5":4,"6":4,
                      "15":4,"21":4,"12":4,"18":4}
        self.__teng = []
        self.__teng_num = []

    def Status(self): # 元祖输入只支持数字，所以甲-癸由1-10表示，子-亥由11-22表示
        # print(self.args,self.dayself,type(self.args),type(self.dayself))
        for item in self.args:
            shengke = (self.__tiangandizhi[str(item)] - self.__tiangandizhi[str(self.dayself)] + 5) % 5
            # print(shengke)
            if abs(self.dayself - item) % 2 == 0:
                self.tengods = self.__tengod[shengke][0]
            elif abs(self.dayself - item) % 2 == 1:
                self.tengods = self.__tengod[shengke][1]
            self.__teng.append(self.tengods)
            self.__teng_num.append(self.__tengod_num.index(self.tengods))
        # print(self.__teng)
        return self.__teng,self.__teng_num
"""
class CangGan(object):

    __canggan = {
        "子":["癸"],
        "丑":["己","癸","辛"],
        "寅": ["甲","丙","戊"],
        "卯": ["乙"],
        "辰": ["乙","戊","癸"],
        "巳": ["丙","戊","庚"],
        "午": ["己","丁"],
        "未": ["乙","己","丁"],
        "申": ["庚","壬","戊"],
        "酉": ["辛"],
        "戌": ["丁","戊","辛"],
        "亥": ["甲","壬"]
    }

    def __init__(self):
        self.all_canggan = []

    def canggan(self,*args):
        self.canggan = args
        # print(self.canggan)
        for i in self.canggan:
            if i in self.__canggan:
                # print(i)
                self.all_canggan.append(self.__canggan[i])
        # print(self.all_canggan)
        return self.all_canggan


class WuxingWangshuai(object):  #  输出五行旺衰主程序，列表形式输出，甲-癸为1-10，子-亥为11-22，输出列表前者为旺的天干
    # 地支，后者为衰的天干地支

    def __init__(self,y,m,d):

        self.__Li = [19700204, 19700506, 19700808, 19701108, 19710204, 19710506, 19710808, 19711108, 19720205, 19720505,
                19720807, 19721107, 19730204, 19730505, 19730808, 19731107, 19740204, 19740506, 19740808, 19741108,
                19750204, 19750506, 19750808, 19751108, 19760205, 19760505, 19760807, 19761107, 19770204, 19770505,
                19770807, 19771107, 19780204, 19780506, 19780808, 19781108, 19790204, 19790506, 19790808, 19791108,
                19800205, 19800505, 19800807, 19801107, 19810204, 19810505, 19810807, 19811107, 19820204, 19820506,
                19820808, 19821108, 19830204, 19830506, 19830808, 19831108, 19840204, 19840505, 19840807, 19841107,
                19850204, 19850505, 19850807, 19851107, 19860204, 19860506, 19860808, 19861108, 19870204, 19870506,
                19870808, 19871108, 19880204, 19880505, 19880807, 19881107, 19890204, 19890505, 19890807, 19891107,
                19900204, 19900506, 19900808, 19901108, 19910204, 19910506, 19910808, 19911108, 19920204, 19920505,
                19920807, 19921107, 19930204, 19930505, 19930807, 19931107, 19940204, 19940506, 19940808, 19941107,
                19950204, 19950506, 19950808, 19951108, 19960204, 19960505, 19960807, 19961107, 19970204, 19970505,
                19970807, 19971107, 19980204, 19980506, 19980808, 19981107, 19990204, 19990506, 19990808, 19991108,
                20000204, 20000505, 20000807, 20001107, 20010204, 20010505, 20010807, 20011107, 20020204, 20020506,
                20020808, 20021107, 20030204, 20030506, 20030808, 20031108, 20040204, 20040505, 20040807, 20041107,
                20050204, 20050505, 20050807, 20051107, 20060204, 20060505, 20060807, 20061107, 20070204, 20070506,
                20070808, 20071108, 20080204, 20080505, 20080807, 20081107, 20090204, 20090505, 20090807, 20091107,
                20100204, 20100505, 20100807, 20101107, 20110204, 20110506, 20110808, 20111108, 20120204, 20120505,
                20120807, 20121107, 20130204, 20130505, 20130807, 20131107, 20140204, 20140505, 20140807, 20141107,
                20150204, 20150506, 20150808, 20151108, 20160204, 20160505, 20160807, 20161107, 20170203, 20170505,
                20170807, 20171107, 20180204, 20180505, 20180807, 20181107, 20190204, 20190506, 20190808, 20191108,
                20200204, 20200505, 20200807, 20201107, 20210203, 20210505, 20210807, 20211107, 20220204, 20220505,
                20220807, 20221107, 20230204, 20230506, 20230808, 20231108, 20240204, 20240505, 20240807, 20241107,
                20250203, 20250505, 20250807, 20251107, 20260204, 20260505, 20260807, 20261107, 20270204, 20270506,
                20270808, 20271107, 20280204, 20280505, 20280807, 20281107, 20290203, 20290505, 20290807, 20291107,
                20300204, 20300505, 20300807, 20301107]  # 1960到2030年的立春立夏立冬立秋,一共284个

        self.__Jijie = {1: '春天',2: '夏天',3: '秋天',0: '冬天'}
        self.__Season_GZ = {1:["甲","乙","丙","丁","寅","卯","巳","午"],2:["丙","丁","戊","己","丑","辰","巳","午","未","戌"],
                            3:["庚","申","壬","癸","申","酉","亥","子"],0:["壬","癸","甲","乙","亥","子","寅","卯"]}

        self.year = y
        self.month = m
        self.day = d
        self.wang = []
        self.shuai = []

    def Season(self):  #  求出季节
        self.celander = self.year * 10000 + self.month * 100 + self.day
        if self.celander in self.__Li:
            self.result = int(self.__Li.index(int(self.celander)) + 1)
        elif self.celander not in self.__Li:
            self.__Li.append(self.celander)
            self.__Li.sort()
            self.result = int(self.__Li.index(self.celander))

        self.final_result = self.result % 4
        self.season_result = self.__Jijie[self.final_result]

        return self.season_result
    def Judge_WangShuai(self, *args):  #  各季节中五行的旺衰
        self.Season()
        self.season = self.__Season_GZ[self.final_result]
        self.args = args
        for item in self.args:
            if item in self.season:
                self.wang.append(item)
            elif item not in self.season:
                self.shuai.append(item)

        # print(self.wang,self.shuai)
        return self.wang,self.shuai

class MeihuaPaipan(object):  #  梅花易数排盘，输出三个列表，列表[0]为本卦，[1]为互卦，[2]为变卦，每一个小列表中，[0]为上卦，[1]为下卦
    #由乾到坤按照先天八卦顺序排列，序号为1-8

    def __init__(self):

        self.bgshang_fianl = []
        self.bgxia_final = []
        self.hgshang_final = []
        self.hgxia_final = []
        self.bg_shang_final = []
        self.bg_xia_final = []
        self.__BaGua = ([1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0])
        self.__ZhongWen = ('乾☰', '兑☱', '离☲', '震☳', '巽☴', '坎☵', '艮☶', '坤☷')
        self.__BaGua1 = ([1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0])

    def Paipan(self, num_one, num_two, num_three):

        self.num_one = (num_one - 1) % 8
        self.num_two = (num_two - 1) % 8
        self.bengua_shang = self.__BaGua[self.num_one]
        self.bengua_xia = self.__BaGua[self.num_two]

        self.hugua_xia = self.bengua_xia + self.bengua_shang
        # print("互卦是： %s" % self.hugua_xia)
        self.hugua_xia = self.hugua_xia[1:4]
        self.hugua_shang = self.bengua_xia + self.bengua_shang
        self.hugua_shang = self.hugua_shang[2:5]
        self.__BenGuaShangGua = self.bengua_shang
        self.__BenGuaXiaGua = self.bengua_xia
        self.__HuGuaShangGua = self.hugua_shang
        self.__HuGuaXiaGua = self.hugua_xia

        if self.bengua_shang in self.__BaGua:
            self.bgshang = int(self.__BaGua.index(self.bengua_shang))
            # print(self.bgshang)
            self.bgshang_final = self.__ZhongWen[self.bgshang]

        if self.bengua_xia in self.__BaGua:
            self.bgxia = int(self.__BaGua.index(self.bengua_xia))
            # print(self.bgxia)
            self.bgxia_final = self.__ZhongWen[self.bgxia]

        if self.hugua_shang in self.__BaGua:
            self.hgshang = int(self.__BaGua.index(self.hugua_shang))
            # print(self.hgshang)
            self.hgshang_final = self.__ZhongWen[self.hgshang]

        if self.hugua_xia in self.__BaGua:
            self.hgxia = int(self.__BaGua.index(self.hugua_xia))
            # print(self.hgxia)
            self.hgxia_final = self.__ZhongWen[self.hgxia]

    # def Num_Three(self, num_three):
        self.num_three = num_three % 6
        self.biangua_shang = self.bengua_shang[:]
        self.biangua_xia = self.bengua_xia[:]
        if 4 <= self.num_three <= 5:
            self.num_three = self.num_three - 4
            if self.biangua_shang[self.num_three] == 0:
                self.biangua_shang[self.num_three] = 1
            else:
                self.biangua_shang[self.num_three] = 0
        elif self.num_three == 0:
            self.num_three = self.num_three + 2
            if self.biangua_shang[self.num_three] == 0:
                self.biangua_shang[self.num_three] = 1
            else:
                self.biangua_shang[self.num_three] = 0
        else:
            self.num_three = self.num_three - 1
            if self.biangua_xia[self.num_three] == 0:
                self.biangua_xia[self.num_three] = 1
            else:
                self.biangua_xia[self.num_three] = 0

        if self.biangua_shang in self.__BaGua1:
            self.bg_shang = int(self.__BaGua1.index(self.biangua_shang))
            # print(self.bg_shang)
            self.bg_shang_final = self.__ZhongWen[self.bg_shang]

        if self.biangua_xia in self.__BaGua1:
            self.bg_xia = int(self.__BaGua1.index(self.biangua_xia))
            # print(self.bg_xia)
            self.bg_xia_final = self.__ZhongWen[self.bg_xia]

        # print(self.bgshang_final,self.bgxia_final,  self.hgshang_final, self.hgxia_final,self.bg_shang_final,  self.bg_xia_final)

        self.bengua_end = [self.__ZhongWen.index(self.bgshang_final) + 1,self.__ZhongWen.index(self.bgxia_final)+1]
        self.hugua_end = [self.__ZhongWen.index(self.hgshang_final)+ 1,self.__ZhongWen.index(self.hgxia_final)+ 1]
        self.biangua_end = [self.__ZhongWen.index(self.bg_shang_final)+ 1,self.__ZhongWen.index(self.bg_xia_final)+ 1]
        #
        return self.bengua_end,self.hugua_end,self.biangua_end


class Gua_Wangshuai(object): # 专门计算八卦的旺衰，由乾到坤按照先天八卦顺序排列，序号为1-8

    def __init__(self):

        self.__Li = [19600205, 19600505, 19600807, 19601107, 19610204, 19610506, 19610808, 19611107, 19620204, 19620506,
                19620808, 19621108, 19630204, 19630506, 19630808, 19631108, 19640205, 19640505, 19640807, 19641107,
                19650204, 19650506, 19650808, 19651107, 19660204, 19660506, 19660808, 19661108, 19670204, 19670506,
                19670808, 19671108, 19680205, 19680505, 19680807, 19681107, 19690204, 19690506, 19690808, 19691107,
                19700204, 19700506, 19700808, 19701108, 19710204, 19710506, 19710808, 19711108, 19720205, 19720505,
                19720807, 19721107, 19730204, 19730505, 19730808, 19731107, 19740204, 19740506, 19740808, 19741108,
                19750204, 19750506, 19750808, 19751108, 19760205, 19760505, 19760807, 19761107, 19770204, 19770505,
                19770807, 19771107, 19780204, 19780506, 19780808, 19781108, 19790204, 19790506, 19790808, 19791108,
                19800205, 19800505, 19800807, 19801107, 19810204, 19810505, 19810807, 19811107, 19820204, 19820506,
                19820808, 19821108, 19830204, 19830506, 19830808, 19831108, 19840204, 19840505, 19840807, 19841107,
                19850204, 19850505, 19850807, 19851107, 19860204, 19860506, 19860808, 19861108, 19870204, 19870506,
                19870808, 19871108, 19880204, 19880505, 19880807, 19881107, 19890204, 19890505, 19890807, 19891107,
                19900204, 19900506, 19900808, 19901108, 19910204, 19910506, 19910808, 19911108, 19920204, 19920505,
                19920807, 19921107, 19930204, 19930505, 19930807, 19931107, 19940204, 19940506, 19940808, 19941107,
                19950204, 19950506, 19950808, 19951108, 19960204, 19960505, 19960807, 19961107, 19970204, 19970505,
                19970807, 19971107, 19980204, 19980506, 19980808, 19981107, 19990204, 19990506, 19990808, 19991108,
                20000204, 20000505, 20000807, 20001107, 20010204, 20010505, 20010807, 20011107, 20020204, 20020506,
                20020808, 20021107, 20030204, 20030506, 20030808, 20031108, 20040204, 20040505, 20040807, 20041107,
                20050204, 20050505, 20050807, 20051107, 20060204, 20060505, 20060807, 20061107, 20070204, 20070506,
                20070808, 20071108, 20080204, 20080505, 20080807, 20081107, 20090204, 20090505, 20090807, 20091107,
                20100204, 20100505, 20100807, 20101107, 20110204, 20110506, 20110808, 20111108, 20120204, 20120505,
                20120807, 20121107, 20130204, 20130505, 20130807, 20131107, 20140204, 20140505, 20140807, 20141107,
                20150204, 20150506, 20150808, 20151108, 20160204, 20160505, 20160807, 20161107, 20170203, 20170505,
                20170807, 20171107, 20180204, 20180505, 20180807, 20181107, 20190204, 20190506, 20190808, 20191108,
                20200204, 20200505, 20200807, 20201107, 20210203, 20210505, 20210807, 20211107, 20220204, 20220505,
                20220807, 20221107, 20230204, 20230506, 20230808, 20231108, 20240204, 20240505, 20240807, 20241107,
                20250203, 20250505, 20250807, 20251107, 20260204, 20260505, 20260807, 20261107, 20270204, 20270506,
                20270808, 20271107, 20280204, 20280505, 20280807, 20281107, 20290203, 20290505, 20290807, 20291107,
                20300204, 20300505, 20300807, 20301107]  # 1960到2030年的立春立夏立冬立秋,一共284个

        self.__Jijie = {1: '春天',
                   2: '夏天',
                   3: '秋天',
                   0: '冬天'}

        self.__LeiXiang = {1: [4, 5, 3], 2: [3, 7, 8], 3: [1, 2, 6], 0: [6, 4, 5]}
        self.today_time = time.time()
        self.final_time = time.strftime('20%y-%m-%d', time.localtime(self.today_time))

        date = self.final_time.split("-")
        self.year = int(date[0])
        self.month = int(date[1])
        self.day = int(date[2])
        self.qiang = []
        self.ruo = []

    def Season(self):  # 求出季节
        self.celander = self.year * 10000 + self.month * 100 + self.day
        if self.celander in self.__Li:
            self.celander = self.celander + 1
        self.int_celander = int(self.celander)
        self.__Li.append(self.int_celander)
        self.__Li.sort()
        self.result = int(self.__Li.index(self.int_celander))
        self.final_result = self.result % 4
        self.__Li.remove(self.int_celander)

        return self.__Jijie[self.final_result]

    def Judge_WangShuai(self, *args):  # 各季节中八卦的旺衰
        self.Season()
        self.season = self.__LeiXiang[self.final_result]
        # print(self.season)
        self.args = args
        for self.item in self.args:
            if self.item in self.season:
                self.qiang.append(self.item)

            else:
                self.ruo.append(self.item)

        return (self.qiang, self.ruo)


if __name__ == '__main__':
    a = Bazi_Number(2020,7,23,12)
    a1 = a.Bazi_Num()
    print(a1)
    b = BaziPaipan(1989,5,23,23)

    b1 = b.pre_Bazi_words()
    print(b1)

    d = WuxingWangshuai(1988,8,6)
    d1 = d.Judge_WangShuai("甲","乙","丙","丁","申","酉","亥","子")
    print(d1)
    e = BaziPaipan(1987,7,7,0)
    e1 = e.QiYun("女")
    print(e1)
    f = Gua_Wangshuai()
    f1 = f.Judge_WangShuai(4,5,6,7)
    print(f1)
    g = MeihuaPaipan()
    g1 = g.Paipan(257,588,634)
    print(g1)
    h = CangGan()
    h1 = h.canggan("寅","卯")
    print(h1)

    o = TenGods()
    o1 = o.Tengods("癸","戊","辰","己","未")
    print(o1)