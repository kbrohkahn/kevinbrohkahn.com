#!/usr/bin/env python

with open("templates/header.html", "r") as header:
	print header.read()
with open("templates/navbar.html", "r") as navbar:
	print navbar.read()

print('<link href="/assets/css/circuit-background.css" rel="stylesheet">')

print("""
<div id="circuit-background">
	<div id="circuit-background-cover">
		<div class="center navigation-links">
			<a href="/all-projects"><h4>Projects</h4></a>
			<ul>
				<li><a href="/projects/view-recipes"><img alt="View Recipes icon" class="small-icon" src="/assets/img/view-recipes/icon.png"><span>View Recipes</span></a></li>
				<li><a href="/projects/website"><img alt="This website icon" class="small-icon" src="/assets/img/kevinbrohkahn.com/icon.png"><span>This website</span></a></li>
			</ul>
		</div>
	</div>
</div>
""")

print('<script src="/assets/js/circuit-background-script.js" type="text/javascript"></script>')

with open("templates/footer.html", "r") as footer:
	print footer.read()