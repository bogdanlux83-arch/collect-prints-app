import streamlit as st

st.set_page_config(page_title="Collect Prints", page_icon="🖨️")
st.title("Collect Prints")
st.header("Custom 3D prints for sale")

st.write(
    "Resin 3D prints for sale — custom keycaps and made-to-order commissions."
)

st.markdown(
    """
    <span style="background: linear-gradient(90deg, #F97316, #EA580C);
                 color: white; padding: 4px 12px; font-weight: bold; border-radius: 4px;">
        COLLECT PRINTS · SHOP
    </span>
    """,
    unsafe_allow_html=True,
)

# Demo auth
st.markdown(
    """
    <span style="background: linear-gradient(90deg, #06B6D4, #3B82F6);
                 color: white; padding: 4px 12px; font-weight: bold; border-radius: 4px;">
        Important
    </span>
    """,
    unsafe_allow_html=True,
)
st.write(
    "Demo accounts only for now — login is stored in session and resets when you leave. "
    "Real checkout/payments can be added with Stripe later."
)

if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin"}
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
if "cart" not in st.session_state:
    st.session_state.cart = []
if "stock" not in st.session_state:
    # starting stock (resets when app session restarts)
    st.session_state.stock = {
        "keycaps": 40,
        "commission": 5,  # limited commission slots
    }

tab_login, tab_signup = st.tabs(["Login", "Signup"])

with tab_login:
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        if (
            login_username in st.session_state.users
            and st.session_state.users[login_username] == login_password
        ):
            st.session_state.logged_in_user = login_username
            st.success(f"Welcome back, {login_username}!")
        else:
            st.error("Invalid username or password")

with tab_signup:
    signup_username = st.text_input("Username", key="signup_username")
    signup_password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Create Account"):
        if not signup_username or not signup_password:
            st.warning("Please enter a username and password")
        elif signup_username in st.session_state.users:
            st.error("Username already exists")
        else:
            st.session_state.users[signup_username] = signup_password
            st.success(f"Account created successfully for {signup_username}!")

if st.session_state.logged_in_user:
    st.write(f"Logged in as **{st.session_state.logged_in_user}**")

# Products for sale
st.subheader("Shop — 3D printed products")

products = [
    {
        "id": "keycaps",
        "name": "Resin Keycaps",
        "price": 8.00,
        "desc": "Custom resin keycaps. Tell me style/colour/legend in order notes.",
    },
    {
        "id": "commission",
        "name": "Custom Resin Commission",
        "price": 35.00,
        "desc": "Your model or idea printed in resin. Message after order to confirm details.",
    },
]

for p in products:
    with st.container():
        left = st.session_state.stock.get(p["id"], 0)
        st.markdown(f"### {p['name']} — £{p['price']:.2f}")
        st.write(p["desc"])
        if left > 0:
            st.caption(f"In stock: {left}")
        else:
            st.error("Out of stock")
        if st.button(
            f"Add to cart — {p['name']}",
            key=f"add_{p['id']}",
            disabled=left <= 0,
        ):
            st.session_state.cart.append(p)
            st.session_state.stock[p["id"]] -= 1
            st.success(f"Added {p['name']} to cart ({st.session_state.stock[p['id']]} left)")
            st.rerun()

st.subheader("Your cart")
if not st.session_state.cart:
    st.info("Cart is empty. Add a print above.")
else:
    total = 0.0
    for i, item in enumerate(st.session_state.cart):
        st.write(f"- {item['name']} — £{item['price']:.2f}")
        total += item["price"]
    st.write(f"**Total: £{total:.2f}**")

    notes = st.text_area("Order notes (colour, legend, keycap style, etc.)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear cart"):
            # put stock back
            for item in st.session_state.cart:
                st.session_state.stock[item["id"]] = st.session_state.stock.get(item["id"], 0) + 1
            st.session_state.cart = []
            st.rerun()
    with col2:
        if st.button("Place order (demo)"):
            st.success(
                "Demo order placed! No real payment yet. "
                "Next step: connect Stripe to take real money."
            )
            if notes.strip():
                st.write(f"Notes saved: {notes}")
            st.session_state.cart = []

st.subheader("Contact / buy")
st.write("For real orders and commissions, reach out or add Stripe checkout next.")
st.link_button("Email enquiries (mailto)", "mailto:hello@collectprints.example")

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
      Copyright 2026 Collect Prints. All rights reserved.<br>
      3D printed products · Demo shop
    </div>
    """,
    unsafe_allow_html=True,
)
