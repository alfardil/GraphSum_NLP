# Targeted inspection: CNN/DM (dev)

Strongest simpler rival on dev: **abl_position** (dev mean ROUGE 34.56 vs ours 24.79). Ours tuned: {'beta': 0.6, 'gamma': 2.0, 'memory': 0.5}; rival tuned: {'beta': 0.0, 'forward_weight': -2.0, 'gamma': 2.0, 'memory': 0.9}. Budget: 3 sentences. Ours is worse than the rival on 15/20 dev docs; listed: the 20 largest gaps.

Sentence markers: **O** ours, **R** rival, **★** Oracle.


---

## 1. `cnn_dm-dev-12194` — gap 49.06 ROUGE (15 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 17.82 | 0.00 | 13.86 |
| abl_position | 62.71 | 53.45 | 62.71 |

**Error category:** ______

**Reference**

> Sally Forrest, an actress-dancer who graced the silver screen throughout the '40s and '50s in MGM musicals and films died on March 15 .
> Forrest, whose birth name was Katherine Feeney, had long battled cancer .
> A San Diego native, Forrest became a protege of Hollywood trailblazer Ida Lupino, who cast her in starring roles in films .

**Ours** (sentences [9, 10, 13])

> She also starred in a Broadway production of The Seven Year Itch.
> City News Service reported that other stage credits included As You Like It, No, No, Nanette and Damn Yankees.
> She is survived by her niece, Sharon Durham, and nephews, Michael and Mark Feeney.

**abl_position** (sentences [0, 1, 2])

> Sally Forrest, an actress-dancer who graced the silver screen throughout the '40s and '50s in MGM musicals and films such as the 1956 noir While the City Sleeps died on March 15 at her home in Beverly Hills, California.
> Forrest, whose birth name was Katherine Feeney, was 86 and had long battled cancer.
> Her publicist, Judith Goffin, announced the news Thursday.

<details><summary>Document</summary>

  0 R★   Sally Forrest, an actress-dancer who graced the silver screen throughout the '40s and '50s in MGM musicals and films such as the 1956 noir While the City Sleeps died on March 15 at her home in Beverly Hills, California.  
  1 R★   Forrest, whose birth name was Katherine Feeney, was 86 and had long battled cancer.  
  2 R    Her publicist, Judith Goffin, announced the news Thursday.  
  3      Scroll down for video .  
  4      Actress: Sally Forrest was in the 1951 Ida Lupino-directed film 'Hard, Fast and Beautiful' (left) and the 1956 Fritz Lang movie 'While the City Sleeps' A San Diego native, Forrest became a protege of Hollywood trailblazer Ida Lupino, who cast her in starring roles in films including the critical and commercial success Not Wanted, Never Fear and Hard, Fast and Beautiful.  
  5      Some of Forrest's other film credits included Bannerline, Son of Sinbad, and Excuse My Dust, according to her iMDB page.  
  6      The page also indicates Forrest was in multiple Climax!  
  7      and Rawhide television episodes.  
  8      Forrest appeared as herself in an episode of The Ed Sullivan Show and three episodes of The Dinah Shore Chevy Show, her iMDB page says.  
  9 O    She also starred in a Broadway production of The Seven Year Itch.  
 10 O    City News Service reported that other stage credits included As You Like It, No, No, Nanette and Damn Yankees.  
 11      Forrest married writer-producer Milo Frank in 1951.  
 12      He died in 2004.  
 13 O    She is survived by her niece, Sharon Durham, and nephews, Michael and Mark Feeney.  
 14 ★    Career: A San Diego native, Forrest became a protege of Hollywood trailblazer Ida Lupino, who cast her in starring roles in films .  

</details>

---

## 2. `cnn_dm-dev-6728` — gap 29.40 ROUGE (56 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 0.00 | 0.00 | 0.00 |
| abl_position | 35.51 | 19.05 | 33.64 |

**Error category:** ______

**Reference**

> Her choice of thigh-high patent boots this week was certainly eyecatching .
> For one brief year in her early 50s Theresa May hit her fashion stride .
> Her outfits now reflect a common loss of fashion confidence .
> Here, FEMAIL looks at Theresa May's fashion mistakes .

**Ours** (sentences [30, 33, 37])

> FEBRUARY 2000 .
> OCTOBER 2004 .
> OCTOBER 2009 .

**abl_position** (sentences [0, 1, 4])

> Her choice of thigh-high patent boots, mini skirt and above-the- knee red-and-gold bobble coat was certainly eyecatching.
> If Theresa May’s intention was to upstage Angelica Rivera, Mexico’s rather beautiful First Lady, then she succeeded — though unfortunately not for the right reasons.
> At 58, what May appears to be suffering from is a classic 50s fashion crisis.

<details><summary>Document</summary>

  0 R★   Her choice of thigh-high patent boots, mini skirt and above-the- knee red-and-gold bobble coat was certainly eyecatching.  
  1 R    If Theresa May’s intention was to upstage Angelica Rivera, Mexico’s rather beautiful First Lady, then she succeeded — though unfortunately not for the right reasons.  
  2      Rather, the Home Secretary looked a disturbing mix of one part dominatrix and one part Fifties housewife, with those gloves that put me in mind of a pair of Marigolds.  
  3      Home Sexetary!Sporting S&M thigh boots, miniskirt and red and gold bobble coat this week, May goes into fashion meltdown on her way to meet the Queen and the President of Mexico .  
  4 R    At 58, what May appears to be suffering from is a classic 50s fashion crisis.  
  5      Having been there, I know the form this crisis takes.  
  6      What happens is this.  
  7      One day you survey yourself in the mirror and decide you’re looking like a middle-aged frump and that if you don’t watch out you’ll soon be morphing, before your time, into a little old lady.  
  8      Your wardrobe is in a rut.  
  9      You buy the same boring basics for weekends and the same smart suits or skirts and tops for work, year in year out.  
 10      So, in an effort to update yourself, you rush out and start buying things that will make you feel fresher, flirtier, more youthful.  
 11      Unless you have teenage children to put you in your fashion place (and May doesn’t have children), you may find yourself with a whole new wardrobe that just doesn’t chime with your looks, age or, in May’s case, profession.  
 12      Husbands, being husbands, tend not to notice these things.  
 13      Girlfriends don’t want to upset or undermine you, so they generally keep schtum.  
 14 ★    In May’s case, the trajectory was slightly different because it appears that for one brief year in her early 50s she did hit her fashion stride with a wardrobe of flatteringly cut separates in a stylish palette of navy, white, black and taupe.  
 15      It’s not known whether she feared they made her invisible, however, but what’s certain is that since 2010 her style has been characterised by eccentric and flamboyant outfits.  
 16      Her look has certainly changed over the years.  
 17      In the early days after her election to Parliament in 1997, and the years from 2002 when she served in the Shadow Cabinet, her style evolved from ill-fitting suits in drab colours to garish: think of the voluminous orange mac she wore to the Tory conference in 2009.  
 18      But once the Tories came into power and she was promoted to Home Secretary, she seemed to embark on a brief transformation after losing weight and finding her fashion feet.  
 19      Shortly after, though, the crisis set in and has been growing worse, culminating in this week’s sartorial disaster.  
 20      While her fetish for S&M style boots — she also wore them in 2013 for the South Korean president’s state visit — is Fifty Shades of Embarrassing, I can empathise.  
 21      When my marriage broke up in my mid-50s, I bought a pair of similar boots in suede rather than patent or PVC, but after catching my reflection one day in a shop window, I thought: ‘Who am I trying to kid?’  
 22      Admittedly, my 50s fashion panic was partly about attracting men in the wake of my divorce, which is not an issue for the happily married May.  
 23      But it reflects a loss of fashion confidence at this stage of our lives when the shops are full of temptations that look great on hangers and 25-year-olds, but not necessarily on us.  
 24      The big difference between May and rest of us, of course, is that her fashion faux pas have to be played out in the full glare of the camera.  
 25      If you play it safe, as the Duchess of Cambridge does, you get criticised for being bland.  
 26      Go too trendy and you will be mocked for trying too hard.  
 27      Perhaps, when it comes to fashion, May should take a leaf out of Sam Cam’s book.  
 28      The Prime Minister’s wife always looks elegant and low-key, while promoting British fashion to an international audience.  
 29      Theresa May is an attractive woman and has shapely and slender legs that are amazing for a woman of any age, but if when you think of the Home Secretary the first thing that springs to mind is her footwear and snazzy coats rather than her policies, she’s getting something wrong.  
 30 O    FEBRUARY 2000 .  
 31      MP May is a relative new girl, opting for sombre grey suit and pearls.  
 32      But even then, the leopard-print bag and slit in her skirt hint at a wilder side .  
 33 O    OCTOBER 2004 .  
 34      Not just any old mac for the Tory party conference — but a Pepto-Bismol pink mac, with extra wide-legged trousers and clashing red shoes .  
 35      DECEMBER 2005 .  
 36      Black suede boots and a techni-colour nightmare coat at a party to celebrate David Cameron becoming Tory leader .  
 37 O    OCTOBER 2009 .  
 38      An unflattering bright orange raincoat, possibly made out of a hot air balloon, for the Tory Conference .  
 39      JULY 2010 .  
 40      Despite the creases, this is a flattering suit with stylish accessories.  
 41      An outfit that says May means business .  
 42      SEPTEMBER 2010 .  
 43      On trend in an elegant floral cocoon coat.  
 44      Just a shame about the mismatched bag and shoes .  
 45      OCTOBER 2010 .  
 46      Leaving a Cabinet meeting at Downing Street in a winning combo of ice-blue silk jacket and flattering palazzo pants, teamed with a stylish bag .  
 47 ★    MAY 2012 .  
 48      Time to remind her that less is more?  
 49      At No 10, the multi-coloured jacket overwhelms the skirt, which looks as if it is caught in her knickers .  
 50      NOVEMBER 2013 .  
 51      First outing of the Stuart Weizman kinky boots and another knock-’em-dead coat for a state visit.  
 52      It’s hard to imagine what she has to smile about in this garish outfit .  
 53      OCTOBER 2014 .  
 54      Ditch the girly bow and inexplicable gauntlets and May would look wonderful for a visit by the President of Singapore.  
 55      Over-icing the cake is never a good idea but it seems she can’t help herself .  

</details>

---

## 3. `cnn_dm-dev-7266` — gap 28.90 ROUGE (34 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 13.56 | 0.00 | 13.56 |
| abl_position | 45.95 | 23.29 | 44.59 |

**Error category:** ______

**Reference**

> Andreas Günter Lubitz deliberately crashed Germanwings plane into Alps .
> Echoes other aviation disasters believed to have been caused by crew .
> Could explain final moments of Flight MH370 which vanished last March .
> Analysis of satellite data suggests plane was deliberately flown off course .
> Would suggest pilot of the doomed jet took actions similar to Lubitz's .

**Ours** (sentences [15, 25, 28])

> He also pushed the aircraft's throttles back to idle and selected the jet's maximum operating speed.
> Captain Gamil al-Batouti said he would relieve the current pilot - even though he wasn't due on the flight deck for a further three hours.
> El-Batouty even shut down the aircraft's engines, which prevented his co-pilot from saving the aircraft.

**abl_position** (sentences [0, 1, 3])

> The fate of Flight FU 9525 that was deliberately crashed into the Alps has chilling similarities to a number of other aircraft  believed to have been downed by flight crew.
> Germanwings pilot Andreas Günter Lubitz locked his captain out of the cockpit before ploughing the Airbus A320 into the mountain at more than 400mph, killing all 150 on board.
> It echoes a number of recent aviation tragedies and could explain what happened to flight MH370 - which vanished last March while flying from Kuala Lumpur to Beijing with 239 people on board.

<details><summary>Document</summary>

  0 R    The fate of Flight FU 9525 that was deliberately crashed into the Alps has chilling similarities to a number of other aircraft  believed to have been downed by flight crew.  
  1 R    Germanwings pilot Andreas Günter Lubitz locked his captain out of the cockpit before ploughing the Airbus A320 into the mountain at more than 400mph, killing all 150 on board.  
  2 ★    The  final moments of the doomed jet were revealed by French prosecutors who said Lubitz's sole aim was to 'destroy the plane'.  
  3 R★   It echoes a number of recent aviation tragedies and could explain what happened to flight MH370 - which vanished last March while flying from Kuala Lumpur to Beijing with 239 people on board.  
  4      Scroll down for video .  
  5      First picture: Germanwings pilot Andreas Günter Lubitz (above) locked his captain out of the cockpit before ploughing the Airbus A320 into the mountain at more than 400mph, killing all 150 on board .  
  6      Germanwings pilot Andreas Günter Lubitz locked his captain out of the cockpit before ploughing the Airbus A320 into the mountain at more than 400mph, killing all 150 on board.  
  7      Above, workers at the crash site today .  
  8      Lubitz's actions could explain what happened to flight MH370 - which vanished last March while flying from Kuala Lumpur to Beijing with 239 people on board.  
  9      Above, file image of a Malaysian Airlines aircraft .  
 10 ★    Recent analysis of satellite data taken from the lost Malaysian Airlines flight indicates the aircraft may have been deliberately flown off course - suggesting the pilot took actions similar to Lubitz's.  
 11      Other pilots believed to be responsible for fatal air crashes include Herminio dos Santos Fernandes, who was captain of Moza LAM flight 470 that crashed in Namibia in November 2013.  
 12      Air crash investigators think the Embraer 190 jet was flown into the ground by the captain after his copilot went to the toilet, killing all 27 passengers and six crew.  
 13      Fernandes was believed to have had serious personal problems at the time of his death.  
 14      When his co-pilot went to the toilet, flight data information recovered from the scene found that Fernandes manually changed the aircraft's altitude from 38,000 feet to almost 600 feet below ground level.  
 15 O    He also pushed the aircraft's throttles back to idle and selected the jet's maximum operating speed.  
 16      Other pilots believed to be responsible for fatal air crashes include Herminio dos Santos Fernandes, who was captain of Moza LAM flight 470 that crashed in Namibia in November 2013.  
 17      Above, the wreckage of the plane .  
 18      Chillingly, the cockpit voice recorder picked up the sound of the co-pilot pounding on the door, similar to Captain Patrick Sondenheimer's attempts to regain access to the flight deck.  
 19      It emerged today that co-pilot Lubitz made similar changes to his autopilot system - entering a new target altitude of just 96ft moments before the crash.  
 20      The first relief officer of an EgyptAir flight was blamed when the aircraft crashed into the Atlantic approximately 30 minutes after leaving John F Kennedy Airport in New York on October 31, 1999.  
 21      The Boeing 767-366 had 14 crew and 203 passengers on board.  
 22      The National Transport Safety Board who investigated the disaster blamed the crash on the flight's relief first officer.  
 23      The first relief officer of an EgyptAir flight was blamed when the aircraft crashed into the Atlantic some 30 minutes after leaving John F Kennedy Airport in New York in 1999.  
 24      Above, debris from the downed plane .  
 25 O    Captain Gamil al-Batouti said he would relieve the current pilot - even though he wasn't due on the flight deck for a further three hours.  
 26      The co-pilot remained with al-Batouti, but when the co-pilot went for a toilet break, the aircraft went into a steep dive and crashed into the sea, killing everyone on board.  
 27      The cockpit flight recorder heard al-Batouti claim in Arabic 'I place my fate in the hands of God' before the aircraft hit the ocean.  
 28 O    El-Batouty even shut down the aircraft's engines, which prevented his co-pilot from saving the aircraft.  
 29      According to the NTSB 'the probable cause of the crash of EgyptAir flight 990 was the airplane's departure from normal cruise flight and subsequent impact with the Atlantic Ocean as a result of the relief first officer's flight control inputs.  
 30      'The reason for the relief first officer's actions was not determined.'  
 31      In December 1997, a Boeing 737 with 97 passengers and seven crew crashed into the Musi River in southern Sumatra, Indonesia.  
 32      The NTSB investigated this crash as it involved a US-built aircraft and determined that the jet crashed due the 'direct flight control inputs' of the pilot, probably the captain.  
 33      However, in both cases, Egyptian and Indonesian authorities do not accept that either of their pilots would have deliberately crashed their own aircraft.  

