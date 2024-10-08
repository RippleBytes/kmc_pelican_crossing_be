from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import School, EntranceExit, RoadwayFacilityNear, RoadwayFacilityFar, FinalizationForm
from django.forms.models import model_to_dict


# Use @csrf_exempt if you have issues with CSRF tokens during form submission
@csrf_exempt
def roadway_near_school_submission(request, school_id):
    if request.method == 'POST':
        # Collecting Roadway Information
        # school_id = request.POST['schoolId']
        carriage_width = request.POST.get('carriage_width')
        carriage_way_direction = request.POST.get('carriage_way_direction')
        carriage_direction_one_way = request.POST.get('carriage_way_direction_oneway')
        carriage_direction_two_way = request.POST.get('carriage_way_direction_two_way')
        # partial_one_way = request.POST.get('partial_one_way')
        # partial_two_way = request.POST.get('partial_two_way')
        partial_start_time_one_way = request.POST.get('partial_start_time_one_way')
        partial_end_time_one_way = request.POST.get('partial_end_time_one_way')
        partial_start_time_two_way = request.POST.get('partial_start_time_two_way')
        partial_end_time_two_way = request.POST.get('partial_end_time_two_way')

        divided_undivided = request.POST.get('divided_undivided')
        intersection_type = request.POST.get('intersection_type')
        num_lanes = request.POST.get('num_lanes')
        central_road_marking = request.POST.get('central_road_marking')
        footpath = request.POST.get('footpath')
        width_side_one = None
        width_side_two = None
        if footpath == 'One-Side':
            width_side_one = request.POST.get('width_side_one')
        elif footpath == 'Both-Side':
            width_side_one = request.POST.get('width_side_one')
            width_side_two = request.POST.get('width_side_two')

        # one_way_two_way = request.POST.get('one_way_two_way')

        pictures_near_side = request.FILES.get('pictures_near_side')
        pictures_far_side = request.FILES.get('pictures_far_side')
        # Collecting Traffic Control System Information
        traffic_lights = request.POST.get('traffic_lights')
        traffic_lights_working = request.POST.get('traffic_lights_working')
        num_traffic_lights = request.POST.get('traffic_light_number')
        traffic_lights_pic1 = request.FILES.get('traffic_lights_pic1')
        traffic_lights_pic2 = request.FILES.get('traffic_lights_pic2')
        traffic_lights_pic3 = request.FILES.get('traffic_lights_pic3')
        traffic_lights_pic4 = request.FILES.get('traffic_lights_pic4')

        # Zebra Crossings Information
        zebra_crossings = request.POST.get('zebra_crossings')
        num_zebra_crossings = request.POST.get('num_zebra_crossings')
        zebra_width = request.POST.get('zebra_width')
        zebra_map_coordinate = request.POST.get('zebraMapCoordinate')

        # Foot-over Bridge Information
        foot_over_bridge = request.POST.get('foot_over_bridge')
        num_foot_over_bridges = request.POST.get('foot_over_bridge_number')
        foot_over_bridge_picture1 = request.FILES.get('foot_over_bridge_picture1')
        foot_over_bridge_picture2 = request.FILES.get('foot_over_bridge_picture2')
        foot_over_bridge_picture3 = request.FILES.get('foot_over_bridge_picture3')
        foot_over_bridge_map_coordinate1 = request.POST.get('foot_over_bridge_map_coordinate1')
        foot_over_bridge_map_coordinate2 = request.POST.get('foot_over_bridge_map_coordinate2')
        foot_over_bridge_map_coordinate3 = request.POST.get('foot_over_bridge_map_coordinate3')

        # Electrical Infrastructure Information
        power_source = request.POST.get('power_source')
        power_source_pictures = request.FILES.get('power_source_pictures')
        electric_poles_picture = request.FILES.get('electric_poles_picture')
        electric_poles_map_coordinate = request.POST.get('electric_poles_map_coordinate')

        on_street_vehicle_parking = request.POST.get('on_street_vehicle_parking')
        on_street_vehicle_parking_pictures_one = request.FILES.get('on_street_vehicle_parking_picture_one')
        on_street_vehicle_parking_pictures_two = request.FILES.get('on_street_vehicle_parking_picture_two')
        on_street_vehicle_parking_coordinate_one = request.POST.get('on_street_vehicle_parking_map_coordinate_one')
        on_street_vehicle_parking_coordinate_two = request.POST.get('on_street_vehicle_parking_map_coordinate_two')

        # Viability to Install System
        viable_installation = request.POST.get('viable_installation')
        reason = request.POST.get('reason')

        # Handling uploaded files (pictures)

        # Do something with the data
        # For example, save it to the database, or process it further
        # This is just a sample response

        rf = RoadwayFacilityNear(
            school=School.objects.get(pk=school_id),
            carriage_width=carriage_width,
            carriage_way_direction=carriage_way_direction,
            divided=divided_undivided,
            intersection_type=intersection_type,
            number_of_lanes=num_lanes,
            central_marking=central_road_marking,

            footpath=footpath,

            pictures_near_side=pictures_near_side,
            pictures_far_side=pictures_far_side,

            traffic_lights=traffic_lights,

            zebra_crossings=zebra_crossings,

            foot_over_bridge=foot_over_bridge,

            power_source=power_source,
            power_source_picture=power_source_pictures,
            electric_poles_picture=electric_poles_picture,

            on_street_vehicle_parking=on_street_vehicle_parking,

            viable_installation=viable_installation,
            reason=reason
        )

        rfOld = RoadwayFacilityNear.objects.filter(school=School.objects.get(pk=school_id))
        if len(rfOld) > 0:
            rf.id = rfOld[0].id

        if rf.carriage_way_direction == 'One-Way':
            rf.carriage_direction = carriage_direction_one_way
        elif rf.carriage_way_direction == 'Two-Way':
            rf.carriage_direction = carriage_direction_two_way
        elif rf.carriage_way_direction == 'Partial':
            rf.partial_direction_one_way = carriage_direction_one_way
            rf.partial_direction_two_way = carriage_direction_two_way
            rf.partial_start_time_one_way = partial_start_time_one_way
            rf.partial_end_time_one_way = partial_end_time_one_way
            rf.partial_start_time_two_way = partial_start_time_two_way
            rf.partial_end_time_two_way = partial_end_time_two_way

        if rf.zebra_crossings == 'Yes':
            rf.num_zebra_crossings = num_zebra_crossings
            rf.zebra_width = zebra_width

        if rf.traffic_lights == 'Yes':
            rf.num_traffic_lights = 3 if num_traffic_lights == 'Three' else 2 if num_traffic_lights == 'Two' else 1
            rf.traffic_lights_working = traffic_lights_working
            if rf.num_traffic_lights == 1:
                rf.traffic_lights_pic_one = traffic_lights_pic1
            elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 2:
                rf.traffic_lights_pic_one = traffic_lights_pic1
                rf.traffic_lights_pic2 = traffic_lights_pic2
            elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 3:
                rf.traffic_lights_pic_one = traffic_lights_pic1
                rf.traffic_lights_pic2 = traffic_lights_pic2
                rf.traffic_lights_pic3 = traffic_lights_pic3
            elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 4:
                rf.traffic_lights_pic_one = traffic_lights_pic1
                rf.traffic_lights_pic2 = traffic_lights_pic2
                rf.traffic_lights_pic3 = traffic_lights_pic3
                rf.traffic_lights_pic4 = traffic_lights_pic4

        if rf.foot_over_bridge == 'Yes':
            rf.num_foot_over_bridges = 3 if num_foot_over_bridges == 'Three' else 2 if num_foot_over_bridges == 'Two' else 1
            if rf.num_foot_over_bridges == 1:
                rf.foot_over_bridge_pic_one = foot_over_bridge_picture1
                rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                    str(foot_over_bridge_map_coordinate1).split(",")
            elif rf.foot_over_bridge == 'Yes' and rf.num_foot_over_bridges == 2:
                rf.foot_over_bridge_pic_one = foot_over_bridge_picture1
                rf.foot_over_bridge_pic_two = foot_over_bridge_picture2
                rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                    str(foot_over_bridge_map_coordinate1).split(",")
                rf.foot_over_bridge_two_latitude, rf.foot_over_bridge_two_longitude = \
                    str(foot_over_bridge_map_coordinate2).split(",")
            elif rf.foot_over_bridge == 'Yes' and rf.num_foot_over_bridges == 3:
                rf.foot_over_bridge_pic_one = foot_over_bridge_picture1
                rf.foot_over_bridge_pic_two = foot_over_bridge_picture2
                rf.foot_over_bridge_pic_three = foot_over_bridge_picture3

                if str(foot_over_bridge_map_coordinate1) != "":
                    rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                        str(foot_over_bridge_map_coordinate1).split(",")

                if str(foot_over_bridge_map_coordinate2) != "":
                    rf.foot_over_bridge_two_latitude, rf.foot_over_bridge_two_longitude = \
                        str(foot_over_bridge_map_coordinate2).split(",")

                if str(foot_over_bridge_map_coordinate3) != "":
                    rf.foot_over_bridge_three_latitude, rf.foot_over_bridge_three_longitude = \
                        str(foot_over_bridge_map_coordinate3).split(",")

        if rf.footpath == 'Both-Side':
            rf.width_side_one = width_side_one
            rf.width_side_two = width_side_two
        elif rf.footpath == 'One-Side':
            rf.width_side_one = width_side_one

        if rf.zebra_crossings == 'Yes':
            if str(zebra_map_coordinate) != "":
                rf.zebra_crossings_latitude, rf.zebra_crossings_longitude = str(zebra_map_coordinate).split(",")

        if rf.on_street_vehicle_parking == 'One-Side':
            rf.street_side_one = on_street_vehicle_parking_pictures_one
            if str(on_street_vehicle_parking_coordinate_one) != "":
                rf.street_side_one_latitude, rf.street_side_one_longitude = str(
                    on_street_vehicle_parking_coordinate_one).split(",")
        elif rf.on_street_vehicle_parking == 'Both-Side':
            rf.street_side_one = on_street_vehicle_parking_pictures_one
            if str(on_street_vehicle_parking_coordinate_one) != "":
                rf.street_side_one_latitude, rf.street_side_one_longitude = str(
                    on_street_vehicle_parking_coordinate_one).split(",")

            rf.street_side_two = on_street_vehicle_parking_pictures_two
            if str(on_street_vehicle_parking_coordinate_two) != "":
                rf.street_side_two_latitude, rf.street_side_two_longitude = str(
                    on_street_vehicle_parking_coordinate_two).split(",")

        if electric_poles_map_coordinate is not None and electric_poles_map_coordinate != "":
            rf.electric_poles_latitude, rf.electric_poles_longitude = str(electric_poles_map_coordinate).split(",")

        rf.save()

        # Return a simple HttpResponse or render to a template
        if rf.viable_installation == 'Yes':
            return redirect(f'/finalize/{school_id}')

        return redirect(f'/roadway-far/{school_id}')

    school_list = School.objects.filter(id=school_id)
    # Render the form if GET request
    return render(request, 'roadway_near_school.html', {"school_id": school_id, "data": school_list})


