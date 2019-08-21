import datetime
import json
import os

# Level of martial arts experience list
exp_list = ['Novice < 1 year training',
            'Intermediate 1-2 years training', 
            'Advanced 2-4 years training', 
            'BlackBelt 4+ years training', 
            'Null']

# Event List
event_list = ['Kata, Forms, Patterns (K)',
                'Demo/Showmanship (DS)',
                'Point Sparring (PS)',
                'Continous Sparring (CS)',
                'Traditional Weapons (W)',
                'Kyokushin Sparring Contact (KSC)',
                'Kyokushin Kata/Forms (KF)',
                'Kata-Beginners (KB)',
                'Sumo (S)',
                'Fastest Kick (A)',
                'Self Defence (SD)',
                'Sword Fighting (SF)']

# Division List
k_list = ['K1, 5 Yrs and under males/females',
            'K2, 6-7 Yrs male/female, Open', 
            'K3, 8-9 Yrs male/female, Open', 
            'K4, 10-11 Yrs female, Open',
            'K5, 10-11 Yrs male, Open', 
            'K6, 12-13 Yrs female, Open', 
            'K7, 12-13 Yrs male, Open', 
            'K8, 14-15 Yrs female, Open', 
            'K9, 14-15 Yrs male, Open', 
            'K10, 16-17 Yrs male, Open', 
            'K11, 16-17 Yrs male, Open', 
            'K12, 18-39 Yrs female, Open', 
            'K13, 18-39 Yrs male, Open', 
            'K14, 40 Yrs +Over female, Open', 
            'K15, 40 Yrs +Over male, Open',
            'Null']

ds_list = ['DS1, 11 Yrs & under male/female',
            'DS2, 12-17 Yrs male/female',
            'DS3, 18 Yrs+ male/female, Open', 
            'Null']

ps_list = ['PS1, 5 Yrs & under male/female, Open',
            'PS2, 6-7 Yrs male/female, Open',
            'PS3, 8-9 Yrs male/female, Open', 
            'PS4, 10-11 Yrs female, Open',
            'PS5, 10-11 Yrs male, Open',
            'PS6, 12-13 Yrs female, Nov/Int', 
            'PS7, 12-13 Yrs male, Nov/Int',
            'PS8, 12-13 Yrs female Adv/Black Belt',
            'PS9, 12-13 Yrs male Adv/Black Belt', 
            'PS10, 14-15 Yrs female, Nov/Int',
            'PS11, 14-15 Yrs male, Nov/int',
            'PS12, 14-15 Yrs female, Adv/Black Belt', 
            'PS13, 14-15 Yrs male, Adv/Black Belt',
            'PS14, 16-17 Yrs female, Nov/Int',
            'PS15, 16-17 Yrs male, Nov/Int', 
            'PS16, 16-17 Yrs female, Adv/Black Belt',
            'PS17, 16-17 Yrs male, Adv/Black Belt',
            'PS18, 18-39 Yrs female, Nov/Int', 
            'PS19, 18-39 Yrs male, Nov/int',
            'PS20, 18-39 Yrs female, Adv/Black Belt', 
            'PS21, 18-39 Yrs male, Adv/Black Belt',
            'PS22, 40 Yrs +Over female, Open',
            'PS23, 40 Yrs +Over male, Open', 
            'Null']

cs_list = ['CS1, 6-7 Yrs male/female, Open',
            'CS2, 8-9 Yrs male/female, Open',
            'CS3, 10-11 Yrs female, Open', 
            'CS4, 10-11 Yrs male, Open',
            'CS5, 12-13 Yrs female, Open',
            'CS6, 12-13 Yrs male, Open', 
            'CS7, 14-15 Yrs female, Open',
            'CS8, 14-15 Yrs male, Open',
            'CS9, 16-17 Yrs female, Open', 
            'CS10, 16-17 Yrs male, Open',
            'CS11, 18-39 Yrs female, Open',
            'CS12, 18-39 Yrs male, Open', 
            'CS13, 40 Yrs +Over female, Open',
            'CS14, 40 Yrs +Over male, Open',
            'Null']

