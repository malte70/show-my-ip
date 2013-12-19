show-my-ip
==========

A simple tool to display your IP address, both local (LAN) and global (Internet)

Requirements
------------

 * Python (tested with v2.7, although v3 should work)
 * Netifaces (http://alastairs-place.net/projects/netifaces/)

Usage
-----

*Note: At the moment, you need to run the Python module directly.*

Run show-my-ip by issuing the following command inside the source code's root directory:

    python2 -m show_my_ip.__init__

Display only the global IP:

    python2 -m show_my_ip.__init__ global

Display only all local IPs:

    python2 -m show_my_ip.__init__ global


