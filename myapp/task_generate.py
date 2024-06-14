from datetime import datetime, timedelta
import random
import pprint
SEARCH_RESULTS=5
ans={}
def pick_cities(city_names):
    from_city=random.choice(city_names)
    to_city=random.choice(city_names)
    while from_city==to_city:
        to_city=random.choice(city_names)
    return from_city,to_city

def flight_task():
# Define the variables

    today = datetime.today()
    from_date= today + timedelta(days=random.randint(0, 20))
    to_date= from_date + timedelta(days=random.randint(1, 15))
    ans["from_date"]=from_date
    ans["to_date"]=to_date
    ans["type"]="airline"
    date_range = f"{from_date.strftime('%m-%d-%Y')} - {to_date.strftime('%m-%d-%Y')}"
    city_names = ["Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
    conditionals=["direct","cheapest","airline"]
    airlines=["Unity Airways","BlueSky Jetlines","GlobalFlyer Express", "Horizon Wings"]

    correct_conditional=random.choice(conditionals)
    ans["correct_conditional"]=correct_conditional

    incorrect_conditional=[condtion for condtion in conditionals if condtion!=correct_conditional]
    from_city,to_city=pick_cities(city_names)
    price=random.randint(200,10000)
    airline=random.choice(airlines)

    ans["from_city"],ans["to_city"],ans["price"],ans["airline"]=from_city,to_city,price,airline

    incorrect_airline=[x for x in airlines if x !=airline]
    ans["results"]=[]
    if correct_conditional != "airline":
        task=f"Book a {correct_conditional} flight from {from_city} to {to_city} for {date_range}"
        ans["task"]=task
        if correct_conditional=="direct":
            correct_result=f"Flight from {from_city} to {to_city} with 0 layovers with {airline} at ${price} on {date_range}"
            ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":0,"airline":airline,"price":price,"from_date":from_date,
    "to_date":to_date,"correct_results":True})
        else:
            ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(1,3),"airline":airline,"price":price,"from_date":from_date,
    "to_date":to_date,"correct_results":True})
            correct_result=f"Flight from {from_city} to {to_city} with {random.randint(1,3)} layovers with {airline} at ${price} on {date_range} "

        incorrect_results=[]
        # selected_dates=date_range
        for index,i in enumerate(range(SEARCH_RESULTS-1)):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
            #date_range_wrong = f"{from_date_wrong.strftime("%m-%d-%Y")} - {to_date_wrong.strftime("%m-%d-%Y")}"
            wrong_dates=False

            if random.random()>0.75:
                # selected_dates=#date_range_wrong
                wrong_dates=True

            if correct_conditional=="direct":
                incorrect_results+=[(index+1,f"Flight from {from_city} to {to_city} with {random.randint(1,3)} layovers with {random.choice(airlines)} at ${price+random.randint(0,1000)} ")]
                ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(1,3),"airline":random.choice(airlines),"price":price+random.randint(0,1000),"from_date":from_date_wrong if wrong_dates else from_date,
    "to_date":to_date_wrong if wrong_dates else to_date,"correct_results":False,'message':f"Flight booked was not a direct flight"})
            else:
                incorrect_results+=[(index+1,f"Flight from {from_city} to {to_city} with {random.randint(0,3)} layovers with {random.choice(airlines)} at ${price+random.randint(5,1000)} on ")]
                ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(0,3),"airline":random.choice(airlines),"price":price+random.randint(5,1000),"from_date":from_date_wrong if wrong_dates else from_date,
    "to_date":to_date_wrong if wrong_dates else to_date,"correct_results":False,'message':f"Flight booked was not the cheapest option"})
        results=incorrect_results+[(0,correct_result)]
        ans["search_results"]=results
        # print(f"Results  : {results}")
        # print(f"ANS : {ans}")

        random.shuffle(results)
        return ans
    else:
        task=f"Book a flight from {from_city} to {to_city} for {date_range} with {airline}"
        ans["task"]=task

        correct_result=f"Flight from {from_city} to {to_city} with {random.randint(1,3)} layovers with {airline} at ${price} for {date_range}"
        ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(1,3),"airline":airline,"price":price,"from_date":from_date,
    "to_date": to_date,"correct_results":True})
        incorrect_results=[]
        #selected_dates=date_range
        for index,i in enumerate(range(SEARCH_RESULTS-1)):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
            ##date_range_wrong = f"{from_date_wrong.strftime("%m-%d-%Y")} - {to_date_wrong.strftime("%m-%d-%Y")}"
            wrong_dates=False

            if random.random()>0.75:
                #selected_dates=##date_range_wrong
                wrong_dates=True

            incorrect_results+=[(index+1,f"Flight from {from_city} to {to_city} with {random.randint(0,3)} layovers with {random.choice(incorrect_airline)} at ${price+random.randint(0,1000)} on ")]
            ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(0,3),"airline":random.choice(incorrect_airline),"price":price+random.randint(0,1000),"from_date":from_date_wrong if wrong_dates else from_date,
    "to_date": to_date_wrong if wrong_dates else to_date,"correct_results":False,"message":f"Flight booked was not with the required airline"})
        results=incorrect_results+[(0,correct_result)]
        ans["search_results"]=results

        # print(f"Results  : {results}")
        # pprint.pprint(f"ANS : {ans}")
        random.shuffle(results)

        return ans

