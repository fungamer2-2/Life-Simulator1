import os as _os

COUNTRIES = [
    _("Afghanistan"),
    _("Albania"),
    _("Algeria"),
    _("Andorra"),
    _("Angola"),
    _("Antigua and Barbuda"),
    _("Argentina"),
    _("Armenia"),
    _("Australia"),
    _("Austria"),
    _("Azerbaijan"),
    _("The Bahamas"),
    _("Bahrain"),
    _("Bangladesh"),
    _("Barbados"),
    _("Belarus"),
    _("Belgium"),
    _("Belize"),
    _("Benin"),
    _("Bhutan"),
    _("Bolivia"),
    _("Bosnia and Herzegovina"),
    _("Botswana"),
    _("Brazil"),
    _("Brunei"),
    _("Bulgaria"),
    _("Burkina Faso"),
    _("Burundi"),
    _("Cabo Verde"),
    _("Cambodia"),
    _("Cameroon"),
    _("Canada"),
    _("Central African Republic"),
    _("Chad"),
    _("Chile"),
    _("China"),
    _("Colombia"),
    _("Comoros"),
    _("Congo, Democratic Republic of the"),
    _("Congo, Republic of the"),
    _("Costa Rica"),
    _("Côte d’Ivoire"),
    _("Croatia"),
    _("Cuba"),
    _("Cyprus"),
    _("Czech Republic"),
    _("Denmark"),
    _("Djibouti"),
    _("Dominica"),
    _("Dominican Republic"),
    _("East Timor (Timor-Leste)"),
    _("Ecuador"),
    _("Egypt"),
    _("El Salvador"),
    _("Equatorial Guinea"),
    _("Eritrea"),
    _("Estonia"),
    _("Eswatini"),
    _("Ethiopia"),
    _("Fiji"),
    _("Finland"),
    _("France"),
    _("Gabon"),
    _("The Gambia"),
    _("Georgia"),
    _("Germany"),
    _("Ghana"),
    _("Greece"),
    _("Grenada"),
    _("Guatemala"),
    _("Guinea"),
    _("Guinea-Bissau"),
    _("Guyana"),
    _("Haiti"),
    _("Honduras"),
    _("Hungary"),
    _("Iceland"),
    _("India"),
    _("Indonesia"),
    _("Iran"),
    _("Iraq"),
    _("Ireland"),
    _("Israel"),
    _("Italy"),
    _("Jamaica"),
    _("Japan"),
    _("Jordan"),
    _("Kazakhstan"),
    _("Kenya"),
    _("Kiribati"),
    _("Korea, North"),
    _("Korea, South"),
    _("Kosovo"),
    _("Kuwait"),
    _("Kyrgyzstan"),
    _("Laos"),
    _("Latvia"),
    _("Lebanon"),
    _("Lesotho"),
    _("Liberia"),
    _("Libya"),
    _("Liechtenstein"),
    _("Lithuania"),
    _("Luxembourg"),
    _("Madagascar"),
    _("Malawi"),
    _("Malaysia"),
    _("Maldives"),
    _("Mali"),
    _("Malta"),
    _("Marshall Islands"),
    _("Mauritania"),
    _("Mauritius"),
    _("Mexico"),
    _("Micronesia, Federated States of"),
    _("Moldova"),
    _("Monaco"),
    _("Mongolia"),
    _("Montenegro"),
    _("Morocco"),
    _("Mozambique"),
    _("Myanmar (Burma)"),
    _("Namibia"),
    _("Nauru"),
    _("Nepal"),
    _("Netherlands"),
    _("New Zealand"),
    _("Nicaragua"),
    _("Niger"),
    _("Nigeria"),
    _("North Macedonia"),
    _("Norway"),
    _("Oman"),
    _("Pakistan"),
    _("Palau"),
    _("Panama"),
    _("Papua New Guinea"),
    _("Paraguay"),
    _("Peru"),
    _("Philippines"),
    _("Poland"),
    _("Portugal"),
    _("Qatar"),
    _("Romania"),
    _("Russia"),
    _("Rwanda"),
    _("Saint Kitts and Nevis"),
    _("Saint Lucia"),
    _("Saint Vincent and the Grenadines"),
    _("Samoa"),
    _("San Marino"),
    _("Sao Tome and Principe"),
    _("Saudi Arabia"),
    _("Senegal"),
    _("Serbia"),
    _("Seychelles"),
    _("Sierra Leone"),
    _("Singapore"),
    _("Slovakia"),
    _("Slovenia"),
    _("Solomon Islands"),
    _("Somalia"),
    _("South Africa"),
    _("Spain"),
    _("Sri Lanka"),
    _("Sudan"),
    _("Sudan, South"),
    _("Suriname"),
    _("Sweden"),
    _("Switzerland"),
    _("Syria"),
    _("Taiwan"),
    _("Tajikistan"),
    _("Tanzania"),
    _("Thailand"),
    _("Togo"),
    _("Tonga"),
    _("Trinidad and Tobago"),
    _("Tunisia"),
    _("Turkey"),
    _("Turkmenistan"),
    _("Tuvalu"),
    _("Uganda"),
    _("Ukraine"),
    _("United Arab Emirates"),
    _("United Kingdom"),
    _("United States"),
    _("Uruguay"),
    _("Uzbekistan"),
    _("Vanuatu"),
    _("Vatican City"),
    _("Venezuela"),
    _("Vietnam"),
    _("Yemen"),
    _("Zambia"),
    _("Zimbabwe"),
]

