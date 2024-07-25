from datetime import datetime, timedelta
import random
import pprint
from django.conf import settings

SEARCH_RESULTS=settings.SEARCH_RESULTS
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
    airline_logos={airline:settings.MEDIA_URL+airline+'.png' for idx,airline in enumerate(airlines)}
    # print(airline_logos)
    correct_conditional=random.choice(conditionals)
    ans["correct_conditional"]=correct_conditional

    incorrect_conditional=[condtion for condtion in conditionals if condtion!=correct_conditional]
    from_city,to_city=pick_cities(city_names)
    price=random.randint(200,2000)
    airline=random.choice(airlines)

    ans["from_city"],ans["to_city"],ans["price"],ans["airline"]=from_city,to_city,price,airline

    incorrect_airlines=[x for x in airlines if x !=airline]
    ans["results"]=[]
    if correct_conditional != "airline":
        task=f"Book a {correct_conditional} flight from {from_city} to {to_city} for {date_range}"
        ans["task"]=task
        if correct_conditional=="direct":
            correct_result=f"Flight from {from_city} to {to_city} with 0 layovers with {airline} at ${price} on {date_range}"
            ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":0,"airline":airline,"price":price,"from_date":from_date,"airline_logo":airline_logos[airline],
    "to_date":to_date,"correct_results":True})
        else:
            ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(1,3),"airline":airline,"price":price,"from_date":from_date,"airline_logo":airline_logos[airline],
    "to_date":to_date,"correct_results":True})
            correct_result=f"Flight from {from_city} to {to_city} with {random.randint(1,3)} layovers with {airline} at ${price} on {date_range} "

        incorrect_results=[]
        # selected_dates=date_range
        for index,i in enumerate(range(SEARCH_RESULTS-1)):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
            wrong_dates=False
            incorrect_airline=random.choice(airlines)


            if random.random()>0.75:
                # selected_dates=#date_range_wrong
                wrong_dates=True

            if correct_conditional=="direct":
                incorrect_results+=[(index+1,f"Flight from {from_city} to {to_city} with {random.randint(1,3)} layovers with {random.choice(airlines)} at ${price+random.randint(-50,500)} ")]
                ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(1,3),"airline":incorrect_airline,"price":price+random.randint(-5,500),"from_date":from_date_wrong if wrong_dates else from_date,
    "to_date":to_date_wrong if wrong_dates else to_date,"correct_results":False,'message':f"Flight booked was not a direct flight","airline_logo":airline_logos[incorrect_airline]})
            else:
                incorrect_results+=[(index+1,f"Flight from {from_city} to {to_city} with {random.randint(0,3)} layovers with {random.choice(airlines)} at ${price+random.randint(5,500)} on ")]
                ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(0,3),"airline":incorrect_airline,"price":price+random.randint(5,500),"from_date":from_date_wrong if wrong_dates else from_date,
    "to_date":to_date_wrong if wrong_dates else to_date,"correct_results":False,'message':f"Flight booked was not the cheapest option","airline_logo":airline_logos[incorrect_airline]})
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
        ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(1,3),"airline":airline,"price":price,"from_date":from_date,"airline_logo":airline_logos[airline],
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
            incorrect_airline=random.choice(incorrect_airlines)


            if random.random()>0.75:
                #selected_dates=##date_range_wrong
                wrong_dates=True

            incorrect_results+=[(index+1,f"Flight from {from_city} to {to_city} with {random.randint(0,3)} layovers with {random.choice(incorrect_airline)} at ${price+random.randint(-50,500)} on ")]
            ans["results"].append({"from_city":from_city,"to_city":to_city,"layovers":random.randint(0,3),"airline":incorrect_airline,"price":price+random.randint(-50,500),"from_date":from_date_wrong if wrong_dates else from_date,
    "to_date": to_date_wrong if wrong_dates else to_date,"correct_results":False,"message":f"Flight booked was not with the required airline","airline_logo":airline_logos[incorrect_airline]})
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
    
    hotels = [
    "Tranquil Stay",
    "Grandview Lodge",
    "Evergreen Suites",
    "Riverside Inn",
    "Skyline Retreat",
    "Regal Plaza",
    "Suncrest Hotel",
    "Sapphire Inn",
    "Horizon Haven",
    "Liberty Resort"
    ]
    hotels_snippets = {
    "Evergreen Suites": ["Discover the charm of coastal luxury at Evergreen Suites", "Nestled by the sea, our hotel offers a serene escape with lush gardens, elegant balconies, and rooms that open up to the soothing sounds of the waves.Experience the pinnacle of comfort and grace at Evergreen Suites, your tranquil haven under the sun."],
    "Grandview Lodge": ["Step into a world of timeless elegance at Grandview Lodge","Surrender to the allure of the sea at Grandview Lodge, your exclusive gateway to sun, sand, and serenity."],
    "Horizon Haven": ["Immerse yourself in the sleek sophistication of Horizon Haven","Our hotel, with its striking glass facade and lush balcony gardens, stands as a beacon of modernity in the heart of the city.At Horizon Haven, indulge in a stay that's as breathtaking as the skyline it adorns."],
    "Liberty Resort": ["Liberty Resort beckons you to a world where contemporary charm and classic elegance blend seamlessly","Welcome to Liberty Resort, where freedom and comfort reside in perfect harmony."],
    "Regal Plaza": ["Experience the epitome of luxury at Regal Plaza Hotel, where modern elegance meets unparalleled service.","Unforgettable stay with state-of-the-art amenities and exquisite dining options."],
    "Riverside Inn": ["Escape to the serene Riverside Inn, a sanctuary of peace and luxury.","Indulge in the ultimate relaxation experience by our pool or explore the vibrant local culture just steps away."],
    "Sapphire Inn": ["Step into Sapphire Inn, a gleaming gem in the city's crown, where every stay is infused with a touch of grandeur.","Revel in our sophisticated rooms that offer panoramic views and immerse yourself in the vibrant culture with our prime location near historical landmarks and bustling business centers."],
    "Skyline Retreat": ["Soar to new heights of luxury at Skyline Retreat","Our high-rise haven offers breathtaking panoramic views, a majestic entrance with a semi-circular glass canopy, and a lush lawn with a circular fountain, perfect for those seeking an urban escape."],
    "Suncrest Hotel": ["Nestled amidst verdant gardens and framed by the breathtaking spectacle of the setting sun","Experience the epitome of comfort and elegance at the Sunset Hotel, your tranquil haven for a rejuvenating getaway."],
    "Tranquil Stay": ["Discover the allure of Tranquil Stay, a beachfront paradise that epitomizes coastal elegance","At Tranquil Stay, every moment is a celebration of peace and luxury by the sea."],
}


    correct_conditional=random.choice(conditionals)
    ans["correct_conditional"]=correct_conditional

    incorrect_conditional=[condtion for condtion in conditionals if condtion!=correct_conditional]
    from_city,to_city=pick_cities(city_names)
    ans["from_city"]=from_city
    price=random.randint(200,1000)
    ans["price"]=price
    ratings=random.randint(1,5)
    ans["ratings"]=ratings
    ans["results"]=[]
    hotel=random.choice(hotels)
    hotel_image=settings.MEDIA_URL+'Hotels/'+hotel


    if correct_conditional != "rooms":
        task=f"Book a {correct_conditional} hotel in {from_city} for {date_range}"
        ans["task"]=task

        if correct_conditional=="highest rated":
            correct_result=f"Hotel in {from_city} at ${price} on {date_range}, Rating :5"
            ans["results"].append({'hotel_snippet_short':hotels_snippets[hotel][0],'hotel_snippet':hotels_snippets[hotel][1],"from_city":from_city,"price":price,"from_date":from_date,"to_date":to_date,"rating":5,"correct_results":True,'hotel':hotel,'hotel_image':hotel_image})
        else:
            correct_result=f"Hotel in {from_city} at ${price} on {date_range}, Rating :{random.randint(1,5)} "
            ans["results"].append({'hotel_snippet_short':hotels_snippets[hotel][0],'hotel_snippet':hotels_snippets[hotel][1],"from_city":from_city,"price":price,"from_date":from_date,"to_date":to_date,"rating": random.randint(1,5),"correct_results":True,'hotel':hotel,'hotel_image':hotel_image})

        incorrect_results=[]
        #selected_dates=date_range
        for i in range(SEARCH_RESULTS-1):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
            incorrect_hotel=random.choice(hotels)
            hotel_image=settings.MEDIA_URL+'Hotels/'+incorrect_hotel

            ##date_range_wrong = f"{from_date_wrong.strftime("%m-%d-%Y")} - {to_date_wrong.strftime("%m-%d-%Y")}"
            wrong_dates=False
            if random.random()>0.75:
                #selected_dates=##date_range_wrong
                wrong_dates=True

            if correct_conditional=="highest rated":
                incorrect_results+=[f"Hotel in {from_city} at ${price+random.randint(0,1000)} on , Rating :{random.randint(1,4)}"]
                ans["results"].append({'hotel_snippet_short':hotels_snippets[incorrect_hotel][0],'hotel_snippet':hotels_snippets[incorrect_hotel][1],"from_city":from_city,'hotel':incorrect_hotel,"price":price+random.randint(-50,500),"from_date":from_date_wrong if wrong_dates else from_date,"to_date":to_date_wrong if wrong_dates else to_date,"rating": random.randint(1,4),"correct_results":False,'message':f"Hotel booked was not the highest rated",'hotel_image':hotel_image})

            else:
                incorrect_results+=[f"Hotel in {from_city} at ${price+random.randint(5,1000)} on ,  Rating :{random.randint(1,5)}"]
                ans["results"].append({'hotel_snippet_short':hotels_snippets[incorrect_hotel][0],'hotel_snippet':hotels_snippets[incorrect_hotel][1],"from_city":from_city,'hotel':incorrect_hotel,"price":price+random.randint(5,500),"from_date":from_date_wrong if wrong_dates else from_date,"to_date":to_date_wrong if wrong_dates else to_date,"rating": random.randint(1,5),"correct_results":False,'message':f"Hotel booked was not the cheapest one",'hotel_image':hotel_image})

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
        ans["results"].append({'hotel_snippet_short':hotels_snippets[hotel][0],'hotel_snippet':hotels_snippets[hotel][1],'hotel_image':hotel_image,'hotel':hotel,"from_city":from_city,"price":price,"from_date":from_date,"to_date":to_date,"rating": random.randint(1,5),"no_of_rooms":random.randint(no_of_rooms,no_of_rooms+5),"correct_results":True})

        incorrect_results=[]
        for i in range(SEARCH_RESULTS-1):
            from_date_wrong= from_date + timedelta(weeks=random.randint(0, 4))
            to_date_wrong= from_date_wrong + timedelta(weeks=random.randint(1, 3))
            from_date_wrong=from_date_wrong
            to_date_wrong=to_date_wrong   
            incorrect_hotel=random.choice(hotels)
            hotel_image=settings.MEDIA_URL+'Hotels/'+incorrect_hotel

            ##date_range_wrong = f"{from_date_wrong.strftime("%m-%d-%Y")} - {to_date_wrong.strftime("%m-%d-%Y")}"
            wrong_dates=False
            if random.random()>0.75:
                #selected_dates=##date_range_wrong
                wrong_dates=True

            incorrect_results+=[f"Hotel in {from_city} at ${price+random.randint(0,1000)} ,  Avaiable Rooms :{random.randint(1,no_of_rooms-1)}"]
            ans["results"].append({'hotel_snippet_short':hotels_snippets[incorrect_hotel][0],'hotel_snippet':hotels_snippets[incorrect_hotel][1],'hotel_image':hotel_image,'hotel':incorrect_hotel,"from_city":from_city,"price":price+random.randint(-50,500),"rating": random.randint(1,5),"from_date":from_date_wrong if wrong_dates else from_date,"to_date": to_date_wrong if wrong_dates else to_date,"no_of_rooms":random.randint(1,no_of_rooms-1),"correct_results":False,'message':f"Hotel booked did not have the required number of rooms"})
    

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
    settings.configure()
    # pprint.pprint(flight_task())
    # file=open('../media/',"rb")
    # print(file)
    pprint.pprint(hotel_booking())
