from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import School, EntranceExit, RoadwayFacilityNear, RoadwayFacilityFar


# Use @csrf_exempt if you have issues with CSRF tokens during form submission
@csrf_exempt
def roadway_near_school_submission(request):
    if request.method == 'POST':
        # Collecting Roadway Information
        school_id = request.POST['schoolId']
        carriage_width = request.POST.get('carriage_width')
        carriage_way_direction = request.POST.get('carriage_way_direction')
        carriage_direction = request.POST.get('carriage_direction')
        partial_one_way = request.POST.get('partial_one_way')
        partial_two_way = request.POST.get('partial_two_way')
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
        elif footpath == 'Two-Side':
            width_side_one = request.POST.get('width_side_one')
            width_side_two = request.POST.get('width_side_two')

        # one_way_two_way = request.POST.get('one_way_two_way')

        pictures_near_side = request.FILES.get('pictures_near_side')
        pictures_far_side = request.FILES.get('pictures_far_side')
        # Collecting Traffic Control System Information
        traffic_lights = request.POST.get('traffic_lights')
        traffic_lights_working = request.POST.get('traffic_lights_working')
        num_traffic_lights = request.POST.get('num_traffic_lights')
        traffic_lights_pic1 = request.FILES.get('traffic_lights_pic1')
        traffic_lights_pic2 = request.FILES.get('traffic_lights_pic12')
        traffic_lights_pic3 = request.FILES.get('traffic_lights_pic3')

        # Zebra Crossings Information
        zebra_crossings = request.POST.get('zebra_crossings')
        num_zebra_crossings = request.POST.get('num_zebra_crossings')
        zebra_width = request.POST.get('zebra_width')
        zebra_map_coordinate = request.POST.get('zebraMapCoordinate')

        # Foot-over Bridge Information
        foot_over_bridge = request.POST.get('foot_over_bridge')
        num_foot_over_bridges = request.POST.get('num_foot_over_bridges')
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
        on_street_vehicle_parking_pictures = request.FILES.getlist('on_street_vehicle_parking_pictures')
        on_street_vehicle_parking_coordinate = request.POST.get('on_street_vehicle_parking_coordinate')

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
            carriage_direction=carriage_direction,
            divided=divided_undivided,
            intersection_type=intersection_type,
            number_of_lanes=num_lanes,
            central_marking=central_road_marking,

            footpath=footpath,

            pictures_near_side=pictures_near_side,
            pictures_far_side=pictures_far_side,

            traffic_lights=traffic_lights,
            traffic_lights_working=traffic_lights_working,
            num_traffic_lights=num_traffic_lights,

            zebra_crossings=zebra_crossings,
            num_zebra_crossings=num_zebra_crossings,
            zebra_width=zebra_width,

            foot_over_bridge=foot_over_bridge,
            num_foot_over_bridges=num_foot_over_bridges,

            power_source=power_source,
            power_source_picture=power_source_pictures,
            electric_poles_picture=electric_poles_picture,

            on_street_vehicle_parking=on_street_vehicle_parking,

            viable_installation=viable_installation,
            reason=reason
        )

        if rf.carriage_way_direction == 'One-Way' and partial_one_way:
            rf.partial_one_way = True
            rf.partial_start_time = partial_start_time
        elif rf.carriage_way_direction == 'Two-Way' and partial_two_way:
            rf.partial_two_way = True
            rf.partial_end_time = partial_end_time

        if rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 1:
            rf.traffic_lights_pic_one = traffic_lights_pic1
        elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 2:
            rf.traffic_lights_pic_one = traffic_lights_pic1
            rf.traffic_lights_pic2 = traffic_lights_pic2
        elif rf.traffic_lights == 'Yes' and rf.num_traffic_lights == 3:
            rf.traffic_lights_pic_one = traffic_lights_pic1
            rf.traffic_lights_pic2 = traffic_lights_pic2
            rf.traffic_lights_pic3 = traffic_lights_pic3

        if rf.foot_over_bridge == 'Yes' and rf.num_foot_over_bridges == 1:
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
            rf.foot_over_bridge_one_latitude, rf.foot_over_bridge_one_longitude = \
                str(foot_over_bridge_map_coordinate1).split(",")
            rf.foot_over_bridge_two_latitude, rf.foot_over_bridge_two_longitude = \
                str(foot_over_bridge_map_coordinate2).split(",")
            rf.foot_over_bridge_three_latitude, rf.foot_over_bridge_three_longitude = \
                str(foot_over_bridge_map_coordinate3).split(",")

        if rf.footpath == 'Two-Side':
            rf.width_side_one = width_side_one
            rf.width_side_two = width_side_two
        elif rf.footpath == 'One-Side':
            rf.width_side_one = width_side_one

        if rf.zebra_crossings == 'Yes':
            if str(zebra_map_coordinate) != "":
                rf.zebra_crossings_latitude, rf.zebra_crossings_longitude = str(zebra_map_coordinate).split(",")

        if on_street_vehicle_parking_pictures is not None:
            if rf.on_street_vehicle_parking == 'One-Side' and len(on_street_vehicle_parking_pictures) == 1:
                rf.street_side_one = on_street_vehicle_parking_pictures[0]
            elif rf.on_street_vehicle_parking == 'Both-Side' and len(on_street_vehicle_parking_pictures) == 2:
                rf.street_side_one = on_street_vehicle_parking_pictures[0]
                rf.street_side_two = on_street_vehicle_parking_pictures[1]

        rf.save()

        # Return a simple HttpResponse or render to a template
        if rf.viable_installation == 'NO':
            return redirect('roadway_far_from_school_submission')

    school_list = School.objects.all()
    # Render the form if GET request
    return render(request, 'roadway_near_school.html', {"data": school_list})


