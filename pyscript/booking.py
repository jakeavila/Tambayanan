
from pyscript import document

# Space Prices
RATES = {
    "chill": 20,
    "study": 25
}


# Confirm Booking
def book_space(event=None):

    # Get the user's choices
    area = document.querySelector("#booking-area").value
    booking_date = document.querySelector("#booking-date").value
    booking_time = document.querySelector("#booking-time").value
    hours_text = document.querySelector("#booking-hours").value
    payment = document.querySelector("#booking-payment").value
    result = document.querySelector("#booking-result")

    # Check the booking date
    if not booking_date:
        result.innerHTML = """
            <h2>Missing Information</h2>
            <p>Please choose your booking date.</p>
        """
        return

    # Check the number of hours
    try:
        hours = int(hours_text)

        if hours < 1 or hours > 8:
            result.innerHTML = """
                <h2>Invalid Duration</h2>
                <p>Please choose between 1 and 8 hours.</p>
            """
            return

    except (ValueError, TypeError):
        result.innerHTML = """
            <h2>Invalid Input</h2>
            <p>Please enter a valid number of hours.</p>
        """
        return

    # Get the space name and price
    if area == "chill":
        area_name = "Chill Zone"
    else:
        area_name = "Quiet Study Room"

    rate = RATES[area]
    total = rate * hours

    # Display the booking summary
    result.innerHTML = f"""
        <h2>Booking Confirmed!</h2>
        <p><strong>Space:</strong> {area_name}</p>
        <p><strong>Date:</strong> {booking_date}</p>
        <p><strong>Start Time:</strong> {booking_time}</p>
        <p><strong>Duration:</strong> {hours} hour(s)</p>
        <p><strong>Payment:</strong> {payment}</p>
        <p><strong>Total:</strong> ₱{total:.2f}</p>
        <p>Please note: This is a demo confirmation only.</p>
    """

    # Reset the form after confirmation
    document.querySelector("#booking-area").value = "chill"
    document.querySelector("#booking-date").value = ""
    document.querySelector("#booking-time").selectedIndex = 0
    document.querySelector("#booking-hours").value = "1"
    document.querySelector("#booking-payment").selectedIndex = 0