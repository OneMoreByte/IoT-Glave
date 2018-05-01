# main.py
#
# Copyright 2018 Jack H
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi

from lifxlan import LifxLAN
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')


lan = LifxLAN()

lights = lan.get_lights()


class Handler:
    def close_window(self, aaa, bbb):
        quit()

    def on_button1_clicked(self, button):
        for a in lights:
            a.set_brightness(65535)

    def on_button2_clicked(self, button):
        for a in lights:
            a.set_brightness(30000)

    def on_button3_clicked(self, button):
        for a in lights:
            a.set_brightness(10000)

    def on_button4_clicked(self, button):
        for a in lights:
            state = a.get_power()
            print(state)
            if state == 0:
                a.set_power(65535)
            else:
                a.set_power(0)
                print("off")

    def on_button5_clicked(self, button):
        print("Previous frame")

    def on_button6_clicked(self, button):
        print("Next frame")


    def on_temp_value_change(self, value):
        temp = int(value.get_value())
        print(temp)
        for a in lights:
            a.set_colortemp(temp)



builder = Gtk.Builder()
builder.add_from_file("./lifxcontrol.glade")
builder.connect_signals(Handler())

window = builder.get_object("IotThingWindow")

window.show_all()
window.fullscreen()
print("GUI Started, {} lights found.".format(len(lights)))
Gtk.main()