@csrf_exempt
def roadway_far_from_school_submission(request):
    if request.method == 'POST':
        # Collecting Roadway Information
        school_id = request.POST['schoolId']
        carriage_width = request.POST.get('carriage_width')
        carriage_way_direction = request.POST.get('carriage_way_direction')
        carriage_direction = request.POST.get('carriage_direction')
        partial_one_way = request.POST.get('partial_one_way')
        partial_two_way = request.POST.get('partial_two_way')
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
        elif footpath == 'Two-Side':
            width_side_one = request.POST.get('width_side_one')
            width_side_two = request.POST.get('width_side_two')

        # one_way_two_way = request.POST.get('one_way_two_way')

        pictures_near_side = request.FILES.get('pictures_near_side')
        pictures_far_side = request.FILES.get('pictures_far_side')
        # Collecting Traffic Control System Information
        traffic_lights = request.POST.get('traffic_lights')
        traffic_lights_working = request.POST.get('traffic_lights_working')
        num_traffic_lights = request.POST.get('num_traffic_lights')
        traffic_lights_pic1 = request.FILES.get('traffic_lights_pic1')
        traffic_lights_pic2 = request.FILES.get('traffic_lights_pic12')
        traffic_lights_pic3 = request.FILES.get('traffic_lights_pic3')
        # Zebra Crossings Information
        zebra_crossings = request.POST.get('zebra_crossings')
        num_zebra_crossings = request.POST.get('num_zebra_crossings')
        zebra_width = request.POST.get('zebra_width')
        zebra_map_coordinate = request.POST.get('zebraMapCoordinate')

        # Foot-over Bridge Information
        foot_over_bridge = request.POST.get('foot_over_bridge')
        num_foot_over_bridges = request.POST.get('num_foot_over_bridges')
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
        on_street_vehicle_parking_pictures = request.FILES.getlist('on_street_vehicle_parking_pictures')
        on_street_vehicle_parking_coordinate = request.POST.get('on_street_vehicle_parking_coordinate')

        # Viability to Install System
        viable_installation = request.POST.get('viable_installation')
        reason = request.POST.get('reason')

        # Handling uploaded files (pictures)

        # Do something with the data
        # For example, save it to the database, or process it further
        # This is just a sample response
        rf = RoadwayFacilityFar(
            school=School.objects.get(pk=school_id),
            carriage_width=carriage_width,
            carriage_way_direction=carriage_way_direction,
            carriage_direction=carriage_direction,
            divided=divided_undivided,
            intersection_type=intersection_type,
            number_of_lanes=num_lanes,
            central_marking=central_road_marking,

            footpath=footpath,

            pictures_near_side=pictures_near_side,
            pictures_far_side=pictures_far_side,

            traffic_lights=traffic_lights,
            traffic_lights_working=traffic_lights_working,
            num_traffic_lights=num_traffic_lights,
            traffic_lights_pictures=traffic_lights_pictures,

            zebra_crossings=zebra_crossings,
            num_zebra_crossings=num_zebra_crossings,
            zebra_width=zebra_width,

            foot_over_bridge=foot_over_bridge,
            num_foot_over_bridges=num_foot_over_bridges,
            foot_over_bridge_picture=foot_over_bridge_picture,

            power_source=power_source,
            power_source_picture=power_source_pictures,
            electric_poles_picture=electric_poles_picture,

            on_street_vehicle_parking=on_street_vehicle_parking,

            viable_installation=viable_installation,
            reason=reason
        )

        if rf.footpath == 'Two-Side':
            rf.width_side_one = width_side_one
            rf.width_side_two = width_side_two
        elif rf.footpath == 'One-Side':
            rf.width_side_one = width_side_one

        if rf.zebra_crossings == 'Yes':
            if str(zebra_map_coordinate) != "":
                rf.zebra_crossings_latitude, rf.zebra_crossings_longitude = str(zebra_map_coordinate).split(",")

        if on_street_vehicle_parking_pictures is not None:
            if rf.on_street_vehicle_parking == 'One-Side' and len(on_street_vehicle_parking_pictures) == 1:
                rf.street_side_one = on_street_vehicle_parking_pictures[0]
            elif rf.on_street_vehicle_parking == 'Both-Side' and len(on_street_vehicle_parking_pictures) == 2:
                rf.street_side_one = on_street_vehicle_parking_pictures[0]
                rf.street_side_two = on_street_vehicle_parking_pictures[1]

        rf.save()

        # Return a simple HttpResponse or render to a template
        return redirect('complete')

    school_list = School.objects.all()
    # Render the form if GET request
    return render(request, 'roadway_far_school.html', {"data": school_list})