w_list = ['W1, 13 Yrs & under male/female, Open',
            'W2, 14-17 Yrs male/female, Open',
            'W3, 18 Yrs & Over male/female, Open', 
            'Null']

ksc_list = ['KSC1, 5 Yrs & under male/female',
            'KSC2, 6-7 Yrs male/female',
            'KSC3, 8-9 Yrs male', 
            'KSC4, 8-9 Yrs female',
            'KSC5, 10-11 Yrs male',
            'KSC6, 10-11 Yrs female', 
            'KSC7, 12-13 Yrs male',
            'KSC8, 12-13 Yrs female',
            'KSC9, 14-15 Yrs male', 
            'KSC10, 14-15 Yrs female',
            'KSC11, 16-17 Yrs male',
            'KSC12, 16-17 Yrs female', 
            'KSC13, 18yrs+ Female -55kg Novice',
            'KSC14, 18yrs+ Female 55.1-65kg Novice',
            'KSC15, 18yrs+ Female Over 65kg Novice', 
            'KSC16, 18yrs+ Female Under 55kg Open',
            'KSC17, 18yrs+ Female 55.l-65kg Open',
            'KSC18, 18yrs+ Female Over 65kg Open', 
            'KSC19, 18yrs+ Male under 70kg Novice',
            'KSC20, 18yrs+ Male 70.l-80kg Novice', 
            'KSC21, 18yrs+ Male Over 80kg Novice',
            'KSC22, 18yrs+ Male under 70kg Open',
            'KSC23, 18yrs+ Male 70.1-80kg Open', 
            'KSC24, 18yrs+ Male Over 80kg Open',
            'KSC25, Over 40yrs Veterans Female',
            'KSC26, Over 40yrs Veterans Male', 
            'Null']

kf_list = ['KF1, 7 Yrs and under male/female',
            'KF2, 8-10 Yrs male/female',
            'KF3, 11-13 Yrs male/female', 
            'KF4, 14-16 Yrs male/female',
            'KF5, 17yrs+ male 7 kyu & under',
            'KF6, 17yrs+ female 7 kyu & under', 
            'KF7, 17yrs+ male 6-3rd kyu',
            'KF8, 17yrs+ female 6-3rd kyu',
            'KF9, 17yrs+ male 2nd kyu +', 
            'KF10, 17yrs+ female 2nd kyu +', 
            'Null']

kb_list = ['KB1, 9 Yrs & under male/female',
            'KB2, 10-14 Yrs male/female',
            'KB3, 15-17 Yrs male/female', 
            'Null']

s_list = ['S1, 5 Yrs and under males/females',
            'S2, Mixed males/females, open',
            'Null']

a_list = ['A1, 5 Yrs and under males/females',
            'A2, 6-17 Yrs males/females, Open',
            'Null']

sd_list = ['SD1, Under 18 Yrs males/females',
            'SD2, Over 18 Yrs males/females',
            'Null']

sf_list = ['SF1, 5 Yrs and under males/females',
            'SF2, Mixed males/females, open',
            'Null']

def get_division(input):
    """Returns division list based on input"""

    options = {'K': k_list,
        'DS': ds_list,
        'PS': ps_list,
        'CS': cs_list,
        'W': w_list,
        'KSC': ksc_list,
        'KF': kf_list,
        'KB': kb_list,
        'S': s_list,
        'A': a_list,
        'SD': sd_list,
        'SF': sf_list
    }
    return options[input]

def score_based_off_placement(input):
    """Returns a score integer based on placement (1st, 2nd, 3rd etc)"""

    options = {
        1: 20,
        2: 15,
        3: 10,
        '>=4': 5,
    }
    return options[input]

def assign_birthday():
    """Returns a list containing day, month and year of birthday"""

    birthday = input("Birthday: ")
    if "-" in birthday: return birthday.split("-")
    elif "/" in birthday: return birthday.split("/")
    elif "\\" in birthday: return birthday.split("\\")
    else: 
        print("Error in birthday string, please try again")
        assign_birthday()

def gender_conversion(number):
    """Converts integer to gender string"""

    if number == 1: return 'male'
    elif number == 2: return 'female'
    else: return None