@csrf_exempt
def roadway_far_from_school_submission(request, school_id):
    if request.method == 'POST':
        # Collecting Roadway Information
        # school_id = request.POST['schoolId']
        carriage_width = request.POST.get('carriage_width')
        carriage_way_direction = request.POST.get('carriage_way_direction')
        carriage_direction_one_way = request.POST.get('carriage_way_direction_oneway')
        carriage_direction_two_way = request.POST.get('carriage_way_direction_two_way')
        # partial_one_way = request.POST.get('partial_one_way')
        # partial_two_way = request.POST.get('partial_two_way')
        partial_start_time = request.POST.get('partial_start_time')
        partial_end_time = request.POST.get('partial_end_time')

        divided_undivided = request.POST.get('divided_undivided')
        intersection_type = request.POST.get('intersection_type')
        num_lanes = request.POST.get('num_lanes')
        central_road_marking = request.POST.get('central_road_marking')
        footpath = request.POST.get('footpath')
        width_side_one = None
        width_side_two = None
        if footpath == 'One-Side':
            width_side_one = request.POST.get('width_side_one')
        elif footpath == 'Both-Side':
            width_side_one = request.POST.get('width_side_one')
            width_side_two = request.POST.get('width_side_two')

        # one_way_two_way = request.POST.get('one_way_two_way')

        pictures_near_side = request.FILES.get('pictures_near_side')
        pictures_far_side = request.FILES.get('pictures_far_side')
        # Collecting Traffic Control System Information
        traffic_lights = request.POST.get('traffic_lights')
        traffic_lights_working = request.POST.get('traffic_lights_working')
        num_traffic_lights = request.POST.get('traffic_light_number')
        traffic_lights_pic1 = request.FILES.get('traffic_lights_pic1')
        traffic_lights_pic2 = request.FILES.get('traffic_lights_pic2')
        traffic_lights_pic3 = request.FILES.get('traffic_lights_pic3')
        traffic_lights_pic4 = request.FILES.get('traffic_lights_pic4')

        # Zebra Crossings Information
        zebra_crossings = request.POST.get('zebra_crossings')
        num_zebra_crossings = request.POST.get('num_zebra_crossings')
        zebra_width = request.POST.get('zebra_width')
        zebra_map_coordinate = request.POST.get('zebraMapCoordinate')

        # Foot-over Bridge Information
        foot_over_bridge = request.POST.get('foot_over_bridge')
        num_foot_over_bridges = request.POST.get('foot_over_bridge_number')
        foot_over_bridge_picture1 = request.FILES.get('foot_over_bridge_picture1')
        foot_over_bridge_picture2 = request.FILES.get('foot_over_bridge_picture2')
        foot_over_bridge_picture3 = request.FILES.get('foot_over_bridge_picture3')
        foot_over_bridge_map_coordinate1 = request.POST.get('foot_over_bridge_map_coordinate1')
        foot_over_bridge_map_coordinate2 = request.POST.get('foot_over_bridge_map_coordinate2')
        foot_over_bridge_map_coordinate3 = request.POST.get('foot_over_bridge_map_coordinate3')

        # Electrical Infrastructure Information
        power_source = request.POST.get('power_source')
        power_source_pictures = request.FILES.get('power_source_pictures')
        electric_poles_picture = request.FILES.get('electric_poles_picture')
        electric_poles_map_coordinate = request.POST.get('electric_poles_map_coordinate')

        on_street_vehicle_parking = request.POST.get('on_street_vehicle_parking')
        on_street_vehicle_parking_pictures_one = request.FILES.get('on_street_vehicle_parking_picture_one')
        on_street_vehicle_parking_pictures_two = request.FILES.get('on_street_vehicle_parking_picture_two')
        on_street_vehicle_parking_coordinate_one = request.POST.get('on_street_vehicle_parking_map_coordinate_one')
        on_street_vehicle_parking_coordinate_two = request.POST.get('on_street_vehicle_parking_map_coordinate_two')

        rf = RoadwayFacilityFar(
            school=School.objects.get(pk=school_id),
            carriage_width=carriage_width,
            carriage_way_direction=carriage_way_direction,
            divided=divided_undivided,
            intersection_type=intersection_type,
            number_of_lanes=num_lanes,
            central_marking=central_road_marking,

            footpath=footpath,

            pictures_near_side=pictures_near_side,
            pictures_far_side=pictures_far_side,

            traffic_lights=traffic_lights,

            zebra_crossings=zebra_crossings,

            foot_over_bridge=foot_over_bridge,

            power_source=power_source,
            power_source_picture=power_source_pictures,
            electric_poles_picture=electric_poles_picture,

            on_street_vehicle_parking=on_street_vehicle_parking,
        )

        rfOld = RoadwayFacilityFar.objects.filter(school=School.objects.get(pk=school_id))
        if len(rfOld) > 0:
            rf.id = rfOld[0].id

        if rf.carriage_way_direction == 'One-Way':
            rf.carriage_direction = carriage_direction_one_way
        elif rf.carriage_way_direction == 'Two-Way':
            rf.carriage_direction = carriage_direction_two_way
        elif rf.carriage_way_direction == 'Partial-One-Way':
            rf.carriage_direction = carriage_direction_one_way
            rf.partial_start_time = partial_start_time
            rf.partial_end_time = partial_end_time
        elif rf.carriage_way_direction == 'Partial-Two-Way':
            rf.carriage_direction = carriage_direction_two_way
            rf.partial_start_time = partial_start_time
            rf.partial_end_time = partial_end_time

        if rf.zebra_crossings == 'Yes':
            rf.num_zebra_crossings = num_zebra_crossings
            rf.zebra_width = zebra_width

        if rf.traffic_lights == 'Yes':
            rf.num_traffic_lights = 3 if num_traffic_lights == 'Three' else 2 if num_traffic_lights == 'Two' else 1
            rf.traffic_lights_working = traffic_lights_working
            if rf.num_traffic_lights == 1:
                rf.traffic_lights_pic_one = traffic_lights_pic1
            elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 2:
                rf.traffic_lights_pic_one = traffic_lights_pic1
                rf.traffic_lights_pic2 = traffic_lights_pic2
            elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 3:
                rf.traffic_lights_pic_one = traffic_lights_pic1
                rf.traffic_lights_pic2 = traffic_lights_pic2
                rf.traffic_lights_pic3 = traffic_lights_pic3
            elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 4:
                rf.traffic_lights_pic_one = traffic_lights_pic1
                rf.traffic_lights_pic2 = traffic_lights_pic2
                rf.traffic_lights_pic3 = traffic_lights_pic3
                rf.traffic_lights_pic4 = traffic_lights_pic4

        if rf.foot_over_bridge == 'Yes':
            rf.num_foot_over_bridges = 3 if num_foot_over_bridges == 'Three' else 2 if num_foot_over_bridges == 'Two' else 1
            if rf.num_foot_over_bridges == 1:
                rf.foot_over_bridge_pic_one = foot_over_bridge_picture1
                rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                    str(foot_over_bridge_map_coordinate1).split(",")
            elif rf.foot_over_bridge == 'Yes' and rf.num_foot_over_bridges == 2:
                rf.foot_over_bridge_pic_one = foot_over_bridge_picture1
                rf.foot_over_bridge_pic_two = foot_over_bridge_picture2
                rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                    str(foot_over_bridge_map_coordinate1).split(",")
                rf.foot_over_bridge_two_latitude, rf.foot_over_bridge_two_longitude = \
                    str(foot_over_bridge_map_coordinate2).split(",")
            elif rf.foot_over_bridge == 'Yes' and rf.num_foot_over_bridges == 3:
                rf.foot_over_bridge_pic_one = foot_over_bridge_picture1
                rf.foot_over_bridge_pic_two = foot_over_bridge_picture2
                rf.foot_over_bridge_pic_three = foot_over_bridge_picture3

                if str(foot_over_bridge_map_coordinate1) != "":
                    rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                        str(foot_over_bridge_map_coordinate1).split(",")

                if str(foot_over_bridge_map_coordinate2) != "":
                    rf.foot_over_bridge_two_latitude, rf.foot_over_bridge_two_longitude = \
                        str(foot_over_bridge_map_coordinate2).split(",")

                if str(foot_over_bridge_map_coordinate3) != "":
                    rf.foot_over_bridge_three_latitude, rf.foot_over_bridge_three_longitude = \
                        str(foot_over_bridge_map_coordinate3).split(",")

        if rf.footpath == 'Both-Side':
            rf.width_side_one = width_side_one
            rf.width_side_two = width_side_two
        elif rf.footpath == 'One-Side':
            rf.width_side_one = width_side_one

        if rf.zebra_crossings == 'Yes':
            if str(zebra_map_coordinate) != "":
                rf.zebra_crossings_latitude, rf.zebra_crossings_longitude = str(zebra_map_coordinate).split(",")

        if rf.on_street_vehicle_parking == 'One-Side':
            rf.street_side_one = on_street_vehicle_parking_pictures_one
            if str(on_street_vehicle_parking_coordinate_one) != "":
                rf.street_side_one_latitude, rf.street_side_one_longitude = str(
                    on_street_vehicle_parking_coordinate_one).split(",")
        elif rf.on_street_vehicle_parking == 'Both-Side':
            rf.street_side_one = on_street_vehicle_parking_pictures_one
            if str(on_street_vehicle_parking_coordinate_one) != "":
                rf.street_side_one_latitude, rf.street_side_one_longitude = str(
                    on_street_vehicle_parking_coordinate_one).split(",")

            rf.street_side_two = on_street_vehicle_parking_pictures_two
            if str(on_street_vehicle_parking_coordinate_two) != "":
                rf.street_side_two_latitude, rf.street_side_two_longitude = str(
                    on_street_vehicle_parking_coordinate_two).split(",")

        if electric_poles_map_coordinate is not None and electric_poles_map_coordinate != "":
            rf.electric_poles_latitude, rf.electric_poles_longitude = str(electric_poles_map_coordinate).split(",")

        rf.save()

        # Return a simple HttpResponse or render to a template
        return redirect(f'/finalize/{school_id}')

    school_list = School.objects.filter(id=school_id)
    # Render the form if GET request
    return render(request, 'roadway_far_school.html', {"school_id": school_id, "data": school_list})


