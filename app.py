import streamlit as st

st.set_page_config(
    page_title="Collect Prints",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
      /* Fonts only globally — don't force colors on all Streamlit widgets */
      html, body, .stApp, [data-testid="stAppViewContainer"] {
        font-family: "Figtree", sans-serif;
      }
      h1, h2, h3, .cp-brand, .cp-section {
        font-family: "Syne", sans-serif !important;
        letter-spacing: -0.02em;
      }
      .stApp {
        background:
          radial-gradient(1200px 500px at 10% -10%, #ffedd5 0%, transparent 55%),
          radial-gradient(900px 400px at 100% 0%, #e2e8f0 0%, transparent 50%),
          #f8fafc;
        color: #1c1917;
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 980px;
      }
      .cp-hero {
        background: linear-gradient(135deg, #1c1917 0%, #292524 55%, #9a3412 140%);
        border-radius: 18px;
        padding: 2.4rem 2rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 18px 40px rgba(28, 25, 23, 0.18);
      }
      .cp-brand {
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0 0 0.35rem 0;
        line-height: 1.05;
        color: #fff7ed;
      }
      .cp-tag {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        background: #ea580c;
        color: #ffffff;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 0.9rem;
      }
      .cp-sub {
        margin: 0;
        font-size: 1.08rem;
        max-width: 36rem;
        line-height: 1.55;
        color: #ffedd5;
        font-weight: 500;
      }
      .cp-note {
        background: #ecfeff;
        border: 1px solid #67e8f9;
        color: #0e7490;
        border-radius: 12px;
        padding: 0.85rem 1rem;
        margin: 1rem 0 1.25rem;
        font-size: 1rem;
        font-weight: 500;
      }
      .cp-note strong { color: #155e75; }
      .cp-card {
        background: #ffffff;
        border: 1px solid #d6d3d1;
        border-radius: 16px;
        padding: 1.15rem 1.2rem 0.4rem;
        margin-bottom: 0.85rem;
        box-shadow: 0 8px 24px rgba(28, 25, 23, 0.05);
      }
      .cp-card h3 { color: #0c0a09; margin: 0 0 0.35rem 0; }
      .cp-card p {
        color: #44403c;
        font-weight: 500;
        margin: 0 0 0.35rem 0;
      }
      .cp-price {
        color: #c2410c;
        font-weight: 700;
      }
      .cp-section {
        font-size: 1.45rem;
        font-weight: 700;
        margin: 1.6rem 0 0.75rem;
        color: #0c0a09;
      }
      .cp-footer {
        text-align: center;
        color: #57534e;
        font-size: 0.95rem;
        margin-top: 2.5rem;
        padding-top: 1.25rem;
        border-top: 1px solid #d6d3d1;
        font-weight: 500;
      }
      div[data-testid="stButton"] button {
        border-radius: 10px !important;
        font-family: "Figtree", sans-serif !important;
        font-weight: 600 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cp-hero">
      <div class="cp-tag">Resin shop</div>
      <p class="cp-brand">Collect Prints</p>
      <p class="cp-sub">
        Custom resin keycaps and made-to-order commissions.
        Built for makers who want detail — not paper crafts.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cp-note">
      <strong>Demo accounts only</strong> — login is stored in session and resets when you leave.
      Real checkout can be added with Stripe later.
    </div>
    """,
    unsafe_allow_html=True,
)

if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin"}
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
if "cart" not in st.session_state:
    st.session_state.cart = []
if "stock" not in st.session_state:
    st.session_state.stock = {
        "keycaps": 40,
        "commission": 5,
    }

st.markdown('<p class="cp-section">Account</p>', unsafe_allow_html=True)
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

st.markdown('<p class="cp-section">Shop</p>', unsafe_allow_html=True)

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
    left = st.session_state.stock.get(p["id"], 0)
    st.markdown(
        f"""
        <div class="cp-card">
          <h3 style="margin:0 0 0.35rem 0;">{p['name']}
            <span class="cp-price">£{p['price']:.2f}</span>
          </h3>
          <p style="margin:0 0 0.35rem 0; color:#292524; font-weight:500;">{p['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
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

st.markdown('<p class="cp-section">Your cart</p>', unsafe_allow_html=True)
if not st.session_state.cart:
    st.info("Cart is empty. Add a print above.")
else:
    subtotal = 0.0
    for item in st.session_state.cart:
        st.write(f"- {item['name']} — £{item['price']:.2f}")
        subtotal += item["price"]

    LABOUR_RATE = 0.15
    TAX_RATE = 0.20
    SHIPPING_FEE = 3.50

    labour = subtotal * LABOUR_RATE
    taxable = subtotal + labour
    tax = taxable * TAX_RATE
    shipping = SHIPPING_FEE
    total = taxable + tax + shipping

    st.write(f"Subtotal: £{subtotal:.2f}")
    st.write(f"Labour (15%): £{labour:.2f}")
    st.write(f"Tax / VAT (20%): £{tax:.2f}")
    st.write(f"Shipping: £{shipping:.2f}")
    st.write(f"**Total: £{total:.2f}**")

    notes = st.text_area("Order notes (colour, legend, keycap style, etc.)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear cart"):
            for item in st.session_state.cart:
                st.session_state.stock[item["id"]] = (
                    st.session_state.stock.get(item["id"], 0) + 1
                )
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

st.markdown('<p class="cp-section">Contact</p>', unsafe_allow_html=True)
st.write("For real orders and commissions, reach out or add Stripe checkout next.")
st.link_button("Email enquiries", "mailto:hello@collectprints.example")

st.markdown(
    """
    <div class="cp-footer">
      Copyright 2026 Collect Prints. All rights reserved.<br>
      Resin 3D printed products · Demo shop
    </div>
    """,
    unsafe_allow_html=True,
)
