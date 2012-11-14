# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, MULTILINE
from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter


class ALessonIsLearned(_BasicScraper):
    latestUrl = 'http://www.alessonislearned.com/'
    stripUrl = 'http://www.alessonislearned.com/lesson%s.html'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)", quote="'")+r"[^>]+previous")
    help = 'Index format: nnn'


class ASofterWorld(_BasicScraper):
    latestUrl = 'http://www.asofterworld.com/'
    stripUrl = 'http://www.asofterworld.com/index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.asofterworld\.com/clean/[^"]+)'))
    prevSearch = compile(tagre("a", "href", "(index\.php\?id=\d+)")+'< back')
    help = 'Index format: n (unpadded)'


class AbleAndBaker(_BasicScraper):
    latestUrl = 'http://www.jimburgessdesign.com/comics/index.php'
    stripUrl = 'http://www.jimburgessdesign.com/comics/index.php?comic=%s'
    imageSearch = compile(tagre('img', 'src', r'(comics/.+)'))
    prevSearch = compile(tagre('a', 'href', r'(.+\d+)') + '.+?previous.gif')
    help = 'Index format: nnn'


class AbominableCharlesChristopher(_BasicScraper):
    latestUrl = 'http://abominable.cc/'
    stripUrl = 'http://abominable.cc/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.abominable\.cc/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"[^<]+Previous")
    help = 'Index format: yyyy/mm/dd/comicname'


class AbsurdNotions(_BasicScraper):
    latestUrl = 'http://www.absurdnotions.org/page129.html'
    stripUrl = 'http://www.absurdnotions.org/page%s.html'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') + tagre('img', 'src', 'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class AbstruseGoose(_BasicScraper):
    starter = bounceStarter('http://abstrusegoose.com/',
       compile(tagre('a', 'href', r'(http://abstrusegoose\.com/\d+)')+"Next &raquo;</a>"))
    stripUrl = 'http://abstrusegoose.com/c%s.html'
    imageSearch = compile(tagre('img', 'src', r'(http://abstrusegoose\.com/strips/[^<>"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(http://abstrusegoose\.com/\d+)') + r'&laquo; Previous</a>')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AcademyVale(_BasicScraper):
    latestUrl = 'http://imagerie.com/vale/'
    stripUrl = 'http://imagerie.com/vale/avarch.cgi?%s'
    imageSearch = compile(tagre('img', 'src', r'(avale\d{4}-\d{2}\.gif)'))
    prevSearch = compile(tagre('a', 'href', r'(avarch[^"]+)') + tagre('img', 'src', 'AVNavBack\.gif'))
    help = 'Index format: nnn'


class Alice(_BasicScraper):
    latestUrl = 'http://alice.alicecomics.com/'
    stripUrl = 'http://alice.alicecomics.com/wp-content/webcomic/alicecomics/%s.jpg'
    imageSearch = compile(tagre("img", "src", r'(http://alice\.alicecomics\.com/wp-content/webcomic/alicecomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alice.alicecomics.com/archive/[^"]+)', after="previous"))
    help = 'Index format: yyyy-mm-dd'


