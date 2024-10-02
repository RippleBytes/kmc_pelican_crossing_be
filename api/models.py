from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    # new_image = File(im_io, name=image.name)
    new_image = InMemoryUploadedFile(im_io, None, image.name, 'image/jpeg', im_io.tell(), None)
    return new_image


class School(models.Model):
    SCHOOL_TYPE_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
    ]

    BUS_OWNERSHIP_CHOICES = [
        ('School-Owned', 'School-Owned'),
        ('Hired', 'Hired'),
        ('Mixed', 'Mixed'),
    ]

    PARKING_CHOICES = [
        ('Inside-Compound', 'Inside-Compound'),
        ('Outside-Compound', 'Outside-Compound'),
    ]

    WARDS_CHOICES = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
        (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19),
        (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
        (31, 31), (32, 32)]

    school_name = models.CharField(max_length=255)
    school_type = models.CharField(max_length=10, choices=SCHOOL_TYPE_CHOICES)
    ward = models.PositiveIntegerField(choices=WARDS_CHOICES)
    same_timings_all_year = models.BooleanField(default=True)
    opening_time_summer = models.TimeField(null=True, blank=True)
    closing_time_summer = models.TimeField(null=True, blank=True)
    opening_time_winter = models.TimeField(null=True, blank=True)
    closing_time_winter = models.TimeField(null=True, blank=True)
    multiple_entrances = models.BooleanField(default=False)

    school_coordinates_latitude = models.CharField(max_length=100)
    school_coordinates_longitude = models.CharField(max_length=100)

    bus_facility = models.BooleanField(default=False)
    bus_count = models.PositiveIntegerField(null=True, blank=True)
    bus_ownership = models.CharField(max_length=100, choices=BUS_OWNERSHIP_CHOICES, null=True, blank=True)
    owned_buses_count = models.PositiveIntegerField(null=True, blank=True)
    hired_buses_count = models.PositiveIntegerField(null=True, blank=True)
    bus_parking = models.CharField(max_length=100, choices=PARKING_CHOICES, null=True, blank=True)
    bus_parking_latitude = models.CharField(max_length=100, null= True, blank=True)
    bus_parking_longitude = models.CharField(max_length=100, null= True, blank=True)
    pick_up_location_latitude = models.CharField(max_length=100, null=True, blank=True)
    pick_up_location_longitude = models.CharField(max_length=100, null=True, blank=True)
    drop_off_location_latitude = models.CharField(max_length=100, null=True, blank=True)
    drop_off_location_longitude = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['school_name']
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __unicode__(self):
        return self.school_name

    def __str__(self):
        return self.school_name



class EntranceExit(models.Model):
    school = models.ForeignKey(School, related_name='entrances', on_delete=models.CASCADE)
    gate_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='entrances/', null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    is_entrance = models.BooleanField(default=False)
    is_exit = models.BooleanField(default=False)

    def __unicode__(self):
        return self.gate_name

    def __str__(self):
        return self.gate_name

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)


