import joblib
import pandas as pd
import math
import re 

model = joblib.load("xgb_model.joblib")


df_train = pd.read_csv("supply_chain_dataset.csv")
medians =  df_train.median(numeric_only=True).to_dict()

print("\nEnter data :\n")
sku_input = input("SKU / product_name / sku_label: ").strip()
daily_demand = float(input("Daily demand: ").strip())
current_stock = float(input("Current stock (inventory_on_hand): ").strip())
shelf_life = float(input("Shelf life (days): ").strip())
lead_time = float(input("Lead time (days): ").strip())
moq = float(input("Supplier minimum order qty (MOQ): ").strip())
unit_cost = float(input("Cost per unit: ").strip())

expected = list(model.feature_names_in_)
input_row = {f:float(medians.get(f,0.0)) for f in expected}


def place(cands, val):
    for c in cands:
        if c in input_row:
            input_row[c] = float(val)
            return True
    return False

place(["sku_label","sku","product_name"], sku_input)
place(["base_daily_demand","observed_daily_demand","daily_demand"], daily_demand)
place(["inventory_on_hand","inventory","current_stock"], current_stock)
place(["shelf_life_days","shelf_life"], shelf_life)
place(["lead_time_days","lead_time"], lead_time)
place(["supplier_min_order_qty","supplier_min_qty","min_order_qty"], moq)
place(["unit_cost","unit_price","price_per_unit"], unit_cost)

X_pred = pd.DataFrame([input_row], columns=expected)
pred = float(model.predict(X_pred)[0])

additional = max(0, pred - current_stock)
if additional > 0 and moq>0 and additional < moq:
    additional = math.ceil(moq)
else:
    additional = math.ceil(additional)


print("\nInitial Calculation Done.")


df_prod = pd.read_csv("supply_chain_dataset.csv", dtype=str)

def pick_col(cols, names):
    for n in names:
        for c in cols:
            if c.lower() == n.lower():
                return c
    return None

sku_col = pick_col(df_prod.columns, ["sku"])
prod_col = pick_col(df_prod.columns, ["product_name"])

def normalize(s):
    s = str(s).strip().upper()
    return re.sub(r'[^A-Z0-9]', '', s)

sku_norm_map = { normalize(k): v for k,v in zip(df_prod[sku_col], df_prod[prod_col]) }

sku_norm = normalize(sku_input)
product_name = sku_norm_map.get(sku_norm)

if product_name is None:
    numbers = re.findall(r'\d+', sku_input)
    if numbers:
        num = numbers[0].lstrip("0")
        for k,v in sku_norm_map.items():
            if num in re.sub(r'[^0-9]', '', k):
                product_name = v
                break

if product_name is None:
    product_name = sku_input  

total_cost = unit_cost * additional
print("\n--------------------------")
print(" PRODUCT SUMMARY")
print("--------------------------")
print("Product name:", product_name)
print("Recommended order qty:", round(pred, 3))
print("Suggested additional order:", additional)
print("Total cost for additional order: $", round(total_cost, 2))
print("--------------------------")