class AlienLovesPredator(_BasicScraper):
    stripUrl = 'http://alienlovespredator.com/%s'
    imageSearch = compile(r'<img src="(.+?)"[^>]+>(<center>\n|\n|</center>\n)<div style="height: 2px;">&nbsp;</div>', MULTILINE)
    prevSearch = compile(r'<a href="(.+?)"><img src="/images/nav_previous.jpg"')
    help = 'Index format: nnn'
    starter = bounceStarter('http://alienlovespredator.com/index.php', compile(r'<a href="(.+?)"><img src="/images/nav_next.jpg"'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        vol = pageUrl.split('/')[-5]
        num = pageUrl.split('/')[-4]
        ccc = pageUrl.split('/')[-3]
        ddd = pageUrl.split('/')[-2]
        return '%s-%s-%s-%s' % (vol, num, ccc, ddd)


class AnarchySD(_BasicScraper):
    stripUrl = 'http://www.anarchycomic.com/page%s.php'
    imageSearch = compile(tagre('img', 'src', r'../(images/page\d+\..+?)'))
    prevSearch = compile(tagre('a', 'href', r'(page\d+\.php)')+'PREVIOUS PAGE')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(
        'http://www.anarchycomic.com/page1.php',
        compile(r'<a href="(page\d+\.php)" class="style15">LATEST'))



class Altermeta(_BasicScraper):
    latestUrl = 'http://altermeta.net/'
    stripUrl = 'http://altermeta.net/archive.php?comic=%s&view=showfiller'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="http://altermeta\.net/template/default/images/sasha/back\.png')
    help = 'Index format: n (unpadded)'



class AltermetaOld(Altermeta):
    name = 'Altermeta/Old'
    latestUrl = 'http://altermeta.net/oldarchive/index.php'
    stripUrl = 'http://altermeta.net/oldarchive/archive.php?comic=%s'
    prevSearch = compile(r'<a href="([^"]+)">Back')



class Angels2200(_BasicScraper):
    latestUrl = 'http://www.janahoffmann.com/angels/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"&laquo; Previous"))
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'



class AppleGeeks(_BasicScraper):
    latestUrl = 'http://www.applegeeks.com/'
    stripUrl = 'http://www.applegeeks.com/comics/viewcomic.php?issue=%s'
    imageSearch = compile(tagre("img", "src", r'"(strips/\d+?\..+?)"'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    help = 'Index format: n (unpadded)'


class Achewood(_BasicScraper):
    latestUrl = 'http://www.achewood.com/'
    stripUrl = 'http://www.achewood.com/index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(/comic\.php\?date=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', after="Previous"))
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date%3D(\d{8})'))



class AstronomyPOTD(_BasicScraper):
    starter = bounceStarter(
        'http://antwrp.gsfc.nasa.gov/apod/astropix.html',
        compile(r'<a href="(ap\d{6}\.html)">&gt;</a>'))
    stripUrl = 'http://antwrp.gsfc.nasa.gov/apod/ap%s.html'
    imageSearch = compile(r'<a href="(image/\d{4}/.+\..+?)">')
    prevSearch = compile(r'<a href="(ap\d{6}\.html)">&lt;</a>')
    help = 'Index format: yymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%s-%s' % (pageUrl.split('/')[-1].split('.')[0][2:],
                          imageUrl.split('/')[-1].split('.')[0])



class AfterStrife(_BasicScraper):
    latestUrl = 'http://afterstrife.com/?p=262'
    stripUrl = 'http://afterstrife.com/?p=%s'
    imageSearch = compile(r'<img src="(http://afterstrife.com/strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" class="navi navi-prev"')
    help = 'Index format: nnn'



class ALLCAPS(_BasicScraper):
    latestUrl = 'http://www.allcapscomix.com/'
    stripUrl = 'http://www.allcapscomix.com/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.allcapscomix\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: yyyy/mm/strip-name'



class ASkeweredParadise(_BasicScraper):
    latestUrl = 'http://aspcomics.net/'
    stripUrl = 'http://aspcomics.net/archindex.php?strip_id=%s'
    imageSearch = compile(tagre("img", "src", r'(http://aspcomics\.net/sites/default/files[^"]*/asp\d+\.jpg)[^"]+'))
    prevSearch = compile(tagre("a", "href", "(/comic/\d+)")+r"[^>]+Previous")
    help = 'Index format: nnn'



class AGirlAndHerFed(_BasicScraper):
    starter = bounceStarter('http://www.agirlandherfed.com/',
      compile(r'<a href="([^"]+)">[^>]+Back'))
    stripUrl = 'http://www.agirlandherfed.com/img/strip/%s'
    imageSearch = compile(tagre("img", "src", r'(img/strip/[^"]+\.jpg)'))
    prevSearch = compile(r'<a href="([^"]+)">[^>]+Back')
    help = 'Index format: nnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('?')[-1]



class AetheriaEpics(_BasicScraper):
    latestUrl = 'http://aetheria-epics.schala.net/'
    stripUrl = 'http://aetheria-epics.schala.net/%s.html'
    imageSearch = compile(r'<td><img src="(\d{5}.\w{3,4})"')
    prevSearch = compile(r'<a href="(\d{5}.html)"><img src="prev.jpg"\/>')
    help = 'Index format: nnn'



class Adrift(_BasicScraper):
    latestUrl = 'http://www.adriftcomic.com/'
    stripUrl = 'http://www.adriftcomic.com/page%s.html'
    imageSearch = compile(r'<IMG SRC="(Adrift_Web_Page\d+.jpg)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="AdriftBackLink.gif"')
    help = 'Index format: nnn'



class AirForceBlues(_BasicScraper):
    latestUrl = 'http://www.afblues.com/'
    stripUrl = 'http://www.afblues.com/?p=%s'
    imageSearch = compile(r'<img src=\'(http://www.afblues.com/comics/.+?)\'>')
    prevSearch = compile(r'<a href="(http://www.afblues.com/.+?)">&laquo; Previous')
    help = 'Index format: nnn'



class AlienShores(_BasicScraper):
    latestUrl = 'http://alienshores.com/alienshores_band/'
    stripUrl = 'http://alienshores.com/alienshores_band/?p=%s'
    imageSearch = compile(r'><img src="(http://alienshores.com/alienshores_band/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://alienshores.com/.+?)" rel="prev">')
    help = 'Index format: nnn'



class AllTheGrowingThings(_BasicScraper):
    latestUrl = 'http://typodmary.com/growingthings/'
    stripUrl = 'http://typodmary.com/growingthings/%s/'
    imageSearch = compile(r'<img src="(http://typodmary.com/growingthings/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://typodmary.com/growingthings/.+?)"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class Amya(_BasicScraper):
    latestUrl = 'http://www.amyachronicles.com/'
    stripUrl = 'http://www.amyachronicles.com/archives/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.amyachronicles\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.amyachronicles\.com/archives/\d+)', after="Previous"))
    help = 'Index format: n'



class Angband(_BasicScraper):
    latestUrl = 'http://angband.calamarain.net/'
    stripUrl = 'http://angband.calamarain.net/view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)')+"Previous")
    help = 'Index format: yyyy-mm-dd'



class ActionAthena(_BasicScraper):
    latestUrl = 'http://actionathena.com/'
    stripUrl = 'http://actionathena.com/2%s'
    imageSearch = compile(r'<img src=\'(http://actionathena.com/comics/.+?)\'>')
    prevSearch = compile(r'<a href="(http://actionathena.com/.+?)">&laquo; Previous</a>')
    help = 'Index format: yyyy/mm/dd/strip-name'



class AlsoBagels(_BasicScraper):
    latestUrl = 'http://www.alsobagels.com/'
    stripUrl = 'http://alsobagels.com/index.php/comic/%s/'
    imageSearch = compile(r'<img src="(http://alsobagels.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://alsobagels.com/index.php/comic/.+?)">')
    help = 'Index format: strip-name'



class Annyseed(_BasicScraper):
    latestUrl = 'http://www.colourofivy.com/annyseed_webcomic_latest.htm'
    stripUrl = 'http://www.colourofivy.com/annyseed_webcomic%s.htm'
    imageSearch = compile(r'<td width="570" height="887" valign="top"><img src="(.+?)"')
    prevSearch = compile(r'<a href="(http://www.colourofivy.com/.+?)"><img src="Last.gif"')
    help = 'Index format: nnn'