class RoadwayFacilityNear(models.Model):
    DIRECTION_CHOICES = [
        ('North-South', 'North-South'),
        ('East-West', 'East-West'),
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West')
    ]

    CARRIAGE_WAY_DIRECTION = [
        ('One-Way', 'One-Way'),
        ('Two-Way', 'Two-Way'),
        ('Partial-One-Way', 'Partial-One-Way'),
        ('Partial-Two-Way', 'Partial-Two-Way'),

    ]

    DIVIDED_CHOICES = [
        ('Undivided', 'Undivided'),
        ('Central-Refuge', 'Central-Refuge'),
        ('Barrier', 'Barrier')
    ]

    INTERSECTION_TYPE = [
        ('No-Intersection', 'No-Intersection'),
        ('T-Junction', 'T-Junction'),
        ('4-Legged-Intersection', '4-Legged-Intersection'),
        ('Y-Junction', 'Y-Junction'),
        ('Staggered-T-Junction', 'Staggered-T-Junction'),
        ('Rotary-Or-Roundabout', 'Rotary-Or-Roundabout'),
    ]

    CENTRAL_MARKING = [
        ('None', 'None'),
        ('Broken-Single', 'Broken-Single'),
        ('Broken-Double', 'Broken-Double'),
        ('Continuous-Single', 'Continuous-Single'),
        ('Continuous-Double', 'Continuous-Double'),
    ]

    BOTH_SIDE_OR_ONE = [
        ('None', 'None'),
        ('Both-Side', 'Both-Side'),
        ('One-Side', 'One-Side')
    ]

    YES_NO_CHOICE = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    TRAFFIC_LIGHT_FUNC = [
        ('Working', 'Working'),
        ('Not-Working', 'Not-Working')
    ]

    school = models.OneToOneField(School, on_delete=models.CASCADE)
    carriage_width = models.FloatField()
    carriage_way_direction = models.CharField(max_length=50, choices=CARRIAGE_WAY_DIRECTION)
    carriage_direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    # is_partial_one_way = models.BooleanField(default=False)
    # is_partial_two_way = models.BooleanField(default=False)
    partial_start_time = models.TimeField(null=True, blank=True)
    partial_end_time = models.TimeField(null=True, blank=True)
    # partial_direction = models.CharField(max_length=50, choices=CARRIAGE_WAY_DIRECTION)
    divided = models.CharField(max_length=20, choices=DIVIDED_CHOICES)
    intersection_type = models.CharField(max_length=50, null=True, blank=True, choices=INTERSECTION_TYPE)
    number_of_lanes = models.CharField(max_length=100, null=True, blank=True)
    central_marking = models.CharField(max_length=50, null=True, blank=True, choices=CENTRAL_MARKING)

    footpath = models.CharField(max_length=100, choices=BOTH_SIDE_OR_ONE)
    width_side_one = models.FloatField(null=True, blank=True)
    width_side_two = models.FloatField(null=True, blank=True)

    pictures_near_side = models.ImageField(upload_to='uploads/', blank=True, null=True)
    pictures_far_side = models.ImageField(upload_to='uploads/', blank=True, null=True)

    traffic_lights = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    traffic_lights_working = models.CharField(max_length=15, null=True, blank=True, choices=TRAFFIC_LIGHT_FUNC)
    num_traffic_lights = models.IntegerField(null=True, blank=True)
    traffic_lights_pic_one = models.ImageField(upload_to='uploads/', blank=True, null=True)
    traffic_lights_pic_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    traffic_lights_pic_three = models.ImageField(upload_to='uploads/', blank=True, null=True)
    traffic_lights_pic_four = models.ImageField(upload_to='uploads/', blank=True, null=True)

    zebra_crossings = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    zebra_crossings_latitude = models.CharField(max_length=100)
    zebra_crossings_longitude = models.CharField(max_length=100)
    num_zebra_crossings = models.IntegerField(null=True, blank=True)
    zebra_width = models.FloatField(null=True, blank=True)

    foot_over_bridge = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    num_foot_over_bridges = models.IntegerField(null=True, blank=True)
    foot_over_bridge_pic_one = models.ImageField(upload_to='uploads/', blank=True, null=True)
    foot_over_bridge_pic_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    foot_over_bridge_pic_three = models.ImageField(upload_to='uploads/', blank=True, null=True)
    foot_over_bridge_one_latitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_one_longitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_two_latitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_two_longitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_three_latitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_three_longitude = models.CharField(max_length=100, blank=True, null=True)

    power_source = models.CharField(max_length=50, null=True, blank=True)
    power_source_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    electric_poles_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    electric_poles_latitude = models.CharField(max_length=100, blank=True, null=True)
    electric_poles_longitude = models.CharField(max_length=100, blank=True, null=True)

    on_street_vehicle_parking = models.CharField(max_length=10, choices=BOTH_SIDE_OR_ONE)
    street_side_one = models.ImageField(upload_to='uploads/', blank=True, null=True)
    street_side_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    street_side_one_latitude = models.CharField(max_length=100, blank=True, null=True)
    street_side_one_longitude = models.CharField(max_length=100, blank=True, null=True)
    street_side_two_latitude = models.CharField(max_length=100, blank=True, null=True)
    street_side_two_longitude = models.CharField(max_length=100, blank=True, null=True)

    viable_installation = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.school.school_name} - Roadway Info Near"

    def save(self, *args, **kwargs):

        if self.pictures_near_side:
            p1 = compress(self.pictures_near_side)
            self.pictures_near_side = p1

        if self.pictures_far_side:
            p2 = compress(self.pictures_far_side)
            self.pictures_far_side = p2

        if self.traffic_lights_pic_one:
            p3 = compress(self.traffic_lights_pic_one)
            self.traffic_lights_pic_one = p3

        if self.traffic_lights_pic_two:
            p4 = compress(self.traffic_lights_pic_two)
            self.traffic_lights_pic_two = p4

        if self.traffic_lights_pic_three:
            p5 = compress(self.traffic_lights_pic_three)
            self.traffic_lights_pic_three = p5

        if self.traffic_lights_pic_four:
            p51 = compress(self.traffic_lights_pic_four)
            self.traffic_lights_pic_four = p51

        if self.foot_over_bridge_pic_one:
            p6 = compress(self.foot_over_bridge_pic_one)
            self.foot_over_bridge_pic_one = p6

        if self.foot_over_bridge_pic_two:
            p7 = compress(self.foot_over_bridge_pic_two)
            self.foot_over_bridge_pic_two = p7

        if self.foot_over_bridge_pic_three:
            p8 = compress(self.foot_over_bridge_pic_three)
            self.foot_over_bridge_pic_three = p8

        if self.power_source_picture:
            p9 = compress(self.power_source_picture)
            self.power_source_picture = p9

        if self.electric_poles_picture:
            p10 = compress(self.electric_poles_picture)
            self.electric_poles_picture = p10

        if self.street_side_one:
            p11 = compress(self.street_side_one)
            self.street_side_one = p11

        if self.street_side_two:
            p12 = compress(self.street_side_two)
            self.street_side_two = p12
        super().save(*args, **kwargs)


