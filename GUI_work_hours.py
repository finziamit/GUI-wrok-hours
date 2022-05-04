# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:03:01 2022

@author: finzi
"""
import tkinter as tk

def hour_to_int(hour):
    """casting an hour given to a nubmer"""
    arr = hour.split(":")
    if(len(arr)>2):
        raise Exception("InValidHour")
    hrs = int(arr[0])
    mins = int(arr[1])
    mins/=60
    res = hrs+mins
    round(res,2)
    return res





def write_to_file():
    """writing the data into the file"""
    date = date_pannel.get("0.0","end-1c")
    for i in range(len(date)):
        if date[i].isdigit()==False and date[i]!=".":
            date[i] = "."
    arrival = arrive_pannel.get("1.0","end-1c")
    leaving = leave_pannel.get("1.0","end-1c")
    
    f = open("Working hours.txt",'a')
    hours_sum = hour_to_int(leaving)-hour_to_int(arrival)
    if hours_sum<0:
        raise Exception("TimeInputError")
        f.close()
        return
    str1 = ("date: "+date+"\tarrival: "+arrival+
            "\tleaving: "+leaving)
    str2 = ("\t sum of hour for the day: "+str(hours_sum))
    f.write("\n")
    
    f.write(str1)
    f.write(str2)
    
    f.close()

def openNewWindow():
    """the function will create the window to the salary page"""
    newRoot = tk.Tk()
    newWindow = tk.Canvas(newRoot, width = 400,height = 400)
    newWindow.grid(columnspan = 3, rowspan = 3)
    
    #labels and pannels
    Month = tk.Label(newRoot, text = "Wanted month")
    Month.grid(column=0,row=0)
    
    MonthGetter = tk.Text(newRoot, height = 2, width = 30)
    MonthGetter.grid(column=1,row=0)
    
    
    #buttons
    exit_button = tk.Button(newRoot,text="Exit",
                        command = newRoot.destroy,
                        bg = '#20bebe',width = 10,height = 3)
    
    submit_button = tk.Button(newRoot, text = "Submit",
                              command = lambda : salary_calc(),
                              bg = '#20bebe',width = 10,height = 3)
    
    submit_button.grid(column = 1, row = 3)
    exit_button.grid(column = 3,row = 3)
    
    #salary function
    def salary_calc():
        """calculating the salary apprx for the monthly salary
        the calculation will show the sum for the given month"""
        given_month = MonthGetter.get("0.0","end-1c")
        #check cases if the month given as a number or by its name
        if given_month.isnumeric():
            month = int(given_month)
            if month<1 or month>12:
                raise Exception("InValidMonth")
        else:
            tmp = given_month.lower()
            dic = {"january" : 1,
                   "february" : 2,
                   "march" : 3,
                   "april" : 4,
                   "may" : 5,
                   "june": 6,
                   "july": 7,
                   "august": 8,
                   "september": 9,
                   "october": 10,
                   "november": 11,
                   "december": 12}
            month = dic[tmp]
        #now we can work with our file
        f = open("Working hours.txt",'r')
        content = f.readlines()
        f.close()
        monthly_hours_sum = 0.0
        while(content.remove("\n")):
            content.remove("\n")
        for line in content: #in each line the date is the first time we get a dot and a number
            if(line == ""):
                content.remove(line)
            else:
                month_str = ""
                line = ''.join(line.split())
                str_hours = ""
                dotindex = line.find(".")
                if(dotindex==-1):
                    print("no dot here")
                    break
                dotindex+=1
                while(line[dotindex].isnumeric()):
                    month_str+=line[dotindex]
                    dotindex+=1
                if(int(month_str) == month):
                    ind = len(line)
                    while (True):
                        if(line[ind-1]==":"):
                            break
                        else:
                            ind -=1
                    for i in range(ind,len(line)):
                        str_hours+=line[i]
                    monthly_hours_sum+= float(str_hours)
                
        if(monthly_hours_sum==0):
            res_str ="you didn't work this month!"
        else:
            wage = 32
            salary =  wage*monthly_hours_sum
            salary = round(salary,2)
            res_str = "your salary for this month is: "+str(salary)
        calculated_salary = tk.Text(newRoot,height = 4,width = 20)
        calculated_salary.insert(1.0,res_str)
        calculated_salary.grid(column = 1 , row = 1)


"""the program will make GUI to enter the hours spent at work
and will save it to a txt file"""
root = tk.Tk()

backgroud = tk.Canvas(root, width = 600, height = 600)
backgroud.grid(columnspan = 4, rowspan = 4)

#labels and pannels
date = tk.Label(root,text="Date of the shift")
date.grid(column=0,row=0)
date_pannel = tk.Text(root,height = 2 , width = 30)
date_pannel.grid(column=1,row=0)
    
    
arrival = tk.Label(root,text="Arrival time")
arrival.grid(column=0,row=1)
arrive_pannel = tk.Text(root,height = 2, width = 30)
arrive_pannel.grid(column=1,row=1)
    


leaving = tk.Label(root,text="Leaving time")
leaving.grid(column=0,row=2)
leave_pannel = tk.Text(root,height = 2 , width = 30)
leave_pannel.grid(column=1, row = 2)


#buttons
exit_button = tk.Button(root,text="Exit",
                        command = root.destroy,
                        bg = '#20bebe',width = 10,height = 3)
OK = tk.Button(root, text = "OK"
               ,command = lambda:write_to_file()
               ,bg = '#20bebe',width = 10,height = 3)
Salary_button = tk.Button(root,text = "Salary"
                          ,command = lambda:openNewWindow()
                          ,bg = '#20bebe',width = 10,height = 3)
OK.grid(column = 1,row = 3)
exit_button.grid(column = 3, row = 3)
Salary_button.grid(column = 0, row = 3)

root.mainloop()