def school_form_view(request):
    if request.method == 'POST':
        # Extract data from POST request
        school_name = request.POST.get('schoolName')
        school_type = request.POST.get('schoolType')
        ward = request.POST.get('ward')
        # entrance_image = request.FILES.get('entranceImage')
        multiple_entrances = request.POST.get('multipleEntrances') == 'yes'
        school_coordinates = request.POST.get('schoolCoordinates')
        bus_facility = request.POST.get('busFacility') == 'yes'
        bus_count = request.POST.get('busCount') or None
        bus_ownership = request.POST.get('busOwnership') or None
        owned_buses_count = request.POST.get('ownedBusesCount') or None
        hired_buses_count = request.POST.get('hiredBusesCount') or None
        bus_parking = request.POST.get('busParking') or None
        is_same_timing_all_year = len(request.POST.get('isSameTimingAllYear')) > 0
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

        s_latitude, s_longitude = str(school_coordinates).split(",")

        pick_location = request.POST.get('pickLocation') or None
        drop_location = request.POST.get('dropLocation') or None

        # Save the school object
        school = School(
            school_name=school_name,
            school_type=school_type,
            ward=ward,
            # entrance_image=entrance_image,
            multiple_entrances=multiple_entrances,
            school_coordinates_latitude=s_latitude,
            school_coordinates_longitude=s_longitude,
            bus_facility=bus_facility,
            bus_count=bus_count,
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
            gate_names = request.POST.get('gateName[]')
            is_entrance = request.POST.get('isExit[]')
            is_exit = request.POST.get('isEntrance[]')
            entrance_images = request.FILES.getlist('entranceImage[]')
            entrance_locations = request.POST.getlist('entranceLocation[]')
            for gateName, isEntrance, isExit, image, location in zip(gate_names, is_entrance, is_exit, entrance_images,
                                                                     entrance_locations):
                latitude, longitude = str(location).split(",")
                en_tx = EntranceExit()
                en_tx.school = school
                en_tx.gate_name = gateName
                en_tx.is_entrance = len(isEntrance) > 0
                en_tx.is_exit = len(isExit) > 0
                en_tx.image = image
                en_tx.latitude = latitude
                en_tx.longitude = longitude
                en_tx.save()

        return redirect('roadway_form_submission')

    return render(request, 'school_form.html')



def finalize_form_view(request):
    return render(request, 'finalization_form.html')

def complete(request):
    return render(request, 'success.html')