class RoadwayFacilityFar(models.Model):
    DIRECTION_CHOICES = [
        ('North-South', 'North-South'),
        ('East-West', 'East-West'),
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West')
    ]

    CARRIAGE_WAY_DIRECTION = [
        ('One-Way', 'One-Way'),
        ('Two-Way', 'Two-Way'),
        ('Partial-One-Way', 'Partial-One-Way'),
        ('Partial-Two-Way', 'Partial-Two-Way'),
    ]

    DIVIDED_CHOICES = [
        ('Undivided', 'Undivided'),
        ('Central-Refuge', 'Central-Refuge'),
        ('Barrier', 'Barrier')
    ]

    INTERSECTION_TYPE = [
        ('No-Intersection', 'No-Intersection'),
        ('T-Junction', 'T-Junction'),
        ('4-Legged-Intersection', '4-Legged-Intersection'),
        ('Y-Junction', 'Y-Junction'),
        ('Staggered-T-Junction', 'Staggered-T-Junction'),
        ('Rotary-Or-Roundabout', 'Rotary-Or-Roundabout'),
    ]

    CENTRAL_MARKING = [
        ('None', 'None'),
        ('Broken-Single', 'Broken-Single'),
        ('Broken-Double', 'Broken-Double'),
        ('Continuous-Single', 'Continuous-Single'),
        ('Continuous-Double', 'Continuous-Double'),
    ]

    BOTH_SIDE_OR_ONE = [
        ('None', 'None'),
        ('Both-Side', 'Both-Side'),
        ('One-Side', 'One-Side')
    ]

    YES_NO_CHOICE = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    TRAFFIC_LIGHT_FUNC = [
        ('Working', 'Working'),
        ('Not-Working', 'Not-Working')
    ]
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    carriage_width = models.FloatField()
    carriage_way_direction = models.CharField(max_length=50, choices=CARRIAGE_WAY_DIRECTION)
    carriage_direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    # is_partial_one_way = models.BooleanField(default=False)
    # is_partial_two_way = models.BooleanField(default=False)
    partial_start_time = models.TimeField(null=True, blank=True)
    partial_end_time = models.TimeField(null=True, blank=True)
    # partial_direction = models.CharField(max_length=50, choices=CARRIAGE_WAY_DIRECTION)
    divided = models.CharField(max_length=20, choices=DIVIDED_CHOICES)
    intersection_type = models.CharField(max_length=50, null=True, blank=True, choices=INTERSECTION_TYPE)
    number_of_lanes = models.CharField(max_length=100, null=True, blank=True)
    central_marking = models.CharField(max_length=50, null=True, blank=True, choices=CENTRAL_MARKING)

    footpath = models.CharField(max_length=100, choices=BOTH_SIDE_OR_ONE)
    width_side_one = models.FloatField(null=True, blank=True)
    width_side_two = models.FloatField(null=True, blank=True)

    pictures_near_side = models.ImageField(upload_to='uploads/', blank=True, null=True)
    pictures_far_side = models.ImageField(upload_to='uploads/', blank=True, null=True)

    traffic_lights = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    traffic_lights_working = models.CharField(max_length=15, null=True, blank=True, choices=TRAFFIC_LIGHT_FUNC)
    num_traffic_lights = models.IntegerField(null=True, blank=True)
    traffic_lights_pic_one = models.ImageField(upload_to='uploads/', blank=True, null=True)
    traffic_lights_pic_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    traffic_lights_pic_three = models.ImageField(upload_to='uploads/', blank=True, null=True)
    traffic_lights_pic_four = models.ImageField(upload_to='uploads/', blank=True, null=True)

    zebra_crossings = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    zebra_crossings_latitude = models.CharField(max_length=100)
    zebra_crossings_longitude = models.CharField(max_length=100)
    num_zebra_crossings = models.IntegerField(null=True, blank=True)
    zebra_width = models.FloatField(null=True, blank=True)

    foot_over_bridge = models.CharField(max_length=3, choices=YES_NO_CHOICE)
    num_foot_over_bridges = models.IntegerField(null=True, blank=True)
    foot_over_bridge_pic_one = models.ImageField(upload_to='uploads/', blank=True, null=True)
    foot_over_bridge_pic_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    foot_over_bridge_pic_three = models.ImageField(upload_to='uploads/', blank=True, null=True)
    foot_over_bridge_one_latitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_one_longitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_two_latitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_two_longitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_three_latitude = models.CharField(max_length=100, blank=True, null=True)
    foot_over_bridge_three_longitude = models.CharField(max_length=100, blank=True, null=True)

    power_source = models.CharField(max_length=50, null=True, blank=True)
    power_source_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    electric_poles_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    electric_poles_latitude = models.CharField(max_length=100, blank=True, null=True)
    electric_poles_longitude = models.CharField(max_length=100, blank=True, null=True)

    on_street_vehicle_parking = models.CharField(max_length=10, choices=BOTH_SIDE_OR_ONE)
    street_side_one = models.ImageField(upload_to='uploads/', blank=True, null=True)
    street_side_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    street_side_one_latitude = models.CharField(max_length=100, blank=True, null=True)
    street_side_one_longitude = models.CharField(max_length=100, blank=True, null=True)
    street_side_two_latitude = models.CharField(max_length=100, blank=True, null=True)
    street_side_two_longitude = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.id

    def __str__(self):
        return f"{self.school.school_name} - Roadway Info Far"

    def save(self, *args, **kwargs):

        if self.pictures_near_side:
            p1 = compress(self.pictures_near_side)
            self.pictures_near_side = p1

        if self.pictures_far_side:
            p2 = compress(self.pictures_far_side)
            self.pictures_far_side = p2

        if self.traffic_lights_pic_one:
            p3 = compress(self.traffic_lights_pic_one)
            self.traffic_lights_pic_one = p3

        if self.traffic_lights_pic_two:
            p4 = compress(self.traffic_lights_pic_two)
            self.traffic_lights_pic_two = p4

        if self.traffic_lights_pic_three:
            p5 = compress(self.traffic_lights_pic_three)
            self.traffic_lights_pic_three = p5

        if self.traffic_lights_pic_four:
            p51 = compress(self.traffic_lights_pic_four)
            self.traffic_lights_pic_four = p51

        if self.foot_over_bridge_pic_one:
            p6 = compress(self.foot_over_bridge_pic_one)
            self.foot_over_bridge_pic_one = p6

        if self.foot_over_bridge_pic_two:
            p7 = compress(self.foot_over_bridge_pic_two)
            self.foot_over_bridge_pic_two = p7

        if self.foot_over_bridge_pic_three:
            p8 = compress(self.foot_over_bridge_pic_three)
            self.foot_over_bridge_pic_three = p8

        if self.power_source_picture:
            p9 = compress(self.power_source_picture)
            self.power_source_picture = p9

        if self.electric_poles_picture:
            p10 = compress(self.electric_poles_picture)
            self.electric_poles_picture = p10

        if self.street_side_one:
            p11 = compress(self.street_side_one)
            self.street_side_one = p11

        if self.street_side_two:
            p12 = compress(self.street_side_two)
            self.street_side_two = p12
        super().save(*args, **kwargs)


class FinalizationForm(models.Model):
    YES_NO_CHOICE = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    is_near_side = models.BooleanField(default=False)
    data_near = models.ForeignKey(RoadwayFacilityNear, on_delete=models.CASCADE, blank=True, null=True)
    data_far = models.ForeignKey(RoadwayFacilityFar, on_delete=models.CASCADE, blank=True, null=True)

    near_side_latitude = models.CharField(max_length=100, blank=True, null=True)
    near_side_longitude = models.CharField(max_length=100, blank=True, null=True)
    far_side_latitude = models.CharField(max_length=100, blank=True, null=True)
    far_side_longitude = models.CharField(max_length=100, blank=True, null=True)
    near_side_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    far_side_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    is_zebra_crossings_available = models.CharField(max_length=3, choices=YES_NO_CHOICE, blank=True, null=True)
    viable_power_source = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return u'%s' % self.id

    def __str__(self):
        return f"Finalization for {self.school.school_name} "

    def save(self, *args, **kwargs):

        if self.near_side_picture:
            p1 = compress(self.near_side_picture)
            self.near_side_picture = p1

        if self.far_side_picture:
            p2 = compress(self.far_side_picture)
            self.far_side_picture = p2
