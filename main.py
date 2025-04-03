from flask import Flask,request,jsonify
import freecurrencyapi

client = freecurrencyapi.Client('fca_live_VXh7xjvALo6SQQZU3qxq4DwT2Xn68fTTDojgHXKm')
app=Flask(__name__)


def converstion_factor(source,target):
    result = client.latest(source,[target])
    # print()
    return result["data"][target]

@app.route("/",methods=["POST"])
def entry():
    data=request.get_json()
    source_currency=data["queryResult"]["parameters"]["unit-currency"]["currency"]
    amount=data["queryResult"]["parameters"]["unit-currency"]["amount"]
    target_currency=data["queryResult"]["parameters"]["currency-name"]
    print("SOURCE CURRENCY :",source_currency)
    print("AMOUNT :",amount)
    print("TARGET CURRENCY :",target_currency)
    cf= converstion_factor(source_currency,target_currency)
    final_amount=cf*amount
    final_amount=round(final_amount,2)
    print(final_amount)
    response={
        "fulfillmentText":f"{amount} {source_currency} is {final_amount} {target_currency}"
    }
    return jsonify(response) 

@app.route("/try")
def entry1():

    return "Hello"

if __name__=="__main__":
    app.run(debug=True)