#!/usr/bin/env python

with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<div id="circuit-background-cover">
		<div class="navigation-links">
			<h4 class="center">Apps</h4>
			<ul>
				<li><a href="ratfink"><img alt="Ratfink icon" class="small-icon" src="/assets/img/ratfink/icon.png"><span>Ratfink</span></a></li>
				<li><a href="music_home"><img alt="Music Home icon" class="small-icon" src="/assets/img/music_home/icon.png"><span>Music Home</span></a></li>
				<li><a href="charging_wear"><img alt="Charging Wear icon" class="small-icon" src="/assets/img/charging_wear/icon.png"><span>Charging Wear</span></a></li>
				<li><a href="prezcon"><img alt="Prezcon icon" class="small-icon" src="/assets/img/prezcon/icon.png"><span>Prezcon</span></a></li>
				<li><a href="wbc"><img alt="WBC icon" class="small-icon" src="/assets/img/wbc/icon.png"><span>WBC</span></a></li>
			</ul>
		</div>
	</div>
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("../templates/footer.html", "r") as footer:
	print footer.read()
