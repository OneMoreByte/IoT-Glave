# window.py
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

from gi.repository import Gtk
from .gi_composites import GtkTemplate


@GtkTemplate(ui='/org/gnome/Iot-Thing/window.ui')
class IotThingWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'IotThingWindow'


    button1 = GtkTemplate.Child().Child();

    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()

    def on_button1_clicked(button, user_data):
        print("butttton1")

    def on_button2_clicked(button, user_data):
        print("button 222")

    def on_button3_clicked(button, user_data):
        print("button3 is here")