</details>

---

## 4. `cnn_dm-dev-12500` — gap 22.53 ROUGE (25 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 36.11 | 22.54 | 34.72 |
| abl_position | 59.54 | 43.41 | 58.02 |

**Error category:** ______

**Reference**

> Gang of attention-seeking cats has taken to the 'selfie' trend, snapping candid pictures of themselves .
> The furry frames have been compiled by cat owner Charlie Ellis who scoured the globe for perfect puss pictures .
> He decided to launch the book after his own cat accidentally took a selfie on his tablet - with hilarious results .

**Ours** (sentences [0, 13, 14])

> It seems these pouting pets have been taking tips out of selfie Queen Kim Kardashian's book - as they appear to pose for their own self portraits.
> Social pet-working: It seems these pouting pets have been taking tips out of selfie Queen Kim Kardashian's book - as they appear to pose for their own self portraits for a new book .
> Strike a paws: This gang of attention-seeking cats has taken to the 'selfie' trend, snapping candid pictures of themselves while their owners are seemingly none the wiser.

**abl_position** (sentences [0, 1, 2])

> It seems these pouting pets have been taking tips out of selfie Queen Kim Kardashian's book - as they appear to pose for their own self portraits.
> This gang of attention-seeking cats has taken to the 'selfie' trend, snapping candid pictures of themselves while their owners are seemingly none the wiser.
> The feline frames have been compiled by cat owner Charlie Ellis, from Reading, Berkshire, who has scoured the globe for the perfect puss pictures.

<details><summary>Document</summary>

  0 OR   It seems these pouting pets have been taking tips out of selfie Queen Kim Kardashian's book - as they appear to pose for their own self portraits.  
  1 R★   This gang of attention-seeking cats has taken to the 'selfie' trend, snapping candid pictures of themselves while their owners are seemingly none the wiser.  
  2 R    The feline frames have been compiled by cat owner Charlie Ellis, from Reading, Berkshire, who has scoured the globe for the perfect puss pictures.  
  3      In his book Cat Selfies moggies try their hand at  the craze - with highly amusing results.  
  4      Mr Ellis said: 'My cat accidentally took a photo on my tablet, and it turned out better than my selfies.  
  5      It was so funny I wanted to share the hilarity with everyone.  
  6      Summersdale - my publisher - ran a big competition asking for cat and dog selfies, with the best ones being in the book, and there was a huge response.  
  7      'It's so hard to choose a favourite, Belang - on page 41 - is giving good face and working both paws.  
  8      That cat has really mastered the art of the selfie.  
  9      'It was the most enjoyable few weeks of my life when the pictures were pouring in.  
 10      After publication, Lady Dinah's Cat Emporium in London ran a competition for cat selfies and there were even more fabulous cats.  
 11      Cat Selfies is available from all good retailers, both online and on the high street.  
 12      Scroll down for video .  
 13 O    Social pet-working: It seems these pouting pets have been taking tips out of selfie Queen Kim Kardashian's book - as they appear to pose for their own self portraits for a new book .  
 14 O    Strike a paws: This gang of attention-seeking cats has taken to the 'selfie' trend, snapping candid pictures of themselves while their owners are seemingly none the wiser.  
 15      One of the pets (left) looks ice cool as he poses in the snow, while this bright-eyed moggy steals the spotlight as it poses on a bed .  
 16      Blue steel: This cat is so tasty that even he can't resist a quick lick, and right, this feline seems to have got a handle on the art of the perfect selfie with a flattering side on shot .  
 17      Ready for your close-up?  
 18      These cats don't seem to have quite mastered their best angle, with their somewhat unflattering under chin shots .  
 19      Bright-eyed and bushy tailed:  
 20 ★    The furry frames have been compiled by cat owner Charlie Ellis who has scoured the globe for the perfect puss pic .  
 21      In his book Cat Selfies moggies try their hand at the craze most of their humans have become addicted to posting on social media .  
 22      Mr Ellis said: 'My cat accidentally took a photo on my tablet, and it turned out better than my selfies.  
 23      It was so funny I wanted to share the hilarity with everyone.  
 24      Summersdale - my publisher - ran a big competition asking for cat and dog selfies, with the best ones being in the book, and there was a huge response'  

</details>

---

## 5. `cnn_dm-dev-6824` — gap 20.90 ROUGE (77 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 40.74 | 21.25 | 38.27 |
| abl_position | 61.36 | 41.38 | 60.23 |

**Error category:** ______

**Reference**

> A Delta flight from Atlanta slid off the runway at LaGuardia Airport in New York on Thursday morning upon landing .
> FDNY rushed to the scene as the plane was leaking fuel and had a broken wing, eventually containing the fuel leak .
> The plane skidded off the runway and struck a fence as it landed during blizzard conditions, .
> Aircraft stopped just short of Flushing Bay .
> Reports say 24 people have been injured as all passengers were avacuated .
> LaGuardia shut down immediately after, with all outgoing flights grounded and all incoming flights diverted .
> The airport began reoperating on limited service at 2pm .

**Ours** (sentences [7, 32, 69])

> Scene: A Delta flight slid off the runway at LaGuardia Airport in New York City on Thursday morning .
> We just skidded off the runway."' He added that through it all,, 'no one was screaming, no one was freaking out, and when we came to a dead stop people were actually really calm.'
> As it started to apply the brakes, it started skidding.

**abl_position** (sentences [0, 1, 2])

> A Delta flight went off the runway at LaGuardia Airport in New York City on Thursday morning, stopping just short of Flushing Bay.
> FDNY rushed to the scene as Delta Flight 1086, an MD-88 arriving from Atlanta, skidded off runway 13, was leaking fuel and had a broken wing after striking a fence during blizzard conditions.
> The airport initially reported that the plane had caught fire, though there were no visible signs from the scene.

<details><summary>Document</summary>

  0 R★   A Delta flight went off the runway at LaGuardia Airport in New York City on Thursday morning, stopping just short of Flushing Bay.  
  1 R★   FDNY rushed to the scene as Delta Flight 1086, an MD-88 arriving from Atlanta, skidded off runway 13, was leaking fuel and had a broken wing after striking a fence during blizzard conditions.  
  2 R    The airport initially reported that the plane had caught fire, though there were no visible signs from the scene.  
  3      The plane was immediately evacuated, and all 127 passengers and five crew members were safely removed within 30 minutes of the plane's landing, walking out on the broken wing and going down a slide.  
  4 ★    LaGuardia was shut down soon after the incident as the plane was leaking 300 gallons of fuel at a rate of a gallon a minute, with all incoming flights being diverted and outgoing flights being grounded.  
  5      The fuel leak was quickly contained.  
  6      Scroll down for videos .  
  7 O    Scene: A Delta flight slid off the runway at LaGuardia Airport in New York City on Thursday morning .  
  8      Crash:  
  9      The plane stopped just feet short of Flushing Bay, right outside the runway .  
 10      Emergency: Delta Airlines flight 1086 from Atlanta skidded off a runway while landing at LaGuardia airport in New York on Thursday .  
 11      Smash: Six people suffered non-life-threatening injuries, said Joe Pentangelo, a spokesman for the Port Authority of New York .  
 12      Gas: The crash caused a fuel leak with a gallon of liquid spilling out each minute .  
 13      So close: One passenger took this photo from inside the plane showing just how close it came to the bay .  
 14      A Delta plane rests on a berm near the water at LaGuardia Airport in New York .  
 15      'Look at this sh*t!  
 16      Knew I shoulda stayed my ass at home,' joked New York Giants star Donnell .  
 17      The plane was immediately evacuated, and all 127 passengers and five crew members were safely removed .  
 18      Rescue personnel outside LaGuardia Airport directed emergency vehicles and traffic .  
 19      A map shows the plane's landing, and where it suddenly slid off the runway and almost into the water .  
 20      A few passengers were taken away in ambulances after the crash .  
 21      CNN reports that only minor injuries had been sustained, with the FDNY saying while numerous individuals were being treated only three were transported to a hospital.  
 22      It has been reported that 24 people were injured in total.  
 23      The transcript from the tower shows that the flight was given the all clear to land on the runway and told that the breaking action had been reported as 'good.'  
 24      Once the plane hit the runway it did not respond to the tower, and as soon as the air traffic controllers realized what happened they immediately announced the airport was closed.  
 25      'Customers deplaned via aircraft slides and have moved to the terminal on buses,' Delta said in a statement. '  
 26      Our priority is ensuring our customers and crew members are safe.  
 27      Delta will work with all authorities and stakeholders to look into what happened in this incident.'  
 28      The Port Authority of New York and New Jersey reported that two planes that landed just before the Delta flight reported good breaking on the runway, and that the plane skid roughly 5,000 feet down the runway.  
 29      'I think the pilot did everything he could to slow the aircraft down,' said Port Authority head Patrick J. Foye during a news conference.  
 30      I'm not even sure what went through my mind because you're not even sure what's happening,' said passenger Mark Clafter.  
 31      'And then it wasn't until the plane came to a stop that all of the sudden you think, 'Holy cow!  
 32 O    We just skidded off the runway."' He added that through it all,, 'no one was screaming, no one was freaking out, and when we came to a dead stop people were actually really calm.'  
 33      He said that when they stopped all power went out and the pilot had no way of speaking to the passengers, but even then no one panicked.  
 34      In this photo provided by passenger Amber Reid, passengers are seen being evacuated from the plane .  
 35      A passenger is wheeled on a stretcher through snowfall by emergency medical services workers at LaGuardia .  
 36      Emergency: Delta Flight 1086, carrying 125 passengers and five crew members, veered off the runway at around 11:10 a.m .  
 37      The FDNY said three people was transported from the scene .  
 38      New York Fire department personnel stage outside LaGuardia Airport .  
 39      This image shows Delta flight 1086 from Atlanta after it skidded off the runway .  
 40      One Instagram user shared this snap of the plane after the crash .  
 41      Port Authority Executive Director Pat Foye said at a news conference that the airport would reopen today .  
 42      Ambulances outside LaGuardia Airport after Delta Airlines flight 1086 from Atlanta, Georgia, skidded off a runway on landing .  
 43      One of the passengers, Jamie Primak, who stars on the Bravo reality show Jersey Belle, wrote; 'We just crash landed at LGA.  
 44      I'm terrified.  
 45      Please...' She later wrote; 'We have all been evacuated.  
 46      Everyone is safe.  
 47      Thank you for your prayers.  
 48      God is good.'  
 49      New York Giants tight end Larry Donnell was also on the plane and shared a photo and video on Instagram as he evacuated on the runway, joking; 'Look at this sh*t!  
 50      Knew I shoulda stayed my ass at home.'  
 51      He later released a statement saying; 'I feel fine physically and hopefully all the other passengers did not have any significant injuries We were all shocked and alarmed when the plane started to skid, but most importantly, as far as I know, all of the passengers and flight crew were able to exit the plane safely.'  
 52      A woman named Vanessa also shared a photo as she left the plane, writing; '#survive #crashlanding #noinjuries.'  
 53      Now some are questioning whether the airport should have even been open during these snowy and icy conditions.  
 54      Though the runway had reportedly been plowed shortly before the landing, there were three inches of snow measured near the airport for the day.  
 55      Members of a family, who said they were on Delta flight 1086 which arrived from Atlanta, embrace at the baggage claim area .  
 56      The FDNY shared this photo of the plane taken from a boat on Flushing Bay .  
 57      Monitors at LaGuardia Airport's Terminal D display canceled flights in New York .  
 58      Delta flight 1086 is seen after it slid off the runway with New York City in the background .  
 59      Ambulances are seen at LaGuardia Airport's Terminal D during a snow storm in New York .  
 60      The pilots were hanging over the water in the cockpit after the crash .  
 61      Emergency medical services workers direct passengers towards an ambulance at LaGuardia Airport's Terminal D .  
 62      Slid off runway: The plane was evacuated in under 30 minutes .  
 63      One passenger named Steve  stressed just how scary it was inside the plane, writing; 'The pics are deceptive.  
 64      That is side of runway.  
 65      We were going in water until hit the hill and spun.  
 66      #crashland.'  
 67      The plane's nose was on the rocks that surround the bay.  
 68      'We came in for landing, the plane hit the ground.  
 69 O    As it started to apply the brakes, it started skidding.  
 70      It didn’t spin around or anything,' passenger Sam Stern told the New York Post. '  
 71      It ended up hitting the embankment.  
 72      The wing broke off.'  
 73      '2 seconds more we would have been in the water!'  
 74      wrote Jared Faellaci, who posted a photo of the view from his window.  
 75      MSNBC thought they had managed to score an interview with Donnell shortly after the crash, but it turned out to be an impostor who said live on air 'F**k her right in the p***y.'  
 76      The FAA has announced the airport will open again at 2pm with limited service.  

