import bs4, requests
import webbrowser




def planTrip( start , dest , gdt , rdt , numad , numch , numin) :
	#input from user
	

	
		
	gdti = gdt[3:5]+gdt[0:2]+gdt[6: ]
	rdti = rdt[3:5]+rdt[0:2]+rdt[6: ]
		
	
	#setting urls for finding airport code
	strurl = "https://airportcodes.io/en/?s=" + start 
	dsturl ="https://airportcodes.io/en/?s=" + dest

	#getting airport code
	try :
		res = requests.get(strurl)
		res.raise_for_status()
		Soup = bs4.BeautifulSoup(res.text , features = "html.parser")
		myEl = Soup.select('h2')

		strid = str(myEl[0].getText()).strip()

		res1 = requests.get(dsturl)
		res1.raise_for_status()
		Soup1 = bs4.BeautifulSoup(res1.text , features = "html.parser")
		myEl1 = Soup1.select('h2')

		dstid = str(myEl1[0].getText()).strip()

		
		
		#opening make my trip for one way journey
		url = "https://www.makemytrip.com/flight/search?tripType=O&itinerary="+strid+"-" + dstid +"-"+ gdt + "&paxType=A-"+numad+"_C-"+numch+"_I-"+numin+"&cabinClass=E&sTime=1618128677992&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM"

		webbrowser.open(url)
	except :
		pass



	#alternative flight search
	afurl = "google.com/search?q=flights+from+"+start+"+to+"+dest+"+on+"+gdt
	webbrowser.open(afurl)

	#railway search
	rurl = "google.com/search?q=railways+from+"+start+"+to+"+dest+"+on+"+gdt
	webbrowser.open(rurl) 

	#bus search
	burl = "google.com/search?q=bus+from+"+start+"+to+"+dest+"+on+"+gdt
	webbrowser.open(burl)


	#searching holiday destinations
	turl = "google.com/search?q=popular+destinations+in+"+dest
	webbrowser.open(turl)


	try:
		#search for hotels
		hurl = "https://www.makemytrip.com/hotels/hotel-listing/?checkin="+gdti+"&city=CT"+dstid+"&checkout="+rdti+"&roomStayQualifier=2e0e&locusId=CT"+dstid+"&country=IN&locusType=city&searchText="+dest
		webbrowser.open(hurl)
	except:
		pass


	#searching for alternative hotels
	ahurl = "google.com/travel/hotels/"+dest
	webbrowser.open(ahurl)




	#searching for local transport
	lurl = "google.com/search?q=local+transport+in+"+dest
	webbrowser.open(lurl)




	#searching for food
	furl= "google.com/search?q=food+in+"+dest
	webbrowser.open(furl)


def planTravel( start , dest , gdt , numad , numch , numin):
	gdti = gdt[3:5]+gdt[0:2]+gdt[6: ]
	
	
	#setting urls for finding airport code
	strurl = "https://airportcodes.io/en/?s=" + start 
	dsturl ="https://airportcodes.io/en/?s=" + dest

	#getting airport code
	try :
		res = requests.get(strurl)
		res.raise_for_status()
		Soup = bs4.BeautifulSoup(res.text , features = "html.parser")
		myEl = Soup.select('h2')

		strid = str(myEl[0].getText()).strip()

		res1 = requests.get(dsturl)
		res1.raise_for_status()
		Soup1 = bs4.BeautifulSoup(res1.text , features = "html.parser")
		myEl1 = Soup1.select('h2')

		dstid = str(myEl1[0].getText()).strip()

		
		
		#opening make my trip for one way journey
		url = "https://www.makemytrip.com/flight/search?tripType=O&itinerary="+strid+"-" + dstid +"-"+ gdt + "&paxType=A-"+numad+"_C-"+numch+"_I-"+numin+"&cabinClass=E&sTime=1618128677992&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM"

		webbrowser.open(url)
	except :
		pass



	#alternative flight search
	afurl = "google.com/search?q=flights+from+"+start+"+to+"+dest+"+on+"+gdt
	webbrowser.open(afurl)

	#railway search
	rurl = "google.com/search?q=railways+from+"+start+"+to+"+dest+"+on+"+gdt
	webbrowser.open(rurl) 

	#bus search
	burl = "google.com/search?q=bus+from+"+start+"+to+"+dest+"+on+"+gdt
	webbrowser.open(burl)