# Todo: Differences in Cultural & Legal systems

# - States (or similar) -
# - Major Cities -
# - Age related - Nb. this will probably need some work.
# Alcohol 
# Alcohol_Beer
# Consent
# Driving
# Marriage
# Matriculation
# Military Service (Conscription)
# Military Service (Choice)
# Schooling (Minimum) - When you can drop-out/leave
# Schooling (Maximum) - When you finish final year
# Smoking / Vaping
# Voting


# - Afghanistan -
# - Albania -
# - Algeria -
# - Andorra -
# - Angola -
# - Antigua and Barbuda -
# - Argentina -
# - Armenia -
# - Australia -
# - Austria -
# - Azerbaijan -
# - The Bahamas -
# - Bahrain -
# - Bangladesh -
# - Barbados -
# - Belarus -
# - Belgium -
# - Belize -
# - Benin -
# - Bhutan -
# - Bolivia -
# - Bosnia and Herzegovina -
# - Botswana -
# - Brazil -
# - Brunei -
# - Bulgaria -
# - Burkina Faso -
# - Burundi -
# - Cabo Verde -
# - Cambodia -
# - Cameroon -
# - Canada -
# - Central African Republic -
# - Chad -
# - Chile -
# - China -
# - Colombia -
# - Comoros -
# - Congo, Democratic Republic of the -
# - Congo, Republic of the -
# - Costa Rica -
# - Côte d’Ivoire -
# - Croatia -
# - Cuba -
# - Cyprus -
# - Czech Republic -
# - Denmark -
# - Djibouti -
# - Dominica -
# - Dominican Republic -
# - East Timor (Timor-Leste) -
# - Ecuador -
# - Egypt -
# - El Salvador -
# - Equatorial Guinea -
# - Eritrea -
# - Estonia -
# - Eswatini -
# - Ethiopia -
# - Fiji -
# - Finland -
# - France -
# - Gabon -
# - The Gambia -
# - Georgia -
# - Germany -
# - Ghana -
# - Greece -
# - Grenada -
# - Guatemala -
# - Guinea -
# - Guinea-Bissau -
# - Guyana -
# - Haiti -
# - Honduras -
# - Hungary -
# - Iceland -
# - India -
# - Indonesia -
# - Iran -
# - Iraq -
# - Ireland -
# - Israel -
# - Italy -
# - Jamaica -
# - Japan -
# - Jordan -
# - Kazakhstan -
# - Kenya -
# - Kiribati -
# - Korea, North -
# - Korea, South -
# - Kosovo -
# - Kuwait -
# - Kyrgyzstan -
# - Laos -
# - Latvia -
# - Lebanon -
# - Lesotho -
# - Liberia -
# - Libya -
# - Liechtenstein -
# - Lithuania -
# - Luxembourg -
# - Madagascar -
# - Malawi -
# - Malaysia -
# - Maldives -
# - Mali -
# - Malta -
# - Marshall Islands -
# - Mauritania -
# - Mauritius -
# - Mexico -
# - Micronesia, Federated States of -
# - Moldova -
# - Monaco -
# - Mongolia -
# - Montenegro -
# - Morocco -
# - Mozambique -
# - Myanmar (Burma) -
# - Namibia -
# - Nauru -
# - Nepal -
# - Netherlands -
# - New Zealand -
# - Nicaragua -
# - Niger -
# - Nigeria -
# - North Macedonia -
# - Norway -
# - Oman -
# - Pakistan -
# - Palau -
# - Panama -
# - Papua New Guinea -
# - Paraguay -
# - Peru -
# - Philippines -
# - Poland -
# - Portugal -
# - Qatar -
# - Romania -
# - Russia -
# - Rwanda -
# - Saint Kitts and Nevis -
# - Saint Lucia -
# - Saint Vincent and the Grenadines -
# - Samoa -
# - San Marino -
# - Sao Tome and Principe -
# - Saudi Arabia -
# - Senegal -
# - Serbia -
# - Seychelles -
# - Sierra Leone -
# - Singapore -
# - Slovakia -
# - Slovenia -
# - Solomon Islands -
# - Somalia -
# - South Africa -
# - Spain -
# - Sri Lanka -
# - Sudan -
# - Sudan, South -
# - Suriname -
# - Sweden -
# - Switzerland -
# - Syria -
# - Taiwan -
# - Tajikistan -
# - Tanzania -
# - Thailand -
# - Togo -
# - Tonga -
# - Trinidad and Tobago -
# - Tunisia -
# - Turkey -
# - Turkmenistan -
# - Tuvalu -
# - Uganda -
# - Ukraine -
# - United Arab Emirates -
# - United Kingdom -
# - United States -
# - Uruguay -
# - Uzbekistan -
# - Vanuatu -
# - Vatican City -
# - Venezuela -
# - Vietnam -
# - Yemen -
# - Zambia -
# - Zimbabwe -