</details>

---

## 6. `cnn_dm-dev-8105` — gap 20.67 ROUGE (23 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 34.78 | 14.16 | 29.57 |
| abl_position | 56.05 | 29.68 | 54.78 |

**Error category:** ______

**Reference**

> Iskander Ehet, Turgun Tohtunyaz and Hasayn Muhammad were executed .
> Comes after their role in a knife attack at Kunming railway station last year .
> The incident saw masked men kill 31 people with knives and machetes .
> The attack which injured 141 people was dubbed as 'China's 9/11'
> Men were convicted of intentional homicide and being in a terrorist group .
> But campaigners have said they may not have been granted a fair trial .

**Ours** (sentences [6, 12, 17])

> The attack in Kunming, in the south western province of Yunnan, was dubbed as 'China's 9/11' by state-run media.
> Police shot four other assailants dead at the time of incident.
> The scene outside the railway station after the attack.

**abl_position** (sentences [0, 1, 2])

> Three Chinese separatists who were involved in an a knife attack that killed 31 people at a train station last year have been executed.
> The three men, Iskandar Ehet, Turgun Tohtunyaz and Hasayn Muhammad were all put to death for their role in the attack at Kuming railway station, which also saw more than 140 people wounded.
> The Supreme People's Court confirmed that the executions had taken place after the men were convicted of 'leading a terrorist organisation and intentional homicide' in September.

<details><summary>Document</summary>

  0 R★   Three Chinese separatists who were involved in an a knife attack that killed 31 people at a train station last year have been executed.  
  1 R★   The three men, Iskandar Ehet, Turgun Tohtunyaz and Hasayn Muhammad were all put to death for their role in the attack at Kuming railway station, which also saw more than 140 people wounded.  
  2 R    The Supreme People's Court confirmed that the executions had taken place after the men were convicted of 'leading a terrorist organisation and intentional homicide' in September.  
  3      A police investigator inspects the scene at Kunming railway station in the aftermath of a mass knife attack, which killed 31 people.  
  4      Three men have now been executed for their role in the attack .  
  5      The attack also left 141 people injured and Chinese state run media dubbed the incident as 'China's 9/11' China uses both lethal injection and firing squad for executions, but the method used this time was not specified.  
  6 O    The attack in Kunming, in the south western province of Yunnan, was dubbed as 'China's 9/11' by state-run media.  
  7      Dressed in black and wielding long knives and machetes, several assailants stormed the station on March 1, 2014 seemingly hacking at anyone in sight.  
  8      Distressing photos circulating online showed bodies, pools of blood and abandoned luggage scattered across the terminal floor in the wake of what authorities termed an 'organised, premeditated, violent terrorist attack'.  
  9      A female attacker, Patigul Tohti, was pregnant at the time of her arrest and was sentenced to life in prison.  
 10      Chinese policemen patrol the area outside the station after the attack.  
 11      Beijing blamed the attack on 'separatists' from the resource-rich far western Xinjiang region .  
 12 O    Police shot four other assailants dead at the time of incident.  
 13      Beijing blamed the attack on 'separatists' from the resource-rich far western Xinjiang region, where at least 200 people have died in attacks and clashes between locals and security forces over the last year.  
 14      The remote autonomous region, which borders Central Asia, is home to the mostly Muslim Uighur minority.  
 15 ★    But campaign groups have accused China of preventing the men from having a fair trial.  
 16      Dilxat Raxit, a spokesman for the Munich-based World Uyghur Congress said: 'China is using the death penalty for political means in order to avoid the root cause of the problem.'  
 17 O    The scene outside the railway station after the attack.  
 18      Dressed in black and wielding long knives and machetes, several assailants stormed the station on March 1, 2014 seemingly hacking at anyone in sight .  
 19      'The defendants did not get a dignified trial and China used this event to incite discrimination against Uighurs.'  
 20      However, China has vowed to step up punishment of 'violent terrorists', and is drafting its first-ever anti-terrorism law.  
 21      Chinese courts convicted 712 people on terrorism-related charges last year, an increase of more than 13 per cent, according to chief justice Zhou Qiang.  
 22      The country executes more people than the rest of the world combined, according to rights organisations, and put an estimated 2,400 people to death in 2013.  

</details>

---

## 7. `cnn_dm-dev-1004` — gap 7.35 ROUGE (54 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 15.50 | 0.00 | 15.50 |
| abl_position | 23.84 | 6.71 | 22.52 |

**Error category:** ______

**Reference**

> A large crowd walks the footsteps of those who marched 50 years ago .
> They are crossing the Edmund Pettus Bridge, named for a former KKK leader .
> President Obama called Saturday for renewal of Voting Rights Act .

**Ours** (sentences [0, 26, 38])

> Selma, Alabama (CNN)Crowds massed at a bridge in Selma, Alabama, Sunday to remember and reflect upon the sacrifices of another crowd that gathered at the same bridge half a century ago on a day that came to be known as "Bloody Sunday."
> Not because the change they won was preordained; not because their victory was complete; but because they proved that nonviolent change is possible; that love and hope can conquer hate."
> There's still work to be done," said Lewis, adding this is an opportunity to "redeem the soul of America."

**abl_position** (sentences [0, 1, 5])

> Selma, Alabama (CNN)Crowds massed at a bridge in Selma, Alabama, Sunday to remember and reflect upon the sacrifices of another crowd that gathered at the same bridge half a century ago on a day that came to be known as "Bloody Sunday."
> Walkers marched across the Edmund Pettus Bridge in the afternoon to commemorate those freedom-marchers who were clubbed and tear-gassed by state troopers as they peacefully filed across on March 7, 1965.
> The protest decades ago against the denial of civil rights to Americans based solely on the color of their skin, and the television coverage of the bludgeoning dealt them, hastened the passage of the Voting Rights Act of 1965.

<details><summary>Document</summary>

  0 OR   Selma, Alabama (CNN)Crowds massed at a bridge in Selma, Alabama, Sunday to remember and reflect upon the sacrifices of another crowd that gathered at the same bridge half a century ago on a day that came to be known as "Bloody Sunday."  
  1 R    Walkers marched across the Edmund Pettus Bridge in the afternoon to commemorate those freedom-marchers who were clubbed and tear-gassed by state troopers as they peacefully filed across on March 7, 1965.  
  2      The crowd was massive.  
  3      It was shoulder to shoulder near the bridge and several blocks away.  
  4      There were so many people that walking is a bit misleading -- people just really moved inch by inch along the way.  
  5 R    The protest decades ago against the denial of civil rights to Americans based solely on the color of their skin, and the television coverage of the bludgeoning dealt them, hastened the passage of the Voting Rights Act of 1965.  
  6      On Sunday at Selma's Brown Chapel AME, a historically black church, leaders in the religious and political realm as well as community organizers gathered to hear speeches, sing hymns and remember what happened 50 years ago.  
  7      U.S. Attorney General Eric Holder was in the audience.  
  8      Rev. Jesse Jackson spoke, as did Rev. Al Sharpton.  
  9      An important figure in the decades-long fight for civil rights, former Atlanta Mayor and U.N. Ambassador Andrew Young remembered the struggle in the 1960s but wanted everyone to keep pushing forward and thinking about achieving economic equality today.  
 10      "We've got to focus on ourselves not as problems but as visionaries," he said.  
 11      "We have come a long, long way, but I have enjoyed every bit of it," Young remarked.  
 12      Several people remarked at how much it meant that the day before, on Saturday, America's first African-American President, Barack Obama, made a rousing speech on racial progress in a diverse country.  
 13      He said that the struggle against discrimination continues today.  
 14      Looking back, the "Bloody Sunday" march was triggered when a law officer shot a black man dead the month before.  
 15      But it was about more -- the right to vote for all Americans.  
 16      About 600 people were going to march 50 miles to the state capital in Montgomery before they were forcibly stopped.  
 17      Sunday's festivities started with a breakfast and end late with a dance.  
 18      A string of parades, receptions, reflections, films and discussions will fill the time in between.  
 19      The  commemoration marking 50 years since "Bloody Sunday" continues on Monday.  
 20      "Our march is not yet finished.  
 21      But we are getting closer," Obama said Saturday, his words echoing into a crowd of thousands lined up in front of him.  
 22 ★    Obama emphasized that a day of commemoration is not enough to repay the debt paid by the marchers who were beaten 50 years ago as they demonstrated for voting rights.  
 23 ★    "If Selma taught us anything, it's that our work is never done," the President said near Edmund Pettus Bridge.  
 24      Read President Obama's prepared remarks .  
 25      The President said that what civil rights marchers did years ago "will reverberate through the ages.  
 26 O    Not because the change they won was preordained; not because their victory was complete; but because they proved that nonviolent change is possible; that love and hope can conquer hate."  
 27      He hailed the marchers as heroes.  
 28      The President said that "the Americans who crossed this bridge, they were not physically imposing, but they gave courage to millions.  
 29      They held no elected office.  
 30      But they led a nation."  
 31      The President called on Congress to restore the Voting Rights Act, first passed in 1965.  
 32      In 2013, the U.S. Supreme Court overturned a key provision of the law that required certain states with a history of racial discrimination at the polls to "pre-clear" any changes to the law with the federal government before implementing them.  
 33      Efforts to revive key provisions of the act have stalled in Congress.  
 34      50 years later: Memories from 'Bloody Sunday' nurse .  
 35      Many of the nation's leaders, activists and celebrities were in Selma on Saturday attending various activities taking place in memory of the historic event.  
 36      On Saturday, Rep. John Lewis -- one of the demonstrators bloodied by troopers 50 years ago -- and nearly 100 other members of Congress from both parties joined the President at the bridge in Selma -- a bridge that still bears the name of Pettus, a Confederate general who was also a Ku Klux Klan leader.  
 37      "We must use this moment to recommit ourselves to do all we can to finish this work.  
 38 O    There's still work to be done," said Lewis, adding this is an opportunity to "redeem the soul of America."  
 39 ★    John Lewis's memories of the march .  
 40      Reflecting a sense of change in the half century since "Bloody Sunday," and with Selma again in a national media spotlight, the mood in the crowd Saturday was of unity, and talks were focused on how to move America forward.  
 41      But some current Selma residents worried that after the dignitaries leave their town -- with a population 82% black and with more than 40% of its people living below the national poverty level -- will fade from view except for its historical significance.  
 42      Geraldine Martin, 59, has lived in Selma all her life.  
 43      She was 9 years old on "Bloody Sunday" and with her mother had just welcomed a little sister, Belinda, to the world on that day.  
 44      The two sisters grew up in Selma less than a decade apart.  
 45      Opinion: Selma's historic bridge deserves a better name .  
 46      Belinda left Selma after high school and now lives in Atlanta.  
 47      Her view of Selma has changed over the years -- looking in from the outside.  
 48      "I don't see how Selma will move forward without togetherness," said Belinda.  
 49      "There is no diversity in Selma.  
 50      People don't live together."  
 51      CNN's Moni Basu reported from Selma.  
 52      CNN's Slma Shelbayah wrote and reported from Atlanta.  
 53      CNN's Steve Almasy and Douglas Brinkley contributed to this report.  

</details>

---

## 8. `cnn_dm-dev-8675` — gap 7.30 ROUGE (52 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 31.40 | 3.36 | 21.49 |
| abl_position | 39.73 | 5.56 | 32.88 |

**Error category:** ______

**Reference**

> Michelle Hennessy killed herself year after attack by Sean Thackaberry .
> Sharon won legal landmark case of conviction without evidence from twin .
> Hired lawyer, pestered police for case to be pursued and trial went ahead .
> Thackaberry was jailed for five years at Dublin Crown Court .

**Ours** (sentences [0, 1, 16])

> A woman has told how she fulfilled a promise to her twin when she successfully fought to get her sex attacker jailed after she committed suicide.
> In a landmark legal case, Sharon Hennessy, 30, won justice for her sister Michelle who killed herself aged 27 in October 2012, a year after she was punched, kicked and sexually abused as she walked home from a night out.
> They sent her abusive messages online too, calling her a liar.

**abl_position** (sentences [0, 1, 2])

> A woman has told how she fulfilled a promise to her twin when she successfully fought to get her sex attacker jailed after she committed suicide.
> In a landmark legal case, Sharon Hennessy, 30, won justice for her sister Michelle who killed herself aged 27 in October 2012, a year after she was punched, kicked and sexually abused as she walked home from a night out.
> At the time of Michelle's death, police were pursuing a rape case against her attacker Sean Thackaberry, but they said they would close it because there was no chance of a conviction without her evidence.

