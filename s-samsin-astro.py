#!/usr/bin/python3.5
import ephem
import os
import sys
from datetime import datetime
import simpleaudio.functionchecks as fc


class AIVoice:

    def __init__(self, topic, voice):
        self.folder_voice = "/voice/"
        os.system("mplayer " + self.folder_voice + str(topic) + "/" + str(voice) + ".wav")

    def sound_test(self):
        # Run sound check
        return fc.LeftRightCheck.run()


class Astronomy:

    def __init__(self,  lat, lon):
        # manually set the horizon that you want to use to one that is
        # exactly 34 arcminutes lower than the normal horizon,
        # to match the value by which the Navy reckons that an object at the horizon is refracted:
        self.city = ephem.Observer()
        self.city.pressure = 0
        self.city.horizon = '-0:34'

        # Location and Timezone.
        self.today = str(datetime.now())
        # only hour with leading zero
        self.hour = int(self.today[11:-13])
        # only minutes with leading zero
        self.minutes = str(self.today[14:-10])
        # hour and minutes with leading zero
        self.time = self.today[11:-10]

        self.city.lat, self.city.lon = lat, lon
        self.city.date = self.today

        # Sunrise/set settings
        self.next_sunrise = str(self.city.next_rising(ephem.Sun()))
        self.next_sunset = str(self.city.next_setting(ephem.Sun()))

    def cmd_check(self):
        print(self.next_sunrise)
        print(self.next_sunset)

    def clockwork(self):
        for i in range(25):
            # convert i with leading zero
            if str(i).zfill(2) == str(self.hour) and self.minutes == "00":
                AIVoice("time", "it-is")
                AIVoice("numbers", i)
                AIVoice("time", "o-clock")
                print('it is ' + str(i) + ' oclock')
                print(self.hour)

    def sun_present(self):

        # Check if the current time is the same as the sunrise/sunset
        if str(self.next_sunrise[10:-3]) == str(self.today[11:-10]):
            AIVoice("astro", "attention-the-sun-is-rising")
            print('Attention the sun is rising.')
        elif str(self.next_sunset[10:-3]) == str(self.today[11:-10]):
            AIVoice("astro", "attention-the-sun-is-setting")
            print('Attention the sun is setting.')

    def moon_present(self):
        moonrise_today = str(self.city.next_rising(ephem.Moon()))
        moonset_today = str(self.city.next_setting(ephem.Moon()))

        # Check if the current time is the same as the moonrise/moonset
        if str(moonrise_today[10:-3]) == str(self.today[11:-10]):
            AIVoice("astro", "attention-the-moon-is-rising")
            print('Attention, the moon is rising.')
        elif str(moonset_today[10:-3]) == str(self.today[11:-10]):
            AIVoice("astro", "attention-the-moon-is-setting")
            print('Attention, the moon is setting.')

# Rotterdam the Netherlands
Astro = Astronomy('51.9', '4.5')
# Print out data if the script is called from the command line
Astronomy.cmd_check(Astro)
# Activate what hour it is.
Astronomy.clockwork(Astro)
# Activate Sunrise and Sunset
Astronomy.sun_present(Astro)
Astronomy.moon_present(Astro)
# Exit Script
sys.exit()
