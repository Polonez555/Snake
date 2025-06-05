# لعبة الثعبان (Lu'bat Ath-Thu'ban - Snake Game)

import pygame  # استيراد مكتبة Pygame (Istīrād maktabat Pygame - Import Pygame library)
import sys     # استيراد مكتبة النظام (Istīrād maktabat an-niẓām - Import system library)
import random  # استيراد مكتبة العشوائية (Istīrād maktabat al-'ashwā'iyyah - Import random library)

# --- تعريف الثوابت (Ta'rīf ath-thawābit - Constant Definitions) ---
عرض_الشاشة = 600     # عرض الشاشة (Arḍ ash-shāshah - Screen width)
ارتفاع_الشاشة = 400  # ارتفاع الشاشة (Irtifā' ash-shāshah - Screen height)
حجم_القطعة = 20       # حجم قطعة الثعبان (Ḥajm qiṭ'at ath-thu'bān - Snake block size)

# الألوان (Al-alwān - Colors)
لون_أسود = (0, 0, 0)         # أسود (Aswad - Black)
لون_أبيض = (255, 255, 255)   # أبيض (Abyaḍ - White)
لون_أخضر = (0, 255, 0)       # أخضر (Akhḍar - Green) - لون الثعبان (Lawn ath-thu'bān - Snake color)
لون_أحمر = (255, 0, 0)       # أحمر (Aḥmar - Red) - لون الطعام (Lawn aṭ-ṭa'ām - Food color)
لون_رمادي = (128, 128, 128)    # رمادي (Ramādī - Gray) - لون نص نهاية اللعبة (Lawn naṣṣ nihāyat al-lu'bah - Game over text color)

معدل_الإطارات = 10          # معدل تحديث الإطارات في الثانية (Mu'addal taḥdīth al-iṭārāt fī ath-thāniyah - Game frame rate)

# --- تهيئة Pygame (Tahyi'at Pygame - Initialize Pygame) ---
pygame.init() # تهيئة جميع وحدات Pygame (Tahyi'at jamī' waḥadāt Pygame - Initialize all Pygame modules)
الشاشة = pygame.display.set_mode((عرض_الشاشة, ارتفاع_الشاشة)) # إنشاء الشاشة (Inshā' ash-shāshah - Create screen)
pygame.display.set_caption("لعبة الثعبان (Lu'bat Ath-Thu'ban)") # تعيين عنوان النافذة (Ta'yīn 'unwān an-nāfidhah - Set window title)
المؤقت = pygame.time.Clock() # إنشاء كائن ساعة للتحكم في معدل الإطارات (Inshā' kā'in sā'ah li-t-taḥakkum fī mu'addal al-iṭārāt - Create clock object to control frame rate)
نمط_الخط = pygame.font.SysFont(None, 40) # نمط الخط (Namaṭ al-khaṭṭ - Font style) # قد تحتاج لتحديد خط عربي مثل "arial" إذا كان النص العربي لا يظهر جيدًا
خط_النقاط = pygame.font.SysFont(None, 30) # خط النقاط (Khaṭṭ an-niqāṭ - Score font)

# --- تعريف الدوال (Ta'rīf ad-dawāl - Function Definitions) ---

def رسم_الثعبان(قائمة_جسم_الثعبان):
    """رسم الثعبان (Rasm ath-thu'bān - Draw snake)"""
    for احداثي_س, احداثي_ص in قائمة_جسم_الثعبان:
        pygame.draw.rect(الشاشة, لون_أخضر, [احداثي_س, احداثي_ص, حجم_القطعة, حجم_القطعة]) # رسم كل قطعة من الثعبان (Rasm kull qiṭ'ah min ath-thu'bān - Draw each segment of the snake)

def رسم_الطعام(احداثي_س_الطعام, احداثي_ص_الطعام):
    """رسم الطعام (Rasm aṭ-ṭa'ām - Draw food)"""
    pygame.draw.rect(الشاشة, لون_أحمر, [احداثي_س_الطعام, احداثي_ص_الطعام, حجم_القطعة, حجم_القطعة]) # رسم قطعة الطعام (Rasm qiṭ'at aṭ-ṭa'ām - Draw food block)