<details><summary>Document</summary>

  0 OR   A woman has told how she fulfilled a promise to her twin when she successfully fought to get her sex attacker jailed after she committed suicide.  
  1 OR   In a landmark legal case, Sharon Hennessy, 30, won justice for her sister Michelle who killed herself aged 27 in October 2012, a year after she was punched, kicked and sexually abused as she walked home from a night out.  
  2 R    At the time of Michelle's death, police were pursuing a rape case against her attacker Sean Thackaberry, but they said they would close it because there was no chance of a conviction without her evidence.  
  3      Michelle (left) and her twin Sharon, pictured together on their 21st birthday.  
  4      Michelle committed suicide a year about being attacked after a night out.  
  5      Sharon reveals how she fought to bring her sister's attacker to justice .  
  6 ★    Sean Thackaberry was jailed for five years in a landmark case over attacking Michelle Hennessy .  
  7      But Sharon, of Kildare Town, Ireland, had promised her beloved twin she would not let her attacker walk free.  
  8      The pledge was important to Sharon because after initially being charged with rape, Thackaberry was released on bail – and Michelle said she did not feel safe while he was on the streets.  
  9      The family believe this was one of the reasons Michelle took her own life.  
 10      Sharon reveals how Michelle - who was a fan of skydiving and nights out - changed after the attack.  
 11      She said: ‘She was afraid and vulnerable and instead of travelling to far-flung corners like she had done, she spent her time sat by the fire, knitting.  
 12      ‘I hardly ever saw her put on make-up  
 13      and she never went out with friends, like she used to.  
 14      ‘She’d been so proud of her girly locks and her sense of fashion, but afterwards she didn’t care.  
 15      ‘We were furious that Thackaberry hadn’t been locked up and whenever Michelle left the house, his supporters would harass her.  
 16 O    They sent her abusive messages online too, calling her a liar.  
 17      ‘The taunts and threats ground her down until she didn’t feel human anymore.’  
 18      In October 2012 Michelle committed suicide at home.  
 19      Her sister recalled finding out – and desperately trying to reach her twin’s body.  
 20      She said: ‘I remember collapsing onto the stairs and screaming from the bottom of my belly.  
 21      ‘I screamed for all the pain and emotion that my twin sister was never able to scream.  
 22      I screamed for the devastation she buried inside her, until it slowly destroyed every inch of her being.  
 23      ‘I screamed for the anger she felt at not being protected from the monster who stole her life.  
 24      It was devastating.’  
 25      Michelle (left) and Sharon, pictured at three years old, had always been close and Sharon vowed to see her sister's attacker jailed, hiring a top lawyer and pestering police to keep the case open .  
 26      Sharon, pictured at her 30th birthday (left) along with a tribute to her sister at the event (right) Michelle (right) and Sharon pictured together on their 27th birthday .  
 27      Sharon was heartbroken when a lawyer told her family the ongoing case against Thackaberry would ‘never see the light of day’ because of her sister’s death.  
 28      ‘It felt like the final nail in Michelle’s coffin,’ she said.  
 29      ‘I felt like that monster was going to win – again.’  
 30 ★    So she hired a top lawyer and repeatedly pestered the police for the case to be pursued – and the trial went ahead.  
 31      In November 2013 Thackaberry, then 20, of Kildare Town, Ireland, appeared at Dublin’s Central Criminal Court where he admitted aggravated sexual assault.  
 32      The court was told the former boxer had violently assaulted Michelle as he walked her home, dragging her onto wasteland around 250m from her home.  
 33      Michelle pictured after skydiving in Spain.  
 34      Her sister Sharon reveals how Michelle changed after the attack and wouldn't leave the house .  
 35      Michelle - pictured (left) skydiving in Spain, and (right) on a night out afterwards - committed suicide a year after she was attacked by Sean Thackaberry after a night out .  
 36      Remembering how Michelle felt after being attacked, her sister said: ‘She told me, “I thought I was going to die”.’  
 37      Sharon told how Thackaberry winked at her as he was jailed for five years at Dublin’s Central Criminal Court.  
 38      Her sister said: ‘I’d made my sister that promise.  
 39      ‘The lawyer said there hadn’t been a case in Irish history like Michelle’s, where someone was convicted after the victim had died.  
 40      But we wouldn’t give up.  
 41      ‘Michelle was dead because of what that man did to her.  
 42      ‘We had hoped he would be prosecuted for rape, but it meant so much that Thackaberry had finally admitted what he’d done.  
 43      ‘His sentence wasn’t long enough for what he’d done, but we were so relieved that we finally had justice for Michelle.’  
 44      She said she was now fighting for other victims.  
 45      ‘They weren’t even going to look at her case and didn’t believe Michelle deserved justice,’ she said.  
 46      ‘Michelle’s case set a precedent for future court cases.  
 47      Hopefully there won’t be other victims like Michelle.  
 48      But if there is, they won’t just be forgotten, like Michelle threatened to be.  
 49      ‘People think it’s bad to talk about these things but, in fact, it’s one of the most important things in the world.  
 50      ‘Because it’s only by talking about them that more women who feel lost like Michelle will go and get help.’  
 51      In the year after her sister's death, Sharon has helped raise more than €30,000 (£21,000) for suicide awareness.  

</details>

---

## 9. `cnn_dm-dev-7484` — gap 7.16 ROUGE (28 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 35.46 | 8.63 | 29.79 |
| abl_position | 44.14 | 13.99 | 37.24 |

**Error category:** ______

**Reference**

> Wild elephants get a 'natural pedicure' by rubbing their feet in the dirt .
> But captive animals can get foot problems if their toenails aren't trimmed .
> Researcher from the University of Queensland, Australia, has developed a pressure pad to measure the pressure exerted on elephants' feet .
> Data could inform the best way to trim toenails and allow zookeepers to spot potential foot problems, which can lead to elephants being put down .

**Ours** (sentences [11, 21, 22])

> Three elephants passed smell tests conducted on a game reserve in South Africa.
> Working with Zebris Biomechanix in Germany, she has developed pressure platforms to measure the pressure and forces applied to elephants’ feet while they are walking.
> ‘The plates were recently transported to the Adventures with Elephants safari park in South Africa to study the foot pressures of elephants kept in semi-wild conditions with natural terrains,’ she said.

**abl_position** (sentences [0, 1, 2])

> You may have experienced the eye-watering pain of an ingrown toenails, but imagine if you weighed 15,000 lbs (7,000 kg).
> Scientists are working to prevent painful and potentially deadly foot diseases in captive elephants by finding the best way to trim their feet.
> Wild elephants benefit from walking long distances on different surfaces and rubbing their feet in abrasive dirt, but their captive peers can experience problems without these ‘natural pedicures’.

<details><summary>Document</summary>

  0 R    You may have experienced the eye-watering pain of an ingrown toenails, but imagine if you weighed 15,000 lbs (7,000 kg).  
  1 R    Scientists are working to prevent painful and potentially deadly foot diseases in captive elephants by finding the best way to trim their feet.  
  2 R★   Wild elephants benefit from walking long distances on different surfaces and rubbing their feet in abrasive dirt, but their captive peers can experience problems without these ‘natural pedicures’.  
  3      Scroll down for video .  
  4 ★    Scientists are working to prevent painful and potentially deadly foot diseases in captive elephants by finding the best way to trim their feet (a stock image is shown) Captive elephants’ feet are routinely trimmed to counter the effects of walking on unnatural ground in restricted spaces, but experts are trying to perfect the most functional pachyderm pedicure.  
  5      Dr Olga Panagiotopoulou, from the University of Queensland’s School of Biomedical Sciences, is working with collaborators around the world to understand how captivity influences elephant foot form and function, as well as identifying the best method of preventative foot trimming.  
  6      ‘Elephants are the largest terrestrial mammals alive today and can weigh up to eight tonnes, with their whole body mass supported by their tiny feet,’ Dr Panagiotopoulou said.  
  7      Wild elephants (a stock image is shown) benefit from walking long distances on various surfaces and rubbing their feet in dirt, but their captive peers can experience problems without these ‘natural pedicures’ Pressure plates were  transported to the Adventures with Elephants safari park in South Africa (pictured) to study the foot pressures of elephants kept in semi-wild conditions with natural terrains .  
  8      ‘We know that when these large animals walk, a huge amount of pressure is applied to their feet.  
  9      Earlier this month, researchers found that elephants excel at identifying explosives by smell, stirring speculation about whether their extraordinary ability could save lives.  
 10      Elephants could be used to detect land mines in areas that have seen conflict and could even do so at a distance with the aid of drones.  
 11 O    Three elephants passed smell tests conducted on a game reserve in South Africa.  
 12      Sniffing at buckets, they were rewarded with a treat of marula - a tasty fruit - when they showed that they recognised samples of TNT by raising a front leg.  
 13      The elephants detected TNT samples 73 out of the 74 times that they encountered in a line of buckets, according to Ashadee Kay Miller, a zoology student at the University of the Witwatersrand in Johannesburg.  
 14      They only got this wrong 3.6 per cent of the time over 502 buckets that contained the explosive, which was dissolved in acetone on filter paper.  
 15      In a second set of tests, the elephants scored 100 percent, detecting TNT in 23 out of 23 buckets when ‘distractor odours’ such as tea, bleach, soap and gasoline were placed in the other buckets, she said.  
 16      It's been suggested that unmanned drones could collect scent samples from mined areas and bring them to a trained elephant, which would smell them and alert handlers to any sign of explosives.  
 17      ‘Preliminary data has indicated that foot pressure is more evenly distributed across the sole of the foot when the animals walk on natural grounds, but when they are walking on surfaces such as concrete the pressure is concentrated around parts of the foot that are more prone to disease, such as the lateral toes.’  
 18      She said that while a range of foot-trimming procedures are followed and typically involve filing the nails and rough skin, none have been tested.  
 19      Elephants' toenails typically grow between five and seven millimetetres a month.  
 20      ‘Our research involves testing different techniques to see which one will be most beneficial for the animal,’ Dr Panagiotopoulou said.  
 21 O★   Working with Zebris Biomechanix in Germany, she has developed pressure platforms to measure the pressure and forces applied to elephants’ feet while they are walking.  
 22 O    ‘The plates were recently transported to the Adventures with Elephants safari park in South Africa to study the foot pressures of elephants kept in semi-wild conditions with natural terrains,’ she said.  
 23      ‘The elephants were trained to walk over the pressure platforms and the individual footsteps were processed using a state-of-the-art neuroimaging technique called statistical parametric mapping, which, in simple words, gives us a high-resolution image of foot pressure changes over the foot.  
 24      ‘We hope to develop smaller versions of these pressure platforms for zoo keepers and managers to use as diagnostic tools.  
 25      ‘If a captive elephant walks over a pad and a different digital pressure pattern from normal is seen, this can be investigated further.’  
 26      Dr Panagiotopoulou said that early diagnosis is important because elephant foot diseases such as osteoarthritis and osteomyelitis are often diagnosed too late for treatment, meaning elephants have to be euthanized.  
 27      Dr Olga Panagiotopoulou, from the University of Queensland’s School of Biomedical Sciences, is working with collaborators around the world to understand how captivity influences elephant foot form and function, as well as identifying the best method of preventative foot trimming (a stock image of a man cutting toenails is shown)  

</details>

---

## 10. `cnn_dm-dev-11354` — gap 6.89 ROUGE (46 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 18.60 | 3.15 | 15.50 |
| abl_position | 26.56 | 7.94 | 23.44 |

**Error category:** ______

**Reference**

> Sister plane of that involved in today's crash lost altitude late last year .
> Air safety agency sent out directive warning operators to be aware .
> Pilot in that incident pulled the plane out of the dive averting problems .
> Airbus A320s involved in number of accidents since introduced in 1980s .
> Plane is considered extremely safe and is widely used around world .

**Ours** (sentences [18, 26, 38])

> It was then purchased by Lufthansa and had its first commercial flight in February 1991.
> In contrast, take-off and the initial climb accounts for 14 per cent of crashes, while final approach and landing accounts for 47 per cent.
> It typical seats around 150 passengers depending on the layout of the plane and has a cruising speed of 511mph and a range of up to 7,500 miles.

**abl_position** (sentences [0, 1, 2])

> Only the quick thinking of a pilot averted a similar tragedy last year when a sister plane of the Germanwings jet suddenly lost altitude and nose-dived.
> A Lufthansa A321 – a longer version of the A320 – unexpectedly descended 3,000ft while cruising over Pamplona, Spain, last November.
> The jet, with 109 passengers and crew aboard, was at an altitude of 31,000ft when it started to lose height.