def school_form_view(request):
    if request.method == 'POST':
        # Extract data from POST request
        school_name = request.POST.get('schoolName')
        school_type = request.POST.get('schoolType')
        ward = request.POST.get('ward')
        # entrance_image = request.FILES.get('entranceImage')
        multiple_entrances = request.POST.get('multipleEntrances') == 'Yes'
        school_coordinates = request.POST.get('schoolCoordinates')
        bus_facility = request.POST.get('busFacility') == 'Yes'
        # bus_count = request.POST.get('busCount') or None
        bus_ownership = request.POST.get('busOwnership') or None
        owned_buses_count = request.POST.get('ownedBusesCount') or 0
        hired_buses_count = request.POST.get('hiredBusesCount') or 0
        bus_parking = request.POST.get('busParking')
        same_timing = request.POST.get('isSameTimingAllYear')
        is_same_timing_all_year = False
        if same_timing is not None:
            is_same_timing_all_year = len(same_timing) > 0
        if is_same_timing_all_year:
            opening_time_summer = request.POST.get('openingTime')
            closing_time_summer = request.POST.get('closingTime')
            opening_time_winter = opening_time_summer
            closing_time_winter = closing_time_summer
        else:
            opening_time_summer = request.POST.get('openingTimeSummer')
            closing_time_summer = request.POST.get('closingTimeSummer')
            opening_time_winter = request.POST.get('openingTimeWinter')
            closing_time_winter = request.POST.get('closingTimeWinter')

        pick_location = request.POST.get('pickLocation') or None
        drop_location = request.POST.get('dropLocation') or None

        # Save the school object
        school = School(
            school_name=school_name,
            school_type=school_type,
            ward=ward,
            # entrance_image=entrance_image,
            multiple_entrances=multiple_entrances,
            bus_facility=bus_facility,
            # bus_count=bus_count,
            bus_ownership=bus_ownership,
            owned_buses_count=owned_buses_count,
            hired_buses_count=hired_buses_count,
            bus_parking=bus_parking,
            same_timings_all_year=is_same_timing_all_year,
            opening_time_summer=opening_time_summer,
            closing_time_summer=closing_time_summer,
            opening_time_winter=opening_time_winter,
            closing_time_winter=closing_time_winter,
        )

        if school_coordinates is not None and school_coordinates != "":
            school.school_coordinates_latitude, school.school_coordinates_longitude = str(school_coordinates).split(",")

        if pick_location is not None:
            latitude, longitude = str(pick_location).split(",")
            school.pick_up_location_latitude = latitude
            school.pick_up_location_longitude = longitude

        if drop_location is not None:
            latitude, longitude = str(drop_location).split(",")
            school.drop_off_location_latitude = latitude
            school.drop_off_location_longitude = longitude

        school.save()

        # Handle multiple entrances
        if multiple_entrances:
            gate_names = request.POST.getlist('gateName[]')
            # is_exit = request.POST.getlist('isExit[]')
            is_entrance = request.POST.getlist('isEntrance[]')
            entrance_images = request.FILES.getlist('entranceImage[]')
            entrance_locations = request.POST.getlist('entranceLocation[]')
            for index, gateName in enumerate(gate_names):
                en_tx = EntranceExit()
                en_tx.school = school
                en_tx.gate_name = gateName
                try:
                    en_tx.is_entrance = is_entrance[index] != "isExit"
                except IndexError:
                    en_tx.is_entrance = False

                try:
                    en_tx.is_exit = is_entrance[index] != "isEntrance"
                except IndexError:
                    en_tx.is_exit = False

                try:
                    en_tx.image = entrance_images[index]
                except IndexError:
                    pass

                try:
                    latitude, longitude = str(entrance_locations[index]).split(",")
                    en_tx.latitude = latitude
                    en_tx.longitude = longitude
                except IndexError:
                    pass
                en_tx.save()

        return redirect(f'/roadway-near/{school.id}')

    return render(request, 'school_form.html')


