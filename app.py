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
      html, body, .stApp, [data-testid="stAppViewContainer"] {
        font-family: "Figtree", sans-serif;
        font-size: 18px;
      }
      h1, h2, h3, .cp-brand, .cp-section {
        font-family: "Syne", sans-serif !important;
        letter-spacing: -0.02em;
      }
      .stApp {
        background:
          radial-gradient(1000px 520px at 8% -8%, #fdba74 0%, transparent 55%),
          radial-gradient(800px 420px at 95% 5%, #fb923c 0%, transparent 45%),
          radial-gradient(700px 380px at 50% 110%, #fed7aa 0%, transparent 50%),
          #fff7ed;
        color: #1c1917;
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1280px;
      }
      section.main > div {
        max-width: 1280px;
      }
      .cp-hero {
        background: linear-gradient(125deg, #9a3412 0%, #c2410c 40%, #ea580c 75%, #fb923c 100%);
        border-radius: 22px;
        padding: 2.8rem 2.2rem 2.3rem;
        margin-bottom: 1.6rem;
        box-shadow: 0 22px 50px rgba(194, 65, 12, 0.28);
      }
      .cp-brand {
        font-size: 3.4rem;
        font-weight: 800;
        margin: 0 0 0.5rem 0;
        line-height: 1.02;
        color: #fff7ed;
      }
      .cp-tag {
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        background: #1c1917;
        color: #fdba74;
        padding: 0.45rem 0.85rem;
        border-radius: 999px;
        margin-bottom: 1rem;
      }
      .cp-sub {
        margin: 0;
        font-size: 1.28rem;
        max-width: 38rem;
        line-height: 1.55;
        color: #ffedd5;
        font-weight: 600;
      }
      .cp-note {
        background: #fff7ed;
        border: 2px solid #fb923c;
        color: #9a3412;
        border-radius: 14px;
        padding: 1rem 1.15rem;
        margin: 1rem 0 1.35rem;
        font-size: 1.12rem;
        font-weight: 600;
      }
      .cp-note strong { color: #7c2d12; }
      .cp-card {
        background: #ffffff;
        border: 2px solid #fdba74;
        border-radius: 18px;
        padding: 1.35rem 1.35rem 0.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 10px 28px rgba(234, 88, 12, 0.12);
      }
      .cp-card h3 {
        color: #0c0a09;
        margin: 0 0 0.45rem 0;
        font-size: 1.55rem;
      }
      .cp-card p {
        color: #44403c;
        font-weight: 600;
        margin: 0 0 0.45rem 0;
        font-size: 1.08rem;
        line-height: 1.5;
      }
      .cp-price {
        color: #ea580c;
        font-weight: 800;
        font-size: 1.35rem;
      }
      .cp-section {
        font-size: 1.85rem;
        font-weight: 800;
        margin: 1.8rem 0 0.9rem;
        color: #9a3412;
      }
      .cp-footer {
        text-align: center;
        color: #7c2d12;
        font-size: 1.05rem;
        margin-top: 2.8rem;
        padding-top: 1.4rem;
        border-top: 2px solid #fdba74;
        font-weight: 600;
      }
      div[data-testid="stButton"] button {
        border-radius: 12px !important;
        font-family: "Figtree", sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 0.55rem 1.1rem !important;
      }
      [data-testid="stCaption"] {
        font-size: 1rem !important;
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

cols = st.columns(2)
for i, p in enumerate(products):
    with cols[i % 2]:
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
            st.success(
                f"Added {p['name']} to cart ({st.session_state.stock[p['id']]} left)"
            )
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
