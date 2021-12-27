log_file = open("um-server-01.txt")






def sales_reports(log_file): #This line is declaring a function, passing in the log_file data as the parameter
    for line in log_file: #this is a for loop saying, for (whatever variable name you want), loop over the information IN this array or list and in this case a file
        line = line.rstrip() #the line variable is being set equal to line.rstrip, the rstrip function will remove whitespace.
        day = line[0:3] #the day is being set to equal the data in the line object to whatever the index is at [0] (come back to this...) itll check the first three letters of the value.
        if day == "Mon": #if the day we are looking for is Monday, then log that information.
            print(line) # if the statement is true then print hte entire line


sales_reports(log_file)


def numbers_reports(log_file)
    for line in log.file:
        line = line.rtrip('')
        count = int(line[2])
        if count >10:
            print(line)




