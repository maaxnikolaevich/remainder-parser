import pandas as pd

def addRecord(productCode,vkorg, wholesale):
    data = pd.read_csv(r'data/search_ecom_sku_word.csv', delimiter=";")
    data=data.head(10000)
    isEmptyValue = data.loc[data['sku'] == productCode].empty
    if not isEmptyValue:
        if wholesale:
            isNull= list(data.isnull().loc[data['sku'] == productCode, "avail_01"])[0]
            if not isNull:
                oldValue=list(data.loc[data['sku'] == productCode, "avail_01"])[0]
                data.loc[data['sku'] == productCode, "avail_01"] = f"{oldValue}, {vkorg}"
            else:
                data.loc[data['sku'] == productCode, "avail_01"] = f"{str(vkorg)}"
        else:
            isNull = list(data.isnull().loc[data['sku'] == productCode, "avail_02"])[0]
            if not isNull:
                oldValue = list(data.loc[data['sku'] == productCode, "avail_02"])[0]
                data.loc[data['sku'] == productCode, "avail_02"] = f"{oldValue}, {vkorg}"
            else:
                data.loc[data['sku'] == productCode, "avail_02"] = f"{str(vkorg)}"
    data.to_csv(r"data/search_ecom_sku_word.csv", sep=';', index_label=False, index=False)

array=[[23362,2000,True],[233629,1000,True], [233032,5000,False], [453243,7000, True], [470682,1000,True], [233629,3000,False]]

for row in array:
     addRecord(row[0],row[1], row[2])

# result.to_csv(r"search_ecom_sku_word.csv", sep=';')
# d=[]
# for i in range(5):
#     d.append(genNewHead(i,i))
# print(d)