<details><summary>Document</summary>

  0 R    Only the quick thinking of a pilot averted a similar tragedy last year when a sister plane of the Germanwings jet suddenly lost altitude and nose-dived.  
  1 R    A Lufthansa A321 – a longer version of the A320 – unexpectedly descended 3,000ft while cruising over Pamplona, Spain, last November.  
  2 R    The jet, with 109 passengers and crew aboard, was at an altitude of 31,000ft when it started to lose height.  
  3      The flight crew managed to regain control at 28,000ft.  
  4      Scroll down for video .  
  5 ★    The Germanwings Airbus involved in today's crash (pictured) would have received a safety warning after a sister plane suddenly lost altitude last year.  
  6 ★    In that incident, the problem was corrected by the pilot .  
  7      According to the European Air Safety Agency, a safety system designed to protect the jet reacted to incorrect data due to a faulty sensor.  
  8      The safety warning related to all Airbus A318, A319, A320 and A321 – including the Airbus A320 involved in today’s disaster.  
  9      In response, Airbus created a ‘temporary revision’ to all of the aircraft's flight manuals.  
 10      The EASA determined that the Lufthansa aircraft's Angle of Attack probes got blocked while flying between Bilbao and Munich.  
 11      The EASA warned that in such a situation 'the flight control laws order a continuous nose down pitch rate that, in a worst case scenario, cannot be stopped with backward sidestick inputs, even in the full backward position.'  
 12      The agency added: 'This condition, if not corrected, could result in loss of control of the aeroplane.'  
 13      A similar Airbus plane to that involved in today's crash was put down in the Hudson River, New York in 2009 .  
 14      In that incident, the pilot managed to crash land in the river and the passengers were saved after a bird strike .  
 15      The A321 involved in the previous incident is a slightly longer version of the plane involved in today's crash, carrying an extra 40 passengers.  
 16      Germanwings today confirmed that today's downed aircraft underwent a major inspection at Lufthansa in summer 2013 while it was last checked yesterday.  
 17      The plane that crashed was called 'Mannheim' and made its first test flight in November 1990.  
 18 O    It was then purchased by Lufthansa and had its first commercial flight in February 1991.  
 19      Experts said the aircraft would have been nearing the end of its commercial life after more than 24 years of service.  
 20      Since the first version of the Airbus A320 was released in 1987, around 4,000 have been built and the company say one takes off or lands somewhere in the world every 2.5 seconds.  
 21      The A320 plane is a workhorse of modern aviation.  
 22      Worldwide, 3,606 A320s are in operation, according to Airbus.  
 23      The A320 family has a good safety record, with just 0.14 fatal accidents per million take-offs, according to a Boeing safety analysis.  
 24      The safest part of a flight is when the plane is at cruise elevation.  
 25      Just 10 per cent of fatal accidents occur at that point.  
 26 O    In contrast, take-off and the initial climb accounts for 14 per cent of crashes, while final approach and landing accounts for 47 per cent.  
 27      The A320 is certified to fly up to 39,000ft, its maximum altitude before its rate of climb begins to erode.  
 28 ★    However, the widely-used A320 family of aircraft have been involved in a number of crashes in the three decades they have been used, resulting in scores of deaths.  
 29      In December an Airbus A320 crashed into the Java Sea killing all 162 people on board in an as-yet unexplained incident.  
 30      The plane operated by AirAsia – owned by QPR chairman Tony Fernandes – vanished from radar screens in bad weather with initial reports suggesting it climbed so fast into a storm that it lost lift and plunged into the sea.  
 31      One the first accident to involve one of the planes happened in the north east of France, not far from the current crash site, when an Air Inter flight came down in the Vosges mountains in 1992.  
 32      The Airbus A320-111 was on its approach to Strasbourg airport when it hit La Bloss Mountain, killing 87 of the 96 people on board.  
 33      Safe: Aviation experts tweeted this graphic showing just how many Airbus A320s are in the air at any time .  
 34      The best-known recent incident involving the plane was when a domestic flight in the US had to put down in the Hudson River in New York.  
 35      The US Airways flight from the city's LaGuardia Airport heading for Charlotte, North Carolina when it is believed to have flown into a flock of geese.  
 36      The Airbus A320 like that involved in today's accident iS a short-haul, narrow-body airliner assembled in France, Germany and China.  
 37      Around 4,000 of the single-aisle aircraft have been built and Airbus says the plane 'sets industry standards for comfort and operating economy on short- to medium-haul routes'.  
 38 O    It typical seats around 150 passengers depending on the layout of the plane and has a cruising speed of 511mph and a range of up to 7,500 miles.  
 39      It was ranked as the world's fastest selling aircraft bewteen 2005 and 2007 when it became popular with low-cost airlines.  
 40      Captain Chesley Sullenberger was widely praised for landing the plane on the river, meaning none of the 155 people on board were seriously injured.  
 41      One of the deadliest accidents involving one of the planes was in May 2006, when Armavia flight 967 crashed into the sea near Sochi, Russia.  
 42      All 113 passengers and crew on the A320-211 died after it flew into terrible weather while approaching the southern Russian city after taking off from Yerevan, Armenia.  
 43      Six years earlier, 143 people, including two Britons, lost their lives when a Gulf Air Airbus A320-212 went down in the Gulf of Bahrain after a three-long flight from Cairo.  
 44      A number of factors were blamed for the night-time crash, including pilot error and poor training of staff.  
 45      An Airbus A320 was  involved in a crash near Sochi, Russia in 2006 which killed 113 passengers and crew .  

</details>

---

## 11. `cnn_dm-dev-547` — gap 5.24 ROUGE (87 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 23.53 | 4.00 | 19.61 |
| abl_position | 28.81 | 8.62 | 25.42 |

**Error category:** ______

**Reference**

> "New Day" Digital Producer Jessica Moskowitz was diagnosed with a brain tumor in September .
> Moskowitz, then 28, was at work when she began to feel strange symptoms and was rushed to the hospital .
> After surgery and ongoing rehabilitation, she says, she gained an appreciation for life she'd never had .

**Ours** (sentences [24, 31, 35])

> My family and I were scheduled to meet with a brain surgeon the next morning.
> I don't remember what I asked him after that, but once he left, I felt hopeless and alone.
> He suspected that the tumor was slowly growing deep in the left ventricle of my brain for years.

**abl_position** (sentences [0, 2, 5])

> (CNN)I've dressed up in the same type of costume on Halloween for years -- always a superhero.
> "Just any excuse to put on a wig and a cape," I'd tell friends.
> See, this Halloween was different: I'd been diagnosed with a brain tumor just weeks before, and donning this costume was a lighthearted way to feel empowered ahead of the biggest fight of my life.

<details><summary>Document</summary>

  0 R    (CNN)I've dressed up in the same type of costume on Halloween for years -- always a superhero.  
  1      Not one character in particular.  
  2 R    "Just any excuse to put on a wig and a cape," I'd tell friends.  
  3      Last year, I found a more specific persona.  
  4      I would be Wonder Woman.  
  5 R★   See, this Halloween was different: I'd been diagnosed with a brain tumor just weeks before, and donning this costume was a lighthearted way to feel empowered ahead of the biggest fight of my life.  
  6      It was Saturday, October 25, 2014 -- earlier than usual for me to think about a costume for my favorite holiday.  
  7      But this year, I wouldn't be able to party on the same day as everyone else.  
  8      I was organizing one last massive celebration to honor my life and the people I love before my brain surgery two days later.  
  9 ★    It all started early one morning in September while I was wrapping up my work as a digital producer for CNN's "New Day."  
 10      As I was typing at the computer, letters were dropping off the right side of the screen.  
 11      I started to feel strange and went to the nurse's office in my building to ask for help.  
 12      My speech began to slur, my hands were tingling, and my head was pounding.  
 13      I also forgot my co-workers' and bosses' names.  
 14      The nurse thought I could be having a stroke and called an ambulance.  
 15      Within an hour, I went from thinking I might have a migraine because I needed new glasses to being rushed to the hospital.  
 16      I was 28 years old.  
 17      They stripped off my clothes in the emergency room to hook me up to the machines that would reveal I wasn't having a stroke.  
 18      Great news!  
 19      But then, what was going on?  
 20      First Person: Shopping for a new coat unleashes old memories .  
 21      After an MRI, we had the beginning of an answer.  
 22      When I looked at the scan of my brain, sitting there, big as an orange, in the left hemisphere was a large black spot.  
 23      My speech came back fully after a few hours, but a terrible headache lingered all day, and I was kept in the hospital overnight without discussing with the medical staff the full details of what was found on the scan.  
 24 O    My family and I were scheduled to meet with a brain surgeon the next morning.  
 25      About 6 a.m., I was asleep when a resident came into my room and woke me up.  
 26      He wanted to talk about my case, he said.  
 27      "My parents are coming later, and we're meeting with the doctor," I told this stranger.  
 28      "Ms. Moskowitz, we suspect you have a meningioma."  
 29      He could have been speaking Russian.  
 30      "We see you have a brain tumor, and you'll have to have surgery to have it removed," he said in a calm, even tone.  
 31 O    I don't remember what I asked him after that, but once he left, I felt hopeless and alone.  
 32      Tears poured out of my eyes, and I sucked in air when I ran out of breath.  
 33      It was the most afraid I've ever been in my life.  
 34      When my parents arrived, we met with the surgeon, who offered more clarity.  
 35 O    He suspected that the tumor was slowly growing deep in the left ventricle of my brain for years.  
 36 ★    And the incident at work?  
 37      Perhaps a miniseizure related to the tumor, but they couldn't be sure.  
 38      I was told the mass wasn't life-threatening at that point and probably was not cancer, but the location was very deep and unique.  
 39      The tumor was growing in an open tunnel in my brain and would eventually grow big enough to block the flow of spinal fluid.  
 40      Surgery was recommended sooner rather than later.  
 41      First Person: Caught in grief's riptide .  
 42      After my terrible experience earlier in the day with the resident who loved to share bad news and disappear, I knew I didn't want to have my surgery at this hospital.  
 43      It was time to shop around for a brain surgeon.  
 44      Two weeks after the incident at work, I saw a doctor at NYU who talked about the surgery in dire terms.  
 45      There was a 10% chance I would need a shunt to help drain excess fluid from my brain for the rest of my life.  
 46      Unsatisfied with that option, I kept browsing.  
 47      Wonderful colleagues and friends within the CNN Medical Unit helped me find Dr. Jeffrey Bruce at New York-Presbyterian Hospital.  
 48      Dr. Bruce is a tall, commanding man with the confidence and swagger you'd hope for in a brain surgeon.  
 49      Somehow, his description of the seven-hour procedure and what would come later didn't seem as scary as before.  
 50      We booked the date for the surgery at the end of October.  
 51      "This is just like a pebble in my brain," I told friends.  
 52      "They'll get it out, and I can move on with my life."  
 53      Two days before the operation, my friends and family gathered at a bar in Brooklyn for that pre-Halloween, prebirthday, presurgery party.  
 54      I wore a short blue wig with my Wonder Woman outfit and set up a photo area to document everyone's costumes.  
 55      We all laughed and danced for hours, and at the end of the party, whoever was left did the Hora.  
 56      We ran in and out of a circle, joyfully raising our hands in the air.  
 57      Ghosts and pumpkins mingled with birthday decor.  
 58      Although I was born at the end of November, I wanted to cover all my holidays since I had no idea what the future would hold.  
 59      First Person:  
 60      The only Cuba I've ever known .  
 61      What if they took the tumor out  
 62      and it was cancer after all?  
 63      What if they couldn't get the whole thing during the operation and had to do radiation later?  
 64      What about that shunt?  
 65      What if ANYTHING went wrong  
 66      and I would never be myself again?  
 67      At the hospital, my family bickered about who got a chair in the waiting room as I sat silently, waiting to be whisked through the double doors and into the rest of my life.  
 68      Once I was on the operating table with the IV in, the anesthesiologist started the magic medicine, and I barely started to count before I was knocked out.  
 69      I woke up one brain tumor lighter and surrounded by the people I love.  
 70      I spent five days in the hospital, mostly sleeping from the antiseizure medicine.  
 71      Real Halloween came and passed.  
 72      Friends and co-workers came to the hospital to tell me stories about their holiday adventures and share pictures of their nights.  
 73      If I was ever lonely or uncertain about my place in the world before, having this experience was a relatively quick way to discover that I have tremendous love and support in my life.  
 74      My recovery has taken a lot of hard work.  
 75      I went straight from the hospital to inpatient rehab to weekly outpatient care, working on speech, occupational therapy and memory recall.  
 76      I did so well there, I was named February's "Patient of the Month."  
 77      When my doctor recently told me I've had the best recovery she's ever seen over her 20-year career, I burst into tears of joy.  
 78      The experience has given me confidence in my resilience and more perspective than before on the importance of living in the present, because things could always be worse -- completely out of nowhere and totally unexpectedly.  
 79      That fact was solidified when just a month after my surgery, my best friend's sister died from a brain aneurysm.  
 80      Survivor's guilt overwhelmed me, but so did a sense of gratitude.  
 81      I don't have an answer as to why I'm OK and my friend is gone, but I know it makes me push harder as I sweat through spin class and linger longer while I stare at sunsets and beautiful views.  
 82      My zest for life itself -- the good and bad -- is so much stronger than before.  
 83      I returned to work part-time, working one day a week starting in February.  
 84      I'm at two days a week now and hope to be back producing digital content full-time for "New Day" by May.  
 85      Though I'm now at the edge of 30 with a new identity as a survivor, I don't consider myself a superhero.  
 86      At least not until next Halloween.  

</details>

---

## 12. `cnn_dm-dev-9748` — gap 3.34 ROUGE (28 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 49.21 | 22.58 | 47.62 |
| abl_position | 54.43 | 24.36 | 50.63 |

**Error category:** ______

**Reference**

> Singer Cher, 68, has vowed to help a 96-year-old woman move back home .
> Edith Hill was separated from her new 95-year-old husband Eddie Harrison .
> Weeks after they were separated by a court, Mr Harrison died .
> Mrs Hill's family said she suffered from mild dementia and needed help .
> Cher said she was outraged the couple had been split against their wishes .
> She has promised to pay for upgrades to Mrs Hall's home in Virginia .

**Ours** (sentences [0, 10, 23])

> Singer Cher has petitioned a court to allow a 96-year-old woman to return to her home in northern Virginia.
> Cher said she will help pay for needed upgrades to Hill's family home in Alexandria.
> She also pledged to help with her ongoing medical bills.

**abl_position** (sentences [0, 1, 2])

> Singer Cher has petitioned a court to allow a 96-year-old woman to return to her home in northern Virginia.
> Edith Hill was taken away from her new 95-year-old husband last year after a court accepted she did not have the mental capacity to enter into a marriage.
> However, the 68-year-old singer was so moved by the story of Mrs Hill and Eddie Harrison that she has pledged to help Mrs Hill return home.