def event_conversion(input):
    """Convert empty event input to Null"""

    if input == "Select Division" or input == "Null": return None
    else: return input

def level_conversion(input):
    """Convert empty level input to Null"""

    if "Select" in input: return None
    else: return input

def empty_conversion(input):
    """Convert empty input to Null"""

    if input == "": return None
    else: return input

def assign_placement(input):
    """Convert empty placement input to N/A"""

    if input == "Select Division" or input == "Null": return None
    else: return "N/A"

def assign_points(input):
    """Convert empty points input to 0"""

    if input == "Select Division" or input == "Null": return None
    else: return 0

def get_json_file():
    """Retrieves competitor.json file for modification"""

    cur_dir = os.getcwd()
    if cur_dir.split("\\")[-1] == 'MartialArtsTournament': return 'competitor.json'
    else: print("Cannot find competitor.json")

def get_age(birthday, age):
    """Return the age as a integer."""

    today_date = datetime.date(2019, 8, 11)
    if "/" in birthday: 
        bday = birthday.split('/')
        dob = datetime.date(int(bday[2]), int(bday[1]), int(bday[0]))
        age_in_days = (today_date - dob).days
        age_in_years = age_in_days / 365

        if age == "": return int(age_in_years)
        elif age != "" and int(age) != int(age_in_years): return str(age + " UNRESOLVED")
        else: return int(age)

def get_list_of_competitors():
    """Retreives a list of all competitor's full names"""

    with open(get_json_file()) as json_file:
        data = json.load(json_file)
        num = len(data['competitors'])
        competitor_list = [None] * num
        count = 0
        for competitors in data['competitors']:
            competitor_list[count] = competitors['full name']
            count += 1
    
    competitor_list.sort()
    return competitor_list

def get_list_of_absent_competitors():
    """Retreives a list of all competitor who are absent"""

    with open(get_json_file()) as json_file:
        data = json.load(json_file)
        # num = len(data['competitors'])
        competitor_list = []
        count = 0
        for competitors in data['competitors']:
            if competitors['attendance'] == False:
                competitor_list.append(f"{competitors['last name']}, {competitors['first name']}")
                count += 1

    competitor_list.sort()
    return competitor_list

def get_list_of_present_competitors():
    """Retreives a list of all competitor who are present"""

    with open(get_json_file()) as json_file:
        data = json.load(json_file)
        # num = len(data['competitors'])
        competitor_list = []
        count = 0
        for competitors in data['competitors']:
            if competitors['attendance'] == True:
                competitor_list.append(f"{competitors['last name']}, {competitors['first name']}")
                count += 1

    competitor_list.sort()
    return competitor_list

def get_selected_details(person_of_interest):
    """Retreives all details of competitor as a dictionary"""
    
    with open(get_json_file()) as json_file:
        data = json.load(json_file)
        for competitor in data['competitors']:
            if competitor['full name'] == person_of_interest:
                person = [None] * 18
                person[0] = competitor['first name']
                person[1] = competitor['last name']
                person[2] = competitor['full name']
                person[3] = competitor['club name']
                person[4] = competitor['D.O.B']
                person[5] = competitor['age']
                person[6] = competitor['weight']
                person[7] = competitor['gender']
                person[8] = competitor['address']
                person[9] = competitor['suburb']
                person[10] = competitor['post code']
                person[11] = competitor['full address']
                person[12] = competitor['contact number']
                person[13] = competitor['email']
                person[14] = competitor['belt']
                person[15] = competitor['martial arts level']
                person[16] = competitor['martial arts level full']

                event = [None] * 12
                event[0] = competitor['events'][0]['K']
                event[1] = competitor['events'][0]['DS']
                event[2] = competitor['events'][0]['PS']
                event[3] = competitor['events'][0]['CS']
                event[4] = competitor['events'][0]['W']
                event[5] = competitor['events'][0]['KSC']
                event[6] = competitor['events'][0]['KF']
                event[7] = competitor['events'][0]['KB']
                event[8] = competitor['events'][0]['S']
                event[9] = competitor['events'][0]['A']
                event[10] = competitor['events'][0]['SD']
                event[11] = competitor['events'][0]['SF']
                person[17] = event
    
    return person

