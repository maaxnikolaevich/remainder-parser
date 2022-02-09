import datetime
import pandas as pd
from Requests import getProducts

def process():
    data = pd.read_csv(r'data/search_ecom_sku_word.csv', delimiter=';', chunksize=10000)
    begin_time = datetime.datetime.now()
    result=pd.DataFrame()
    for item in data:
        codesList=item["sku"].values
        result=pd.concat([result, formToDf(codesList, item)])
    result.to_csv(r'data/res.csv', sep=';', index=False)
    print(f"Время выполнения запроса: {datetime.datetime.now() - begin_time}")


def convToDict(products):
    result={}
    for currProduct in products:
        if not currProduct['MATNR'] in result:
            result[currProduct['MATNR']]=[]
        result[currProduct['MATNR']].append(currProduct)
    return result

def formToDf(codesList,data):
    listProductCodes=[]
    for productCode in codesList:
        listProductCodes.append(f"{productCode}")
    products=getProducts(listProductCodes)
    product_dict=convToDict(products)

    def vkorgForAvail_01(products):
        vkorgList=[]
        for currProduct in products:
            if currProduct['WHOLESALE']=='X':
                vkorgList.append(currProduct['VKORG'])
        vkorgList=list(set(vkorgList))
        return vkorgList

    def vkorgForAvail_02(products):
        vkorgList=[]
        for currProduct in products:
            if currProduct['WHOLESALE']=='':
                vkorgList.append(currProduct['VKORG'])
        vkorgList=list(set(vkorgList))
        return vkorgList

    data['avail_01'] = data['sku'].apply(lambda x: ",".join(vkorgForAvail_01(product_dict[str(x)])) if str(x) in product_dict else 'False')
    data['avail_02'] = data['sku'].apply(lambda x: ",".join(vkorgForAvail_02(product_dict[str(x)])) if str(x) in product_dict else 'False')
    return data

