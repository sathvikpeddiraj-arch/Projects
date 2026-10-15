
import json
import streamlit as st

# Configure page
st.set_page_config(
    page_title="Smart Menu System",
    page_icon="🍛"
)

# Read JSON file
with open("menu.json", "r", encoding="utf-8") as file:
    menu_items = json.load(file)

st.title("🍛 Smart Menu")
st.write("Choose your favourite items!")

# Initialize session state
if "confirmed_order" not in st.session_state:
    st.session_state.confirmed_order = None

# Category filtering
categories = sorted({
    item["Category"] for item in menu_items
})

selected_category = st.selectbox(
    "Filter by category",
    ["All"] + categories
)

if selected_category == "All":
    filtered_items = menu_items
else:
    filtered_items = [
        item for item in menu_items
        if item["Category"] == selected_category
    ]

quantities = {}

# Menu form
with st.form("menu_order_form"):

    columns = st.columns(3)

    for index, item in enumerate(filtered_items):
        with columns[index % 3]:
            st.subheader(item["Item_Name"])
            st.write(f"Category: {item['Category']}")
            st.write(f"Price: ${item['Price']}")

            quantities[item["Item_ID"]] = st.number_input(
                f"QTY - {item['Item_Name']}",
                min_value=0,
                max_value=10,
                value=0,
                step=1,
                key=f"qty_{item['Item_ID']}"
            )

    submitted = st.form_submit_button(
        "Place order & generate bill",
        use_container_width=True
    )

# Process order after submission
if submitted:
    order = []

    for item in filtered_items:
        quantity = quantities[item["Item_ID"]]

        if quantity > 0:
            order.append({
                "id": item["Item_ID"],
                "Name": item["Item_Name"],
                "Price": item["Price"],
                "quantity": quantity,
                "subtotal": item["Price"] * quantity
            })

    st.session_state.confirmed_order = order

# Display bill
if st.session_state.confirmed_order is not None:
    st.divider()
    st.header("🧾 Your Bill")

    order = st.session_state.confirmed_order

    if order:
        for item in order:
            st.write(
                f"**{item['Name']}** — "
                f"{item['quantity']} × ${item['Price']} "
                f"= ${item['subtotal']}"
            )

        total = sum(item["subtotal"] for item in order)
        st.metric("Grand Total", f"${total:.2f}")
        st.success("Order confirmed successfully!")

    else:
        st.warning("You haven't selected any items.")
