# Matthew Ragan | matthew.ragan@obscuradigital.com
# -----

# 8.19.15

# Simple and essential web functions to be called in various
# executes and buttomns throughout this network.

# -----

def openLink( URL ):
	
	import webbrowser
	
	webbrowser.open_new( URL )