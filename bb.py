import pytz
import datetime

time_zone = {'0': 'America/Thunder_Bay',
             '1': 'America/Tijuana',
             '2': 'America/Toronto',
             '3': 'America/Tortola',
             '4': 'America/Vancouver',
             '5': 'America/Virgin',
             '6': 'America/Whitehorse',
             '7': 'America/Winnipeg',
             '8': 'America/Yellowknife'}


print("Enter your choice:")

for place in time_zone:
    print("{}. {}".format(place, time_zone[place]))


while True:
    choice = input()
    if choice == 'quit':
        break

    if choice in time_zone.keys():
        zone_info = pytz.timezone(time_zone[choice])
        world_time = datetime.datetime.now(zone_info)
        local_time = datetime.datetime.utcnow()
        timezoneonly = world_time.strftime('%Z')
        print("the timezone of {} is {}".format(time_zone[choice],world_time))
        print("the local time is {}".format(local_time))
        print("the timezone is {}".format(timezoneonly))