def convert_to_full(input):
    last_name = input.split(',')[0]
    first_name = (input.split(',')[-1]).lstrip()
    return f"{first_name} {last_name}"

def set_attendance_val(person_of_interest, bool_val):
    full_name = convert_to_full(person_of_interest)
    with open(get_json_file(), 'r+') as json_file:
        data = json.load(json_file)
        for competitor in data['competitors']:
            if competitor['full name'] == full_name:
                competitor['attendance'] = bool_val
    
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()

def add_competitor(first_name, last_name, club_name, dob, age, weight, gender,
                    address, suburb, post_code, number, email, malvl, belt,
                    k, ds, ps, cs, w, ksc, kf, kb, s, a, sd, sf):

    """Add Competitor details to competitor.json"""
    
    print("===> Adding Competitor")

    json_file = get_json_file()
    new_c = {}
    new_c['first name'] = first_name
    new_c['last name'] = last_name
    new_c['full name'] = f"{first_name} {last_name}"
    new_c['club name'] = empty_conversion(club_name)
    new_c['D.O.B'] = empty_conversion(dob)
    new_c['age'] = get_age(dob, age)
    new_c['weight'] = empty_conversion(weight)
    new_c['gender'] = gender_conversion(gender)

    new_c['address'] = address
    new_c['suburb'] = suburb
    new_c['post code'] = post_code
    new_c['full address'] = f"{address}, {suburb} {post_code}"
    new_c['contact number'] = number
    new_c['email'] = empty_conversion(email)
    new_c['belt'] = empty_conversion(belt)
    new_c['martial arts level'] = level_conversion(malvl.split(" ")[0])
    new_c['martial arts level full'] = level_conversion(malvl)
    
    event_c = {}
    event_c['K'] = event_conversion(k)
    event_c['K placement'] = assign_placement(k)
    event_c['K score'] = assign_points(k)

    event_c['DS'] = event_conversion(ds)
    event_c['DS placement'] = assign_placement(ds)
    event_c['DS score'] = assign_points(ds)

    event_c['PS'] = event_conversion(ps)
    event_c['PS placement'] = assign_placement(ps)
    event_c['PS score'] = assign_points(ps)

    event_c['CS'] = event_conversion(cs)
    event_c['CS placement'] = assign_placement(cs)
    event_c['CS score'] = assign_points(cs)

    event_c['W'] = event_conversion(w)
    event_c['W placement'] = assign_placement(w)
    event_c['W score'] = assign_points(w)

    event_c['KSC'] = event_conversion(ksc)
    event_c['KSC placement'] = assign_placement(ksc)
    event_c['KSC score'] = assign_points(ksc)

    event_c['KF'] = event_conversion(kf)
    event_c['KF placement'] = assign_placement(kf)
    event_c['KF score'] = assign_points(kf)

    event_c['KB'] = event_conversion(kb)
    event_c['KB placement'] = assign_placement(kb)
    event_c['KB score'] = assign_points(kb)

    event_c['S'] = event_conversion(s)  
    event_c['S placement'] = assign_placement(s) 
    event_c['S score'] = assign_points(s)

    event_c['A'] = event_conversion(a)
    event_c['A placement'] = assign_placement(a)
    event_c['A score'] = assign_points(a)

    event_c['SD'] = event_conversion(sd)
    event_c['SD placement'] = assign_placement(sd)
    event_c['SD score'] = assign_points(sd)

    event_c['SF'] = event_conversion(sf)
    event_c['SF placement'] = assign_placement(sf)
    event_c['SF score'] = assign_points(sf)

    new_c['events'] = [event_c]

    new_c['attendance'] = False
    new_c['score'] = 0

    with open(json_file, 'r') as read_file:
        data = json.load(read_file)
        read_file.close()

    data['competitors'].append(new_c)

    with open(json_file, 'w') as write_file:
        json.dump(data, write_file, indent=4)
        write_file.close()

    print("===> Registration Complete")

