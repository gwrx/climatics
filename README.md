# CLIMATICS - A foolish approach to controlling weather

You take:
* A really, really cheap AC
* fix it! Of course it's broken
* grab a RaspberryPi, a coin acceptor, some sensors
* take this repository and fix it! Of course it's broken
* screw everthing to a wall and enjoy
  * eventualy you'd have to fix something else too...


## Main Purpose of this Repo

Our local [Hackerspace](https://it-syndikat.org) got an old AC and repaired it. Now, to prevent nasty discussions about the power bill, I thought it might be a cool idea to keep track of the power consumption of the AC and use an coin acceptor for this.

* insert a coin in the box and keep track of it
* report the credit to a more or less secure server to make shure it won't be lost on power failure
* measure the power consumption of the AC and calculate the cost to decrement the credit
* cut power to the AC if credit == 0
* on Thuesdays the Hackerspace will pay for power - this amount is to report annually
* keep track of the outside temperature, (eventually) cut power if it's colder outside
* keep track if the windows are closed
* keep track of the room temperature and report to server
* display useful information (e.g. temperatures, credit, etc.)


### Hardware used

* the cheapest AC to find (ours was free... yay!)
* a RaspberryPi 1st gen
* a coin acceptor (we are using NRI G40, reconfigured for Euros)
* an Arduino Mini as ADC
* an [amperemeter](https://www.aliexpress.com/item/1PCS-Analog-Current-Meter-Module-AC-0-5A-Ammeter-Sensor-Board-for-Arduino-NEW/32813352436.html)
* a [powersupply](https://www.aliexpress.com/item/1PCS-SANMIN-AC220V-to-DC24V-250MA-5W-Power-supply-Isolated-switching-power-supply-module-220V-to/32799017575.html) used to power the coin acceptor
* a [step-down converter](https://www.aliexpress.com/item/3pcs-5W-9V-12V-24V-to-5V-DC-DC-Step-Down-Buck-Converter-Module-replace-TO/32766296476.html) used to power the RaspberryPi and the Arduino
* a [TFT Display](https://www.aliexpress.com/item/3-0-inch-TFT-LCD-Touch-Screen-Module-240-x-400-SPI-RGB-Display-For-Raspberry/32713346673.html) to be a bit useful
* a [4x4 Keypad](https://www.aliexpress.com/item/Free-shipping-10PCS-LOT-4-4-Matrix-Array-Matrix-Keyboard-16-Key-Membrane-Switch-Keypad-for/1879700029.html) to be really useful
* some sort of box, some wires etc...
