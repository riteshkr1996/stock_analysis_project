import pandas as pd
import csv
from bsedata.bse import BSE
from matplotlib import pyplot as plt
import matplotlib

bse = BSE()
code_list= ['500325', '532540', '500180', '532174', '500696', '500875', '500209', '500112', '500010', '532454',
'500247', '500034', '500510', '532281', '500820', '532215', '532500', '500114', '524715', '512599',
'532538', '532978', '507685', '500790', '500312', '500228', '500570', '532555', '532898', '500520',
'532921', '533278', '500470', '532977', '540777', '540719', '500300', '500825', '532755', '500440',
'505200', '532187', '532488', '500124', '500547', '500087', '500800', '508869', '512070' ,'500182']
p_change = []
c_name = []
my_dic = {}

for code in code_list:
    q = bse.getQuote(code)
    c_name.append(q['companyName'])
    p_change.append(round(float(q['pChange']),2))


my_dic = {'Company_Name': c_name,
         '%Change': p_change}
df = pd.DataFrame(my_dic)

fig, ax = plt.subplots(figsize = (45,5))
plt.bar(c_name, p_change, color=['r' if v < 0 else 'g' for v in p_change])
plt.xticks(rotation=65, ha='right')
plt.title("Top 50 Stock's daily % change")
plt.show()