#Code for calander
year=int(input("Enter name of year: "))
month = input("Enter the name of month: ").upper()
#check month name
month_check = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
if month in month_check:
    month_name = month
else:
    print("You made a spelling mistake in Month name.Try again.")
    quit()

num_blank = int(input("Number of blank Space in Start: "))
print()


#this code for white space as a pair and make a list of white space
total_blank = '  '*num_blank
def b_create(total_blank):
    x=[total_blank[i:i+2] for i in range(0,len(total_blank),2)]
    return x
blank_list = b_create(total_blank)
print(blank_list)

day_list31 =['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31' ]

day_list30 =['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29', '30' ]

day_list28 =['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28' ]

day_list29 =['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29']

#condition for number of days in a month
if (year%4==0 and month_name == 'FEBRUARY'):
    fianl_list=blank_list+day_list29
elif (year%4!=0 and month_name == 'FEBRUARY'):
    fianl_list = blank_list + day_list28
elif (month_name=='APRIL' or month_name=='JUNE' or month_name=='SEPTEMBER' or month_name=='NOVEMBER'):
    fianl_list = blank_list + day_list30
else:
    fianl_list = blank_list + day_list31

#code for printing date
print(f'       {month_name}-{year}')
day_name=['SUN','MON','TUE','WED','THI','FRI','SAT']
for j in day_name:
    print(j,end=' ')
print()
l = 0
for day in fianl_list:
    l =l+1
    print(day, end='  ')
    if l %7==0:
        print()
print()
