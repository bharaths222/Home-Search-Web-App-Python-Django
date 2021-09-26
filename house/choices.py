category_choices = (
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent'),
)

new_construction_choices = (
    ('yes', 'yes'),
    ('no','no'),
)

gated_community_choices = (
    ('yes', 'yes'),
    ('no', 'no'),
)

ready_to_move_choices = (
    ('yes', 'yes'),
    ('no', 'no'),
)

furnished_choices = (
    ('yes', 'yes'),
    ('no', 'no'),
)

house_type_choices = (
    (None,'Select House Type'),  
    ('Apartment', 'Apartment'),
    ('House', 'House'),
)

house_type_choices_view = (
    ('All Houses','All Houses'),  
    ('Apartment', 'Apartment'),
    ('House', 'House'),
)

facing_choices = (
    (None,'Select Facing'),  
    ('East', 'East'),
    ('West', 'West'),
    ('North', 'North'),
    ('South', 'South'),
    ('North-East', 'North-East'),
    ('North-West', 'North-West'),
    ('South-East', 'South-East'),
    ('South-West', 'South-West'),
)

# For Model
bedroom_choices = (
  (None,'Select Beds'),  
  ('1','1'),
  ('2','2'),
  ('3','3'),
  ('4','4'),
  ('5','5'),
  ('6','6'),
  ('7','7'),
  ('8+','8+'),
  )

# For View
bedroom_choices_2 = (
  ('All', 'All'),
  ('1','1'),
  ('2','2'),
  ('3','3'),
  ('4','4'),
  ('5','5'),
  ('6+','6+'),
  )

# For Model
bathroom_choices = (
  (None,'Select Baths'),  
  ('1','1'),
  ('1.5','1.5'),
  ('2','2'),
  ('2.5','2.5'),
  ('3','3'),
  ('3.5','3.5'),
  ('4','4'),
  ('4.5','4.5'),
  ('5','5'),
  ('5.5','5.5'),
  ('6','6'),
  ('6.5','6.5')
  )

# For View
bathroom_choices_2 = (
  ('1+','1+'),
  ('2+','2+'),
  ('3+','3+'),
  ('4+','4+'),
  ('5+','5+'),
  ('6+','6+'),
  )

min_price_choices = (
#   ('','Min'),
  ('0','0'),
  ('4000000','4000000'),
  ('6000000','6000000'),
  ('8000000','8000000'),
  ('10000000','10000000'),
  ('12000000','12000000'),
  ('14000000','14000000'),
  ('16000000','16000000'),
  ('18000000','18000000'),
  ('20000000','20000000'),
  ('22000000','22000000'),
)
max_price_choices = (
#   ('','Max'),
  ('4000000','4000000'),
  ('6000000','6000000'),
  ('8000000','8000000'),
  ('10000000','10000000'),
  ('12000000','12000000'),
  ('14000000','14000000'),
  ('16000000','16000000'),
  ('18000000','18000000'),
  ('20000000','20000000'),
  ('22000000','22000000'),
  ('25000000','25000000'),
)

# min_price_choices_view = (
#   (None,'No Min'),
#   ('0','0'),
#   ('100000','100000'),
#   ('500000','500000'),
#   ('1000000','1000000'),
#   ('1500000','1500000'),
#   ('2000000','2000000'),
#   ('2500000','2500000'),
#   ('3000000','3000000'),
#   ('3500000','3500000'),
#   ('4000000','4000000'),
#   ('4500000','4500000'),
# )

# max_price_choices_view = (
#   (None,'No Max'),
#   ('100000','100000'),
#   ('500000','500000'),
#   ('1000000','1000000'),
#   ('1500000','1500000'),
#   ('2000000','2000000'),
#   ('2500000','2500000'),
#   ('3000000','3000000'),
#   ('3500000','3500000'),
#   ('4000000','4000000'),
#   ('4500000','4500000'),
#   ('5000000','5000000'),
# )

### Rental CHOICES ###
rental_type_choices = (
    (None,'Select Rental Type'), 
    ('Private/Shared Room', 'Private/Shared Room'),
    ('Apartment', 'Apartment'),
    ('House', 'House'),
)

rental_type_choices_view = (
    ('All Houses','All Houses'),
    ('Private/Shared Room', 'Private/Shared Room'),
    ('Apartment', 'Apartment'),
    ('House', 'House')
)

# amenities
washer_dryer_choices_rental = (
    ('yes', 'yes'),
    ('no', 'no'),
)
air_conditioner_choices_rental = (
    ('yes', 'yes'),
    ('no', 'no'),
)
kitchen_choices_rental = (
    ('yes', 'yes'),
    ('no', 'no'),
)
balcony_choices_rental = (
    ('yes', 'yes'),
    ('no', 'no'),
)
gym_choices_rental = (
    ('yes', 'yes'),
    ('no', 'no'),
)

min_price_choices_rental = (
#   (None,'No Min'),
  ('0','0'),
  ('1000','1000'),
  ('3000','3000'),
  ('6000','6000'),
  ('10000','10000'),
  ('15000','15000'),
  ('20000','20000'),
  ('30000','30000'),
  ('40000','40000'),
)
max_price_choices_rental = (
#   (None,'No Max'),
  ('1000','1000'),
  ('3000','3000'),
  ('6000','6000'),
  ('10000','10000'),
  ('15000','15000'),
  ('20000','20000'),
  ('30000','30000'),
  ('40000','40000'),
  ('50000','50000'),
)

# min_price_choices_rental_view = (
#   ('0','0'),
#   ('1000','1000'),
#   ('3000','3000'),
#   ('6000','6000'),
#   ('10000','10000'),
#   ('15000','15000'),
#   ('20000','20000'),
#   ('30000','30000'),
#   ('40000','40000'),
# )
# max_price_choices_rental_view = (
#   ('1000','1000'),
#   ('3000','3000'),
#   ('6000','6000'),
#   ('10000','10000'),
#   ('15000','15000'),
#   ('20000','20000'),
#   ('30000','30000'),
#   ('40000','40000'),
#   ('50000','50000'),
# )







