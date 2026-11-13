from textwrap import dedent

import streamlit as st


def show_html(content: str) -> None:
    """Render HTML without Streamlit treating indented lines as code."""
    st.html(dedent(content).strip())


def stock_label(left: int) -> str:
    if left <= 0:
        return "Out of stock"
    if left <= 5:
        return f"{left} left!"
    return f"In stock: {left}"


def show_stock(left: int, out_message: str = "Out of stock") -> None:
    if left <= 0:
        st.error(out_message)
    elif left <= 5:
        st.warning(stock_label(left))
    else:
        st.caption(stock_label(left))


st.set_page_config(
    page_title="Collect Prints",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

show_html(
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
      .cp-glow-panel {
        background: linear-gradient(160deg, #1c1917 0%, #7c2d12 55%, #ea580c 100%);
        border-radius: 20px;
        padding: 1.6rem 1.3rem 1.3rem;
        color: #fff7ed;
        min-height: 280px;
        border: 2px solid #fdba74;
        animation: cpGlow 2.2s ease-in-out infinite;
        box-shadow: 0 0 0 0 rgba(251, 146, 60, 0.55);
      }
      .cp-glow-panel h3 {
        font-family: "Syne", sans-serif;
        font-size: 1.55rem;
        margin: 0 0 0.55rem 0;
        color: #ffedd5;
      }
      .cp-glow-panel p {
        margin: 0 0 1rem 0;
        font-weight: 600;
        line-height: 1.45;
        color: #ffedd5;
      }
      @keyframes cpGlow {
        0%, 100% {
          box-shadow:
            0 0 12px 2px rgba(251, 146, 60, 0.45),
            0 0 28px 8px rgba(234, 88, 12, 0.25);
          border-color: #fdba74;
        }
        50% {
          box-shadow:
            0 0 22px 6px rgba(253, 186, 116, 0.85),
            0 0 48px 14px rgba(234, 88, 12, 0.45);
          border-color: #ffedd5;
        }
      }
      .size-ring {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.75rem;
        margin: 1.2rem 0 1.5rem;
      }
      .size-chip {
        text-align: center;
        background: #fff7ed;
        border: 2px solid #fb923c;
        border-radius: 999px;
        font-weight: 700;
        color: #7c2d12;
        box-shadow: 0 8px 18px rgba(234, 88, 12, 0.12);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      .size-chip.tiny { width: 4.2rem; height: 4.2rem; font-size: 0.75rem; }
      .size-chip.smallish { width: 5.2rem; height: 5.2rem; font-size: 0.82rem; }
      .size-chip.small { width: 6.2rem; height: 6.2rem; font-size: 0.9rem; }
      .size-chip.medium { width: 7.4rem; height: 7.4rem; font-size: 0.98rem; }
      .size-chip.big { width: 8.8rem; height: 8.8rem; font-size: 1.05rem; }
      .size-chip .label { font-family: "Syne", sans-serif; }
      .size-chip .meta { font-size: 0.78em; font-weight: 600; color: #9a3412; margin-top: 0.2rem; }
    </style>
    """
)

if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin"}
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
if "cart" not in st.session_state:
    st.session_state.cart = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "stock" not in st.session_state:
    st.session_state.stock = {
        "keycaps": 40,
        "commission": 15,
        "ring_tiny": 3,
        "ring_smallish": 4,
        "ring_small": 5,
        "ring_medium": 6,
        "ring_big": 8,
    }
else:
    for key, qty in {
        "commission": 15,
        "ring_tiny": 3,
        "ring_smallish": 4,
        "ring_small": 5,
        "ring_medium": 6,
        "ring_big": 8,
    }.items():
        st.session_state.stock.setdefault(key, qty)
    # Keep Custom Resin Commission well stocked (was low before)
    if st.session_state.stock.get("commission", 0) < 15:
        st.session_state.stock["commission"] = 15

RING_SIZES = [
    {"id": "ring_tiny", "label": "Tiny", "css": "tiny", "price": 6.00},
    {"id": "ring_smallish", "label": "Smallish", "css": "smallish", "price": 7.00},
    {"id": "ring_small", "label": "Small", "css": "small", "price": 8.00},
    {"id": "ring_medium", "label": "Medium", "css": "medium", "price": 9.00},
    {"id": "ring_big", "label": "Big", "css": "big", "price": 10.00},
]

KEYCAP_ONE_SIZE = {
    "id": "keycaps",
    "name": "Resin Keycap",
    "price": 8.00,
    "desc": "One standard size. Add colour/legend details in cart notes on the home page.",
}

# --- Next page ---
if st.session_state.current_page == "next":
    show_html(
        """
        <div class="cp-hero">
          <div class="cp-tag">Next page</div>
          <p class="cp-brand">More items</p>
          <p class="cp-sub">
            Keycaps come in one size. Rings come in five sizes — tiny to big.
          </p>
        </div>
        """
    )

    if st.button("← Back to home", key="back_home"):
        st.session_state.current_page = "home"
        st.rerun()

    show_html('<p class="cp-section">Keycaps — one size</p>')
    keycap_left = st.session_state.stock.get(KEYCAP_ONE_SIZE["id"], 0)
    show_html(
        f"""
        <div class="cp-card">
          <h3 style="margin:0 0 0.35rem 0;">
            {KEYCAP_ONE_SIZE['name']}
            <span class="cp-price">£{KEYCAP_ONE_SIZE['price']:.2f}</span>
          </h3>
          <p style="margin:0; color:#292524; font-weight:500;">
            {KEYCAP_ONE_SIZE['desc']}
          </p>
        </div>
        """
    )
    show_stock(keycap_left)
    if st.button(
        "Add keycap to cart",
        disabled=keycap_left <= 0,
        key="add_keycap_next",
    ):
        st.session_state.cart.append(KEYCAP_ONE_SIZE)
        st.session_state.stock[KEYCAP_ONE_SIZE["id"]] -= 1
        left_now = st.session_state.stock[KEYCAP_ONE_SIZE["id"]]
        st.success(
            f"Added {KEYCAP_ONE_SIZE['name']} to cart — {stock_label(left_now)}"
        )
        st.rerun()

    show_html('<p class="cp-section">Rings — pick a size</p>')
    chips = []
    for s in RING_SIZES:
        left = st.session_state.stock.get(s["id"], 0)
        chips.append(
            f'<div class="size-chip {s["css"]}"><div class="label">{s["label"]}</div>'
            f'<div class="meta">£{s["price"]:.2f} · {stock_label(left)}</div></div>'
        )
    show_html(f'<div class="size-ring">{"".join(chips)}</div>')

    size_labels = [s["label"] for s in RING_SIZES]
    choice = st.radio("Ring size", size_labels, horizontal=True, key="ring_size_choice")
    selected = next(s for s in RING_SIZES if s["label"] == choice)
    ring_left = st.session_state.stock.get(selected["id"], 0)

    show_html(
        f"""
        <div class="cp-card">
          <h3 style="margin:0 0 0.35rem 0;">
            Resin Ring — {selected['label']}
            <span class="cp-price">£{selected['price']:.2f}</span>
          </h3>
          <p style="margin:0; color:#292524; font-weight:500;">
            Resin ring in <strong>{selected['label']}</strong> size.
            Add colour details in cart notes on the home page.
          </p>
        </div>
        """
    )

    show_stock(ring_left, out_message="Out of stock for this size")

    if st.button(
        f"Add {selected['label']} ring to cart",
        disabled=ring_left <= 0,
        key="add_ring",
    ):
        item = {
            "id": selected["id"],
            "name": f"Resin Ring ({selected['label']})",
            "price": selected["price"],
            "desc": f"Resin ring — {selected['label']}",
        }
        st.session_state.cart.append(item)
        st.session_state.stock[selected["id"]] -= 1
        left_now = st.session_state.stock[selected["id"]]
        st.success(f"Added {item['name']} to cart — {stock_label(left_now)}")
        st.rerun()

    st.info("Cart and checkout are on the home page.")
    show_html(
        """
        <div class="cp-footer">
          Copyright 2026 Collect Prints · Next page
        </div>
        """
    )
    st.stop()

# --- Home page ---
show_html(
    """
    <div class="cp-hero">
      <div class="cp-tag">Resin shop</div>
      <p class="cp-brand">Collect Prints</p>
      <p class="cp-sub">
        Custom resin keycaps and made-to-order commissions.
        Built for makers who want detail — not FDM 3D prints For now.
      </p>
    </div>
    """
)

show_html(
    """
    <div class="cp-note">
      <strong>Demo accounts only</strong> — login is stored in session and resets when you leave.
      Real checkout can be added with Stripe later.
    </div>
    """
)

show_html('<p class="cp-section">Account</p>')
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

show_html('<p class="cp-section">Shop</p>')

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

shop_left, shop_right = st.columns([1.35, 1], gap="large")

with shop_left:
    for p in products:
        left = st.session_state.stock.get(p["id"], 0)
        show_html(
            f"""
            <div class="cp-card">
              <h3 style="margin:0 0 0.35rem 0;">{p['name']}
                <span class="cp-price">£{p['price']:.2f}</span>
              </h3>
              <p style="margin:0 0 0.35rem 0; color:#292524; font-weight:500;">{p['desc']}</p>
            </div>
            """
        )
        show_stock(left)
        if st.button(
            f"Add to cart — {p['name']}",
            key=f"add_{p['id']}",
            disabled=left <= 0,
        ):
            st.session_state.cart.append(p)
            st.session_state.stock[p["id"]] -= 1
            left_now = st.session_state.stock[p["id"]]
            st.success(f"Added {p['name']} to cart — {stock_label(left_now)}")
            st.rerun()

with shop_right:
    show_html(
        """
        <div class="cp-glow-panel">
          <h3>Next page</h3>
          <p>
            More items are on the next page.
          </p>
        </div>
        """
    )
    if st.button("Next page →", key="goto_next_page", use_container_width=True):
        st.session_state.current_page = "next"
        st.rerun()

show_html('<p class="cp-section">Your cart</p>')
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

show_html('<p class="cp-section">Contact</p>')
st.write("For real orders and commissions, reach out or add Stripe checkout next.")
st.link_button("Email enquiries", "mailto:hello@collectprints.example")

show_html(
    """
    <div class="cp-footer">
      Copyright 2026 Collect Prints. All rights reserved.<br>
      Resin 3D printed products · Demo shop
    </div>
    """
)
