from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from garage_manager.views import local_log_car

''' COMMENT TO ALLOW LOCAL USE
from openalpr import Alpr
import openalpr
'''

import time

import sys

@csrf_exempt
def index(request):
    sys.stdout = open("/home/ubuntu/logs.txt", "a")
    print "Method is: ",request.method
    if request.method == "POST":
        return HttpResponse("ALPR not available Locally")
        ''' COMMENT TO ALLOW LOCAL USE
        start_time = time.time();
        print "start: ",  start_time
        try:
            alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
            alpr.set_top_n(20)

            print "Setup ALPR Succesfully"

            mid1_time = time.time();

            if 'image' not in request.FILES:
                print "image was not in files"
                alpr.unload()
                return 'Image parameter not provided'

            print "Going to Load Image"

            jpeg_bytes = request.FILES['image'].read()

            print "Loaded Image"

            if len(jpeg_bytes) <= 0:
                print "there are no bytes!"
                alpr.unload()
                return False

            mid2_time = time.time();

            print "Entering ALPR"

            results = alpr.recognize_array(jpeg_bytes)

            if results["results"]:
                plate = results['results'][0]['plate']
                print "Got result from ALPR"
                print "Plate Number:", plate
                gid = 2 # TODO: update for multiple garages
                response = local_log_car(plate, gid)
                if response:
                    print "Logging Car: ", response
                    r = "Plate Number: " + plate
                else:
                    r = "License Plate: " + plate + " not in database!"    
            else:
                print "no license plate detected"
                r = "False"

            end_time = time.time();

            print("total_time: " + str(end_time-start_time));
            #print("alpr_time: " + str(mid1_time-start_time));
            #print("jpeg_time: " + str(mid2_time-mid1_time));
            #print("processing_time: " + str(end_time-mid2_time));

            alpr.unload()
            print "Unloaded Data"

            print "Returning Results........................."
            return HttpResponse(r)

        except Exception, e:
            if alpr:
                alpr.unload()
            print e
            raise e
        '''
    else:
        return HttpResponse("Hello, world. You're at the alpr index.")

