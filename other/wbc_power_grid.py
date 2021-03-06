#!/usr/bin/env python
with open("../templates/header.html", "r") as header:
	print header.read()
with open("../templates/navbar.html", "r") as navbar:
	print navbar.read()

print("""
<div class="row">
	<div class="col-xxs-6 col-xxs-offset-3 col-xs-4 col-sm-3 col-md-2 col-lg-1">
		<img class="img-responsive" alt="kevin.broh-kahn.com Icon" src="/assets/img/power_grid/icon.png">
	</div>
	<div class="col-xxs-12 col-xs-8 col-sm-9 col-md-10 col-lg-11">
		<h1>WBC-Power Grid</h1>
		<div class="subheader">Information on Power Grid tournament at the World Boardgaming Championships.</div>
	</div>
	<div class="col-xs-12">
		<h4>Info</h4>
		<p>Power Grid will be played per the printed rules from Rio Grande Games. 2F's FAQ is located here: http://www.2f-spiele.de/spiele/faq/faq_frames_eng.htm</p>
		<p><b>Money should be hidden, but must be kept on table!</b></p>
		<h6>Setup</h6>
		<p>5-player games use five of the six board regions and 4-player use four of the six; these regions are selected by each player in player order (randomly determined). There is some bad wording in the rulebook and here is how it shall be handled: each player in turn order selects a region they want to be "in play"; you can select any region with the caveat that all regions must be contiguous when the last player selects.</p>
		<h6>Example</h6>
		<p>5-player game on the Italy board. P1 choose the brown boot section, P2 selects the Green northern region, and P3/P4/P5 must choose Yellow, Red, and Purple. This will help speed setup for some boards.</p>
		<p>We will use 5-player games by preference, resorting to 4-player games if necessary based on the number of players.</p?
		<h4>Maps</h4>
		<ul>
			<li>Heat 1: Benelux or Central Europe</li>
			<li>Heat 2: UK & Ireland or Northern Europe</li>
			<li>Heat 3: France or Italy</li>
			<li>Semifinal: Brazil</li>
			<li>Final: Russia</li>
		</ul>
		<em>If there are not enough maps in any of the heats, games will be played on the default US map</em>
		<h4>Tournament format</h4>
		<p>HMWG. Up to 36 players will advance to the semifinal. Rankings determined by:
		<ol type="A">
			<li>Most Wins</li>
			<li>Win in first heat entered</li>
			<li>Win in second heat entered</li>
			<li>Win in third heat entered</li>
			<li>Based on points earned</li>
			<li>Margin of victory (or defeat if between two 2nd places)</li>
		</ol>
		<h4>Points</h4>
		<h6>5-player game (default)</h6>
		<ol>
			<li>10 Points</li>
			<li>4 Points</li>
			<li>2 Points</li>
			<li>1 Point</li>
			<li>0 Points</li>
		</ol>
		<h6>4-player game (if necessary)</h6>
		<ol>
			<li>10 Points</li>
			<li>4 Points</li>
			<li>1 Point</li>
			<li>0 Points</li>
		</ol>
		<em>Points are heavily weighted to first place, so much that a win is worth two and a half times as many points as second place.</em>
		<h4>Game Ending</h4>
		<b>Winner: Supply electricity to the most cities the final round</b>
		<h6>Tie breakers</h6>
		<ol>
			<li>Most money</li>
			<li>Most cities</li>
			<li>Highest power plant number (added by GM)</li>
		</ol>
		<p>Event Sheet: In order for a game to count an event form must be accurately completed recording ALL pertinent info and submitted promptly to the GM. <b>Winners are responsible for seeing that this is accomplished.</b> Event form(s) will be handed out by the GM before play begins.</p>
	</div>
</div>
""")

with open("../templates/footer.html", "r") as footer:
	print footer.read()