def عرض_النقاط(النقاط_الحالية):
    """عرض النقاط (Arḍ an-niqāṭ - Display score)"""
    # استخدام "arial" كخط بديل إذا كان الخط الافتراضي لا يدعم العربية جيداً
    try:
        خط_لعرض_النقاط = pygame.font.SysFont("arial", 25) # أو أي خط عربي مثبت لديك
    except:
        خط_لعرض_النقاط = pygame.font.SysFont(None, 25) # الرجوع للخط الافتراضي

    قيمة_النقاط = خط_لعرض_النقاط.render("النقاط: " + str(النقاط_الحالية), True, لون_أبيض) # إنشاء سطح نص النقاط (Inshā' saṭḥ naṣṣ an-niqāṭ - Create score text surface)
    الشاشة.blit(قيمة_النقاط, [10, 10]) # عرض النص (Arḍ an-naṣṣ - Display text)

def عرض_رسالة(نص_الرسالة, لون_الرسالة, ازاحة_عمودية=0):
    """عرض رسالة (Arḍ risālah - Display message)"""
    # استخدام "arial" كخط بديل إذا كان الخط الافتراضي لا يدعم العربية جيداً
    try:
        خط_للرسالة = pygame.font.SysFont("tahoma", 35) # أو أي خط عربي مثبت لديك
    except:
        خط_للرسالة = pygame.font.SysFont(None, 35) # الرجوع للخط الافتراضي

    سطح_الرسالة = خط_للرسالة.render(نص_الرسالة, True, لون_الرسالة) # إنشاء سطح نص الرسالة (Inshā' saṭḥ naṣṣ ar-risālah - Create message text surface)
    # حساب موقع النص لجعله في المنتصف (Ḥisāb mawqi' an-naṣṣ li-ja'lihi fī al-muntaṣaf - Calculate text position to center it)
    مستطيل_النص = سطح_الرسالة.get_rect(center=(عرض_الشاشة / 2, ارتفاع_الشاشة / 2 + ازاحة_عمودية))
    الشاشة.blit(سطح_الرسالة, مستطيل_النص) # عرض الرسالة (Arḍ ar-risālah - Display message)

def توليد_موقع_الطعام(قائمة_جسم_الثعبان):
    """توليد موقع جديد للطعام، والتأكد من أنه ليس على جسم الثعبان (Tawlīd mawqi' jadīd li-ṭ-ṭa'ām, wa-t-ta'akkud min annahu laysa 'alā jism ath-thu'bān - Generate new food position, ensure it's not on the snake)"""
    while True:
        موقع_س_الطعام_الجديد = round(random.randrange(0, عرض_الشاشة - حجم_القطعة) / حجم_القطعة) * حجم_القطعة
        موقع_ص_الطعام_الجديد = round(random.randrange(0, ارتفاع_الشاشة - حجم_القطعة) / حجم_القطعة) * حجم_القطعة
        if [موقع_س_الطعام_الجديد, موقع_ص_الطعام_الجديد] not in قائمة_جسم_الثعبان: # التحقق مما إذا كان الطعام على جسم الثعبان (At-taḥaqquq mimmā idhā kān aṭ-ṭa'ām 'alā jism ath-thu'bān - Check if food is on the snake)
            return موقع_س_الطعام_الجديد, موقع_ص_الطعام_الجديد

