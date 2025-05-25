import streamlit as st
import base64
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="JANET - Luxury Fashion",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match the original design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Montserrat:wght@200;300;400;500;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');
    
    :root {
        --primary-black: #000000;
        --soft-white: #fefefe;
        --warm-gray: #f8f8f6;
        --medium-gray: #8a8a8a;
        --light-gray: #e8e8e6;
        --accent-gold: #d4af37;
    }
    
    .stApp {
        background-color: #fefefe;
    }
    
    .main-header {
        font-family: 'Cormorant Garamond', serif;
        font-size: 4rem;
        font-weight: 300;
        text-align: center;
        color: #000000;
        margin-bottom: 2rem;
        letter-spacing: -1px;
    }
    
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3rem;
        font-weight: 400;
        text-align: center;
        color: #000000;
        margin-bottom: 1rem;
        letter-spacing: -0.5px;
    }
    
    .section-subtitle {
        font-family: 'Crimson Text', serif;
        font-style: italic;
        font-size: 1.2rem;
        text-align: center;
        color: #8a8a8a;
        margin-bottom: 3rem;
    }
    
    .hero-section {
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.2)),
                    url('https://images.unsplash.com/photo-1558769132-cb1aea458c5e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1974&q=80');
        background-size: cover;
        background-position: center;
        padding: 8rem 2rem;
        text-align: center;
        color: white;
        border-radius: 10px;
        margin-bottom: 4rem;
    }
    
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 5rem;
        font-weight: 300;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-text {
        font-family: 'Crimson Text', serif;
        font-style: italic;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .collection-card {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 2rem;
    }
    
    .collection-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    
    .product-card {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .product-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem;
        font-weight: 400;
        margin: 1rem 0 0.5rem 0;
        color: #000000;
    }
    
    .product-price {
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #8a8a8a;
        margin-bottom: 1rem;
    }
    
    .collection-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        font-weight: 400;
        margin: 1rem 0 0.5rem 0;
        text-align: center;
        color: #000000;
    }
    
    .collection-category {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #8a8a8a;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .journal-card {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .journal-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 400;
        margin: 1rem 0;
        color: #000000;
    }
    
    .journal-text {
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        line-height: 1.7;
        color: #8a8a8a;
        margin-bottom: 1rem;
    }
    
    .journal-date {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #8a8a8a;
    }
    
    .cta-button {
        display: inline-block;
        padding: 15px 40px;
        background: transparent;
        border: 2px solid #000000;
        color: #000000;
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
        font-weight: 400;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        font-size: 0.9rem;
        border-radius: 0;
        transition: all 0.3s ease;
    }
    
    .cta-button:hover {
        background: #000000;
        color: white;
    }
    
    .newsletter-section {
        background: #f8f8f6;
        padding: 3rem 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 4rem 0;
    }
    
    .footer-section {
        background: #000000;
        color: white;
        padding: 3rem 2rem 2rem 2rem;
        margin-top: 4rem;
        border-radius: 10px;
    }
    
    .footer-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        color: white;
    }
    
    .footer-link {
        color: #8a8a8a;
        text-decoration: none;
        font-size: 0.9rem;
        line-height: 2;
    }
    
    .footer-link:hover {
        color: white;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom button styling */
    .stButton > button {
        background: transparent;
        border: 2px solid #000000;
        color: #000000;
        font-family: 'Montserrat', sans-serif;
        font-weight: 400;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        padding: 15px 40px;
        border-radius: 0;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: #000000;
        color: white;
        border-color: #000000;
    }
    
    /* Navigation styling */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid #e8e8e6;
    }
    
    .logo {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 600;
        letter-spacing: 2px;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

def create_navigation():
    """Create the navigation bar"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.markdown('<div class="logo">JANET</div>', unsafe_allow_html=True)

    with col2:
        nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
        with nav_col1:
            if st.button("SHOP"):
                st.session_state.current_page = "shop"
        with nav_col2:
            if st.button("COLLECTIONS"):
                st.session_state.current_page = "collections"
        with nav_col3:
            if st.button("ABOUT"):
                st.session_state.current_page = "about"
        with nav_col4:
            if st.button("JOURNAL"):
                st.session_state.current_page = "journal"
        with nav_col5:
            if st.button("CONTACT"):
                st.session_state.current_page = "contact"

    with col3:
        icon_col1, icon_col2, icon_col3 = st.columns(3)
        with icon_col1:
            st.button("🔍")
        with icon_col2:
            st.button("👤")
        with icon_col3:
            st.button("🛍️")

def create_hero_section():
    """Create the hero section"""
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Timeless Elegance</h1>
        <p class="hero-text">Crafted with precision, designed for the discerning individual who values heritage and contemporary sophistication in every thread.</p>
    </div>
    """, unsafe_allow_html=True)