<details><summary>Document</summary>

  0 OR   Singer Cher has petitioned a court to allow a 96-year-old woman to return to her home in northern Virginia.  
  1 R★   Edith Hill was taken away from her new 95-year-old husband last year after a court accepted she did not have the mental capacity to enter into a marriage.  
  2 R★   However, the 68-year-old singer was so moved by the story of Mrs Hill and Eddie Harrison that she has pledged to help Mrs Hill return home.  
  3      Cher was moved to act after she saw a documentary on Edith Hill and her husband Eddie Harrison .  
  4      A court ruled that Edith Hill, left should be removed from her home and transferred to Florida.  
  5      Her husband Eddie Harrison remained at home in Virginia but later died a couple of weeks after they were split apart .  
  6      Unfortunately Mr Harrison died several weeks after his wife was taken away.  
  7      However, Cher was inspired by the story and decided to act on behalf of Mrs Hill and see whether it was feasible to return her to her long-term home.  
  8      A judge in McClean, Virginia has ruled that Mrs Hill should be returned home following Cher's commitment.  
  9      Mr Harrison died in December, just weeks after Hill was taken away to Florida on the recommendation of a court-appointed guardian, but a custody dispute continued over who should care for Hill and where she should live.  
 10 O★   Cher said she will help pay for needed upgrades to Hill's family home in Alexandria.  
 11      In a telephone interview, Cher expressed frustration that Eddie and Edith had been split up against their wishes.  
 12      She said: 'This whole thing is a travesty, what happens to old people.  
 13      Once they do the repairs and she comes back home, it's going to be bittersweet because she only wanted to be with him.'  
 14      Earlier this month, after Cher offered to pay for the home improvements, a judge ordered that Hill should return to Alexandria once repairs are complete.  
 15      Mrs Hill's daughter Rebecca Wright said: 'Mom's coming home!'  
 16      Mrs Hill was in favour of her mother's marriage to Mr Harrison.  
 17      Mr Harrison and Mrs Hill had been companions for more than a decade before they got married.  
 18      In December, the court ruled that Mrs Hill should be moved to Florida and later that same month, Mr Harrison died.  
 19      Mrs Wright said: 'He actually gave his life to this effort.'  
 20      She said Mr Harrison became depressed after Mrs Hill was taken away as he thought it was unlikely that they would ever see each other again.  
 21      Cher became aware of the case when a TV news broadcast showed the couple dancing.  
 22      The singer said she would pay for any repairs inside the Alexandria home and ensure it was suitable for a 96-year-old woman.  
 23 O    She also pledged to help with her ongoing medical bills.  
 24      Cher saw a documentary about the couple when Mrs Hill was taken to Florida.  
 25      She said she was impressed by how in love the pair seemed to be and was outraged over their treatment.  
 26      She added: 'I think this is an important story.  
 27      It's not right what is going on.'  

</details>

---

## 13. `cnn_dm-dev-10863` — gap 0.96 ROUGE (17 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 32.32 | 4.12 | 26.26 |
| abl_position | 29.91 | 9.52 | 26.17 |

**Error category:** ______

**Reference**

> Former HSBC private banking boss said he was unaware of tax evasion .
> Chief executive Stuart Gulliver and Rona Fairhead also angered MPs .
> BBC Trust chairman was either 'incompetent' or aware of wrongdoing .

**Ours** (sentences [0, 7, 9])

> MPs have accused bosses of HSBC of being ‘utterly incompetent’ and ducking responsibility for the Swiss tax dodging scandal.
> The committee’s chairman Margaret Hodge, a Labour MP, said: ‘Nobody at the bank... has deigned to accept responsibility for what was massive, illegal terrible tax evasion.’
> Her fellow committee members also expressed disbelief that HSBC’s bosses in London were unaware of what was happening in Switzerland.

**abl_position** (sentences [0, 1, 2])

> MPs have accused bosses of HSBC of being ‘utterly incompetent’ and ducking responsibility for the Swiss tax dodging scandal.
> Chris Meares, who ran HSBC’s global private banking arm between 2006 and 2011, told the Public Accounts Committee he was not aware of alleged tax evasion taking place on his watch.
> Asked repeatedly whether he accepted personal responsibility for the scandal, he said he took responsibility for ‘controls failings’ which allowed the wrongdoing to occur.

<details><summary>Document</summary>

  0 OR   MPs have accused bosses of HSBC of being ‘utterly incompetent’ and ducking responsibility for the Swiss tax dodging scandal.  
  1 R★   Chris Meares, who ran HSBC’s global private banking arm between 2006 and 2011, told the Public Accounts Committee he was not aware of alleged tax evasion taking place on his watch.  
  2 R    Asked repeatedly whether he accepted personal responsibility for the scandal, he said he took responsibility for ‘controls failings’ which allowed the wrongdoing to occur.  
  3      But he added: ‘I do not take fairly direct responsibility for individual actions of people in Switzerland that I was unaware of.'  
  4      Scroll down for video .  
  5      Chris Meares, who ran HSBC’s global private banking arm between 2006 and 2011, told the Public Accounts Committee he was not aware of alleged tax evasion taking place on his watch .  
  6 ★    Chief executive Stuart Gulliver and HSBC board director Rona Fairhead also angered MPs by insisting they were oblivious to the wrongdoing in Switzerland, where staff allegedly helped wealthy clients including arms dealers and a blood diamond smuggler evade taxes between 2005 and 2007.  
  7 O    The committee’s chairman Margaret Hodge, a Labour MP, said: ‘Nobody at the bank... has deigned to accept responsibility for what was massive, illegal terrible tax evasion.’  
  8      She added: ‘Either you were incompetent, completely and utterly incompetent, in your oversight duties or you knew about it… I don’t believe you did not know.’  
  9 O    Her fellow committee members also expressed disbelief that HSBC’s bosses in London were unaware of what was happening in Switzerland.  
 10      Conservative MP David Burrows said: ‘You are asking us to accept that Switzerland was off on a frolic on its own - that nobody in London knew what was going on’.  
 11      He added: ‘I cannot believe that nobody knew the unlawful actions that were taking place in Switzerland, and if they didn’t know then they jolly well should have done.  
 12      ‘What we’ve essentially got is blind eye knowledge – holding the telescope to the blind eye so that you in London didn’t see what you suspected was going on in Switzerland.’  
 13      Question time: MPs accused BBC Trust chairman Rona Fairhead as either being aware of wrongdoing or being 'utterly incompetent' HSBC’s chairman Douglas Flint has already heaped blame on Mr Meares and his predecessor Clive Bannister, the son of four-minute mile legend Sir Roger Bannister, who now runs insurance company Phoenix.  
 14      Mr Flint told the Treasury Select Committee last month that the two men ‘certainly bear fairly direct responsibility’.  
 15      Yesterday, Mr Meares - who is now chairman of fund manager Quilter Cheviot - rejected claims that he was being made the ‘fall guy’ by HSBC.  
 16      But he was described as a ‘wholly unreliable witness’ by Conservative MP Stephen Hammond.  

</details>

---

## 14. `cnn_dm-dev-8503` — gap 0.73 ROUGE (42 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 36.36 | 15.38 | 36.36 |
| abl_position | 39.69 | 13.95 | 36.64 |

**Error category:** ______

**Reference**

> Fragments from ceramic basins were pulled from 17 pits in Tel Aviv, Israel .
> Basins were used 5,000 years ago to make fruity beer, which was a staple .
> Beer was made from part baked barley and water, with added fruits .
> Finds are first to prove an Egyptian occupation in Tel Aviv 5,000 years ago .

**Ours** (sentences [1, 13, 29])

> Now, 5,000-year-old fragments of pottery used by ancient Egyptians to make beer, have been discovered on a building site in Tel Aviv, Israel.
> ‘Among the hundreds of pottery shards that characterise the local culture, a number of fragments of large ceramic basins were discovered that were made in an Egyptian tradition and were used to prepare beer,’ he said in a statement.
> The walls of the tomb contain paintings showing everyday life and rituals.

**abl_position** (sentences [0, 1, 2])

> Beer is one of the world's most ancient brews and has played an essential role in society - both for its nutritional and ritual importance - for millennia.
> Now, 5,000-year-old fragments of pottery used by ancient Egyptians to make beer, have been discovered on a building site in Tel Aviv, Israel.
> The pottery shards come from large ceramic basins, which were used to prepare fruity beer that was left to ferment under the sun.

<details><summary>Document</summary>

  0 R    Beer is one of the world's most ancient brews and has played an essential role in society - both for its nutritional and ritual importance - for millennia.  
  1 OR   Now, 5,000-year-old fragments of pottery used by ancient Egyptians to make beer, have been discovered on a building site in Tel Aviv, Israel.  
  2 R    The pottery shards come from large ceramic basins, which were used to prepare fruity beer that was left to ferment under the sun.  
  3      Scroll down for video .  
  4      ‘Among the hundreds of pottery shards (pictured) that characterise the local culture, a number of fragments of large ceramic basins were discovered that were made in an Egyptian tradition and were used to prepare beer,’ Dr Barkan said .  
  5      Diego Barkan, of the Israeli Antiquities Authority, said that 17 pits were found that had been used to store produce in the Early Bronze Age, from 3,500 to 3,000 BC.  
  6      Beer was the favourite drink of humans and gods in ancient Egypt.  
  7      It was also drank by rich and poor, adults and children.  
  8      This was because it was cleaner than water, which came from a river or canal and was often polluted.  
  9      Beer was considered as staple, along with bread, Reshafim.org reported.  
 10      Workers were paid with bread, oil, beer and vegetables by their employers.  
 11      The standard ration was two jars containing three-and-a-half pints (two litres) of beer.  
 12      Just like today, the Egyptians liked their beer cooled and kept jars in water.  
 13 O    ‘Among the hundreds of pottery shards that characterise the local culture, a number of fragments of large ceramic basins were discovered that were made in an Egyptian tradition and were used to prepare beer,’ he said in a statement.  
 14      The vessels were made with ‘straw temper’ and other organic material to strengthen them – a method which was not in local potteries.  
 15 ★    The excavation is the first to offer evidence of an ‘Egyptian occupation’ in the centre of Tel Aviv 5,000 years ago.  
 16      As well as the basins, a bronze dagger and 6,000-year-old flint tools were uncovered.  
 17      Dr Barken said: ‘This is also the northernmost evidence we have of an Egyptian presence in the early Bronze Age.  
 18      ‘Until now we were only aware of an Egyptian presence in the northern Negev and southern coastal plain, whereby the northernmost point of Egyptian occupation occurred in Azor.  
 19 ★    Fragments of pottery that are around 5,000 years old and were used by ancient Egyptians to make beer, have been discovered on a building site in Tel Aviv.  
 20      Here, Diego Barkan holds the basin parts .  
 21      Employees of the Israel Antiquities Authority(pictured) work at the site in Tel Aviv where fragments of pottery used by ancient Egyptians have been discovered.  
 22      A total of 17 pits have revealed finds .  
 23      As well as the basins, which were pulled from pits in the centre of Tel Aviv (pictured left) a bronze dagger and 6,000-year-old flint tools were uncovered.  
 24      A flint blade is pictured right .  
 25      Last year, the tomb of a leading ancient Egyptian beer brewer was discovered.  
 26      The tomb of Khonso Em Heb, who lived 3,200 years ago, was found by a Japanese team and has been been described as 'one of the most important discoveries' made at the Thebes necropolic site in the city of Luxor.  
 27      Egypt's antiquities minister Mohamed Ibrahim described Khonso Em Heb as the chief ‘maker of beer for gods of the dead'.  
 28      He was thought to be the head of a warehouse and judging by the decorations in his tomb was an important and wealthy man.  
 29 O    The walls of the tomb contain paintings showing everyday life and rituals.  
 30      ‘Now we know that they also appreciated what the Tel Aviv region had to offer and that they too knew how to enjoy a glass of beer, just as Tel Avivians do today’.  
 31      According to the antiquities authority, ‘beer was the Egyptian national drink and was a staple along with bread.’  
 32      It said beer was consumed by the entire population of Egypt, regardless of age, gender or status.  
 33 ★    ‘It was made from a mixture of barley and water that was partially baked and then left to ferment in the sun.  
 34      ‘Various fruit concentrates were added to this mixture in order to flavour the beer.’  
 35      The mixture was filtered in special vessels before serving.  
 36      Previous excavations carried out in Egypt's Delta region uncovered breweries that indicate beer was already being produced in the mid-fourth millennium BC, the Israeli authority said.  
 37      The fragments were discovered in pits on Ha-Masger Street in central Tel Aviv (marked on the map).  
 38      Excavations are taking place before the construction of an office building .  
 39      The vessels (pictured) were made with ‘straw temper’ and other organic material to strengthen them – a method which was not in local potteries.  
 40      This one dates to the Early Bronze Age I (3,500 BC) Dr Barken said: ‘This is also the northernmost evidence we have of an Egyptian presence in the early Bronze Age.  
 41      Here, a worker for the Israel Antiquities Authority cleans findings at the site .  

</details>

---

## 15. `cnn_dm-dev-3602` — gap 0.25 ROUGE (14 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 74.58 | 63.79 | 71.19 |
| abl_position | 76.56 | 58.73 | 75.00 |

**Error category:** ______

**Reference**

> Martin Odegaard started for Norway against Croatia on Saturday .
> He is now the youngest player to start a European Championship qualifier .
> Odegaard, who plays for Real Madrid, is 16 years and 101 days old .
> He previously became the youngest footballer to play in a Euro qualifier when he was brought on as a substitute at 15 years and 300 days .

**Ours** (sentences [0, 2, 3])

> Norway international Martin Odegaard has become the youngest player to start a European Championship qualifier.
> Odegaard previously became the youngest footballer to play in a Euro qualifier when he came on as a substitute against Bulgaria at the age of 15 years and 300 days.
> Real Madrid youngster Martin Odegaard started for Norway against Croatia on Saturday evening .

**abl_position** (sentences [0, 1, 2])

> Norway international Martin Odegaard has become the youngest player to start a European Championship qualifier.
> The Real Madrid star, aged 16 years and 101 days, started for his country in their Group H tie against Croatia on Saturday.
> Odegaard previously became the youngest footballer to play in a Euro qualifier when he came on as a substitute against Bulgaria at the age of 15 years and 300 days.

<details><summary>Document</summary>

  0 OR   Norway international Martin Odegaard has become the youngest player to start a European Championship qualifier.  
  1 R    The Real Madrid star, aged 16 years and 101 days, started for his country in their Group H tie against Croatia on Saturday.  
  2 OR★  Odegaard previously became the youngest footballer to play in a Euro qualifier when he came on as a substitute against Bulgaria at the age of 15 years and 300 days.  
  3 O★   Real Madrid youngster Martin Odegaard started for Norway against Croatia on Saturday evening .  
  4 ★    The 16 year-old has become the youngest player ever to start a European Championship qualifier .  
  5      Odegaard (top left) lines up alongside his international team-mates ahead of their match against Croatia .  
  6      The game did not start well though, as Croatia took the lead after half an hour.  
  7      Marcelo Brozovic was the scorer as the group leaders went ahead once more.  
  8      Going into the game, Croatia had not lost any of their opening four fixtures, and they continued that run, eventually winning 5-1 and brushing Norway aside with ease.  
  9      Odegaard, although unable to stop his country from losing on Saturday, is a talented young forward with a big future ahead of him.  
 10      He joined Real Madrid in January, and has been plying his trade with Castilla, Madrid's reserve side.  
 11      Odegaard, pictured signing autographs while training with Norway, played for his country on Saturday .  
 12      Odegaard joined Real Madrid in January, and is playing his football for Castilla, their reserve side .  
 13      Odegaard signed for Madrid after copious amounts of attention from a number of clubs around the world .  

