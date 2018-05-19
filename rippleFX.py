import python_bitbankcc
from time import sleep

API_KEY = 'bf389d35-8d89-4289-8d5a-cb31ee341d92'
API_SECRET = '9d797a7d6ffa027cf9069f62e9787a7e80442e393c658256af252cb07bef0b53'
prv = python_bitbankcc.private(API_KEY, API_SECRET)
#activeOrders = prv.get_active_orders(pair)
balances = prv.get_asset()
for data in balances['assets']:

    print('●通貨：' + data['asset'])

    print('保有量：' + data['onhand_amount'])

    pub = python_bitbankcc.public()

# -*- ticker取得 -*-

value = pub.get_ticker(
    'xrp_jpy' # ペア
)
print(value)
#現在の売り注文の最安値
print('sell:' + value['sell'])
#現在の買い注文の最高値
print('buy:' + value['buy'])
#過去24時間の最高値取引価格
print('high:' + value['high'])
#過去24時間の最安値取引価格
print('low:' + value['low'])

# -*- ticker取得 -*-

#注文データ
buyOrderInfo = {"pair":"xrp_jpy",#ペア
             "amount":2,#注文枚数
             "price":73.5,#注文価格
             "orderSide":"buy", #buy or sell
             "orderType":"limit" #指値注文の場合はlimit
             }
sellOrderInfo = {"pair":"xrp_jpy",#ペア
             "amount":2,#注文枚数
             "price":73.7,#注文価格
             "orderSide":"sell", #buy or sell
             "orderType":"limit" #指値注文の場合はlimit
             }

#注文処理
def Order(orderInfo):
    #Order
    value = prv.order(
        orderInfo["pair"], # ペア
        orderInfo["price"], # 価格
        orderInfo["amount"], # 注文枚数
        orderInfo["orderSide"], # 注文サイド 売 or 買(buy or sell)
        orderInfo["orderType"] # 注文タイプ 指値 or 成行(limit or market))
    )
    return value

#注文を行う
while True:
    if float(data['onhand_amount']) > 20.0:

        print("注文開始")

        buyInfo = Order(buyOrderInfo)

        print('sellPrice:' + buyInfo['price'])
        print('amount:' + buyInfo['amount'])
        print('orderSide:' + buyInfo['orderSide'])
        print('orderType:' + buyInfo['orderType'])

        sellInfo = Order(sellOrderInfo)

        print('buyPrice:' + buyInfo['price'])
        print('amount:' + buyInfo['amount'])
        print('orderSide:' + buyInfo['orderSide'])
        print('orderType:' + buyInfo['orderType'])

        print("注文完了")
        sleep(60)
