import pandas as pd
from pandas import DataFrame as df
from sklearn.linear_model import LinearRegression 
import numpy as np

BILL = pd.read_csv('home/billtest.csv',index_col=0)
BILL.to_csv('home/billtest.csv')
lis = ['BILL1','BILL2','BILL3','BILL4','BILL5','BILL6','BILL7','BILL8','BILL9','BILL10','BILL11','BILL12','BILL13']
OP=[]
CP=[]
dp = ['Kunal Thakur','Upendra Dwivedi','Yamini Sharma','Yojan Sharma','Atharv Sood','Yugank Sharma','Nehal Singhal','Saksham Sayal','Vivek Kumar','Prakhar Pratyush','Ghanshaym Shukla','Ritwik Kumar','Aditya Singh']
kp = ['Hamirpur,Himachal Pradesh','Kanpur,Uttar Pradesh','Shimla,Himachal Pradesh','Jaipur,Rajasthan','Shimla,Himachal Pradesh','Shimla,Himachal Pradesh','Ghaziabad,Uttar Pradesh','Shimla,Himachal Pradesh','Begusarai,Bihar','Chapra,Bihar','Shimla,Himachal Pradesh','Shimla,Himachal Pradesh','Shimla,Himachal Pradesh']
met = ['192040','192056','192006',"194523",'12345','56789','11111','3456','23455','16723','11904','23456','5634']
act = ['230','130','670','120','390','190','100','234','456','160','380','780.24','123']
email = ['kt192@gmail.com','dwivediupendra0509@gmail.com','yamini1243@gmail.com','yojans@gmail.com','soodatharv@gmail.com','yugisharma@gmail.com','nehal1902@gmail.com','saksham@gmail.com','vivu69@gmail.com','prakharp@gmail.com','ghanshyam@gmail.com','ritw1234@gmail.com','adi543@gmail.com']
BILL.to_csv('home/billtest.csv')
da = pd.read_csv('home/data.csv',index_col=0)
for m in range(len(lis)):
    y = df(BILL,columns=[lis[m]])
    x = df(BILL,columns=['MONTH'])
    regression = LinearRegression()
    regression.fit(x,y)


    slope=regression.coef_ #slope hai bhaisaab



    inter=regression.intercept_ #intercept hai bhai saab

    def predict(month):
        if 1<=month<=12:
            bill=month*slope+inter
        else:
            print("invalid month number")
        return bill

    #THRESHOLD FOR PREDICTED BILLS
    prd_bill = pd.read_csv('home/predicted.csv',index_col=0)
    mon = prd_bill['MONTHS'].values
    lis1 = []
    for i in mon:
        lis1.append(predict(i)[0][0])
        if i == 3:
            OP.append(predict(3)[0][0])
    prd_bill['BILL'] = lis1 #inserting a column of name BILL
    lis1 = []
    for k in mon:
        l = [j for j in BILL[lis[m]].values if j < prd_bill['BILL'].values[k-1]]
        a = np.std(l)
        b = np.mean(l)
        thres = b - 2*a 
        lis1.append(thres) 
    prd_bill['Threshold'] = lis1
    act_bill = pd.read_csv('home/Actual_bill.csv')


    prd_bill['Actual Bill'] = act_bill['BILL1'].values
    #saving a column 'Suspect' with True if folowing boolean expression satified otherwise false
    prd_bill['Suspect'] = prd_bill['Actual Bill'] < prd_bill['Threshold'] 
    #saving the changes in predicted.csv file
    prd_bill.to_csv('home/predicted.csv') 
    #GETTING A SUSPECT
    #IF A USER ACTUAL BILL IS BELOW THE THRESHOLD FOR MORE THAN 4 TIMES THEN HE MAY BE A SUSPECT
    if prd_bill['Suspect'].values.sum() >= 4: #adding up the suspect column
        CP.append('user is a suspect')
    else:
        CP.append('user is not a suspect')
# threshold  prediction
kt = ['suspect','prediction','user','address','meter','actual','email']
gp = []
for i in range(len(dp)):
    gp.append([CP[i],OP[i],dp[i],kp[i],met[i],act[i],email[i]])
gp = sorted(gp)

for i in range(7):
    que = []
    for j in range(len(dp)):
        que.append(gp[j][i])
    da[kt[i]] = que
for i in range(3,7):
    que=[]
    if kt[i] == 'address':
        for j in range(len(dp)):
            que.append(gp[j][i])
        da[kt[i]] = que
    elif kt[i] == 'meter':
        for j in range(len(dp)):
            que.append(gp[j][i])
        da[kt[i]] = que
    else:
        for j in range(len(dp)):
            que.append(gp[j][i])
        da[kt[i]] = que

da.to_csv('home/data.csv')
def abc():
    return OP
def sus():
    return CP


"""try:
    uff=int(input("Enter the month number to predict the bill"))
    result=float(predict(uff))
    print(result)
   
except:
    print("Pls enter the month number for example 1 for january")


#inserting a column 'Threshold'
lis1 = []
for i in mon:
    l = [j for j in da['BILL1'].values if j < prd_bill['BILL'].values[i-1]]
    a = np.std(l)
    b = np.mean(l)
    thres = b - 2*a 
    lis1.append(thres) 
prd_bill['Threshold'] = lis1
act_bill = pd.read_csv('home/Actual_bill.csv')


prd_bill['Actual Bill'] = act_bill['BILL1'].values
#saving a column 'Suspect' with True if folowing boolean expression satified otherwise false
prd_bill['Suspect'] = prd_bill['Actual Bill'] < prd_bill['Threshold'] 
#saving the changes in predicted.csv file
prd_bill.to_csv('home/predicted.csv') 
#GETTING A SUSPECT
#IF A USER ACTUAL BILL IS BELOW THE THRESHOLD FOR MORE THAN 4 TIMES THEN HE MAY BE A SUSPECT
if prd_bill['Suspect'].values.sum() >= 4: #adding up the suspect column
    print("User may be a suspect")"""
#ploting the graph
"""draw.figure(figsize=(14,4))
draw.plot(x, regression.predict(x),color='red',linewidth=4)

draw.title('Month vs Electricty Bill')
draw.xlabel('Month')
draw.ylabel('Cost in rupees')
draw.xlim(0,13)
draw.plot(prd_bill['MONTHS'],prd_bill['Threshold'])
draw.plot(prd_bill['MONTHS'],prd_bill['Actual Bill'])
draw.show()"""