def حلقة_اللعبة():
    """الحلقة الرئيسية للعبة (Al-ḥalaqah ar-ra'īsiyyah lil-lu'bah - Main game loop)"""
    انتهاء_اللعبة = False   # علامة انتهاء اللعبة (Alāmat intihā' al-lu'bah - Game over flag)
    اغلاق_شاشة_النهاية = False  # علامة إغلاق اللعبة (تستخدم لعرض شاشة نهاية اللعبة) (Alāmat ighlāq al-lu'bah (tustakhdam li-'arḍ shāshat nihāyat al-lu'bah) - Game close flag, used for displaying game over screen)

    # الموقع والطول الأولي للثعبان (Al-mawqi' wa-ṭ-ṭūl al-awwalī lith-thu'bān - Snake's initial position and length)
    احداثي_س_الرأس = عرض_الشاشة / 2
    احداثي_ص_الرأس = ارتفاع_الشاشة / 2
    جسم_الثعبان = [[احداثي_س_الرأس, احداثي_ص_الرأس]] # قائمة جسم الثعبان، كل عنصر هو إحداثيات [س, ص] (Qā'imat jism ath-thu'bān, kull 'unṣur huwa iḥdāthiyyāt [s, ṣ] - Snake body list, each element is [x, y] coordinates)
    طول_الثعبان = 1        # الطول الأولي للثعبان (Aṭ-ṭūl al-awwalī lith-thu'bān - Snake's initial length)

    # اتجاه حركة الثعبان (Ittijāh ḥarakat ath-thu'bān - Snake's movement direction)
    تغير_س = 0
    تغير_ص = 0
    الاتجاه = "يمين" # الاتجاه الأولي نحو اليمين (Al-ittijāh al-awwalī naḥwa al-yamīn - Initial direction to the right)

    # الموقع الأولي للطعام (Al-mawqi' al-awwalī li-ṭ-ṭa'ām - Food's initial position)
    احداثي_س_الطعام, احداثي_ص_الطعام = توليد_موقع_الطعام(جسم_الثعبان)

    النقاط = 0 # النقاط الأولية (An-niqāṭ al-awwaliyyah - Initial score)

    # --- بدء حلقة اللعبة (Bad' ḥalqat al-lu'bah - Game loop starts) ---
    while not انتهاء_اللعبة:

        # --- شاشة ما بعد انتهاء اللعبة (Shāshat mā ba'da intihā' al-lu'bah - Screen after game over) ---
        while اغلاق_شاشة_النهاية:
            الشاشة.fill(لون_أسود) # ملء لون الخلفية (Mal' lawn al-khalfiyyah - Fill background color)
            عرض_رسالة("!لقد خسرت", لون_أحمر, -50) # ("Laqad khasirt! - You Lost!")
            عرض_رسالة("اضغط Q للخروج أو R لإعادة اللعب", لون_أبيض, 50) # ("Iḍghaṭ Q lil-khurūj aw R li-i'ādat al-la'ib - Press Q to Quit or R to Restart")
            عرض_النقاط(النقاط)
            pygame.display.update() # تحديث الشاشة (Taḥdīth ash-shāshah - Update screen)

            for حدث in pygame.event.get(): # معالجة الأحداث (Mu'ālajat al-aḥdāth - Event handling)
                if حدث.type == pygame.QUIT: # إذا تم النقر على زر الإغلاق (Idhā tamma an-naqr 'alā zirr al-ighlāq - If close button is clicked)
                    انتهاء_اللعبة = True
                    اغلاق_شاشة_النهاية = False
                if حدث.type == pygame.KEYDOWN: # إذا تم الضغط على مفتاح (Idhā tamma aḍ-ḍaghṭ 'alā miftāḥ - If a key is pressed)
                    if حدث.key == pygame.K_q: # إذا تم الضغط على مفتاح Q (Idhā tamma aḍ-ḍaghṭ 'alā miftāḥ Q - If Q key is pressed)
                        انتهاء_اللعبة = True
                        اغلاق_شاشة_النهاية = False
                    if حدث.key == pygame.K_r: # إذا تم الضغط على مفتاح R (Idhā tamma aḍ-ḍaghṭ 'alā miftāḥ R - If R key is pressed)
                        حلقة_اللعبة() # إعادة بدء اللعبة (I'ādat bad' al-lu'bah - Restart game)

        # --- معالجة الأحداث (Mu'ālajat al-aḥdāth - Event handling) ---
        for حدث in pygame.event.get():
            if حدث.type == pygame.QUIT:
                انتهاء_اللعبة = True
            if حدث.type == pygame.KEYDOWN:
                if حدث.key == pygame.K_LEFT and الاتجاه != "يمين": # إلى اليسار (Ilá al-yasār - Left)
                    تغير_س = -حجم_القطعة
                    تغير_ص = 0
                    الاتجاه = "يسار"
                elif حدث.key == pygame.K_RIGHT and الاتجاه != "يسار": # إلى اليمين (Ilá al-yamīn - Right)
                    تغير_س = حجم_القطعة
                    تغير_ص = 0
                    الاتجاه = "يمين"
                elif حدث.key == pygame.K_UP and الاتجاه != "أسفل": # إلى الأعلى (Ilá al-a'lá - Up)
                    تغير_ص = -حجم_القطعة
                    تغير_س = 0
                    الاتجاه = "أعلى"
                elif حدث.key == pygame.K_DOWN and الاتجاه != "أعلى": # إلى الأسفل (Ilá al-asfal - Down)
                    تغير_ص = حجم_القطعة
                    تغير_س = 0
                    الاتجاه = "أسفل"

        # --- كشف الاصطدام بالحدود (Kashf al-iṣṭidām bil-ḥudūd - Boundary collision detection) ---
        if احداثي_س_الرأس >= عرض_الشاشة or احداثي_س_الرأس < 0 or احداثي_ص_الرأس >= ارتفاع_الشاشة or احداثي_ص_الرأس < 0:
            اغلاق_شاشة_النهاية = True # الاصطدام بالجدار يعني انتهاء اللعبة (Al-iṣṭidām bil-jidār ya'nī intihā' al-lu'bah - If hits wall, game over)

        # تحديث موقع رأس الثعبان (Taḥdīth mawqi' ra's ath-thu'bān - Update snake head position)
        احداثي_س_الرأس += تغير_س
        احداثي_ص_الرأس += تغير_ص

        الشاشة.fill(لون_أسود) # مسح الشاشة (Masḥ ash-shāshah - Clear screen)
        رسم_الطعام(احداثي_س_الطعام, احداثي_ص_الطعام) # رسم الطعام (Rasm aṭ-ṭa'ām - Draw food)

        # تحديث جسم الثعبان (Taḥdīth jism ath-thu'bān - Snake body update)
        رأس_الثعبان_الجديد = [احداثي_س_الرأس, احداثي_ص_الرأس] # رأس الثعبان الجديد (Ra's ath-thu'bān al-jadīd - New snake head)
        جسم_الثعبان.insert(0, رأس_الثعبان_الجديد) # إضافة رأس الثعبان إلى بداية قائمة الجسم (Iḍāfat ra's ath-thu'bān ilá bidāyat qā'imat al-jism - Add snake head to the beginning of the body list)

        if len(جسم_الثعبان) > طول_الثعبان: # إذا تجاوز الطول الفعلي للثعبان الطول المفترض (Idhā tajāwaz aṭ-ṭūl al-fi'lī lith-thu'bān aṭ-ṭūl al-muftaraḍ - If snake's actual length exceeds its due length)
            del جسم_الثعبان[-1] # حذف ذيل الثعبان (Ḥadhf dhayl ath-thu'bān - Delete snake tail)

        # --- كشف الاصطدام الذاتي (Kashf al-iṣṭidām adh-dhātī - Self-collision detection) ---
        # التحقق بدءًا من العنصر الثاني، لأن العنصر الأول هو رأس الثعبان الجديد (At-taḥaqquq bad'an min al-'unṣur ath-thānī, li'anna al-'unṣur al-awwal huwa ra's ath-thu'bān al-jadīd - Check from the second element, as the first is the new head)
        for قطعة in جسم_الثعبان[1:]:
            if قطعة == رأس_الثعبان_الجديد: # إذا اصطدم رأس الثعبان بأي جزء من جسمه (Idhā iṣṭadama ra's ath-thu'bān bi-ayy juz' min jismihi - If snake head hits any part of its body)
                اغلاق_شاشة_النهاية = True

        رسم_الثعبان(جسم_الثعبان) # رسم الثعبان (Rasm ath-thu'bān - Draw snake)
        عرض_النقاط(النقاط)      # عرض النقاط (Arḍ an-niqāṭ - Display score)

        pygame.display.update() # تحديث الشاشة بأكملها (Taḥdīth ash-shāshah bi-akmaliha - Update the entire screen)

        # --- كشف الاصطدام بالطعام (Kashf al-iṣṭidām bi-ṭ-ṭa'ām - Food collision detection) ---
        if احداثي_س_الرأس == احداثي_س_الطعام and احداثي_ص_الرأس == احداثي_ص_الطعام:
            احداثي_س_الطعام, احداثي_ص_الطعام = توليد_موقع_الطعام(جسم_الثعبان) # توليد طعام جديد (Tawlīd ṭa'ām jadīd - Generate new food)
            طول_الثعبان += 1 # زيادة طول الثعبان (Ziyādat ṭūl ath-thu'bān - Snake length increases)
            النقاط += 1        # زيادة النقاط (Ziyādat an-niqāṭ - Score increases)

        المؤقت.tick(معدل_الإطارات) # التحكم في سرعة اللعبة (At-taḥakkum fī sur'at al-lu'bah - Control game speed)

    # --- الخروج من Pygame بعد انتهاء اللعبة (Al-khurūj min Pygame ba'da intihā' al-lu'bah - Quit Pygame after game ends) ---
    pygame.quit() # إلغاء تهيئة جميع وحدات Pygame (Ilghā' tahyi'at jamī' waḥadāt Pygame - Uninitialize all Pygame modules)
    sys.exit()    # الخروج من البرنامج (Al-khurūj min al-barnāmaj - Exit program)

# --- تشغيل اللعبة (Tashghīl al-lu'bah - Run game) ---
if __name__ == "__main__":
    حلقة_اللعبة()
