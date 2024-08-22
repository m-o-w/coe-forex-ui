import streamlit as st
import requests
from datetime import date

# List of possible currencies
currencies = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", 
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", 
    "GBP"
]

# API subscription key
subscription_key = "196b986195024d4699c982b6a4b740e1"

# Streamlit UI
st.title("Forex Rate Fetcher")

# Sidebar with tabs
tab = st.sidebar.selectbox("Select Tab", ["Get Forex Rates", "Design"])

if tab == "Get Forex Rates":
    st.write("Select the base and target currencies, and choose a date to fetch the exchange rate.")

    # Drop-downs for base and target currencies
    base_currency = st.selectbox("Base Currency", currencies)
    target_currency = st.selectbox("Target Currency", currencies)

    # Date input
    selected_date = st.date_input("Select Date", value=date.today())

    # Button to invoke API
    if st.button("Get Rate"):
        if base_currency == target_currency:
            st.error("Base currency and target currency cannot be the same. Please select different currencies.")
        else:
            # Formatting the date in the required format (DD-MM-YYYY)
            formatted_date = selected_date.strftime("%d-%m-%Y")
            
            # Constructing the URL
            url = f"https://coe-apim-02.azure-api.net/forex/rate?baseCurrency={base_currency}&targetCurrency={target_currency}&date={formatted_date}"
            
            # Setting the headers
            headers = {
                "Ocp-Apim-Subscription-Key": subscription_key
            }
            
            # Making the API request
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                st.success("Request Successful")
                st.write("Exchange Rate:", response.json())
            else:
                st.error(f"No Data found. Response code: INT-{response.status_code}")
                st.write(response.text)

elif tab == "Design":
    st.write("Design Image")
    st.image("Design.jpg")