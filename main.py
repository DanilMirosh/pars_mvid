import json

import requests


def get_data():
    cookies = {
        '__lhash_': '9f83ad94c8aa9c3b234cb7639fe6080b',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_6276',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_GUEST_ID': '21206344031',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '5600000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '0',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '17',
        'MVID_REGION_SHOP': 'S930',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        'MVID_SUPER_FILTERS': 'true',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '5',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '1',
        '_gid': 'GA1.2.857063911.1659895986',
        '_ym_uid': '165989598647554477',
        '_ym_d': '1659895986',
        '_ym_isad': '2',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '34428f2e2e857db0575055089505635f',
        'tmr_lvidTS': '1659895988509',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'c25d006c-5de2-4129-b416-d77d338b5143',
        'uxs_uid': '974e72d0-167c-11ed-966e-2b8fb72cf25d',
        'advcake_track_id': '9dbef5c7-9177-720b-b37b-92e6eaecabdb',
        'advcake_session_id': '555b9d08-489c-0c66-5d6b-98b712110b06',
        'st_uid': 'dd7dc0178f74c93aa5a58316bae4e646',
        'flocktory-uuid': 'e190b69c-8115-4bcf-ae22-08910a90ac38-8',
        'afUserId': '42ba1634-ae9f-439e-a724-38f843a7cb68-p',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': '2XrSvwQVvGQFTsNRBhvpb2CGFTDnh0pKMhn5fsm0R525TF1nGhTv!141656296',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2919554058.20480.0000',
        'bIPs': '1595647062',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrYy9ALRZ6RRFsbhdJXC8hfVsdRz1dUFgLHz15JR0nYnZXCVoLRGIZM3xtKHMdDCFUeRlBGjxpHmVMXyFMWz56Kx4af3QoWA8UX0BFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyfDFEaiZoSFkmSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==Y3jwYw==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrYy9ALRZ6RRFsbhdJXC8hfVsdRz1dUFgLHz15JR0nYnZXCVoLRGIZM3xtKHMdDCFUeRlBGjxpHmVMXyFMWz56Kx4af3QoWA8UX0BFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyfDFEaiZoSFkmSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==Y3jwYw==',
        'cfidsgib-w-mvideo': 'NZWufuB7W2Z1oXbN7PifphqQ/7sKlZSHaPScwsxQWg9WlfZDBqUyn6rPoKVBnJ5UeDv0xrIG5vjPiEZ2LzxYrPn1MvhdKszYW6DGfI+P3l96wjEXmN6uVa7ebFJR1/DVTvw4a08nV4yMP3x8aeKOfl+tWt9ycZn7dLYr',
        'cfidsgib-w-mvideo': 'NZWufuB7W2Z1oXbN7PifphqQ/7sKlZSHaPScwsxQWg9WlfZDBqUyn6rPoKVBnJ5UeDv0xrIG5vjPiEZ2LzxYrPn1MvhdKszYW6DGfI+P3l96wjEXmN6uVa7ebFJR1/DVTvw4a08nV4yMP3x8aeKOfl+tWt9ycZn7dLYr',
        'gsscgib-w-mvideo': 'Scoxng1knrgESqbmS4Uk1BWYEZqk2MQnQFa9UJN1xgXx0aKkNyBerXUftuyx5YHrRpqOzOmase+ywSQyewe7KgvN/7jaDstANs9Z2Lr5kazSYlla6dzcXNujv610kPzsaH15Sel4nMZ1xKjmTMg0tXmxh/14qbdXdj0Rsr6Zy9IoR/Xy8SblhdefnZ7cLQwffyi804ft9JEvbTNnyktLA+5c7NEJKCYTyHcvKGHBViR5yxr9VtPq2mL8arKtow==',
        'gsscgib-w-mvideo': 'Scoxng1knrgESqbmS4Uk1BWYEZqk2MQnQFa9UJN1xgXx0aKkNyBerXUftuyx5YHrRpqOzOmase+ywSQyewe7KgvN/7jaDstANs9Z2Lr5kazSYlla6dzcXNujv610kPzsaH15Sel4nMZ1xKjmTMg0tXmxh/14qbdXdj0Rsr6Zy9IoR/Xy8SblhdefnZ7cLQwffyi804ft9JEvbTNnyktLA+5c7NEJKCYTyHcvKGHBViR5yxr9VtPq2mL8arKtow==',
        'AF_SYNC': '1659895992946',
        'fgsscgib-w-mvideo': '5BwW8870e61cc16516a2cbeba33fb7b021d9e6a7',
        'fgsscgib-w-mvideo': '5BwW8870e61cc16516a2cbeba33fb7b021d9e6a7',
        'cfidsgib-w-mvideo': 'YlXaboepS2gaEkckNKjKcVI0bbrMTGsoh6y9yOLRWE6UTQnV6mBPzLA1WtxpxGHd6rzHPggprnKpfRRJ8B+uexcuBTVnNj/xR91htnGpgbrACDkbczncmTRMlO1El1JBI/Uz4YNPYyBeUmQWb5tYS0yuo0wXFBlDvNE/',
        'CACHE_INDICATOR': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CREDIT_AVAILABILITY': 'true',
        '_ga': 'GA1.2.180640817.1659895986',
        'tmr_detect': '0%7C1659896015188',
        'tmr_reqNum': '26',
        '_ga_CFMZTSS5FM': 'GS1.1.1659895985.1.1.1659896146.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1659895985.1.1.1659896146.60',
        'mindboxDeviceUUID': 'ecf84945-5f18-470a-82e9-5d1f44b289be',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22ecf84945-5f18-470a-82e9-5d1f44b289be%22%7D',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=9f83ad94c8aa9c3b234cb7639fe6080b; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_6276; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_GUEST_ID=21206344031; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=5600000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=17; MVID_REGION_SHOP=S930; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=true; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=1; _gid=GA1.2.857063911.1659895986; _ym_uid=165989598647554477; _ym_d=1659895986; _ym_isad=2; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; tmr_lvid=34428f2e2e857db0575055089505635f; tmr_lvidTS=1659895988509; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=c25d006c-5de2-4129-b416-d77d338b5143; uxs_uid=974e72d0-167c-11ed-966e-2b8fb72cf25d; advcake_track_id=9dbef5c7-9177-720b-b37b-92e6eaecabdb; advcake_session_id=555b9d08-489c-0c66-5d6b-98b712110b06; st_uid=dd7dc0178f74c93aa5a58316bae4e646; flocktory-uuid=e190b69c-8115-4bcf-ae22-08910a90ac38-8; afUserId=42ba1634-ae9f-439e-a724-38f843a7cb68-p; wurfl_device_id=generic_web_browser; JSESSIONID=2XrSvwQVvGQFTsNRBhvpb2CGFTDnh0pKMhn5fsm0R525TF1nGhTv!141656296; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; bIPs=1595647062; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrYy9ALRZ6RRFsbhdJXC8hfVsdRz1dUFgLHz15JR0nYnZXCVoLRGIZM3xtKHMdDCFUeRlBGjxpHmVMXyFMWz56Kx4af3QoWA8UX0BFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyfDFEaiZoSFkmSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==Y3jwYw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrYy9ALRZ6RRFsbhdJXC8hfVsdRz1dUFgLHz15JR0nYnZXCVoLRGIZM3xtKHMdDCFUeRlBGjxpHmVMXyFMWz56Kx4af3QoWA8UX0BFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyfDFEaiZoSFkmSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==Y3jwYw==; cfidsgib-w-mvideo=NZWufuB7W2Z1oXbN7PifphqQ/7sKlZSHaPScwsxQWg9WlfZDBqUyn6rPoKVBnJ5UeDv0xrIG5vjPiEZ2LzxYrPn1MvhdKszYW6DGfI+P3l96wjEXmN6uVa7ebFJR1/DVTvw4a08nV4yMP3x8aeKOfl+tWt9ycZn7dLYr; cfidsgib-w-mvideo=NZWufuB7W2Z1oXbN7PifphqQ/7sKlZSHaPScwsxQWg9WlfZDBqUyn6rPoKVBnJ5UeDv0xrIG5vjPiEZ2LzxYrPn1MvhdKszYW6DGfI+P3l96wjEXmN6uVa7ebFJR1/DVTvw4a08nV4yMP3x8aeKOfl+tWt9ycZn7dLYr; gsscgib-w-mvideo=Scoxng1knrgESqbmS4Uk1BWYEZqk2MQnQFa9UJN1xgXx0aKkNyBerXUftuyx5YHrRpqOzOmase+ywSQyewe7KgvN/7jaDstANs9Z2Lr5kazSYlla6dzcXNujv610kPzsaH15Sel4nMZ1xKjmTMg0tXmxh/14qbdXdj0Rsr6Zy9IoR/Xy8SblhdefnZ7cLQwffyi804ft9JEvbTNnyktLA+5c7NEJKCYTyHcvKGHBViR5yxr9VtPq2mL8arKtow==; gsscgib-w-mvideo=Scoxng1knrgESqbmS4Uk1BWYEZqk2MQnQFa9UJN1xgXx0aKkNyBerXUftuyx5YHrRpqOzOmase+ywSQyewe7KgvN/7jaDstANs9Z2Lr5kazSYlla6dzcXNujv610kPzsaH15Sel4nMZ1xKjmTMg0tXmxh/14qbdXdj0Rsr6Zy9IoR/Xy8SblhdefnZ7cLQwffyi804ft9JEvbTNnyktLA+5c7NEJKCYTyHcvKGHBViR5yxr9VtPq2mL8arKtow==; AF_SYNC=1659895992946; fgsscgib-w-mvideo=5BwW8870e61cc16516a2cbeba33fb7b021d9e6a7; fgsscgib-w-mvideo=5BwW8870e61cc16516a2cbeba33fb7b021d9e6a7; cfidsgib-w-mvideo=YlXaboepS2gaEkckNKjKcVI0bbrMTGsoh6y9yOLRWE6UTQnV6mBPzLA1WtxpxGHd6rzHPggprnKpfRRJ8B+uexcuBTVnNj/xR91htnGpgbrACDkbczncmTRMlO1El1JBI/Uz4YNPYyBeUmQWb5tYS0yuo0wXFBlDvNE/; CACHE_INDICATOR=false; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; _ga=GA1.2.180640817.1659895986; tmr_detect=0%7C1659896015188; tmr_reqNum=26; _ga_CFMZTSS5FM=GS1.1.1659895985.1.1.1659896146.0; _ga_BNX5WPP3YK=GS1.1.1659895985.1.1.1659896146.60; mindboxDeviceUUID=ecf84945-5f18-470a-82e9-5d1f44b289be; directCrm-session=%7B%22deviceGuid%22%3A%22ecf84945-5f18-470a-82e9-5d1f44b289be%22%7D; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; MVID_ENVCLOUD=prod1',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-set-application-id': '4526b8db-656d-41ed-b1ec-fcd3f4ce6ee8',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)
    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_base_price'] = prices.get('item_basePrice')
        item['item_sale_price'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
