import datetime 
import pytz


class Time:
    
    today = datetime.datetime.today()
    tehran = datetime.datetime.now(tz=pytz.timezone("Asia/Tehran"))
    irvine = datetime.datetime.now(tz=pytz.timezone("PST8PDT"))
    
    def __init__(self,continent,country,city):
        self.continent = continent
        self.country = country
        self.city = city
    
    @staticmethod
    def calculate_age_day(birthday):
        birthday = str(birthday)
        birthday = datetime.datetime.strptime(birthday,"%m/%d/%Y")
        result = (Time.today - birthday).days
        return f"You are {result} days old!"
    
    @staticmethod
    def calculate_age_seconds(birthday):
        birthday = str(birthday)
        birthday = datetime.datetime.strptime(birthday,"%m/%d/%Y")
        result = (Time.today - birthday).total_seconds()
        return f"About {result} seconds have passed since you were born!"
    
    def __str__(self):
        str1 = f"{self.continent}/{self.city}"
        return f"Your Location is {self.continent},{self.country},{self.city} and\
        Timezone:{datetime.datetime.now(tz=pytz.timezone(str1))}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.continent},{self.country},{self.city})"
    
    
if __name__ == '__main__':
    t1 = Time("Asia","Iran","Tehran")
    print(t1)
    print(Time.calculate_age_seconds("11/22/2000"))

    