def mod_competitor(lookup_name, first_name, last_name, club_name, dob, age, weight, gender,
                    address, suburb, post_code, number, email, malvl, belt,
                    k, ds, ps, cs, w, ksc, kf, kb, s, a, sd, sf):
                    
    """Modify Competitors Details"""

    print("===> Modifying Competitor")
    json_file = get_json_file()
    with open(json_file, 'r+') as current_file:
        data = json.load(current_file)
        for competitor in data['competitors']:
            if competitor['full name'] == lookup_name:
                # competitor['full name'] = "test"

                competitor['first name'] = first_name
                competitor['last name'] = last_name
                competitor['full name'] = f"{first_name} {last_name}"
                competitor['club name'] = empty_conversion(club_name)
                competitor['D.O.B'] = empty_conversion(dob)
                competitor['age'] = get_age(dob, age)
                competitor['weight'] = empty_conversion(weight)
                competitor['gender'] = gender_conversion(gender)

                competitor['address'] = address
                competitor['suburb'] = suburb
                competitor['post code'] = post_code
                competitor['full address'] = f"{address}, {suburb} {post_code}"
                competitor['contact number'] = number
                competitor['email'] = empty_conversion(email)
                competitor['belt'] = empty_conversion(belt)
                competitor['martial arts level'] = level_conversion(malvl.split(" ")[0])
                competitor['martial arts level full'] = level_conversion(malvl)

                # competitor['events'][0]['K'] = "test"
                competitor['events'][0]['K'] = event_conversion(k)
                competitor['events'][0]['K placement'] = assign_placement(k)
                competitor['events'][0]['K score'] = assign_points(k)

                competitor['events'][0]['DS'] = event_conversion(ds)
                competitor['events'][0]['DS placement'] = assign_placement(ds)
                competitor['events'][0]['DS score'] = assign_points(ds)

                competitor['events'][0]['PS'] = event_conversion(ps)
                competitor['events'][0]['PS placement'] = assign_placement(ps)
                competitor['events'][0]['PS score'] = assign_points(ps)

                competitor['events'][0]['CS'] = event_conversion(cs)
                competitor['events'][0]['CS placement'] = assign_placement(cs)
                competitor['events'][0]['CS score'] = assign_points(cs)

                competitor['events'][0]['W'] = event_conversion(w)
                competitor['events'][0]['W placement'] = assign_placement(w)
                competitor['events'][0]['W score'] = assign_points(w)

                competitor['events'][0]['KSC'] = event_conversion(ksc)
                competitor['events'][0]['KSC placement'] = assign_placement(ksc)
                competitor['events'][0]['KSC score'] = assign_points(ksc)

                competitor['events'][0]['KF'] = event_conversion(kf)
                competitor['events'][0]['KF placement'] = assign_placement(kf)
                competitor['events'][0]['KF score'] = assign_points(kf)

                competitor['events'][0]['KB'] = event_conversion(kb)
                competitor['events'][0]['KB placement'] = assign_placement(kb)
                competitor['events'][0]['KB score'] = assign_points(kb)

                competitor['events'][0]['S'] = event_conversion(s)  
                competitor['events'][0]['S placement'] = assign_placement(s)
                competitor['events'][0]['S score'] = assign_points(s)

                competitor['events'][0]['A'] = event_conversion(a)
                competitor['events'][0]['A placement'] = assign_placement(a)
                competitor['events'][0]['A score'] = assign_points(a)

                competitor['events'][0]['SD'] = event_conversion(sd)
                competitor['events'][0]['SD placement'] = assign_placement(sd)
                competitor['events'][0]['SD score'] = assign_points(sd)

                competitor['events'][0]['SF'] = event_conversion(sf)
                competitor['events'][0]['SF placement'] = assign_placement(sf)
                competitor['events'][0]['SF score'] = assign_points(sf)
                            
                current_file.seek(0)
                json.dump(data, current_file, indent=4)
                current_file.truncate()
                print("===> Modification Complete")

