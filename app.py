import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st

LOGO_PATH = (Path(__file__).resolve().parent / "assets" / "collect_prints_logo.jpg")


def show_html(content: str) -> None:
    """Render HTML without Streamlit treating indented lines as code."""
    st.html(dedent(content).strip())


def logo_data_uri() -> str | None:
    if not LOGO_PATH.is_file():
        return None
    encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def hero_logo_html() -> str:
    uri = logo_data_uri()
    if not uri:
        return ""
    return f'<img class="cp-logo" src="{uri}" alt="Collect Prints logo" />'


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


_page_icon = "🖨️"
if LOGO_PATH.is_file():
    _page_icon = str(LOGO_PATH)

st.set_page_config(
    page_title="Collect Prints",
    page_icon=_page_icon,
    layout="wide",
    initial_sidebar_state="collapsed",
)

show_html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;600&display=swap" rel="stylesheet">
    <style>
      :root {
        --cp-display: "Source Serif 4", Georgia, serif;
        --cp-sans: "Source Sans 3", sans-serif;
        --cp-ink: #2a2724;
        --cp-muted: #6b645c;
        --cp-line: #e3ddd6;
        --cp-paper: #f7f5f2;
        --cp-accent: #5c534c;
      }

      /* Force nice type on Streamlit chrome + shop content */
      html, body, .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"],
      [data-testid="stCaption"], [data-testid="stAlert"],
      .stTextInput input, .stTextArea textarea, [data-baseweb="tab"],
      [data-testid="stRadio"] label, [data-testid="stCheckbox"] label,
      div[data-testid="stButton"] button, .stLinkButton a {
        font-family: var(--cp-sans) !important;
      }

      html, body, .stApp {
        font-size: 16px;
        line-height: 1.55;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
        color: var(--cp-ink);
      }

      .cp-brand, .cp-section {
        font-family: var(--cp-display) !important;
        font-optical-sizing: auto;
      }

      .stApp {
        background: var(--cp-paper);
      }
      #MainMenu, footer, header { visibility: hidden; }
      .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1280px;
      }
      section.main > div { max-width: 1280px; }

      .cp-hero {
        background: #fff;
        border: 1px solid var(--cp-line);
        border-radius: 8px;
        padding: 1.5rem 1.4rem 1.35rem;
        margin-bottom: 1.4rem;
      }
      .cp-hero-top {
        display: flex;
        align-items: center;
        gap: 0.85rem;
        margin-bottom: 0.55rem;
      }
      .cp-logo {
        width: 48px;
        height: 48px;
        border-radius: 6px;
        object-fit: cover;
        border: 1px solid var(--cp-line);
        background: #fff;
        flex-shrink: 0;
      }
      .cp-brand {
        font-size: clamp(1.7rem, 3vw, 2.15rem);
        font-weight: 600;
        margin: 0 0 0.35rem 0;
        line-height: 1.15;
        color: var(--cp-ink);
        letter-spacing: -0.02em;
      }
      .cp-tag {
        display: inline-block;
        font-family: var(--cp-sans) !important;
        font-size: 0.78rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: var(--cp-muted);
        margin: 0 0 0.35rem;
      }
      .cp-sub {
        margin: 0;
        font-family: var(--cp-sans) !important;
        font-size: 1rem;
        max-width: 36rem;
        line-height: 1.6;
        color: var(--cp-muted);
        font-weight: 400;
      }
      .cp-note {
        background: #fff;
        border: 1px solid var(--cp-line);
        color: var(--cp-ink);
        border-radius: 8px;
        padding: 0.85rem 1rem;
        margin: 0.8rem 0 1.2rem;
        font-family: var(--cp-sans) !important;
        font-size: 0.98rem;
        font-weight: 400;
        line-height: 1.55;
      }
      .cp-note strong {
        color: var(--cp-ink);
        font-weight: 600;
      }
      .cp-card {
        background: #fff;
        border: 1px solid var(--cp-line);
        border-radius: 8px;
        padding: 1.1rem 1.1rem 0.45rem;
        margin-bottom: 0.85rem;
      }
      .cp-card h3 {
        font-family: var(--cp-display) !important;
        color: var(--cp-ink);
        margin: 0 0 0.35rem 0;
        font-size: 1.2rem;
        font-weight: 600;
        letter-spacing: -0.015em;
        line-height: 1.25;
      }
      .cp-card p {
        font-family: var(--cp-sans) !important;
        color: var(--cp-muted);
        font-weight: 400;
        margin: 0 0 0.4rem 0;
        font-size: 0.98rem;
        line-height: 1.55;
      }
      .cp-price {
        font-family: var(--cp-sans) !important;
        color: var(--cp-ink);
        font-weight: 600;
        font-size: 1.05rem;
      }
      .cp-section {
        font-size: 1.35rem;
        font-weight: 600;
        margin: 1.6rem 0 0.75rem;
        color: var(--cp-ink);
        letter-spacing: -0.02em;
        line-height: 1.2;
      }
      .cp-footer {
        text-align: center;
        color: var(--cp-muted);
        font-family: var(--cp-sans) !important;
        font-size: 0.92rem;
        margin-top: 2.4rem;
        padding-top: 1.1rem;
        border-top: 1px solid var(--cp-line);
        font-weight: 400;
        line-height: 1.6;
      }

      div[data-testid="stButton"] button,
      .stLinkButton a {
        border-radius: 6px !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        padding: 0.5rem 0.95rem !important;
        background: #fff !important;
        color: var(--cp-ink) !important;
        border: 1px solid #cfc8c0 !important;
        box-shadow: none !important;
      }
      div[data-testid="stButton"] button:hover,
      .stLinkButton a:hover {
        background: #f3f0ec !important;
        border-color: var(--cp-accent) !important;
        color: var(--cp-ink) !important;
      }
      div[data-testid="stButton"] button:disabled {
        background: #f3f0ec !important;
        border-color: var(--cp-line) !important;
        color: #a39c95 !important;
        box-shadow: none !important;
      }
      [data-testid="stCaption"] {
        font-size: 0.98rem !important;
        font-weight: 500 !important;
        letter-spacing: -0.01em !important;
      }
      [data-testid="stAlert"] p,
      [data-testid="stMarkdownContainer"] p {
        font-family: var(--cp-sans) !important;
        letter-spacing: -0.01em;
      }
      [data-baseweb="tab"] {
        font-weight: 600 !important;
        letter-spacing: -0.015em !important;
      }
      label, [data-testid="stWidgetLabel"] p {
        font-weight: 600 !important;
        letter-spacing: -0.015em !important;
      }

      .cp-glow-panel {
        background: #fff;
        border-radius: 8px;
        padding: 1.2rem 1.15rem 1.05rem;
        color: var(--cp-ink);
        min-height: 220px;
        border: 1px solid var(--cp-line);
      }
      .cp-glow-panel h3 {
        font-family: var(--cp-display) !important;
        font-size: 1.25rem;
        font-weight: 600;
        margin: 0 0 0.45rem 0;
        color: var(--cp-ink);
        letter-spacing: -0.015em;
        line-height: 1.2;
      }
      .cp-glow-panel p {
        font-family: var(--cp-sans) !important;
        margin: 0 0 0.75rem 0;
        font-weight: 400;
        line-height: 1.55;
        color: var(--cp-muted);
        font-size: 0.98rem;
      }
      .size-ring {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        align-items: flex-end;
        gap: 0.7rem;
        margin: 0.9rem 0 1.2rem;
      }
      .size-chip {
        text-align: center;
        background: #fff;
        border: 1px solid var(--cp-line);
        border-radius: 8px;
        color: var(--cp-ink);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      .size-chip.small { width: 5.2rem; height: 5.2rem; }
      .size-chip.medium { width: 6.2rem; height: 6.2rem; }
      .size-chip.big { width: 7.2rem; height: 7.2rem; }
      .size-chip .label {
        font-family: var(--cp-sans) !important;
        font-weight: 600;
        font-size: 0.95em;
      }
      .size-chip .meta {
        font-family: var(--cp-sans) !important;
        font-size: 0.72em;
        font-weight: 400;
        color: var(--cp-muted);
        margin-top: 0.2rem;
      }
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
        "spacebar_keycap": 20,
        "ring_small": 10,
        "ring_medium": 10,
        "ring_big": 10,
    }
