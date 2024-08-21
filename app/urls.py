from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index_view,about_view, appointment_view, blog_details_view, blog_grid_view, blog_view, cart_grocery_view, cart_pharmacy_view, cart_view, checkout_grocery_view, checkout_pharmacy_view, checkout_view, coming_soon_view, contact_view, dashboard_view, error_view, faq_view, grocery_details_view, grocery_grocery_product_view, grocery_product_view, grocery_view, home_startup_view, pharmacy_details_view, pharmacy_pharmacy_product_view, pharmacy_product_view, pharmacy_view, portfolio_2_view, portfolio_details_view, portfolio_view, product_details_view, product_view, service_view, services_view, store_view, wishlist_grocery_view, wishlist_pharmacy_view, wishlist_view

urlpatterns = [
    path('',index_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('appointment/',appointment_view,name='appointment-page'),
    path('blog-details/',blog_details_view,name='blog-details-page'),
    path('blog-grid/',blog_grid_view,name='blog-grid-page'),
    path('blog/',blog_view,name='blog-page'),
    path('cart-grocery/',cart_grocery_view,name='cart-grocery-page'),
    path('cart-pharmacy/',cart_pharmacy_view,name='cart-pharmacy-page'),
    path('cart/',cart_view,name='cart-page'),
    path('checkout-grocery/',checkout_grocery_view,name='checkout-grocery-page'),
    path('checkout-pharmacy/',checkout_pharmacy_view,name='checkout-pharmacy-page'),
    path('checkout/',checkout_view,name='checkout-page'),
    path('coming-soon/',coming_soon_view,name='coming-soon-page'),
    path('contact/',contact_view,name='contact-page'),
    path('dashboard/',dashboard_view,name='dashboard-page'),
    path('error/',error_view,name='error-page'),
    path('faq/',faq_view,name='faq-page'),
    path('grocery_details/',grocery_details_view,name='grocery_details-page'),
    path('grocery-grocery-product/',grocery_grocery_product_view,name='grocery-grocery-product-page'),
    path('grocery-product/',grocery_product_view,name='grocery-product-page'),
    path('grocery/',grocery_view,name='grocery-page'),
    path('home_startup/',home_startup_view,name='home_startup-page'),
    path('pharmacy-details/',pharmacy_details_view,name='pharmacy-details-page'),
    path('pharmacy-pharmacy/',pharmacy_pharmacy_product_view,name='pharmacy-pharmacy-page'),
    path('pharmacy_product/',pharmacy_product_view,name='pharmacy-product-page'),
    path('pharmacy/',pharmacy_view,name='pharmacy-page'),
    path('portfolio-2/',portfolio_2_view,name='portfolio-2-page'),
    path('portfolio-details/',portfolio_details_view,name='portfolio-details-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('product-details/',product_details_view,name='product-details-page'),
    path('product/',product_view,name='product-page'),
    path('service/',service_view,name='service-page'),
    path('services/',services_view,name='services-page'),
    path('store/',store_view,name='store-page'),
    path('wishlist-grocery/',wishlist_grocery_view,name='wishlist-grocery-page'),
    path('wishlist-pharmacy/',wishlist_pharmacy_view,name='wishlist-pharmacy-page'),
    path('wishlist/',wishlist_view,name='wishlist-page'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)