def get_list_of_competitors_from_event_division(event_name, division_name):
    """Retreives a list of all competitor in specific event and divison"""
    
    event_str = event_name.split('(')[-1].split(')')[0]
    with open(get_json_file()) as json_file:
        data = json.load(json_file)
        competitor_list = []
        for competitors in data['competitors']:
            if competitors['attendance'] == True:
                for event in competitors['events']:
                    if event[event_str] != None and event[event_str] == division_name:
                        # print(competitors['full name'] + event[event_str + ' placement'])
                        competitor_list.append([competitors['full name'], event[event_str + ' placement'], event[event_str + ' score']])

    competitor_list.sort()
    return competitor_list

def score_placement_entry(full_name, placement, event, division):
    """Assign placement and scores to competitor"""

    if full_name != 'null':
        event_convert = event.split('(')[-1].split(')')[0]

        with open(get_json_file(), 'r+') as json_file:
            data = json.load(json_file)
            for comp in data['competitors']:
                if comp['full name'] == full_name:
                    for eve in comp['events'][0]:
                        if eve == event_convert and comp['events'][0][event_convert] == division:
                            comp['events'][0][event_convert + " placement"] = placement
                            comp['events'][0][event_convert + " score"] = score_based_off_placement(placement)

            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()

def score_convert(input):
    """Convert null scores to 0"""

    if input == None: return 0
    else: return input

def get_club_list():
    """Generate a list of all unique clubs"""

    club_list = []
    with open(get_json_file(), 'r+') as current_file:
        data = json.load(current_file)
        for comp in data['competitors']:
            club_list.append(comp['club name'])

    unique_list = []
    for x in club_list:
        if x not in unique_list:
            unique_list.append(x)

    final_list = []
    for y in unique_list:
        final_list.append([y, 0])

    return final_list

def get_total_score_competitor(full_name):
    """Retrieves total points accumulated by a competitor"""

    with open(get_json_file(), 'r+') as current_file:
        data = json.load(current_file)
        for comp in data['competitors']:
            if comp['full name'] == full_name:
                event_array = [score_convert(comp['events'][0]['K score']),
                                score_convert(comp['events'][0]['DS score']),
                                score_convert(comp['events'][0]['PS score']),
                                score_convert(comp['events'][0]['CS score']),
                                score_convert(comp['events'][0]['W score']),
                                score_convert(comp['events'][0]['KSC score']),
                                score_convert(comp['events'][0]['KF score']),
                                score_convert(comp['events'][0]['KB score']),
                                score_convert(comp['events'][0]['S score']),
                                score_convert(comp['events'][0]['A score']),
                                score_convert(comp['events'][0]['SD score']),
                                score_convert(comp['events'][0]['SF score'])
                ]
                total_score = sum(event_array)
    return total_score

def get_top_scores(classification):
    """Returns a list of top individuals, top males, top females or top clubs"""

    new_list = []
    with open(get_json_file(), 'r+') as current_file:
        data = json.load(current_file)
        if classification == 'ind':
            for competitor in data['competitors']:
                name = competitor['full name']
                total_score = get_total_score_competitor(competitor['full name'])
                competitor['score'] = total_score
                new_list.append([name, total_score])

        elif classification == 'male':
            for competitor in data['competitors']:
                if competitor['gender'] == 'male':
                    name = competitor['full name']
                    total_score = get_total_score_competitor(competitor['full name'])
                    competitor['score'] = total_score
                    new_list.append([name, total_score])

        elif classification == 'female':
            for competitor in data['competitors']:
                if competitor['gender'] == 'female':
                    name = competitor['full name']
                    total_score = get_total_score_competitor(competitor['full name'])
                    competitor['score'] = total_score
                    new_list.append([name, total_score])

        elif classification == 'club':
            new_club_list = get_club_list()
            for competitor in data['competitors']:
                for club in new_club_list:
                    if competitor['club name'] == club[0]:
                        total_score = get_total_score_competitor(competitor['full name'])
                        competitor['score'] = total_score 
                        club[1] += total_score
            new_list = new_club_list

        else:
            print("===> ERROR in get_top_scores()")

        current_file.seek(0)
        json.dump(data, current_file, indent=4)
        current_file.truncate()

    sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True) 
    sorted_ten = sorted_list[:10]
    return sorted_ten












 