</details>

---

## 16. `cnn_dm-dev-8450` — gap -0.03 ROUGE (47 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 42.42 | 21.54 | 37.88 |
| abl_position | 43.48 | 20.59 | 37.68 |

**Error category:** ______

**Reference**

> Former student Graeme Phillip Harris indicted on civil rights charge .
> Noose and former Georgia flag with Confederate symbol hung on statue .
> Harris, who has transferred, faces 11 years in prison for incident .
> James Meredith, first black student at Ole Miss, wants statue destroyed .

**Ours** (sentences [0, 1, 5])

> The Justice Department has indicted a former Ole Miss student on civil rights charges after he allegedly hung a noose on a statue of his university's first black student.
> Graeme Phillip Harris, 20, of Alpharetta, Georgia, has been indicted on one count of conspiracy to violate civil rights and one count of using a threat of force to intimidate African-American students.
> The student faces up to 11 years in prison for conspiracy to violate civil rights and using a threat of force to intimidate African-American students.

**abl_position** (sentences [0, 1, 2])

> The Justice Department has indicted a former Ole Miss student on civil rights charges after he allegedly hung a noose on a statue of his university's first black student.
> Graeme Phillip Harris, 20, of Alpharetta, Georgia, has been indicted on one count of conspiracy to violate civil rights and one count of using a threat of force to intimidate African-American students.
> The indictment is connected to a February 2014 incident in which a noose and a former Georgia flag, prominently featuring the Confederate battle emblem, were placed on a statue of James Meredith.

<details><summary>Document</summary>

  0 OR   The Justice Department has indicted a former Ole Miss student on civil rights charges after he allegedly hung a noose on a statue of his university's first black student.  
  1 OR   Graeme Phillip Harris, 20, of Alpharetta, Georgia, has been indicted on one count of conspiracy to violate civil rights and one count of using a threat of force to intimidate African-American students.  
  2 R    The indictment is connected to a February 2014 incident in which a noose and a former Georgia flag, prominently featuring the Confederate battle emblem, were placed on a statue of James Meredith.  
  3      Scroll down for video .  
  4 ★    Graeme Phillip Harris, 20, of Alpharetta, Georgia, was indicted on  civil rights charges after allegedly putting a noose and Confederate symbols on a state of the first black student to go to Ole Miss .  
  5 O★   The student faces up to 11 years in prison for conspiracy to violate civil rights and using a threat of force to intimidate African-American students.  
  6      He has reportedly transferred to a new school in Georgia .  
  7      Harris, who is white, was an Ole Miss student when the noose was left on the statue.  
  8      It wasn't immediately clear whether Harris had an attorney to contact for comment on his behalf.  
  9      University spokesman Danny Blanton said Friday that Harris is no longer enrolled and that university officials turned the case over to federal prosecutors and deferred to their judgment..  
 10      Harris has transferred to University of North Georgia – Oconee Campus, according to the Daily Mississippian.  
 11      He is free on bond, though his movement is restricted to areas of Georgia and Mississippi.  
 12      James Meredith, who integrated the University of Mississippi under federal protection a half-century ago, says it's a shame that state authorities deferred to the federal government to bring charges.  
 13      Mr Meredith, who is 81 and lives in Jackson, said state authorities should have pursed charges.  
 14      'What it is saying is that the only possible justice for a black in the state of Mississippi is the federal government and if there's anything that we don't need it's that being our only means of expecting justice,' Mr Meredith said in a phone interview Friday.  
 15      'I think Mississippi is better than that.  
 16      If it's not better than that, it should be made better than that.'  
 17      The Lafayette County district attorney said in 2014 that state charges wouldn't be filed because no state laws were broken.  
 18      Mississippi's hate crime law requires an underlying crime for additional charges.  
 19      Because the statute wasn't marred or broken, prosecutors said typical vandalism charges didn't apply.  
 20      James Meredith (statue of him in center during anti-racism demonstration) said that state authorities should have filed charges rather than only the Justice Department .  
 21      Mr Meredith (center) was the first black student to attend Ole Miss in 1962 but has said that the statue of him erected in 2006 should be taken down .  
 22      The punishment for conspiracy to violate civil rights ranges to up to ten years in prison.  
 23      Threat of force to intimidate is punishable by up to one year in prison.  
 24      In 1962, anti-integration protests erupted into violence and Meredith had to be escorted by armed federal agents as he enrolled under court order as the first black student at the university.  
 25      In announcing the indictment of Harris on Friday, Attorney General Eric Holder said of the noose incident:  'This shameful and ignorant act is an insult to all Americans and a violation of our most strongly-held values. '  
 26      No one should ever be made to feel threatened or intimidated because of what they look like or who they are,' Holder said in a news release.  
 27      '  
 28      By taking appropriate action to hold wrongdoers accountable, the Department of Justice is sending a clear message that flagrant infringements of our historic civil rights will not go unnoticed or unpunished.'  
 29      Hundreds of Ole Miss students attended a racial reconciliation rally on campus after the 2014 incident.  
 30      The federal authorities' investigation into the incident, which involved two other freshmen students, is ongoing .  
 31      The university, which replaced its Confederate officer mascot with a bear (pictured) in 2010, has had a string of racism-related incidents, including a protest on Barack Obama's reelection night with racist epithets .  
 32      'It has taken time, but the process has worked and I'm confident justice will be done,' Ole Miss Chancellor Dan Jones said in a statement Friday.  
 33      'I am thankful for the strong, united response of our university community to the desecration of the James Meredith statue last year, confirming our university values of civility and respect.'  
 34      The national office of Sigma Phi Epsilon fraternity suspended its Ole Miss chapter after three of the chapter's members were accused of leaving the noose and flag on the Meredith statue.  
 35      Names of the three white freshmen students from Georgia were not released at the time.  
 36      Federal authorities' investigation into the incident is still ongoing.  
 37      The recent indictment against Harris comes as another fraternity chapter, Sigma Alphia Epsilon at University of Oklahoma, was suspended after a video showed them singing a racist song about lynching on a bus.  
 38      Members of the organization were found to have learned the chant informally at a national leadership cruise.  
 39      Hundreds of students at Ole Miss attended a racial reconciliation rally after the incident at the beginning of last year .  
 40      Mr Meredith said that his statue had been used as 'a public relations tool for the powers that be at Ole Miss,' which has continued to see racism (file photo, 2012)  
 41      Other fraternities are currently being investigated for allegedly racist behavior.  
 42      The Meredith statue was erected in 2006 near the main administrative building at Ole Miss, the Lyceum.  
 43      In a 2012 autobiography, Mr Meredith said the university should destroy the statue because he said it trivialized his effort to destroy a system of white supremacy that had long dominated Mississippi, his native state.  
 44      'I have become a piece of art, a tourist attraction, a soothing image on the civil rights tour of the South, a public relations tool for the powers that be at Ole Miss, and feel-good icon of brotherly love and racial reconciliation, frozen in gentle docility,' Mr Meredith wrote.  
 45      The university banned Confederate battle flags from football games in 2003 and changed its mascot, Confederate Colonel Reb, for a black bear in 2010.  
 46      White students at Ole Miss in 2012 started a protest the night of President Barack Obama's reelection in which they burned his signs and racial epithets were heard being shouted.  

</details>

---

## 17. `cnn_dm-dev-12972` — gap -0.13 ROUGE (46 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 43.90 | 13.22 | 40.65 |
| abl_position | 44.44 | 11.27 | 41.67 |

**Error category:** ______

**Reference**

> Colours of two-tone dress became a topic of global debate on social media .
> Some viewers see the bodycon dress as white with gold lace detailing .
> Others see royal blue with black while a few insist the colours change .
> Roman Originals, who made dress, have produced white and gold version .
> It was auctioned for Comic Relief and sold for £1,356.78 .

**Ours** (sentences [11, 13, 19])

> Roman Originals produced a white and gold version of the dress, which was auctioned off on eBay for Comic Relief .
> Even celebrities weighed in on the fashion debate, with Kim Kardashian asking her 29.4million Twitter followers to help settle a disagreement between herself and husband Kanye West.
> This picture of the dress sparked debate, with viewers disagreeing over the colour .

**abl_position** (sentences [0, 1, 2])

> A gold and white version of the black and blue dress that sparked a global online debate over its appearance has raised more than a thousand pounds for charity.
> Roman Originals, who made #thedress that went viral, produced the new version in order to raise money for Comic Relief.
> The garment was sold to a businessman from the Czech Republic on ebay for £1,356.78, with the dress company matching the fee, meaning the final total came to £2,713.56.

<details><summary>Document</summary>

  0 R    A gold and white version of the black and blue dress that sparked a global online debate over its appearance has raised more than a thousand pounds for charity.  
  1 R    Roman Originals, who made #thedress that went viral, produced the new version in order to raise money for Comic Relief.  
  2 R    The garment was sold to a businessman from the Czech Republic on ebay for £1,356.78, with the dress company matching the fee, meaning the final total came to £2,713.56.  
  3      This one really IS white and gold!  
  4      Roman Originals, whose blue and black dress went viral, have produced a gold and white version.  
  5      It has been bought by Tomas Petru from the Czech Republic for £1,356.78 .  
  6      Roman Originals, who made the dress originally worn by Cecilia Bleasdale for her daughter Grace's wedding decided to make the white and gold version to help out a good cause - it was auctioned off on ebay, with the bidding ending today.  
  7      The winning bidder was Tomas Petru, a business man from the Czech Republic who fought it out against 52 other bidders to buy the item for his wife as a gift.  
  8      She will now fly over to the Birmingham-based store to be fitted for the lacy shift.  
  9      The original black and blue lace dress which created the internet sensation divided the world about what colour it actually was.  
 10 ★    Some saw it as white and gold, while others saw it as blue and black.  
 11 O★   Roman Originals produced a white and gold version of the dress, which was auctioned off on eBay for Comic Relief .  
 12      The picture of #TheDress - as it became known - was first posted on Tumblr by Caitlin McNeill, a 21-year-old aspiring singer from Scotland, after noticing her friends saw different colours in the photograph.  
 13 O    Even celebrities weighed in on the fashion debate, with Kim Kardashian asking her 29.4million Twitter followers to help settle a disagreement between herself and husband Kanye West.  
 14      Actress Mindy Kaling also joined the discussion, writing on Twitter: 'IT'S A BLUE AND BLACK DRESS!  
 15      ARE YOU F***ING KIDDING ME'.  
 16      Her friend and fellow actor BJ Novak replied: 'white and gold.'  
 17      Then recent Oscar winner Julianne Moore jumped in, writing to Novak and Kaling; 'what's the matter with u guys, it's white and gold.'  
 18      To that, Novak replied to Moore; 'Thank you!And congratulations on your Oscar, which Mindy thinks is purple and green.'  
 19 O    This picture of the dress sparked debate, with viewers disagreeing over the colour .  
 20      The hashtag #TheDress started trending worldwide on Twitter as the debate when global.  
 21      There have been more than 1 million tweets mentioning the hashtag.  
 22      Taylor Swift wrote: 'I don't understand this odd dress debate and I feel like it's a trick somehow.  
 23      I'm confused and scared.  
 24      PS it's OBVIOUSLY BLUE AND BLACK.'  
 25      And Justin Bieber kept his fans happy by telling them that he sees 'blue and black'.  
 26      Some celebrities avoided the issue completely, simply declaring that the dress was ugly.  
 27      Model Chrissy Teigen told her 655,000 Twitter followers: 'F*** the dress it's heinous.  
 28      While Oscar-winner Jared Leto branded it 'fugly'.  
 29      McNeill said she never expected the picture to spark a star-studded debate, explaining that she just thought her followers on Tumblr would have a 'good reaction'.  
 30      The dress, made by the company Roman Originals, is in fact blue and black striped .  
 31 ★    Despite the debate, the body-con dress is in fact royal blue with black lace detailing.  
 32      It is made by British clothing company Roman Originals, which offers 'affordable women's clothing and designer ladies fashion.'  
 33      There are also white, pink and red options, all with black lace.  
 34      Speaking on Friday, Ian Johnson, of Roman Originals, said: We were absolutely ecstatic about the reception of our fabulous blue and black dress.  
 35      'We sold out within the first 30 minutes of sale and have since restocked all colours and sizes.'  
 36      The dress, in black and blue, is also for sale on Amazon, and Depop, and user comments have been just as amusing.  
 37      'This dress made me lose all of my friends and now I am so lonely,' wrote one.  
 38      'Where's the white & gold option!?  
 39      I KNOW IT EXISTS  
 40      SOMEWHERE IT HAS TO,' said another.  
 41      And now it does - heading for a wardrobe in the Czech Republic.  
 42      Kim Kardashian called on her 29.4million  
 43      Twitter followers to help settle a disagreement .  
 44      Celebrities including Mindy Kaling, B.J. Novak and Oscar-winner Julianne Moore join the debate .  
 45      'Confused and scared': Taylor Swift told her Twitter followers that the dress is 'obviously blue and black' Justin Bieber was one of the last celebrities to chime with his views on the dress on Twitte .  

</details>

---

## 18. `cnn_dm-dev-220` — gap -1.93 ROUGE (16 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 24.30 | 3.81 | 20.56 |
| abl_position | 22.22 | 1.61 | 19.05 |

**Error category:** ______

**Reference**

> A push to retake Tikrit stalled as ISIS repositioned its forces around the city .
> Spokesman: Iraq's leader requested help because coalition has "advanced" capabilities .
> Leaders of predominantly Shiite militia fighting in area had resisted such intervention .