def hotel_booking():
    # Define the variables
    today = datetime.today()
    from_date= today + timedelta(days=random.randint(0, 20))
    to_date= from_date + timedelta(days=random.randint(1, 15))
    ans["from_date"]=from_date
    ans["to_date"]=to_date
    ans["type"]="hotel"

    date_range = f"{from_date.strftime('%m-%d-%Y')} - {to_date.strftime('%m-%d-%Y')}"
    city_names = ["Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
    conditionals=["highest rated","cheapest","rooms"]
    
    #TODO
    hotels=["Unity Airways","BlueSky Jetlines","GlobalFlyer Express", "Horizon Wings"]
    snippets=[
    ("MetroView Suites", "Located in the heart of Manhattan, these boutique suites offer stunning views of the city skyline and easy access to iconic landmarks."),
    ("Harbor Heights Hotel", "Nestled in a historic building near the waterfront, this luxury hotel combines old-world charm with modern amenities, providing a serene retreat in bustling NYC."),
    ("Central Park Grand", "A lavish hotel overlooking Central Park, boasting elegant rooms, fine dining options, and impeccable service for a truly upscale experience."),
    ("Broadway Bliss Inn", "Situated near Times Square, this boutique hotel captures the excitement of Broadway with stylish accommodations and personalized service for theater enthusiasts."),
    ("Midtown Majesty", "With its prime location in Midtown Manhattan, this sleek and sophisticated hotel offers convenience, comfort, and contemporary elegance for business and leisure travelers alike."),
    ("Empire Elite Tower", "Rising high in the skyline, this iconic hotel offers breathtaking views of the Empire State Building and luxurious amenities for discerning guests seeking the ultimate NYC experience."),
    ("Greenwich Grand", "Tucked away in the historic Greenwich Village, this boutique hotel exudes charm and sophistication with its intimate atmosphere, stylish decor, and personalized service."),
    ("Soho Sanctuary Suites", "Located in the trendy Soho neighborhood, this chic hotel offers spacious suites, artistic flair, and easy access to galleries, boutiques, and dining hotspots."),
    ("Chelsea Chic Hotel", "Embodying the vibrant spirit of Chelsea, this boutique hotel features modern design, creative cuisine, and a lively atmosphere that reflects the neighborhood's artistic culture."),
    ("Financial District Haven", "Catering to both business and leisure travelers, this upscale hotel offers refined accommodations, state-of-the-art facilities, and attentive service for a productive and relaxing stay."),
    ("Lakefront Lodge", "Perched along the shores of Lake Michigan, this boutique hotel offers panoramic views of the lake and city skyline, along with luxurious amenities and personalized service."),
    ("Windy City Towers", "Rising high in the downtown skyline, this modern hotel exudes urban sophistication and offers easy access to renowned attractions, dining, and entertainment."),
    ("Magnificent Mile Manor", "Set amidst the upscale shops and boutiques of the Magnificent Mile, this boutique hotel provides an oasis of luxury and tranquility with its plush accommodations and upscale amenities."),
    ("Riverwalk Retreat", "Overlooking the Chicago River, this boutique hotel offers a serene escape from the bustling city, with stylish rooms, riverside dining, and breathtaking views."),
    ("Loop Luxury Suites", "Located in the vibrant Loop district, this chic hotel combines contemporary design with comfort and convenience, making it an ideal base for exploring all that Chicago has to offer."),
    ("Gold Coast Grand", "Nestled in the prestigious Gold Coast neighborhood, this elegant hotel offers opulent accommodations, world-class dining, and unparalleled service for an unforgettable experience."),
    ("Lincoln Park Lodge", "Surrounded by lush greenery and historic charm, this boutique hotel provides a tranquil retreat with easy access to the city's cultural attractions and outdoor activities."),
    ("West Loop Wharf", "Embracing the industrial-chic vibe of the West Loop, this boutique hotel offers stylish loft-style rooms, artisanal dining options, and a vibrant atmosphere that reflects the neighborhood's eclectic spirit."),
    ("South Side Serenity", "Located in the vibrant South Loop, this contemporary hotel offers modern comforts, skyline views, and proximity to museums, parks, and entertainment venues, making it an ideal choice for urban explorers."),
    ("Navy Pier Nook", "Situated near the iconic Navy Pier, this boutique hotel offers a blend of nautical charm and urban sophistication, with upscale amenities and waterfront views that capture the essence of the city's lakefront lifestyle."),
    ("Sunset Serenity Resort", "Nestled in the Hollywood Hills, this luxury resort offers a tranquil retreat with panoramic views of the city skyline and the iconic Hollywood sign."),
    ("Oceanfront Oasis", "Situated along the coast of Santa Monica, this boutique hotel captures the essence of coastal living with its breezy rooms, beachfront access, and laid-back luxury."),
    ("Beverly Hills Boutique", "Tucked away in the exclusive enclave of Beverly Hills, this intimate hotel offers personalized service, elegant accommodations, and a serene atmosphere for discerning travelers."),
    ("Downtown Dream Hotel", "Set in the heart of downtown LA, this stylish hotel embodies the energy and excitement of the city with its modern design, vibrant atmosphere, and convenient location."),
    ("Venice Vibes Resort", "Located steps away from Venice Beach, this hip hotel offers a relaxed beachside vibe with bohemian-chic decor, eclectic dining options, and easy access to iconic attractions."),
    ("Malibu Mirage", "Perched above the Pacific Coast Highway, this luxury hotel offers breathtaking views of the Malibu coastline, along with luxurious accommodations and personalized service for a truly memorable stay."),
    ("West Hollywood Hideaway", "Located in the heart of West Hollywood, this boutique hotel offers stylish rooms, rooftop poolside cabanas, and a lively atmosphere that embodies the neighborhood's glamorous and eclectic spirit."),
    ("Silver Lake Sanctuary", "Set amidst the trendy Silver Lake neighborhood, this boutique hotel offers a tranquil escape with modern comforts, scenic views, and proximity to hip cafes, boutiques, and galleries."),
    ("DTLA Dwellings", "Embracing the dynamic energy of downtown LA, this modern hotel offers sleek accommodations, rooftop dining, and panoramic city views, providing guests with an urban oasis in the heart of the city."),
    ("Pacific Palisades Paradise", "Nestled in the affluent enclave of Pacific Palisades, this luxury resort offers unparalleled ocean views, world-class amenities, and exclusive access to the coastal lifestyle, making it a haven for relaxation and rejuvenation."),
    ("Riverfront Retreat Hotel", "Overlooking the Connecticut River, this boutique hotel offers serene views and modern amenities, providing a peaceful escape in the heart of Hartford."),
    ("Capital City Comfort Inn", "Located downtown, this welcoming hotel combines convenience with comfort, making it an ideal choice for business travelers and tourists exploring the city."),
    ("Parkside Plaza Hotel", "Situated near Bushnell Park, this elegant hotel offers a tranquil oasis amidst the urban hustle, with spacious rooms and easy access to attractions."),
    ("Downtown Delight Hotel", "Embracing the vibrant energy of downtown, this chic hotel offers stylish accommodations, trendy dining options, and proximity to theaters, museums, and nightlife."),
    ("Hartford Haven Resort", "Nestled in a secluded spot just outside the city, this resort-style hotel offers a peaceful retreat with lush gardens, a pool, and luxurious amenities for a relaxing getaway."),
    ("Riverfront Regency", "With its prime location along the riverfront, this upscale hotel offers breathtaking views and luxurious accommodations, providing a serene escape from the city bustle."),
    ("Historic Hartford Hotel", "Housed in a restored historic building, this boutique hotel combines old-world charm with modern comforts, offering a unique glimpse into the area's rich heritage."),
    ("Cityscape Suites", "Rising high in the skyline, this contemporary hotel offers panoramic views of the city and spacious suites with all the comforts of home, perfect for extended stays or weekend getaways."),
    ("Capital Courtyard Inn", "Tucked away in a quiet corner of the city, this charming inn offers cozy accommodations and personalized service, providing a warm welcome to visitors."),
    ("Hartford Heights Resort", "Set atop a hill overlooking the city, this luxurious resort offers sweeping views and upscale amenities, including a spa, fitness center, and gourmet dining options, ensuring a memorable stay.")
]

    correct_conditional=random.choice(conditionals)
    ans["correct_conditional"]=correct_conditional

    incorrect_conditional=[condtion for condtion in conditionals if condtion!=correct_conditional]
    from_city,to_city=pick_cities(city_names)
    ans["from_city"]=from_city
    price=random.randint(200,10000)
    ans["price"]=price
    ratings=random.randint(1,5)
    ans["ratings"]=ratings
    ans["results"]=[]


    if correct_conditional != "rooms":
        task=f"Book a {correct_conditional} hotel in {from_city} for {date_range}"
        ans["task"]=task

        if correct_conditional=="highest rated":
            correct_result=f"Hotel in {from_city} at ${price} on {date_range}, Rating :5"
            ans["results"].append({"from_city":from_city,"price":price,"from_date":from_date,"to_date":to_date,"rating":5,"correct_results":True})
        else:
            correct_result=f"Hotel in {from_city} at ${price} on {date_range}, Rating :{random.randint(1,5)} "
            ans["results"].append({"from_city":from_city,"price":price,"from_date":from_date,"to_date":to_date,"rating": random.randint(1,5),"correct_results":True})

        incorrect_results=[]
        #selected_dates=date_range
        for i in range(SEARCH_RESULTS-1):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
 
            ##date_range_wrong = f"{from_date_wrong.strftime("%m-%d-%Y")} - {to_date_wrong.strftime("%m-%d-%Y")}"
            wrong_dates=False
            if random.random()>0.75:
                #selected_dates=##date_range_wrong
                wrong_dates=True

            if correct_conditional=="highest rated":
                incorrect_results+=[f"Hotel in {from_city} at ${price+random.randint(0,1000)} on , Rating :{random.randint(1,4)}"]
                ans["results"].append({"from_city":from_city,"price":price+random.randint(0,1000),"from_date":from_date_wrong if wrong_dates else from_date,"to_date":to_date_wrong if wrong_dates else to_date,"rating": random.randint(1,4),"correct_results":False,'message':f"Hotel booked was not the highest rated"})

            else:
                incorrect_results+=[f"Hotel in {from_city} at ${price+random.randint(5,1000)} on ,  Rating :{random.randint(1,5)}"]
                ans["results"].append({"from_city":from_city,"price":price+random.randint(5,1000),"from_date":from_date_wrong if wrong_dates else from_date,"to_date":to_date_wrong if wrong_dates else to_date,"rating": random.randint(1,5),"correct_results":False,'message':f"Hotel booked was not the cheapest one"})

        results=incorrect_results+[correct_result]
        # print(f"Results  : {results}")
        random.shuffle(results)
        return ans
    else:
        no_of_rooms=random.randint(3,6)
        ans["no_of_rooms"]=no_of_rooms
        task=f"Book {no_of_rooms} rooms at a hotel in {from_city} for {date_range}"
        ans["task"]=task

        correct_result=f"Hotel in {from_city} at ${price} , Avaiable Rooms :{random.randint(no_of_rooms,no_of_rooms+5)}"
        ans["results"].append({"from_city":from_city,"price":price,"from_date":from_date,"to_date":to_date,"no_of_rooms":random.randint(no_of_rooms,no_of_rooms+5),"correct_results":True})

        incorrect_results=[]
        for i in range(SEARCH_RESULTS-1):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
 
            ##date_range_wrong = f"{from_date_wrong.strftime("%m-%d-%Y")} - {to_date_wrong.strftime("%m-%d-%Y")}"
            wrong_dates=False
            if random.random()>0.75:
                #selected_dates=##date_range_wrong
                wrong_dates=True

            incorrect_results+=[f"Hotel in {from_city} at ${price+random.randint(0,1000)} ,  Avaiable Rooms :{random.randint(1,no_of_rooms-1)}"]
            ans["results"].append({"from_city":from_city,"price":price+random.randint(0,1000),"from_date":from_date_wrong if wrong_dates else from_date,"to_date": to_date_wrong if wrong_dates else to_date,"no_of_rooms":random.randint(1,no_of_rooms-1),"correct_results":False,'message':f"Hotel booked did not have the required number of rooms"})
    

        results=incorrect_results+[correct_result]
        # print(f"Results  : {results}")
        random.shuffle(results)

        return ans

def generate_task():
    all_tasks=[flight_task,hotel_booking]
    ans=random.choice(all_tasks)()
    # print(f"Task : {task}\n")
    # print(f"Search Results : {results}\n")
    return ans



if __name__=="__main__":

    pprint.pprint(flight_task())

    pprint.pprint(hotel_booking())
