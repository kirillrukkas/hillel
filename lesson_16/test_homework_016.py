class Employee:

    def __init__(self, name:str, salary:int):
        self.name = name
        self.salary = salary
        print("Employee Class method called")


class Manager(Employee):
    
    def __init__(self, name:str, salary:int, department:str):
        super().__init__(self, name, salary)
        self.department = department
        print("Manager Class method called")


class Developer(Employee):
    
    def __init__(self, name:str, salary:int, programming_language:str):
        super().__init__(name, salary)
        self.programming_language = programming_language
        print("Developer Class method called")

class TeamLead(Manager, Developer):
    
    def __init__(self, name:str, salary:int, programming_language:str,  department:str, team_size:int):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size
        print("TeamLead Class method called")

class TestsClasses:

    def test_class_inheritance(self):

        team_lead = {"name":"Vasya", 
                     "salary":16, 
                     "programming_language":"python", 
                     "department":"AQA", "team_size":5
                     }
        
        tmld = TeamLead(name=team_lead["name"], 
                      salary=team_lead["salary"], 
                      programming_language=team_lead["programming_language"], 
                      department=team_lead["department"], 
                      team_size=team_lead["team_size"])
        
        assert tmld.name == team_lead["name"], "Unexpected name of Team Lead"
        assert tmld.salary == team_lead["salary"], "Unexpected salary of Team Lead"
        assert tmld.programming_language == team_lead["programming_language"], "Unexpected programming_language of Team Lead"
        assert tmld.department == team_lead["department"], "Unexpected department of Team Lead"
        assert tmld.team_size == team_lead["team_size"], "Unexpected team_size of Team Lead"


        