**Ours** (sentences [2, 3, 12])

> The gains, according to the official, came after a slow advance into the city as the forces dealt with more than 300 improvised explosive devices planted in the city's streets.
> At least 26 militants were killed in the operation, the official said.
> ISIS responded by adjusting its positions in and around the city, hiding in buildings and other key infrastructure, said Saad al-Hadithi, a spokesman for al-Abadi.

**abl_position** (sentences [0, 1, 2])

> (CNN)Iraqi forces say they've captured key areas in their offensive to take back Tikrit, which has been under ISIS control since June.
> The security forces, backed by Shia militias, raised the Iraqi flag over the governorate and the main hospital buildings in the city Monday night, a security official with the forces in Tikrit told CNN.
> The gains, according to the official, came after a slow advance into the city as the forces dealt with more than 300 improvised explosive devices planted in the city's streets.

<details><summary>Document</summary>

  0 R    (CNN)Iraqi forces say they've captured key areas in their offensive to take back Tikrit, which has been under ISIS control since June.  
  1 R    The security forces, backed by Shia militias, raised the Iraqi flag over the governorate and the main hospital buildings in the city Monday night, a security official with the forces in Tikrit told CNN.  
  2 OR   The gains, according to the official, came after a slow advance into the city as the forces dealt with more than 300 improvised explosive devices planted in the city's streets.  
  3 O    At least 26 militants were killed in the operation, the official said.  
  4      Earlier Monday, Iraqi federal police said in a statement aired on Iraqi television that the forces had liberated four neighborhoods in southern Tikrit.  
  5 ★    The renewed push into Tikrit comes days after a series of U.S.-led airstrikes aimed at ISIS targets around the city.  
  6      The goal of those airstrikes was to pave the way for Iraqi forces to go in.  
  7      Now security forces and fighters from Hashd Al-Shaabi, a predominantly Shia paramilitary force that has doing much of the fighting in the critical battle to take Tikrit back from ISIS, say they're gaining ground.  
  8      Iraqi forces have tried multiple times to win back Tikrit since ISIS, which calls itself the Islamic State, conquered the city in June as part of its campaign to amass an expansive Islamic caliphate.  
  9      And each time, so far, they've failed.  
 10 ★    The latest push began after Iraqi Prime Minister Haider al-Abadi on March 1 ordered Iraqi forces to retake Tikrit and Salahuddin province.  
 11      Militants have been under pressure ever since in the battleground city, which is the birthplace of former Iraqi dictator Saddam Hussein and  located about 160 kilometers (100 miles) north of Baghdad.  
 12 O    ISIS responded by adjusting its positions in and around the city, hiding in buildings and other key infrastructure, said Saad al-Hadithi, a spokesman for al-Abadi.  
 13      This movement led Iraq's military to pause its operation, out of growing worries that a full-on invasion could produce heavy Iraqi military and some civilian casualties.  
 14      The situation spurred the Iraqi Prime Minister to request help from the U.S.-led coalition, which conducted airstrikes around Tikrit last week.  
 15      CNN's Jomana Karadsheh, Catherine E. Shoichet,  Ashley Fantz, Ben Wedeman and Greg Botelho contributed to this report.  

</details>

---

## 19. `cnn_dm-dev-4110` — gap -4.29 ROUGE (44 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 33.57 | 4.26 | 29.37 |
| abl_position | 24.47 | 5.38 | 24.47 |

**Error category:** ______

**Reference**

> Gareth Bale shrunk, disappeared and even hid against Barcelona last week .
> The former Tottenham Hotspur star should return to the Premier League .
> Bale would be a perfect signing for Arsenal or Jose Mourinho's Chelsea .
> But Manchester United should blow the others out of the water .
> Louis van Gaal has bargaining chips in David de Gea and Angel di Maria .
> ADRIAN DURHAM: International football should not be about a Brazilian playing for Spain, an Argentine in Italy colours or an English-born Scot .

**Ours** (sentences [6, 18, 43])

> Bale has been brilliant for Wales but his form for Real Madrid has left a lot to be desired in Spain .
> Bale has failed to meet the high standards at Real Madrid this season in front of football's harshest critics .
> United goalkeeper David de Gea could be used as a bargaining chip for Bale to leave Madrid this summer .

**abl_position** (sentences [0, 1, 2])

> A lot of Gareth Bale’s friends and fans are letting their hearts rule their heads and are making themselves look spectacularly naive.
> Bale was stunning again for Wales in Israel.
> With a little bit of help from his friends – notably Joe Allen, Aaron Ramsey and Joe Ledley – he has spearheaded the charge to the top of Group B. Chris Coleman is arguably the luckiest manager in international football – Bale is shining for Wales at exactly the same time as the European Championship has been expanded, and it would be a huge failure if Wales didn’t qualify for the finals in France next year.

<details><summary>Document</summary>

  0 R    A lot of Gareth Bale’s friends and fans are letting their hearts rule their heads and are making themselves look spectacularly naive.  
  1 R    Bale was stunning again for Wales in Israel.  
  2 R    With a little bit of help from his friends – notably Joe Allen, Aaron Ramsey and Joe Ledley – he has spearheaded the charge to the top of Group B. Chris Coleman is arguably the luckiest manager in international football – Bale is shining for Wales at exactly the same time as the European Championship has been expanded, and it would be a huge failure if Wales didn’t qualify for the finals in France next year.  
  3      Coleman is well on course to make history with his current squad.  
  4      Gareth Bale scored two goals for Wales in Israel but has not been up to scratch for Real Madrid this season .  
  5      Bale celebrates one of his two goals in Israel as Wales won their Euro 2016 qualifying match in Group B .  
  6 O    Bale has been brilliant for Wales but his form for Real Madrid has left a lot to be desired in Spain .  
  7 ★    International football should be the best of one country against another... not a Brazilian playing for Spain, an Argentina in Italy colours or an English-born Scot .  
  8      England's exciting squad and flawless form give real reasons for optimism ahead of Euro 2016...  
  9      but only if Roy Hodgson can instil a positive mentality .  
 10      But as brilliant as Bale has been for Wales, his form this season for Real Madrid is still a subject for debate.  
 11      He hasn’t been good enough, and needs to step up to the plate between now and the end of the season to keep his reputation at the Bernebeu intact.  
 12      His supporters have expressed their disgust at anyone who dares to question Bale’s Real Madrid credentials.  
 13      Honestly, did these people think that Bale or any player for that matter, could go to a club the size of Real Madrid and not be scrutinised?  
 14      It seems these people are unaware of the amazing history and traditions of this great club – and the demands that go with it.  
 15      This isn’t the Welsh national team, where a couple of goals in Israel makes you a national treasure.  
 16      This isn’t Spurs where reaching the quarter-finals of the Champions League is a once-in-a-lifetime achievement.  
 17      Real Madrid's Cristiano Ronaldo vents his frustration next to team-mate Bale during a La Liga match .  
 18 O    Bale has failed to meet the high standards at Real Madrid this season in front of football's harshest critics .  
 19      No, this is Real Madrid, where they win their 10th European Cup and immediately ask if the players are good enough to win it again the following season.  
 20      Where finishing behind Barcelona is almost regarded as a crime.  
 21      Where finishing third last season behind Atletico Madrid AND Barca was seen as utter humiliation.  
 22      Standards are spectacularly high at Real Madrid and it’s hard to make a case to support the notion that Bale has maintained the level he reached last season.  
 23      As far as his Bernebeu future is concerned, Saturday’s man-of-the-match display in Haifa will have done nothing to appease the Madridistas.  
 24      In a Wales shirt Bale is everywhere – it’s exhausting watching him.  
 25      He scored two, he set up the other, he created more chances with some awesome passing.  
 26      He ran at defenders, committing them, forcing fouls or mistakes from them.  
 27      In short he was brilliant.  
 28      Compare that with the Bale who shrunk, disappeared (dare I say hid?) in the Nou Camp in the second half of El Clasico the week before.  
 29      Now you can see why Real Madrid fans are so frustrated with Bale.  
 30      Unless his form and impact changes at club level, Bale could be on the way out of Real Madrid this summer.  
 31      Bale scored recently against Levante to end a goal drought and covered his ears as if to mute the criticism .  
 32      Bale could be on the way out of Madrid this summer if his form does not pick up by the end of the season .  
 33      The club demands big-name signings every summer and Bale’s second-season slump may be enough to render him dispensable.  
 34      It might seem harsh to some, but if you know how high the standards are at Real Madrid, then it’s perfectly normal.  
 35 ★    Bale should come back to the Barclays Premier League.  
 36      He’d be the perfect signing for Arsenal in so many ways, but he’d also fit perfectly into Jose Mourinho’s way of thinking at Chelsea.  
 37      Manchester City’s inertia in evolving their team could be tackled by the signing of Bale.  
 38 ★    But Manchester United should blow the others out of the water – they have bargaining chips in David de Gea or possibly Angel di Maria who has struggled to settle after his blistering start.  
 39      Bale has the energy to raise United’s tempo and take them back to the big time.  
 40      Whatever happens to Bale he should feel proud of his achievements.  
 41      He has helped create special history at Real Madrid, and he’s on the brink of doing the same for Wales.  
 42      Angel di Maria has struggled at Manchester United this season so far following his £59.7million move .  
 43 O    United goalkeeper David de Gea could be used as a bargaining chip for Bale to leave Madrid this summer .  

</details>

---

## 20. `cnn_dm-dev-2341` — gap -8.90 ROUGE (28 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 43.56 | 30.30 | 41.58 |
| abl_position | 32.56 | 23.62 | 32.56 |

**Error category:** ______

**Reference**

> Renault is considering pulling out of Formula One .
> The threat in Malaysia comes following criticism of their engine .
> Renault supplies engines to the Red Bull and Toro Rosso teams .

**Ours** (sentences [0, 1, 10])

> Renault, which supplies engines to the Red Bull and Toro Rosso teams, is considering pulling out of Formula One because of the damage done to its reputation after a difficult start to the season.
> Renault Sport F1 managing director Cyril Abiteboul said Friday he is looking at his options, 'including getting out of Formula One.'
> Red Bull driver Daniel Ricciardo in action during the first practice session for the Malaysian Grand Prix .

**abl_position** (sentences [0, 1, 2])

> Renault, which supplies engines to the Red Bull and Toro Rosso teams, is considering pulling out of Formula One because of the damage done to its reputation after a difficult start to the season.
> Renault Sport F1 managing director Cyril Abiteboul said Friday he is looking at his options, 'including getting out of Formula One.'
> 'If Formula One is that bad for Renault's reputation, if we see that we will continue to struggle with the current formula, if Formula One is not delivering on the value that it costs Renault ... this is what we're looking at,' he said.

<details><summary>Document</summary>

  0 OR★  Renault, which supplies engines to the Red Bull and Toro Rosso teams, is considering pulling out of Formula One because of the damage done to its reputation after a difficult start to the season.  
  1 OR   Renault Sport F1 managing director Cyril Abiteboul said Friday he is looking at his options, 'including getting out of Formula One.'  
  2 R    'If Formula One is that bad for Renault's reputation, if we see that we will continue to struggle with the current formula, if Formula One is not delivering on the value that it costs Renault ... this is what we're looking at,' he said.  
  3      Renault's Cyril Abiteboul (centre) is pictured at a press conference in Kuala Lumpur on Friday .  
  4      However, Abiteboul was also asked whether Renault was weighing up the option of buying an existing F1 team and becoming a race constructor again.  
  5      'We'll have to review the situation from a marketing and strategic perspective,' Abiteboul said.  
  6      Renault won championships in 2005 and 2006 but withdrew from the sport after heavy penalties for fixing the 2008 Singapore Grand Prix.  
  7      The team principal of Toro Rosso, which is considered to be a takeover target if Renault took that step, said the Italy-based team would be receptive to an offer from Renault.  
  8      'This would be a fantastic opportunity for Toro Rosso to make the next step forward,' Franz Tost said.  
  9      'To be part of a manufacturer, to work together with a manufacturer, and be owned by a manufacturer would be exactly the step the team needs.'  
 10 O    Red Bull driver Daniel Ricciardo in action during the first practice session for the Malaysian Grand Prix .  
 11      Two other teams considered to be possible targets for Renault are Force India and Lotus, which have had financial troubles, but both played down any interest.  
 12      Both teams have engine supply deals with Mercedes through 2020.  
 13      'We are not looking for a buyer and are not for sale,' Lotus chief executive Matthew Carter said.  
 14      Force India deputy principal Bob Fernley said: 'I have had absolutely no discussion at all with Renault.'  
 15      If Renault pulls out of F1, or switches from engine supplier to competitor, it would put Red Bull in a difficult situation.  
 16      Toro Rosso's Max Verstappen drives during Friday's practice at the Sepang International Circuit .  
 17      Red Bull team principal Christian Horner said such a change may leave the Austrian-based parent company with no option but to withdraw from the sport, too, because there would be no other viable option for engine supply.  
 18      'It sound like Franz wants to sell his team to Cyril and we will then need an engine,' Horner said.  
 19      'Should we find ourselves in a situation without an engine supplier ... you could find yourself actually forced out of the sport.'  
 20      Red Bull and Horner have expressed frustration with the lack of cost control in the sport, and he referenced that again Friday.  
 21      Abiteboul (left) sits alongside Red Bull team principal Christian Horner at a press conference on Friday .  
 22      'Is Formula One delivering for Red Bull as a brand?  
 23      There are some worrying signs,' Horner said. '  
 24      Red Bull wants to be in Formula One and we want to try and address some of the issues that are currently plaguing the sport that we don't seem to be able to find any traction with.'  
 25      Horner also said Red Bull has no plans to start making its own engines - a theory fueled by the team's new deal with engineering group Ilmor.  
 26      'We have no intention of being an engine manufacturer,' Horner said.  
 27      'We (Red Bull and Ilmor) are trying to work in co-ordination with Renault to assist in the areas where perhaps they are not strong.'  

</details>