def create_collections_section():
    """Create the collections section"""
    st.markdown('<h2 class="section-title">Curated Collections</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Each piece tells a story of craftsmanship and timeless design</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    collections = [
        {
            "title": "Autumn Essence",
            "category": "Ready-to-Wear",
            "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?ixlib=rb-4.0.3&auto=format&fit=crop&w=720&q=80"
        },
        {
            "title": "Evening Couture",
            "category": "Formal Wear",
            "image": "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?ixlib=rb-4.0.3&auto=format&fit=crop&w=720&q=80"
        },
        {
            "title": "Heritage Accessories",
            "category": "Leather Goods",
            "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?ixlib=rb-4.0.3&auto=format&fit=crop&w=720&q=80"
        }
    ]

    for i, collection in enumerate(collections):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div class="collection-card">
                <img src="{collection['image']}" style="width: 100%; height: 300px; object-fit: cover;">
                <div style="padding: 1.5rem;">
                    <h3 class="collection-title">{collection['title']}</h3>
                    <p class="collection-category">{collection['category']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def create_featured_products():
    """Create the featured products section"""
    st.markdown('<div style="background: #f8f8f6; padding: 4rem 2rem; border-radius: 10px; margin: 4rem 0;">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Featured Pieces</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Handpicked selections from our latest collection</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    products = [
        {
            "title": "Silk Meridian Dress",
            "price": "$1,250",
            "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?ixlib=rb-4.0.3&auto=format&fit=crop&w=480&q=80"
        },
        {
            "title": "Cashmere Noir Coat",
            "price": "$2,850",
            "image": "https://images.unsplash.com/photo-1544022613-e87ca75a784a?ixlib=rb-4.0.3&auto=format&fit=crop&w=480&q=80"
        },
        {
            "title": "Heritage Leather Tote",
            "price": "$890",
            "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?ixlib=rb-4.0.3&auto=format&fit=crop&w=480&q=80"
        },
        {
            "title": "Midnight Velvet Blazer",
            "price": "$1,650",
            "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?ixlib=rb-4.0.3&auto=format&fit=crop&w=480&q=80"
        }
    ]

    for i, product in enumerate(products):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
            <div class="product-card">
                <img src="{product['image']}" style="width: 100%; height: 250px; object-fit: cover;">
                <div style="padding: 1.5rem;">
                    <h4 class="product-title">{product['title']}</h4>
                    <p class="product-price">{product['price']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

def create_journal_section():
    """Create the journal section"""
    st.markdown('<h2 class="section-title">The Journal</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Stories of craftsmanship, heritage, and contemporary culture</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    articles = [
        {
            "title": "The Art of Slow Fashion",
            "content": "Exploring the meticulous process behind each handcrafted piece, from initial sketch to final stitch. Our commitment to sustainable luxury continues to shape every collection.",
            "date": "March 15, 2024",
            "image": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        },
        {
            "title": "Heritage Meets Innovation",
            "content": "A behind-the-scenes look at our atelier where traditional techniques merge with contemporary design philosophy to create tomorrow's classics.",
            "date": "February 28, 2024",
            "image": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        }
    ]

    for i, article in enumerate(articles):
        with [col1, col2][i]:
            st.markdown(f"""
            <div class="journal-card">
                <img src="{article['image']}" style="width: 100%; height: 250px; object-fit: cover;">
                <div style="padding: 2rem;">
                    <h3 class="journal-title">{article['title']}</h3>
                    <p class="journal-text">{article['content']}</p>
                    <p class="journal-date">{article['date']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def create_newsletter_section():
    """Create the newsletter signup section"""
    st.markdown("""
    <div class="newsletter-section">
        <h3 class="section-title" style="font-size: 2rem; margin-bottom: 1rem;">Stay Connected</h3>
        <p class="section-subtitle">Subscribe to receive exclusive updates about new collections, special events, and editorial content.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("newsletter"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            email = st.text_input("", placeholder="Enter your email address")
            submitted = st.form_submit_button("Subscribe")

            if submitted and email:
                st.success("Thank you for subscribing! Welcome to the JANET community.")

def create_footer():
    """Create the footer section"""
    st.markdown('<div class="footer-section">', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<h4 class="footer-title">Customer Care</h4>', unsafe_allow_html=True)
        st.markdown("""
        <div>
            <a href="#" class="footer-link">Size Guide</a><br>
            <a href="#" class="footer-link">Shipping Information</a><br>
            <a href="#" class="footer-link">Returns & Exchanges</a><br>
            <a href="#" class="footer-link">Care Instructions</a><br>
            <a href="#" class="footer-link">Contact Us</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<h4 class="footer-title">About Janet</h4>', unsafe_allow_html=True)
        st.markdown("""
        <div>
            <a href="#" class="footer-link">Our Story</a><br>
            <a href="#" class="footer-link">Craftsmanship</a><br>
            <a href="#" class="footer-link">Sustainability</a><br>
            <a href="#" class="footer-link">Careers</a><br>
            <a href="#" class="footer-link">Press</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown('<h4 class="footer-title">Legal</h4>', unsafe_allow_html=True)
        st.markdown("""
        <div>
            <a href="#" class="footer-link">Privacy Policy</a><br>
            <a href="#" class="footer-link">Terms of Service</a><br>
            <a href="#" class="footer-link">Cookie Policy</a><br>
            <a href="#" class="footer-link">Accessibility</a>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown('<h4 class="footer-title">Follow Us</h4>', unsafe_allow_html=True)
        st.markdown("""
        <div>
            <a href="#" class="footer-link">Facebook</a><br>
            <a href="#" class="footer-link">Instagram</a><br>
            <a href="#" class="footer-link">Twitter</a><br>
            <a href="#" class="footer-link">Pinterest</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr style="margin: 2rem 0; border-color: #333;">', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #8a8a8a; font-size: 0.8rem;">© 2024 Janet. All rights reserved. | Crafted with precision and care.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application function"""
    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    # Load custom CSS
    load_css()

    # Create navigation
    create_navigation()

    # Main content based on current page
    if st.session_state.current_page == 'home' or st.session_state.current_page == 'collections':
        create_hero_section()
        create_collections_section()
        create_featured_products()
        create_journal_section()
        create_newsletter_section()
        create_footer()

    elif st.session_state.current_page == 'shop':
        st.markdown('<h1 class="main-header">Shop</h1>', unsafe_allow_html=True)
        create_featured_products()
        st.info("Full shopping functionality would be implemented here with product catalog, filters, and cart system.")
        create_footer()

    elif st.session_state.current_page == 'about':
        st.markdown('<h1 class="main-header">About JANET</h1>', unsafe_allow_html=True)
        st.markdown("""
        <div style="max-width: 800px; margin: 0 auto; padding: 2rem;">
            <p style="font-size: 1.2rem; line-height: 1.8; color: #8a8a8a; text-align: center; font-family: 'Crimson Text', serif; font-style: italic;">
            Founded on the principles of timeless elegance and exceptional craftsmanship, JANET represents the pinnacle of luxury fashion. 
            Each piece in our collection is meticulously designed and crafted by master artisans who understand that true luxury lies in the details.
            </p>
            <br>
            <p style="font-size: 1.1rem; line-height: 1.7; color: #666; text-align: center;">
            Our commitment to sustainable luxury means that every garment is created to last, using only the finest materials sourced responsibly 
            from around the world. We believe in slow fashion - creating pieces that transcend trends and become cherished wardrobe staples.
            </p>
        </div>
        """, unsafe_allow_html=True)
        create_footer()

    elif st.session_state.current_page == 'journal':
        st.markdown('<h1 class="main-header">The Journal</h1>', unsafe_allow_html=True)
        create_journal_section()
        create_footer()

    elif st.session_state.current_page == 'contact':
        st.markdown('<h1 class="main-header">Contact Us</h1>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<h3 class="section-title" style="font-size: 1.5rem;">Get In Touch</h3>', unsafe_allow_html=True)
            with st.form("contact_form"):
                name = st.text_input("Full Name")
                email = st.text_input("Email Address")
                subject = st.selectbox("Subject", ["General Inquiry", "Custom Orders", "Press Inquiry", "Partnership"])
                message = st.text_area("Message", height=150)

                if st.form_submit_button("Send Message"):
                    if name and email and message:
                        st.success("Thank you for your message. We'll get back to you within 24 hours.")
                    else:
                        st.error("Please fill in all required fields.")

        with col2:
            st.markdown('<h3 class="section-title" style="font-size: 1.5rem;">Visit Our Atelier</h3>', unsafe_allow_html=True)
            st.markdown("""
            <div style="padding: 1rem;">
                <p><strong>JANET Flagship Store</strong></p>
                <p>123 Fashion Avenue<br>
                New York, NY 10001</p>
                <br>
                <p><strong>Hours:</strong><br>
                Monday - Saturday: 10AM - 7PM<br>
                Sunday: 12PM - 6PM</p>
                <br>
                <p><strong>Phone:</strong> +1 (555) 123-4567<br>
                <strong>Email:</strong> info@janet.luxury</p>
            </div>
            """, unsafe_allow_html=True)

        create_footer()

if __name__ == "__main__":
    main()