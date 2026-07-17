def create_invoice():
    return {
        "status": "success",
        "invoice_id": "INV-1001",
        "message": "Invoice created successfully"
    }

def send_payment():
    return {
        "status": "success",
        "transaction_id": "TXN-7788",
        "message": "Payment sent successfully"
    }

def check_dispute():
    return {
        "status": "open",
        "dispute_id": "DSP-9001",
        "message": "Dispute is currently open"
    }

def get_sales_report():
    return {
        "status": "success",
        "total_sales": "$12,450",
        "month": "Last Month"
    }

def rag_search():
    return {
        "status": "success",
        "answer": "Retrieved relevant documentation from the knowledge base"
    }

def system_search():
    return {
        "status": "success",
        "available_tools": [
            "create_invoice",
            "send_payment",
            "check_dispute",
            "get_sales_report",
            "rag_search",
            "system_search"
        ]
    }
