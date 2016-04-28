Django Google Analytics
=======================

Django template tag app for inserting google analytic code on a per
site basis.

Copyright (C) 2011 Benjamin Wilbur 

License
-------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


* This codes underlying structure is largely based off Django's
  documentation at the following url.  
  http://docs.djangoproject.com/en/dev/howto/custom-template-tags/

Installation
------------
1. `pip install django_google_analytics`
1. Ensure you have sites configured. https://docs.djangoproject.com/en/1.8/ref/contrib/sites/#enabling-the-sites-framework
1. add `analytics` to your `INSTALLED_APPS`
1. `python manage.py migrate`
1. In the django admin interface visit the "Sites"
   page and add your google web property id for the site you
   wish to track.
1. Add the following to your desired templates.
   `{% load analytics %}`
1. at the very bottom of your head section add this
   `{% analytics %}`
1. if you want to avoid counting logged in user visits
   surround the above line with the following
   `{% if not user.is_staff %}`
   `{% endif %}`
1. Go to your google analytics control panel and refresh
   frantically to see if it is working