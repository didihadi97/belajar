bot1_name = {
    "1" : "JANGAN GANGGU GW",
    "2" : "ANGAN GANGGU GW ",
    "3" : "NGAN GANGGU GW J",
    "4" : "GAN GANGGU GW JA",
    "5" : "AN GANGGU GW JAN",
    "6" : "N GANGGU GW JANG",
    "7" : " GANGGU GW JANGA",
    "8" : "GANGGU GW JANGAN",
    "9" : "ANGGU GW JANGAN ",
    "10" : "NGGU GW JANGAN G",
    "11" : "GGU GW JANGAN GA",
    "12" : "GU GW JANGAN GAN",
    "13" : "U GW JANGAN GANG",
    "14" : " GW JANGAN GANGG",
    "15" : "GW JANGAN GANGGU",
    "16" : "W JANGAN GANGGU ",
    "17" : " JANGAN GANGGU G",
    "18" : "JANGAN GANGGU GW",
}

def upload_tempimage(cl):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = cl.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image

def nameUpdate_Bot1():
    while True:
        try:
            profile = cl.getProfile()
            profile.displayName = bot1_name["1"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["2"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["3"]
            cl.updateProfile(profile)                                                                             time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["4"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["5"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["6"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["7"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()                                                                             profile.displayName = bot1_name["8"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["8"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["9"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["10"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["11"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["12"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["13"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["14"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["15"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["16"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["17"]
            cl.updateProfile(profile)
            time.sleep(0.5)
            profile = cl.getProfile()
            profile.displayName = bot1_name["18"]
            cl.updateProfile(profile)
            time.sleep(0.5)
        except:
            pass
            
thread1 = threading.Thread(target=nameUpdate_Bot1)
thread1.daemon = True
thread1.start()
thread2 = threading.Thread(target=nameUpdate_Bot2)
thread2.daemon = True
thread2.start()
thread3 = threading.Thread(target=nameUpdate_Bot3)
thread3.daemon = True
thread3.start()
thread4 = threading.Thread(target=nameUpdate_Bot4)
thread4.daemon = True
thread4.start()
thread5 = threading.Thread(target=nameUpdate_Bot5)
thread5.daemon = True
thread5.start()
thread6 = threading.Thread(target=nameUpdate_Bot6)
thread6.daemon = True
thread6.start()
thread7 = threading.Thread(target=nameUpdate_Bot7)
thread7.daemon = True
thread7.start()
thread8 = threading.Thread(target=nameUpdate_Bot8)
thread8.daemon = True
thread8.start()
thread9 = threading.Thread(target=nameUpdate_Bot9)
thread9.daemon = True
thread9.start()
thread10 = threading.Thread(target=nameUpdate_Bot10)
thread10.daemon = True
thread10.start()
thread11 = threading.Thread(target=nameUpdate_Bot11)
thread11.daemon = True
thread11.start()
thread12 = threading.Thread(target=nameUpdate_Bot12)
thread12.daemon = True
thread12.start()
thread13 = threading.Thread(target=nameUpdate_Bot13)
thread13.daemon = True
thread13.start()
thread14 = threading.Thread(target=nameUpdate_Bot14)
thread14.daemon = True
thread14.start()
thread15 = threading.Thread(target=nameUpdate_Bot15)
thread15.daemon = True
thread15.start()
thread16 = threading.Thread(target=nameUpdate_Bot16)
thread16.daemon = True
thread16.start()
thread17 = threading.Thread(target=nameUpdate_Bot17)
thread17.daemon = True
thread17.start()
thread18 = threading.Thread(target=nameUpdate_Bot18)
thread18.daemon = True
thread18.start()