else:
    for key, qty in {
        "commission": 15,
        "spacebar_keycap": 20,
        "ring_small": 10,
        "ring_medium": 10,
        "ring_big": 10,
    }.items():
        st.session_state.stock.setdefault(key, qty)

RING_SIZES = [
    {"id": "ring_small", "label": "Small", "css": "small", "price": 8.00},
    {"id": "ring_medium", "label": "Medium", "css": "medium", "price": 9.00},
    {"id": "ring_big", "label": "Big", "css": "big", "price": 10.00},
]

SPACEBAR_KEYCAP = {
    "id": "spacebar_keycap",
    "name": "Spacebar Keycap",
    "price": 4.00,
    "desc": "One spacebar keycap. Add colour/legend details in cart notes on the home page.",
}

# --- Next page ---
if st.session_state.current_page == "next":
    show_html(
        f"""
        <div class="cp-hero">
          <div class="cp-hero-top">
            {hero_logo_html()}
            <div class="cp-tag">Next page</div>
          </div>
          <p class="cp-brand">More items</p>
          <p class="cp-sub">
            Spacebar keycaps — one each at £4. Rings in small, medium, and big.
          </p>
        </div>
        """
    )

    if st.button("← Back to home", key="back_home"):
        st.session_state.current_page = "home"
        st.rerun()

    show_html('<p class="cp-section">Spacebar keycaps</p>')
    spacebar_left = st.session_state.stock.get(SPACEBAR_KEYCAP["id"], 0)
    show_html(
        f"""
        <div class="cp-card">
          <h3 style="margin:0 0 0.35rem 0;">
            {SPACEBAR_KEYCAP['name']}
            <span class="cp-price">£{SPACEBAR_KEYCAP['price']:.2f}</span>
          </h3>
          <p style="margin:0; color:#292524; font-weight:500;">
            {SPACEBAR_KEYCAP['desc']}
          </p>
        </div>
        """
    )
    show_stock(spacebar_left)
    if st.button(
        "Add spacebar keycap to cart",
        disabled=spacebar_left <= 0,
        key="add_spacebar_next",
    ):
        st.session_state.cart.append(SPACEBAR_KEYCAP)
        st.session_state.stock[SPACEBAR_KEYCAP["id"]] -= 1
        left_now = st.session_state.stock[SPACEBAR_KEYCAP["id"]]
        st.success(
            f"Added {SPACEBAR_KEYCAP['name']} to cart — {stock_label(left_now)}"
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
    f"""
    <div class="cp-hero">
      <div class="cp-hero-top">
        {hero_logo_html()}
        <div class="cp-tag">Resin shop</div>
      </div>
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
