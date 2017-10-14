##Chris Sowden
## Temp Program
## Homework 1b





import os.path

#define global variables
database = []#list to store monthly temperatures
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
WEEKS = 6

'''
This function read input from a text file and adds the data to the
list called database. The data values are added as strings.
Data for each week is one row in the list. '''

class monthTemp:
    
    def getInputFromFile(filename = None):
        result = False
        if(filename == None):
            filename = input("Enter name of input file: ")
        if(os.path.isfile(filename)):
            infile = open(filename, 'r')
            count = 0
            for line in infile:
                week = line.strip()
                weekList = week.split()
                database.append(weekList)
                count += 1
            infile.close()
            return True
        else:
            print("Invalid filename ... aborting ...")
                
        return False

    '''
    This function creates and returns a list with seven values,
    each one being a day average for that month.
    '''
    def getWeekAverages():
        pass
        weekAverages = []
        MAX = WEEKS
    ##    total = 0
        for week in range (WEEKS):
            total = 0
            for day in range(len(DAYS)):
              total += int(database[week][day])
            weekAverages.append(total/7)
        return weekAverages

    def getDayAverages():
        pass
        dayAverages = []
        MAX = WEEKS
        for day in range(len(DAYS)):
            total = 0
            for week in range (WEEKS):
                total += int(database[week][day])
            dayAverages.append(total/WEEKS)
        return dayAverages


    ## Highest day average
    def getHighestDayAverage(dayAverages):
        return max(dayAverages)


    ## Lowest day average
    def getLowestDayAverage(dayAverages):
        return min(dayAverages)


    ## Hightest Week Average
    def getHighestWeekAverage(weekAverages):
        return max(weekAverages)

    ## Lowest Week Average
    def getLowestWeekAverage(weekAverages):
        return min(weekAverages)


    ## Highest temp function
    def getHighestTemp():
        highestTemp = int(database[0][0])
        
        for week in range (WEEKS):
            for day in range(len(DAYS)):
               if highestTemp < int(database[week][day]):
                   highestTemp = int(database[week][day])
        return highestTemp


    ## Lowest Temp function
    def getLowestTemp():
        lowestTemp = int(database[0][0])
        
        for week in range (WEEKS):
            for day in range(len(DAYS)):
               if lowestTemp > int(database[week][day]):
                   lowestTemp = int(database[week][day])
        return lowestTemp

    ## Average Temp function

    def getAverageTemp():
        total = 0
        for week in range (WEEKS):
            for day in range(len(DAYS)):
                total += int(database[week][day])
        return total / (WEEKS * len(DAYS))

    
#Define other methods

def main():
    
    print("//////Welcome to the program that will get you High, Low, and Average tempertures of the month://////")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
## this is where the file name is entered
    goodFile = monthTemp.getInputFromFile()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if(goodFile == True):
        monthTemp.dayAverages = monthTemp.getDayAverages()
        monthTemp.weekAverages = monthTemp.getWeekAverages()
        monthTemp.highestDay = monthTemp.getHighestDayAverage(monthTemp.dayAverages)
        monthTemp.lowestDay = monthTemp.getLowestDayAverage(monthTemp.dayAverages)
        monthTemp.highestWeek = monthTemp.getHighestWeekAverage(monthTemp.weekAverages)
        monthTemp.lowestWeek = monthTemp.getLowestWeekAverage(monthTemp.weekAverages)
        monthTemp.highestTemp = monthTemp.getHighestTemp()
        monthTemp.lowestTemp = monthTemp.getLowestTemp()
        monthTemp.averageTemp = monthTemp.getAverageTemp()
        monthTemp.dayIndex = monthTemp.dayAverages.index(monthTemp.lowestDay)
        print("This is the weeks averages" , (monthTemp.weekAverages))
        print("Weekday with lowest average temperature was ", DAYS[monthTemp.dayIndex], " with ", format(monthTemp.getAverageTemp(), "0.2f"))
        print("Weekday with highest average temperature was ", DAYS[monthTemp.dayIndex], " with ", format(monthTemp.getHighestDayAverage(monthTemp.dayAverages), "0.2f"))
        
        print("Weekday with lowest average temperature was ", DAYS[monthTemp.dayIndex], " with ", '{0:.2f}'.format(monthTemp.lowestDay))
        
        print("The highest average temperature of a given week is: ", '{0:.2f}'.format(monthTemp.highestWeek))
        print("The lowest average temperature of a given week is: ", '{0:.2f}'.format(monthTemp.lowestWeek))
        print("The lowest temperature in a given day is the following: ", '{0:.2f}'.format(monthTemp.lowestTemp))
        print("The highest temperature in a given day is the following: ", '{0:.2f}'.format(monthTemp.highestTemp))
        print("The average temperature in a given day is the following: ",'{0:.2f}'.format(monthTemp.averageTemp))

    #... and so on
        
#call main program
main()
