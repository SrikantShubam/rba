from ipaddress import ip_address
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from authen.models import data_collected

from .forms import SignUpForm
import time 
import datetime
from django.utils.timezone import make_aware
import requests
import ctypes
from time import gmtime, strftime
from datetime import date
def home(request):
    
        
        if request.user is not None:
            obj11=datetime.datetime.now()
            time_stamp=str(make_aware(obj11).hour)+"H"+str(make_aware(obj11).minute)+"M"
            # current_time = datetime.datetime.now()
            # print("asdasdasdasdsadasdsa",str(date.today()))
            uid=str(request.user)+"UID"+time_stamp

            total_start=time.time()
            #username start--------------------
            user_start=time.time()
            print("User: ", request.user)
            username=request.user
            # uid=username+"UID"+current_time

            # print("uidasdasdasdasdasd",uid)
            user_end=time.time()
            totaltime_user=user_end-user_start
    #username end-------------------------------------
            #lang----------------start-----------
            lang_start=time.time()
            lang=request.META['HTTP_ACCEPT_LANGUAGE']
            print(lang)
            lang_end=time.time()
            lang_totaltime=lang_end-lang_start
             #-------------lang end---------------
             #getting date and time ----------------------
            naive_datetime = datetime.datetime.now()
            naive_datetime.tzinfo  # None

            # settings.TIME_ZONE  # 'UTC'
            aware_datetime = make_aware(naive_datetime)
            aware_datetime.tzinfo  # <UTC>


            
            start_timezone = time.time()

            local_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
            print("Timezone of the user is --> ",local_timezone)
            # printing date and time 
            print("Date Time: ",aware_datetime)
            print('date time -----',naive_datetime.date())
            print('date time -----',naive_datetime.time())
            time_collected=naive_datetime.time()   #time collected 
            end_timezone = time.time()
            final_timezone=end_timezone-start_timezone
            print(final_timezone)

            #timezone done------------------------


             # getting ip-----------------------------------
            start_ip = time.time()
            # response = requests.get('https://api64.ipify.org?format=json').json()
            # ip_address = response["ip"]

            ip_address=print(request.META['REMOTE_ADDR'])

            print('the ip address-------',ip_address)
            end_ip = time.time()
            final_ip = print(end_ip-start_ip)
            #final ip=----------------



            #location start ----------------------
            # getting location from the ip 
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_start=time.time()
                # "ip": ip_address,
            city= response.get("city")
            region=response.get("region")
            country= response.get("country_name")
            location_end=time.time()
            location_totaltime=location_end-location_start
            #location end-------------------------


            #browser start----------------------------

            ua_starttime = time.time()

            browser_ua = request.user_agent.browser
            system_ua = request.user_agent.os
            ua_endtime = time.time()
            ua_totaltime = ua_endtime - ua_starttime

            print("ua----------- ",ua_totaltime)
            #browser end----------------------
            #screen size ---------------------------
            # screen_start=time.time()
            # user32 = ctypes.windll.user32
            # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            # screen_end=time.time()
            # screen_totaltime=screen_end-screen_start
            #screen size end ---------------------------



            #system fonts start ---------------------
            
            import os  #for windows
        
            systemfonts_start=time.time()
            from sys import platform
            sys_fonts=[]
            if platform == "win32":
                sys_font=os.listdir((r'C:\Windows\fonts'))
                sys_fonts=list(set(sys_font))
                print("system fonts are ",sys_fonts)
            elif platform =="macOS":
                import pycocoa #for mac
                manager = pycocoa.NSFontManager.sharedFontManager()
                font_families = list(manager.availableFontFamilies())
                print(font_families)
            
            else:
                print("system fonts are not available")

            systemfonts_final=time.time()
            fonts_totaltime=systemfonts_final-systemfonts_start

            #system fonts end ---------------------

            
            #browser fonts,canvas,webgl,plugins
            # import json
            # browser_fonts_start=time.time()
            # f=open(r"C:\Users\Srikant Shubham\Downloads\data.json")
            # plugins_start=time.time()
            # g=open(r"C:\Users\Srikant Shubham\Downloads\plugins.json")
            # h=open(r"C:\Users\Srikant Shubham\Downloads\canvas.json")
            # i=open(r"C:\Users\Srikant Shubham\Downloads\webgl.json")


            # browser_fonts = json.load(f)
            # browser_fonts_end=time.time()
            # browser_totaltime=browser_fonts_end-browser_fonts_start
            # plugins=json.load(g)
            # plugins_end=time.time()
            # plugins_totaltime=plugins_end-plugins_start
            # canvas_data=json.load(h)
            # canvas=canvas_data["canvas"]
            # canvas_totaltime=canvas_data["total_time"]
        
            
            # webgl_data=json.load(i)
            # webgl=webgl_data["webgl"]
            # webgl_totaltime=webgl_data["webgl_totaltime"]
            # print(plugins)
            # f.close()
            # g.close()
            # h.close()
            # i.close()
            # print(canvas,webgl)
            # os.remove(r'C:\Users\Srikant Shubham\Downloads\data.json')
            # os.remove(r'C:\Users\Srikant Shubham\Downloads\plugins.json')
            # os.remove(r"C:\Users\Srikant Shubham\Downloads\canvas.json")
            # os.remove(r"C:\Users\Srikant Shubham\Downloads\webgl.json")
           
            total_end=time.time()
            overall_totaltime=total_end-total_start
            data=data_collected(Uid=uid,userid=username,ip=ip_address,system_fonts=sys_fonts,language=lang,time_zone =local_timezone,date=naive_datetime.date(),time_collected=time_collected,city=city,region=region,country=country,browser_name=browser_ua.family, browser_version =browser_ua.version_string,os_family=system_ua.family,os_version=system_ua.version_string,ua_totaltime=ua_totaltime,ip_totaltime=final_ip,timezone_totaltime=final_timezone,location_totaltime=location_totaltime,system_fonts_totaltime=fonts_totaltime,lang_totaltime=lang_totaltime,overall_totaltime=overall_totaltime)
            data.save()

    
            return render(request, 'auth/home.html')




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})
