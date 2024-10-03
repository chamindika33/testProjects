
class TestFunction:

    def palidrome_function(self,s): #abba
        try:
            if len(s) <= 1:
                return True
            
            elif s[0] == s[-1]:
                return testfunction.palidrome_function(s[1:-1])
            
            return False

        except Exception as e:
            return False
        
testfunction =  TestFunction()