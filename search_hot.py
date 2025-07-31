from dealabs import Dealabs
import json

dealabs = Dealabs()
deals = dealabs.get_hot_deals()   # ← C'EST LE BON NOM DE METHODE

def deal_to_dict(deal):
    return deal.__dict__ if hasattr(deal, "__dict__") else deal

deals_list = [deal_to_dict(deal) for deal in deals["data"]]

print(json.dumps(deals_list, ensure_ascii=False, indent=2))
