bad_words = ['блядь', 'сука', 'суки', 'сучка', 'сучара', 'твари', 'ублюдки', 'уебки','не рекомендую', 'не советую', 'отстой', 'отстойный', 'отстойное',
             'стремно', 'стремное', 'говнянское', 'убогое', 'дерьмовое', 'бляха-муха','бляха муха','ебань', 'ебарь', 'ебанавт', 'хуйло', 'хуйлан',
             'пенис', 'шлюха', 'шаболда', 'пиздолиз', 'дыроеб', 'пиздализ','хер', 'член', 'вагина', 'блядина', 'хуеплет', 'очко',  'бля', 'бля буду',
             'блядство', 'блядун', 'бляди', 'блядское', 'блядская', 'блядские', 'блядский',
             'блядища', 'блядовать', 'выблядок', 'блять', 'еб твою мать', 'ебёныть', 'ебнулся', 'еб', 'в рот ебать', 'мозги ебать', 'ебанутый',
             'ебать-копать', 'ебать', 'ебаться', 'ёбырь', 'ебальник', 'ебало', 'ебло', 'ёбнуть', 'ебануть', 'ёбнутый', 'выебнулся', 'наебнуться',
             'выебнуться','долбоёб', 'заеблись', 'заебатый', 'настоебенить', 'настоебать', 'ебаквакнуться', 'наебать', 'ебысь', 'еблысь', 'ёбс',
             'наёбка' , 'подъебать', 'подъёб', 'подъёбка', 'поебень', 'поеботина', 'коноебля', 'коноёбиться', 'ебля', 'уёбище', 'бомбоуёбище',
             'уёбывать', 'съёбывать', 'изъебнуться', 'изъёб', 'невъебенно', 'заебатый', 'заебательский', 'разъебай', 'разъёба', 'поёбка', 'еблан',
             'ебанат', 'туебень', 'ёбово', 'еботятина', 'ебливый', 'ебучий', 'злоебучий', 'косоёбиться', 'шароёбиться',  'хуй', 'хуевый', 'хуево',
             'хуета', 'хуйня', 'хуетень', 'хуевина', 'хуетина', 'хули', 'хуячить', 'хуярить', 'хуярыжить', 'охуенный', 'охуительный', 'охуевательный',
             'охуенный', 'охуеть', 'нихуя', 'не хуя', 'похую', 'похуй', 'хуяк', 'похуист', 'похуизм', 'на хуй','нахуй', 'хуила', 'хуебяка', 'хуйнуть',
             'семихуй', 'полухуй', 'хуемполбия', 'хуесос','пиздец', 'пизда', 'пизданутый', 'спизжены', 'до пизды', 'пиздатый', 'пиздобол','пиздабол' ,
             'опиздол', 'пиздить', 'спиздить', 'пиздануть', 'пиздеть', 'пиздеж', 'пиздун', 'пиздяной', 'пиздной', 'пиздюля', 'пиздюлина', 'пиздючка',
             'распиздяй', 'пиздовать', 'пиздануться', 'пиздюк', 'пездолочь', 'спиздометр', 'пизданутый', 'припизднутый', 'пиздячить', 'пиздюхать',
             'пиздюхаханьки', 'пиздовать', 'пиздёхать', 'пиздорванец', 'пиздобратия', 'припиздь', 'пиздотекарь', 'пиздёныш', 'чепиздон', 'распиздон',
              'пиздой накрыться', 'опиздохуительно пиздоебля', 'пиздоплюйство', 'пиздопроёбина', 'пиздопроушина', 'без пизды', 'перебздеть', 'недобздеть',
              'мудак', 'мудство', 'мудями', 'мудаковатый', 'мудила', 'мудозвон', 'мудохать', 'мудофель', 'мудель', 'мудень', 'мудильник',  'дрочить', 'дрочила',
             'конченый', 'задроченный', 'придрочиться', 'трахать', 'трахаться', 'трахает', 'трахаются', 'ебутся', 'ебуться', 'трахались', 'трахнулись',
              'манда', 'пизда', 'мандовуха', 'мандовка', 'прошмандовка', 'мандавошка', 'мандовошка', 'хер', 'хрен', 'херить', 'похерить', 'выхерить', 'хером', 'хреном',
             'хреновый', 'херовый', 'по хрену', 'по херу', 'на хер', 'ни хера', 'хрен', 'сосать', 'до хрена', 'дохрена', 'охрененский', 'охренел','охренела', 'охренели',
             'хрень', 'херь', 'херня', 'херьня', 'не хрен', 'нехер', 'говно', 'дерьмо', 'говнюк', 'говноед', 'кал', 'какашка', 'какаха',  'залупа', 'залупывать', 'залупливать',
             'залуплять', 'залупать','залупаться', 'залупа', 'залупка', 'срать', 'поднасрать', 'засранный', 'обосранный', 'мухосранск', 'обосрать', 'засратый', 'серить', 'срака',
             'сральник', 'засранец', 'срун', 'обосраться', 'пересрать','просрать', 'насрать', 'засрать', 'обосрать', 'срач', 'усираться', 'подосрать', 'высрать', 'ссать', 'зассатый',
             'обоссанный', 'поднассать', 'писать', 'пописать', 'мочиться', 'оправляться', 'проссывать','ссыкун' , 'ссыкло', 'сыкло', 'пидор', 'пидар', 'педик', 'пидрила', 'педрильо',
             'гомосек', 'гомосятина', 'гей', 'голубой', 'пидарас', 'пидораз', 'пидорас', 'пидарасить', 'пидорасина', 'жопа', 'задница','задничный', 'жопорванец', 'зажопить',
             'жополиз', 'хитрожопый', 'целка','гандон', 'гандошить', 'гондон','anal','anus','arse','arsehole','aryan','asanchez','ass','assbang','assbanged','asses','assfuck',
             'assfucker','assfukka','asshole','assmunch','asswhole','autoerotic','ballsack','bastard','bdsm','beastial','beastiality','bellend','bestial',
             'bestiality','bimbo','bimbos','bitch','bitches','bitchin','bitching','blowjob','blowjobs','blue waffle','bondage','boner','boob','boobs','booobs',
             'boooobs','booooobs','booooooobs','booty call','clit','clitoris','clits','cnut','cock','cockface','cockhead','cockmunch','cockmuncher','cocks',
             'cocksuck','cocksucked','cocksucker','cocksucking','cocksucks','cokmuncher','cum','cuming','cummer','cumming','cums','cumshot','cunilingus','cunillingus',
             'cunnilingus','cunt','cuntlicker','cuntlicking','cunts','damn','deepthroat','dick','dickhead','dildo','dildos','dink','dinks','dlck','dog style','dog - fucker',
             'doggiestyle','doggin','dogging','doggystyle','dong','donkeyribber','doofus','doosh','dopey','douche','douchebag','douchebags','douchey','drunk','duche','dumass',
             'dumbass','dumbasses','dummy','dyke','dykes','eatadick','eathairpie','erect','erection','erotic','erotism','essohbee','extacy','extasy','facial','fack','fag','fagg',
             'fagged','fagging','faggit','faggitt','faggot','faggs','fagot','fagots','fags','faig','fat','fatass','fcuk','fcuker','fcuking','feck','fecker','felch','felcher','felching',
             'fellate','fellatio','feltch','feltcher','femdom','fingerfuck','fingerfucked','fingerfucker','fingerfuckers','fingerfucking','fingerfucks','fingering','fisted','fistfuck',
             'fistfucked','fistfucker','fistfuckers','fistfucking','fistfuckings','fistfucks','fisting','fisty','flange','flogthelog','floozy','foad','fondle','foobar','fook','fooker',
             'footjob','foreskin','freex','frigg','frigga','fubar','fuck','fucka','fuckass','fuckbitch','fucked','fucker','fuckers','fuckface','fuckhead','fuckheads','fuckhole','fuckin',
             'fucking','fuckings','fuckingshitmotherfucker','fuck me','fuckmeat','fucknugget','fucknut','fuckoff','fuckpuppet','fucks','fucktard','fucktoy','fucktrophy','fuckup','fuckwad',
             'fuckwhit','fuckwit','fuckyomama','fudgepacker','fuk','fuker','fukker','fukkin','fukking','fuks','fukwhit','fukwit','futanari','futanary','fux','fuxor','gai','gangbang','gangbanged',
             'gangbangs','ganja','gassyass','gay','gaylord','gays','gaysex','gey','gfy','ghay','ghey','gigolo','glans','goatse','god','godamn','godamnit','goddam','goddammit','goddamn',
             'goddamned','homo','homoerotic','homoey','honky','hooch','hookah','hooker','hoor','hootch','hooter','hooters','hore','horniest','horny','hotsex','howtokill','howtomurdep','hump',
             'humped','humping','hussy','hymen','inbred','incest','injun','jackass','jackhole','jackoff','jap','japs','jerk','jerked','jerkoff','jism','jiz','jizm','jizz','jizzed','kill','mothafuck',
             'mothafucka','mothafuckas','mothafuckaz','mothafucked','mothafucker','mothafuckers','mothafuckin','mothafucking','mothafuckings','mothafucks','motherfuck','motherfucka','motherfucked',
             'motherfucker','motherfuckers','motherfuckin','motherfucking','motherfuckings','motherfuckka','motherfucks','mtherfucker','mthrfucker','mthrfucking','muff', 'muffdiver','muffpuff','murder',
             'mutha','muthafecker','muthafuckaz','muthafucker','muthafuckker','muther','mutherfucker', 'mutherfucking','muthrfucking',

             ]


def have_bad_words(messege:str):
    marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''

    for x in messege:
        if x in marks:
            messege = messege.replace(x, "")

    lst = messege.split()

    for word in lst:
        if word in bad_words:
            return False
    return True
