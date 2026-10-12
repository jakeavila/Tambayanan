from pyscript import document

# Hour rates
RATES = {
    "chill": 20,
    "study": 25,
}

def calculate_price(event=None):
    area = document.querySelector("#area").value
    hours_text = document.querySelector("#hours").value
    result = document.querySelector("#price-result")
    details = document.querySelector("#price-details")

    try:
        hours = float(hours_text)
        if hours <= 0:
            raise ValueError
    except (ValueError, TypeError):
        result.innerText = "Please check your input"
        details.innerText = "Enter a number of hours greater than zero."
        return

    rate = RATES[area]
    total = rate * hours
    area_name = "Chill Zone" if area == "chill" else "Quiet Study Room"
    result.innerText = f"₱{total:,.2f}"
    details.innerText = f"{area_name} · {hours:g} hour(s) · ₱{rate}/hour"

def reset_estimator(event=None):
    document.querySelector("#area").value = "chill"
    document.querySelector("#hours").value = "1"
    document.querySelector("#price-result").innerText = "₱20.00"
    document.querySelector("#price-details").innerText = "Chill Zone · 1 hour · ₱20/hour"
