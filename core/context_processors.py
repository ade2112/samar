def company_info(request):
    return {
        'company_name': 'Samar Craft',
        'company_email': 'samarcrafts.marketing@gmail.com',
        'company_phone': '+60 12-7678651',
        'company_phone_clean': '+60127678651',
        'company_address': 'Lot 33070, No Tiang 1/12, Taman Mewah, Jalan Kemboja, 31000 Batu Gajah, Perak.',
        'social_tiktok': 'https://www.tiktok.com/@samar.crafts001?_r=1&_t=ZS-93ij55UWg1i',
        'social_facebook': '#', # Placeholder as requested
        'social_instagram': '#', # Placeholder as requested
        'whatsapp_number': '60127678651', # Clean number for API
    }