def finalize_form_view(request, school_id):
    if request.method == 'POST':
        near_side_coordinate = request.POST.get('nearSideCoordinates')
        far_side_coordinate = request.POST.get('farSideCoordinates')
        zebra_crossings = request.POST.get('zebra_crossings')
        viable_text = request.POST.get('viabletext')
        near_side_picture = request.POST.get('near_side_picture')
        far_side_picture = request.POST.get('far_side_picture')

        final_form = FinalizationForm.objects.get(school_id=school_id)
        if near_side_coordinate != "":
            final_form.near_side_latitude, final_form.near_side_longitude = str(near_side_coordinate).split(",")

        if far_side_coordinate != "":
            final_form.far_side_latitude, final_form.far_side_longitude = str(far_side_coordinate).split(",")

        if near_side_picture != "":
            final_form.near_side_picture = near_side_picture

        if far_side_picture != "":
            final_form.far_side_picture = far_side_picture

        final_form.is_zebra_crossings_available = zebra_crossings
        final_form.viable_power_source = viable_text
        final_form.save()

        return redirect(f'/complete/{school_id}')

    old_form = None
    school_list = School.objects.filter(id=school_id)
    rf_near = RoadwayFacilityNear.objects.get(school_id=school_id)
    finalize_form = FinalizationForm()
    try:
        old_form = FinalizationForm.objects.get(school_id=school_id, )
        finalize_form.id = old_form.id
    except:
        pass
    finalize_form.school = school_list[0]
    if rf_near.viable_installation == 'Yes':
        finalize_form.is_near_side = True
        finalize_form.data_near = rf_near
    else:
        rf_far = RoadwayFacilityFar.objects.get(school_id=school_id)
        finalize_form.is_near_side = False
        finalize_form.data_far = rf_far

    finalize_form.save()

    return render(request, 'finalization_form.html',
                  {"school_id": school_id, "school": school_list, "data": finalize_form})


def complete(request, school_id):
    return render(request, 'success.html')


def home(request):
    school_list = School.objects.all().order_by('-id')
    return render(request, 'home.html', {"school_list": school_list})


def check_path(request, school_id):
    if school_id != 0:
        try:
            school = School.objects.get(id=school_id)
            near = RoadwayFacilityNear.objects.get(school_id=school_id)
            far = RoadwayFacilityFar.objects.get(school_id=school_id)
            finalize = FinalizationForm.objects.get(school_id=school_id)
        except School.DoesNotExist:
            return redirect('/home')
        except RoadwayFacilityNear.DoesNotExist:
            return redirect(f'/roadway-near/{school_id}')
        except RoadwayFacilityFar.DoesNotExist:
            return redirect(f'/roadway-far/{school_id}')
        except FinalizationForm.DoesNotExist:
            return redirect(f'/finalize/{school_id}')

        return redirect(f'/complete/{school_id}')
    return redirect('/home')




