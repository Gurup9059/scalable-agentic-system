def route(query: str):
    q = query.lower()

  
    if "invoice" in q:
        return ["create_invoice"]

   
    elif "payment" in q or "pay" in q:
        return ["send_payment"]


    elif "dispute" in q:
        return ["check_dispute"]


    elif "sales" in q or "report" in q or "volume" in q:
        return ["get_sales_report"]

   
    elif "tool" in q or "available" in q or "status" in q:
        return ["system_search"]

    else:
        return ["rag_search"]
