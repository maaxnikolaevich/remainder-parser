import datetime
import pandas as pd
from Requests import get_products_by_store


def process():
    data = pd.read_csv(r'data/search_ecom_sku_word.csv', delimiter=';', chunksize=10000)
    begin_time = datetime.datetime.now()
    result = pd.DataFrame()
    for item in data:
        codes_list = item["sku"].values
        result = pd.concat([result, form_to_df(codes_list, item)])
    result.to_csv(r'data/res.csv', sep=';', index=False)
    print(f"Время выполнения запроса: {datetime.datetime.now() - begin_time}")


def conv_to_dict(products):
    result = {}
    for curr_product in products:
        if not curr_product['MATNR'] in result:
            result[curr_product['MATNR']] = []
        result[curr_product['MATNR']].append(curr_product)
    return result


def vkorg_for_avail_01(products):
    vkorg_list = []
    for curr_product in products:
        if curr_product['WHOLESALE'] == 'X':
            vkorg_list.append(curr_product['VKORG'])
    vkorg_list = list(set(vkorg_list))
    return vkorg_list


def vkorg_for_avail_02(products):
    vkorg_list = []
    for curr_product in products:
        if curr_product['WHOLESALE'] == '':
            vkorg_list.append(curr_product['VKORG'])
    vkorg_list = list(set(vkorg_list))
    return vkorg_list


def form_to_df(codes_list, data):
    list_product_codes = []
    for product_code in codes_list:
        list_product_codes.append(f"{product_code}")
    products = get_products_by_store(list_product_codes)
    product_dict = conv_to_dict(products)
    data['avail_01'] = data['sku'].apply(
        lambda x: ",".join(vkorg_for_avail_01(product_dict[str(x)])) if str(x) in product_dict else 'False')
    data['avail_02'] = data['sku'].apply(
        lambda x: ",".join(vkorg_for_avail_02(product_dict[str(x)])) if str(x) in product_dict else 'False')
    return data
