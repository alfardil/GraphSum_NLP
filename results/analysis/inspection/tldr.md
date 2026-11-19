# Targeted inspection: tldr-17 (dev)

Strongest simpler rival on dev: **abl_position** (dev mean ROUGE 11.58 vs ours 10.34). Ours tuned: {'beta': 0.3, 'gamma': inf, 'memory': 0.5}; rival tuned: {'beta': 0.6, 'forward_weight': -2.0, 'gamma': 1.0, 'memory': 0.5}. Budget: 1 sentences. Ours is worse than the rival on 9/20 dev docs; listed: the 20 largest gaps.

Sentence markers: **O** ours, **R** rival, **★** Oracle.


---

## 1. `tldr-dev-539513` — gap 24.18 ROUGE (25 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 0.00 | 0.00 | 0.00 |
| abl_position | 28.57 | 15.38 | 28.57 |

**Error category:** ______

**Reference**

> went out with friends, felt boobs, peed pants, confessed when called out.

**Ours** (sentences [1])

> I am a five second pee-er as well.

**abl_position** (sentences [2])

> I went out with my friends a while ago and got to having a good time.

<details><summary>Document</summary>

  0      Oh god.  
  1 O    I am a five second pee-er as well.  
  2 R★   I went out with my friends a while ago and got to having a good time.  
  3      One of my friends is telling me about her fake tits and I'm just getting way too into the conversation.  
  4      I stay there and continue the conversation even though I realized that I had to pee.  
  5      Eventually she let's me feel her glorious titties (under shirt and bra).  
  6      As a bisexual woman, I was in heaven.  
  7      Anyways, after I got my mental video of that moment I decided I was going going to finally go pee.  
  8      I get to the bathroom and the mine was fucking 15 people deep.  
  9      I decided fuck it, I have no shame, I'll use the men's restroom.  
 10      I walk over there and there was the same problem.  
 11      Instead of making the wise decision and standing in line for the men's restroom I go back to the women's restroom.  
 12      The line was no about 18 people deep.  
 13      So I stand and wait in the line for about fifteen minutes.  
 14      Finally, I was the next person in line.  
 15      As I am standing there hearing this woman flush the toilet my bladder empties.  
 16      I am not sure what the chances are, but there was literally no one behind me in line.  
 17      So I am standing there waiting for a moment to punch it off, but it seems like forever.  
 18      I am able to pinch it off right as the girl is opening her stall and run outside to my car.  
 19      I get about five feet away from my car, all while thinking I was in the clear, when my coworkers chimed in.  
 20      "Where are you going, iliveinatauntaun? "  
 21      "it's a little cold, so I'm taking off my shorts and putting on some pants."  
 22      I replied.  
 23      "Um, you totally peed your pants, didn't you." 
 drunk me thought it would be a good idea to tell the truth, so I did  
 24      and I still get made made fun of.  

</details>

---

## 2. `tldr-dev-491344` — gap 18.88 ROUGE (17 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 4.17 | 0.00 | 4.17 |
| abl_position | 32.35 | 9.09 | 23.53 |

**Error category:** ______

**Reference**

> There is virtually no risk in ordinary people.
> There is a population of people with heart valve diseases who are at risk of endocarditis, but even these people receive no special treatment now.

**Ours** (sentences [11])

> Extraction of teeth, deep periodontal scaling (root surface debridement) or soft tissue surgery probably qualify.

**abl_position** (sentences [0])

> People who have had diseases that are known to effect the heart valves (such as rheumatic fever) are at higher risk of an acute episode of inflammation inside the heart (endocarditis) after certain dental procedures.

<details><summary>Document</summary>

  0 R    People who have had diseases that are known to effect the heart valves (such as rheumatic fever) are at higher risk of an acute episode of inflammation inside the heart (endocarditis) after certain dental procedures.  
  1      Normal people who have not had this problem are NOT at risk.  
  2      However, there IS a small bacteraemia after these procedures.  
  3      Most people are more than capable of clearing this quickly.  
  4 ★    People who have had valvular diseases are at risk because bacteria have usually built a thick plaque across the surface of your heart valves.  
  5      These are incredibly difficult to shift - antibiotics may kill the surface layer, but do not reach the centre of the plaque.  
  6      Bacteria are incredibly efficient at protecting each other by bundling into layers on surfaces called "biofilms".  
  7      One other example being dental plaque.  
  8      However, the incidence of endocarditis even in at-risk patients is very low.  
  9      We used to give antibiotic cover for these at-risk people before certain procedures, but we do not anymore.  
 10      We would not call flossing an at-risk dental procedure, especially in an ordinary person.  
 11 O    Extraction of teeth, deep periodontal scaling (root surface debridement) or soft tissue surgery probably qualify.  
 12      Hard tissue surgery e.g. a filling or crown etc. do not qualify.  
 13      Also, people who have significantly higher than normal levels of gum inflammation and bacteria (periodontal disease, severe gum disease) can be at risk of future problems.  
 14      The likelihood of the development of chronic endocarditis is low, though there may be a small association.  
 15      In ordinary people, the bacteria that manage to get into your bloodstream are mopped up before they can do any damage.  
 16      If the levels get too high, they can settle and form a plaque on your heart valves.  

</details>

---

## 3. `tldr-dev-208656` — gap 7.02 ROUGE (40 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 0.00 | 0.00 | 0.00 |
| abl_position | 10.53 | 0.00 | 10.53 |

**Error category:** ______

**Reference**

> different every time

**Ours** (sentences [15])

> AFTER THAT... that group finally left me alone.

**abl_position** (sentences [3])

> The 3 childhood fights I was in when I was a kid all had different outcomes.

<details><summary>Document</summary>

  0      Adrenaline rush.  
  1      To some, it's exciting, to some, it makes them ill.  
  2      Some people run, some people duck/flinch, and some people go tits out and face first into it.  
  3 R    The 3 childhood fights I was in when I was a kid all had different outcomes.  
  4      They all had to deal with local bullies.  
  5      First things first, when I was around 9-10 or so, my mom enrolled me in Tae Kwon Do because I got my ass kicked by a teenager at our local park.  
  6      I was kinda half-assing it as it wasn't my favorite martial art (and it didn't seem very practical or instantly effective), but it was close to my house.  
  7      One of the times, I punched someone really hard (in the chest) that was pushing me around and slapping me in the face.  
  8      I felt a lot of rage, let out a loud yell-powered punch (a similar punch yielded a broken board during a belt promotion for me), and instantly felt better.  
  9      Bully got up, white washed me (tackled me into the snow, to which I still wound up in a better position), and ran home crying.  
 10      After my friends witnessed this, I was basically treated like a hero for the remainder of the year.  
 11      The dude used to pick on everyone in my friends group.  
 12      This time, it felt awesome, and my parents were proud of me for standing up to a bully.  
 13      A week later, same bully showed up with his posse to kick my ass.  
 14      There must have been 6 guys there, so at the time, I blasted the same bully in the face with a roundhouse kick (yeah, I know, douchey), and ran home.  
 15 O    AFTER THAT... that group finally left me alone.  
 16      This attempted group-jumping ... left me feeling instantly terrified and was probably my first experience with anxiety 
 My last bully of grade school (I was in 3rd grade, he was in 5th grade ... and I believe he flunked a year, so he was a good 3 years older and nearly a foot taller than me), would throw baseballs or apples (it sucks getting hit by an apple in the face when it's about 40 degrees outside).  
 17      He used to corner me on my way home from school.  
 18      There wasn't much I could do with this guy, but I went down swinging regardless.  
 19      Totally lost the fight.  
 20      Bleeding nose, black eye, you name it.  
 21      I might have gotten in a good punch or two, I don't remember.  
 22      Not much I could have done during that time.  
 23      At the time my "feeling" was that I was going to die... kind of numbing.  
 24      There wasn't much I could do against this guy, so I think I just accepted the reality of the situation.  
 25      Finally, when I was in high school (about 16 years old), involved another bully that had it out for me.  
 26      Fucker would wait for me during odd parts of the day in very quiet/unpatrolled/odd parts of the school.  
 27      And stiff shoulder me, slam me into a locker, trip me, hit me with his backpack loaded full of books, etc.  
 28      I took this abuse for nearly an entire school year.  
 29      Toward the end of this school year, I was feeling a lot of frustration about this, so I decided it was time to end it with him.  
 30      I knew he'd be up to his usual tricks, so I let him slam me into a locker, to which I immediately slammed him back into the locker and slugged him in the gut, yelled at him, told him to leave me alone, or I'd really beat the crap out of him (in front of other people).  
 31      I had no real klout behind that as we were about the same height and weight, and I  was no longer  skilled in any martial art at the time (only did TKD for 3 years and half-assed it).  
 32      He didn't call my bluff and left me alone.  
 33 ★    This time, I was afraid... more than anything.  
 34      I didn't want to get into trouble at school.  
 35      Ironically, in college I fell in love with Judo and did it really hard for 3-4 years.  
 36      Since then, nobody has fucked with me AT ALL.  
 37      I think I got bullied based on how I carried myself.  
 38      Future note: if I do ever get into a fight again, I will not strike my aggressor, I will attempt to subdue, throw, pin, or apply some sort of arm lock, or an artery choke (not a wind pipe choke).  
 39      All in all, I'd say those are much less bloody ways to end a fight.  

</details>

---

## 4. `tldr-dev-61380` — gap 5.34 ROUGE (8 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 25.00 | 13.04 | 25.00 |
| abl_position | 29.27 | 20.51 | 29.27 |

**Error category:** ______

**Reference**

> You're not going to find a Sprint Spark capable phone within your budget.
> Save up or settle for a single-band LTE device (S3 or Moto X?) and hope for the best.

**Ours** (sentences [4])

> I don't know if you'll be able to find one within your budget.

**abl_position** (sentences [0])

> You definitely want a Sprint Spark capable phone.

<details><summary>Document</summary>

  0 R★   You definitely want a Sprint Spark capable phone.  
  1      And if you want to tether then the Google Play Store Nexus 5 is probably going to be the phone with the least amount of hassles.  
  2      Best bet is to check  
  3      [Swappa]( for used phones.  
  4 O    I don't know if you'll be able to find one within your budget.  
  5      It would probably be a good idea to run your potential phones ESN/MEID through [Tings BYOD tool]( in order to verify that the phone could be activated on Sprint.  
  6      If you eventually acquire a phone then you could activate it on Ting to test out the service for a while then move on to Sprint unlimited if you're satisfied with your testing.  
  7      PM me for $25 Ting referral credit.  

</details>

---

## 5. `tldr-dev-1070120` — gap 5.15 ROUGE (4 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 27.27 | 10.00 | 27.27 |
| abl_position | 40.00 | 0.00 | 40.00 |

**Error category:** ______

**Reference**

> I'm addicted to statistics.

**Ours** (sentences [0])

> Whenever I read manga, I'm plagued to know the order of who was drawn the most.

**abl_position** (sentences [1])

> I absolutely have to know.

<details><summary>Document</summary>

  0 O    Whenever I read manga, I'm plagued to know the order of who was drawn the most.  
  1 R★   I absolutely have to know.  
  2      It's like a tobacco addiction.  
  3      I've only ended up doing it a few times though.  

</details>

---

## 6. `tldr-dev-180450` — gap 4.34 ROUGE (55 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 13.04 | 0.00 | 8.70 |
| abl_position | 19.23 | 4.00 | 11.54 |

**Error category:** ______

**Reference**

> GNU/Linux and it community was built great from the bottom up, MacOSX's core was built great from the bottom up, windows base/core is very half-assed and needs to patched constantly just to be decent

**Ours** (sentences [43])

> In windows, they do it for the money).

**abl_position** (sentences [1])

> MacOSX and GNU/Linux share some of the reasons why they are "virus-proof".

<details><summary>Document</summary>

  0      While, there are multiple reasons.  
  1 R    MacOSX and GNU/Linux share some of the reasons why they are "virus-proof".  
  2      Some say it is Market share.  
  3      Yes and no.  
  4      While MacOSX and Linux don't have a huge desktop market share, the *nix kernels are used everywhere (like servers for example), meaning a virus for macOSX or linux, could potentially be worth more than a windows virus.  
  5      Now there is another reason, this is a smaller, but still real reason.  
  6      By default MacOSX and Linux make you admin (sorta, there is an actual "admin" account and a separate "root" account), but not root.  
  7      In windows, the default user user account will always have the "run as administrator /what ever" and it will also autorun certain files.  
  8      If you get an email with some fishy attachment, your computer will auto-run it as your account "administrator", meaning the attachment has full privileges.  
  9      In MacOSX and Linux, it won't auto-run the files(s), meaning you have to manually click on it to get it to run.  
 10      And even then, the program doesn't have full privileges.  
 11      In order for a program to get full privileges, it has to upfront ask you for it, and then you have to put your password in.  
 12      That in itself is a red alarm.  
 13      If you download some (porn, shitty game, browser addon) that needs Super User privileges then you know somethings wrong, because said types of programs don't need them to run.  
 14      Also it has to do with the kernel.  
 15      The  nix kernel has very secure and clean cut user accounts/privileges.  
 16      In windows, when they shifted over from the DOS to the NT kernel, shit got difficult.  
 17      DOS is single user, meaning there only is one account, so all programs you ran in DOS were "root".  
 18      The NT kernel is multiuser.  
 19      And you know that the C:\ is for important stuff.  
 20      In DOS you could write/read to C:\ easily since there was only one account.  
 21      When they moved to NT, non admin accounts could/should not read/write to C:\, meaning that all the existing programs people had would break.  
 22      If everything broke nobody would want it/buy it.  
 23      So that had to make a whole lot of shitty compromises.  
 24      So in general, windows user accounts/privileges are total shit compared to  nix ones.  
 25      This means getting from restricted user to super user is easier on windows than *nix.  
 26      There is also some random reasons.  
 27      Like windows doing fonts in kernel space.  
 28      That is an extremely dumbass thing to do.  
 29      And it shows.  
 30      There was a virus where if you installed a certain font, a program could obtain super user privileges.  
 31      Yicks!  
 32      Now for a reason that impacts GNU/Linux more than MacOSX: OpenSource.  
 33      GNU/Linux is opensource.  
 34      (GNU and Linux them selves are both open source).  
 35      This is Linus's Law (By Eric Raymond)  "given enough eyeballs, all bugs are shallow".  
 36      Meaning, many eyes reading the source code make light work of bugs.  
 37      In GNU/Linux, you have 10,000's of people reading source code from all types of backgrounds and walks of life.  
 38      It also motivates you to write good open source code or you'll get public shamed (Usually by Linus Torvalds himself).  
 39      Also, the culture within Linux makes it a lot better.  
 40      You  get rewarded and encouraged to rewrite code better.  
 41      In Microsoft, it's do the code once, get paid, patch it to hell.  
 42      (Also that stuff made by people who love it is usually better than people doing for the money, GNU/Linux is made by people who love it, it's their hobby/Job, it their passion.  
 43 O    In windows, they do it for the money).  
 44      I did say this does impact MacOSX though.  
 45 ★    MacOSX's is built off many opensource technologies, their kernel (Darwin) is opensource, the kernel itself was built from other opensource kernels.  
 46      Now before you call Apple an asshole for using a lot of opensource code and making money and giving nothing back; The license allows them to do that  AND  Apple has given back some pretty good opensource software.  
 47      For example, webkit and CUPS.  
 48      You noticed I said their kernel was opensource, meaning yes, there are OSes that essentially are MacOSX, but with out the mac and Apple part of it.  
 49      Now this is the last one, and has to do with GNU/Linux Distros/packages.  
 50      In Windows or MacOSX you know that a fresh install of them will always have certain programs.  
 51      You find a bug in some of those programs and you have a virus that effects ALL of them.  
 52      A Linux Distro has various software in them.  
 53      No two Distros are the same, meaning if there is a bug in a program in a Mint install, it will only effect Mint distros.  
 54      This combined with the fact that you can install or change any of the default, fast bug patching, the fact that most zero-days usually need a chain of bugs (but not always), and that even the kernel itself can be custom/customized; it is very hard to target linux.  

</details>

---

## 7. `tldr-dev-694928` — gap 2.42 ROUGE (5 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 0.00 | 0.00 | 0.00 |
| abl_position | 3.64 | 0.00 | 3.64 |

**Error category:** ______

**Reference**

> two or three, depending on how you count.

**Ours** (sentences [0])

> My first one scratched discs until I ripped it open and installed padding.

**abl_position** (sentences [1])

> This of course voided the warranty, so it was only a matter of time until I got the RRoD.  I shelved it and bought a new one, which turned out to be much cooler, WAY quieter and didn't scratch discs no matter how hard I tried.

<details><summary>Document</summary>

  0 O    My first one scratched discs until I ripped it open and installed padding.  
  1 R★   This of course voided the warranty, so it was only a matter of time until I got the RRoD.  I shelved it and bought a new one, which turned out to be much cooler, WAY quieter and didn't scratch discs no matter how hard I tried.  
  2      That one was great for a few months and then it died with the E74 error.  
  3      Microsoft fixed that for free (including shipping) very quickly, but assuming it would take a while I cracked open my first 360 and did some heatsink and cooling mods.  
  4      Now they're both working fine, although the first one is still noisy as hell.  

</details>

---

## 8. `tldr-dev-725262` — gap 0.65 ROUGE (23 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 24.53 | 3.85 | 15.09 |
| abl_position | 21.43 | 7.32 | 16.67 |

**Error category:** ______

**Reference**

> Helped my friend with a Rock the Vote event at a Neil Young concert, forgot the actual voter registration forms, snuck in Nalgenes-of-gin, gave out 6,000,000 Winterfresh Strip samples, Neil Young got upset with us and almost kicked us out... possibly soured his relationship with Rock the Vote as a secondary consequence.

**Ours** (sentences [10])

> There was one good use for the huge bags of Winterfresh Strips though, and that was hiding the Nalgene bottles of gin amongst the samples in order to sneak them into the show... but clearly I was already visibly drunk as evidenced by the "Are you actually DRUNK right now?"

**abl_position** (sentences [1])

> Friend of mine (who has since passed sadly) was the head "Voter Registration Partner" for Rock the Vote for the whole New England region or some such silliness.

<details><summary>Document</summary>

  0      Okay, I'll try to keep it brief (kinda impossible though):  
  1 R    Friend of mine (who has since passed sadly) was the head "Voter Registration Partner" for Rock the Vote for the whole New England region or some such silliness.  
  2      Basically it meant MTV sent him literally 30 garbage bags full of " Winterfresh Strips ... how pathetically corporatized it was.  
  3      The idea was, apparently, to get college-age kids to register to vote using the Winterfresh Strips samples as a sort of minty lure.  
  4      (They sent him so many bags of these things that the campus post office was literally threatening to permanently suspend his mailbox privileges if he didn't get the bags out of there...)  
  5      He ended up requesting more registration forms, yet none ever did end up arriving, interesting that.  
  6      The cool thing though, was that he got to go to all of these sweet concerts for free, and usually could take someone else along to help him and man the "Voter Registration" table (more importantly though, help give out 10,000 Winterfresh Strips to drunk college kids).  
  7      So one time he invited me to go see the Neil Young show, and we did what any irresponsible college sophomores would do and filled Nalgene bottles with gin and got way too high before we left.  
  8      Ironically, we completely forgot the few voter registration forms we actually did have, only realizing this when we got to the show.  
  9      (We must've unconsciously picked up on the cue that the organization only gave a shit about marketing corporate breath fresheners, because we brought a whole hell of a lot of those puppies!).  
 10 O    There was one good use for the huge bags of Winterfresh Strips though, and that was hiding the Nalgene bottles of gin amongst the samples in order to sneak them into the show... but clearly I was already visibly drunk as evidenced by the "Are you actually DRUNK right now?"  
 11      I received from the ticket-taker lady as I walked (then ran) through the turnstile.  
 12      So we are setting up the tables and this official-looking guy with a clipboard and a headset comes up and quickly gathers that we're (possibly intoxicated) idiots and forgot the forms etc.  
 13      (Hey, I'm just along for the ride, not my responsibility buddy!).  
 14      He says he's going to go backstage and "Speak with Mr. Young about this..." 
 15 minutes later, he's back and says something to the effect of "I explained the situation to him, and Mr. Young is very upset about this.  
 15      Not only is he angry at you two idiots personally, but he may be canceling his association with Rock the Vote for the rest of the tour.  
 16      This is extremely unprofessional and I have half a mind to kick you morons out of here right now, blah blah blah" 
 Ruh roh.  
 17      Strangely enough, we were ultimately allowed to stay for the duration of the show (awesome by the way), and we improvised some kind of DIY registration forms I think.  
 18 ★    But I guess it was too little too late, and my friend got in big trouble with his "boss" but by that point he didn't give a shit anyway (and obviously the whole Rock the Vote thing was a big corporate scam...  
 19      so really we did Neil a favor even though he was pissed at us).  
 20      And so even though it wasn't exactly a positive (indirect) interaction, it was actually pretty hilarious both while it was happening and looking back on it...  
 21      plus I am now able to say that Neil Young was personally angry with me, which is actually pretty cool all things considered.  
 22      I mean there's probably a good number of people out there who have met him and what not, but how many can say "He got really angry at me and almost kicked me out of his show" ?  

</details>

---

## 9. `tldr-dev-617212` — gap 0.59 ROUGE (89 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 11.11 | 0.00 | 11.11 |
| abl_position | 16.00 | 0.00 | 8.00 |

**Error category:** ______

**Reference**

> Don't break the rules, or you'll have a gang war in your home.

**Ours** (sentences [56])

> The Final Encounter

**abl_position** (sentences [2])

> Nothing happened and I never participated in a cheating thing.

<details><summary>Document</summary>

  0      Backstory   So in the beginning The Ex  
  1      and I hung out as friends though The Ex had a fiance.  
  2 R    Nothing happened and I never participated in a cheating thing.  
  3      (Even if I had the chance I wouldn't have)  
  4      But we were hanging out for a few months, one night we were watching a movie and fell asleep together.  
  5      That's when she decided to break up with the fiance (they lived on the literal opposite sides of the country for a few years before this happened).  
  6      So The Ex essentially decided to break up with the fiance to date me.  
  7      Which at the time I was iffy with, but we had like interests(I thought) and they were pretty chill and didn't hound me to hang out or anything and everything was just really chill.  
  8      Fast forward about 4 months.  
  9      I wasn't feeling more than when we were chillin but it was getting obvious The Ex was falling hard and fast.  
 10      (there were a few more factors but I won't get into it unless asked) I was also about to leave for a study abroad  
 11      so I decided to end it as I didn't really see it going anywhere.  
 12      The Breakup  
 13 ★    So I have a few rules I follow when breaking up with someone.  
 14      Follow them and I guarantee it'll be smooth sailing.  
 15      You may ask yourself "Well then if you have these rules then why are you posting this?"  
 16      Well...I broke them because I'm dumb.  
 17      Rule Number One: Never break up at your place.  
 18      I asked The Ex if I could come over for a bit, in which she said sure.  
 19      Rule Number Two: Have an escape plan  I luckily did, I had an event I was doing that I couldn't miss so if things started to go too long, I had a valid excuse to leave.  
 20      So I went over and told the Ex that I wasn't feeling it anymore.  
 21      I used much nicer language than that but that was the gist of it.  
 22      The ex stayed pretty calm and accepting and soon it was time for me to go.  
 23      So I apologized and left.  
 24      Rule Number Three: Give you both some space for a while.  
 25      This is where I started f$cking up.  
 26      At my event I got a text from The Ex asking if we could talk again.  
 27      I, at first, stuck to my guns but I gave.  
 28      We met up later that night at a mutual friends place (the mutual friend was more my friend but The Ex didn't have too many)  
 29      So we went for a walk and talked.  
 30      The entire time The Ex  tried to convince me I didn't want to break up.  
 31      I was kind of taken aback and didn't know what to say.  
 32      I convinced them that this wasn't the case  
 33      and I just didn't see it going anywhere.  
 34      I unfortunately forgot Rule Number Two for this meeting so we ended up talking in circles for like four hours.  
 35      We eventually made it back to the friends place and I booked it home as soon as I could.  
 36      Fast forward to the next day.  
 37      Our mutual friend told me the horror story that was The Ex breaking down and crying and all of that typical stuff, but as The Ex didn't have any other friends around, the mutual friend was keeping an eye on them.  
 38      Felt bad as I had no ill will or anything  
 39      but I had to stick to Rule Number Three.  
 40      Well that night at like 11:30 The Ex texted me asking to come over.  
 41      I said no  
 42      and it wasn't a good idea.  
 43      (especially since I had been drinking.  
 44      Well not too long after, The Ex showed up at my place anyway.  
 45      Breaking all the rules  I let the Ex into my place to talk (out of guilt and being a few drinks in) and stuff happened.  
 46      The next day I kicked out The Ex and made sure they knew this was no longer and option and that we are done for real.  
 47      But that day I noticed everyone including the mutual friend weren't responding to my texts or calls.  
 48      Finally ran into the mutual friend who started yelling at me for taking advantage of The Ex.  
 49      I was pretty confused and asked what was meant.  
 50      The Mutual Friend was hanging out and consoling The Ex when The Ex told all our mutual friends that I asked The Ex to come over.  
 51      I was baffled but told my side of the story, and at first the mutual friend was skeptical until I showed the texts I had with The Ex the night before how I said to not come over.  
 52      The Mutual friend was baffled as well but this was the tip of the iceberg.  
 53      The Ex eventually started spreading a ton of lies and whatnot about our relationship in an attempt to look like a victim and get people to shun me.  
 54      It unfortunately worked on a few people and I lost some friends.  
 55      Two years later I've reconciled with most of those friends as they found out The Ex's weird word twistings and lies about us, but unfortunately that's not the end of the tale.  
 56 O    The Final Encounter  
 57      So it's been two years  
 58      and we happened to run into each other.  
 59      We start to talk and one drunken night, things happened again.  
 60      So I sat The Ex down and explained it was a one time thing and probably shouldn't continue as I just wanted to stay friends.  
 61      The Ex agreed we should stay friends, but asked if a friends-with-benefits thing would work.  
 62      After a bit of thought I stupidly said sure.  
 63      So for a month or two in the summer we had that.  
 64      I decided to play it save  
 65      and eventually when I thought things might be getting a little too much for The Ex I decided to break it off as I thought The Ex was getting attached again.  
 66      The Ex took it really well and said it's cool and that they had been talking to someone at work anyway and was considering trying to date that person.  
 67      I told The Ex good luck and we went our separate ways.  
 68      Fast Forward two months  
 69      It's October and another one of our mutual friends(and current S/O as they'll be referred to now)  
 70      and I start hooking up.  
 71      Eventually after a few weeks I had a Halloween party at my place where many friends showed up including The Ex.  
 72      Well S/O  
 73      and I are dancing in skimpy costumes and whatnot most of the night  
 74      and I saw The Ex once for a moment.  
 75      I asked what The Ex was for Halloween as they wore a non-descript mask and cape and The Ex replied "I'm Super Available."  
 76      To which I replied, "Oh cool", and walked on, as I became worried.  
 77      I then went to find the S/O and we danced a bit more.  
 78      I had to go adjust my costume  
 79      and so I went into my room for a minute.  
 80      As I was in there The Ex saw my S/O  
 81      and I dancing and took the opportunity to talk to them.  
 82      The Ex took my S/O into another room to tell them not to do anything with me.  
 83      The S/O said we already had and at that point the The Ex shoved my S/O out of the way and went into the crowded party hallway.  
 84      Which just so happened to be when I came out.  
 85      I had no idea what just happened and saw my S/O in the room behind so as I tried to walk past The Ex shoulder checked me into the opposite wall and a few people spilling drinks everywhere and all over me.  
 86      Not taking to that shit and not knowing why this had just happened even though it was an obvious attack, I pointed to the door and yelled over the people and music  "GET THE FUCK OUT OF MY HOUSE!"  
 87      The Ex left instantly and The Ex's friends came over to yell and scream at me, and they happened to shove my S/O's ratchet friend who had to have people hold them back and it essentially turned into a shit show of two groups of 5-10 people fighting in my house fueled by alcohol and ignorance of the situation.  
 88      The Ex still lives nearby but I not talked to them since.  

</details>

---

## 10. `tldr-dev-320835` — gap 0.00 ROUGE (1 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 8.96 | 3.08 | 8.96 |
| abl_position | 8.96 | 3.08 | 8.96 |

**Error category:** ______

**Reference**

> Tourist in London?
> Put £10 on an Oyster card, then you practically run through the gates.

**Ours** (sentences [0])

> I live just a moment away from Gatwick airport, everything in the town near me is pretty cheap, the one thing that does piss me off up in London though are the people that use only tickets to get everywhere, fumble around and have to dig around for the right one.

**abl_position** (sentences [0])

> I live just a moment away from Gatwick airport, everything in the town near me is pretty cheap, the one thing that does piss me off up in London though are the people that use only tickets to get everywhere, fumble around and have to dig around for the right one.

<details><summary>Document</summary>

  0 OR★  I live just a moment away from Gatwick airport, everything in the town near me is pretty cheap, the one thing that does piss me off up in London though are the people that use only tickets to get everywhere, fumble around and have to dig around for the right one.  

</details>

---

## 11. `tldr-dev-359735` — gap 0.00 ROUGE (7 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 0.00 | 0.00 | 0.00 |
| abl_position | 0.00 | 0.00 | 0.00 |

**Error category:** ______

**Reference**

> Doesn't matter, had sex.

**Ours** (sentences [3])

> After class she told me that she wanted to talk.

**abl_position** (sentences [3])

> After class she told me that she wanted to talk.

<details><summary>Document</summary>

  0      I know a lot of people think we're all lying, but for me, it was the same, except different.  
  1 ★    I don't think the details matter, but since we're all sharing, I'll just tell it.  
  2      I was a shy kid on the football team and I think she liked that.  
  3 OR   After class she told me that she wanted to talk.  
  4      We started making out and then she realized that I didn't have a condom.  
  5      She said she'd have to go to the store to get one, and I asked her how much do they usually cost and she said about three fiddy  
  6      and that's when I realized she wasn't my teacher but actually a goddamn loch ness monster, so I told her I wasn't giving any money for no condom and we barebacked it right there at my desk.  

</details>

---

## 12. `tldr-dev-591415` — gap 0.00 ROUGE (3 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 35.29 | 16.33 | 31.37 |
| abl_position | 35.29 | 16.33 | 31.37 |

**Error category:** ______

**Reference**

> America's laws are fucked up and if you're going to help somebody, make sure that without your interventions, they're going to die.
> Either that, or know wtf you're doing.

**Ours** (sentences [0])

> Also, you have to make sure that you're doing stuff correctly and have the most recent certifications.

**abl_position** (sentences [0])

> Also, you have to make sure that you're doing stuff correctly and have the most recent certifications.

<details><summary>Document</summary>

  0 OR★  Also, you have to make sure that you're doing stuff correctly and have the most recent certifications.  
  1      I believe that even under the good samaritan law, if you start doing CPR and do some damage to them, they can sue you for damages if you don't have a BLS cert.  
  2      I've heard of people being sued for pulling people out of cars causing the patient to get paralyzed because during the circumstances, the pt did not need to get extricated from the vehicle.  

</details>

---

## 13. `tldr-dev-932207` — gap 0.00 ROUGE (4 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 25.00 | 0.00 | 16.67 |
| abl_position | 25.00 | 0.00 | 16.67 |

**Error category:** ______

**Reference**

> He/she does not know if BJP volunteers are paid or not.

**Ours** (sentences [2])

> Here are a few FAKE pics prepared by BJP fans or workers.

**abl_position** (sentences [2])

> Here are a few FAKE pics prepared by BJP fans or workers.

<details><summary>Document</summary>

  0      Let me save you a click and having to wade through a wall of text to read the responder's answer to the question.  
  1 ★    This is what he/she wrote: 
 >  
  2 OR   Here are a few FAKE pics prepared by BJP fans or workers.  
  3      Whether these are paid workers or not is anyone's guess, but BJP would do best to take steps to reign in on them, including the FB/Twitter accounts that post them.  

</details>

---

## 14. `tldr-dev-1007430` — gap -1.16 ROUGE (17 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 7.14 | 0.00 | 7.14 |
| abl_position | 5.41 | 0.00 | 5.41 |

**Error category:** ______

**Reference**

> 80% extinction probably causes nuclear war, causing 99% extinction and world fuckery.

**Ours** (sentences [1])

> Similar situation if 80% vanished into thin air, except far less disease due to no corpses.

**abl_position** (sentences [0])

> If 80% of the population dropped dead, major cities would be unlivable due to disease, fires breaking out, transport accidents, loss of essential services etc.

<details><summary>Document</summary>

  0 R    If 80% of the population dropped dead, major cities would be unlivable due to disease, fires breaking out, transport accidents, loss of essential services etc.  
  1 O    Similar situation if 80% vanished into thin air, except far less disease due to no corpses.  
  2      Another factor to consider would be the emotional state of those left, you could probably expect a fairly high suicide rate.  
  3      Lots of elderly people and children would be left without carers, and would pass.  
  4      So at this point we're probably down another 5-8%.  
  5      Considering as well, population distribution, this leaves anywhere between one and four million people in most major western cities.  
  6      These people are likely to be confused, depressed and afraid, and will probably not be in any state to do crucial jobs.  
  7      Supply chains would be broken (ie not enough people to tend crops, drive trucks, stock stores etc) and there would probably not be enough people left willing to work in law enforcement or to maintain power and water supplies.  
  8      After the initial shock, it would depend on how quickly whoever is left in positions of power is able to restore communications.  
  9      There's likely to be a good deal of chaos at this point (looting, mass exodus) and many people will be ready to adopt a 'everyone for themselves' mentality.  
 10      If whatever authority is left is able to communicate with the people, it may be possible to restore order in some smaller cities, although never to the standard we expect now.  
 11      Manufactured goods would be easy to get originally, but would run out quickly.  
 12      So much of what we use in our daily lives travels thousands of miles, which will no longer be possible (think: 80% of pilots vanish/die?)  
 13      As others have said, in less populated and rural areas, life may be able to resume fairly normally (although with less of the original population and more migrants who are less skilled at farming etc) but to answer your original question re world order, I'd think most countries would stop worrying about external issues and concentrate on their own needs, at least initially.  
 14      Over time, as some countries restore order, there's likely to be some trade or resource wars.  
 15 ★    That is, of course, if the original mass extinction doesn't trigger a nuclear war.  
 16      Which it probably would.  

</details>

---

## 15. `tldr-dev-436205` — gap -3.16 ROUGE (9 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 23.53 | 0.00 | 11.76 |
| abl_position | 12.90 | 0.00 | 12.90 |

**Error category:** ______

**Reference**

> fighting fire with fire makes you just as much of an asshole as those you claim are assholes

**Ours** (sentences [0])

> Neither of you is really making a substantial point with any clarity or of any consequence.

**abl_position** (sentences [3])

> As an atheist myself it's tiresome and embarrassing to read these posts.

<details><summary>Document</summary>

  0 O    Neither of you is really making a substantial point with any clarity or of any consequence.  
  1      This is atheist masturbation.  
  2      The same non points in every thread since this subreddit came into existence.  
  3 R    As an atheist myself it's tiresome and embarrassing to read these posts.  
  4      Is the comparison to any other religion that bashes others lost on everyone in this subreddit?  
  5      You all continually bash people for believing in something and pushing it on you when you all do the exact same thing.  
  6 ★    The existence of this subreddit makes you all as bad as them, pushing your non-beliefs and claiming it's "better".  
  7      Again, I'm an atheist and my goal as an atheist is to believe what I believe and not care what anyone else does.  
  8      It's not a discussion anymore, it's simply an internet flame-war.  

</details>

---

## 16. `tldr-dev-95678` — gap -4.04 ROUGE (15 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 6.06 | 0.00 | 6.06 |
| abl_position | 0.00 | 0.00 | 0.00 |

**Error category:** ______

**Reference**

> probably guilty of receiving stolen goods.
> Statute of limitations achieved!

**Ours** (sentences [4])

> This was a few years ago, and I'm not sure if he had PayPal, but it probably wasn't mandatory back then.

**abl_position** (sentences [9])

> :/

<details><summary>Document</summary>

  0      Not Craigslist, but eBay, I won a brand new network KVM switch at a bargain price because it was poorly listed.  
  1      This is a like a KVM switch that allows you to switch one monitor between 8 computers, but it also contains frame-grabber so you can access and control those computers over the network using VNC.  
  2      So this item was currently retailing at c £1000 and I got it for £100.  
  3      The seller is a new eBayer, doesn't respond when I contact him after the close.  
  4 O    This was a few years ago, and I'm not sure if he had PayPal, but it probably wasn't mandatory back then.  
  5      He lived in a town maybe 20 or 30 miles from me, and I wanted to collect, anyway - it was pretty obvious he wasn't replying because he wanted to weasel out of the sale.  
  6 ★    I certainly had the bloke's name from the eBay confirmation, and I knew what town he was in, so I pirated a copy of the "UK Info Disc" CD-ROM, a compilation of phone book and public electoral roll data and looked him up.  
  7      I may have had his postcode, I'm not sure if I had to ask eBay for that, but I found a house with the right initial and surname in the right area, and took a chance and drove down the next evening.  
  8      I knocked on the door, asked for him, and it turns out the lady answering the door was the kid's mum.  
  9 R    :/  
 10      He was at work at the moment, at a local computer warehouse.  
 11      :/  
 12      So his mother offered me his mobile phone number, and I gave him a bell and said I was just passing and could I pick up the item I had won on eBay, please.  
 13      I had to wait about 45 minutes for his break from work, then he came home and gave me the KVM switch.  
 14      He was about 19 and didn't look in the least like a computer geek.  

</details>

---

## 17. `tldr-dev-155936` — gap -4.19 ROUGE (10 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 16.33 | 0.00 | 12.24 |
| abl_position | 8.00 | 0.00 | 8.00 |

**Error category:** ______

**Reference**

> progression is not inherently bad - most like them, developers work in options for people that dont like it all the time

**Ours** (sentences [8])

> Heres a token for doing it once, go ahead and unlock that gun permanently, along with the attachments and skins you've unlocked for it, you deserved it.

**abl_position** (sentences [0])

> Unlocking stuff is fun?

<details><summary>Document</summary>

  0 R    Unlocking stuff is fun?  
  1      Idk, i might have a different mentality than most of reddit on this, but i enjoy the progression of unlocks most of the time.  
  2      Some iterations better than others, but none the less it gives me something to achieve down the road.  
  3      I mean, the whole idea of prestiging is a testiment to that, people wouldnt prestige unless they enjoyed unlocking things again, all it does is add replay value to the game..  
  4      For example i love TF2, but get bored quickly, theres a lack of reward for playing the game, besides the completely random chance of gaining drops.  
  5      This incentive can hold me for 3 hours at most, but since i really only enjoy the spy, once i have my essential loadout, the novelty of those random drops is gone :/ 
 I can play COD for hours, and still have incentive to play the next day, because i reeeeaallly want that gun locked at lvl 52, or because i want to max out my guns attachments, or just get the gold title for the gun.  
  6 ★    Black Ops 2 definately had the best progression by far, and even catered to those that dont like the system by giving them a token every prestige.  
  7      Dont wanna wait till lvl 52 again?  
  8 O    Heres a token for doing it once, go ahead and unlock that gun permanently, along with the attachments and skins you've unlocked for it, you deserved it.  
  9      So  

</details>

---

## 18. `tldr-dev-1303311` — gap -8.01 ROUGE (6 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 23.53 | 13.33 | 23.53 |
| abl_position | 18.18 | 0.00 | 18.18 |

**Error category:** ______

**Reference**

> Big boobs make great life jackets

**Ours** (sentences [4])

> Life jackets they had supplied couldn't fit over my bust

**abl_position** (sentences [0])

> I have H size boobs.

<details><summary>Document</summary>

  0 R    I have H size boobs.  
  1      We went overboard in white water rapids.  
  2      Father with a life jacket on couldn't stay afloat.  
  3 ★    Me with no life jacket on and just boobs floated np.  
  4 O    Life jackets they had supplied couldn't fit over my bust  
  5      so i didn't wear one. :)  

</details>

---

## 19. `tldr-dev-327140` — gap -8.31 ROUGE (19 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 22.54 | 2.90 | 16.90 |
| abl_position | 8.70 | 0.00 | 8.70 |

**Error category:** ______

**Reference**

> Learning to pick locks manually so you can steal things is a horrible idea and you will get caught.
> Learning how to pick locks so you can have a fun hobby to show off is great sport.

**Ours** (sentences [15])

> If you google, you can find practice locks that are graudated from 1 pin up to help teach you the skill, or cutaway/transparent locks that are easy to see what you're doing.

**abl_position** (sentences [1])

> I have practiced manual lockpicking for many years now.

<details><summary>Document</summary>

  0      Constant Reader's claim that there's much easier ways is an accurate statement.  
  1 R    I have practiced manual lockpicking for many years now.  
  2      I'm ok at it - there's many who are better.  
  3      There are competitions (I don't) and people enjoy it as a sport.  
  4      might be a good place to begin learning and find links; or at least the are good people.  
  5      (Edit:  meant to link to  )  
  6      But if I wanted to pick a lock in a critical situation, I'd never rely on my manual skills or lockpicks.  
  7      If the situation allowed, I'd use a bumpkey, and if not, I'd use a drill or a big rock.  
  8      Or a crowbar.  
  9      Or my foot.  
 10      Depending.  
 11      Once in my life I have picked a lock 'for real' - one of my coworkers had locked their keys in a desk, and another one was going to smash it open with a large object.  
 12      I found a screwdriver and a paper clip, and desk locks are pretty weak, so it only took a minute.  
 13      It is a fun skill to have, it takes a lot of practice to do well, and it impresses people that don't know there are much much easier ways to bypass most locks.  
 14      There's plenty of places to buy lockpicks online - check your local laws first though.  
 15 O    If you google, you can find practice locks that are graudated from 1 pin up to help teach you the skill, or cutaway/transparent locks that are easy to see what you're doing.  
 16      I recommend against these gimmicks; just go to your hardware store and buy a keyed padlock, start there.  
 17 ★    You may find that a cheaper brand is easier to pick, I suggest getting a few or various brands through, as you can sometimes be surprised.  
 18      I have an "Ace Hardware" store brand lock that's nearly impossible and a "Master" brand that nearly picks itself.  

</details>

---

## 20. `tldr-dev-848314` — gap -14.80 ROUGE (5 sentences)

| | R-1 | R-2 | R-L |
|---|---:|---:|---:|
| ours | 26.32 | 5.56 | 26.32 |
| abl_position | 6.90 | 0.00 | 6.90 |

**Error category:** ______

**Reference**

> sponsors are busy folks sometimes.
> if you need something it always helps to reach out and try and make contact first.

**Ours** (sentences [1])

> On the sponsor thing, if you can get a number for your gaining unit it might help.

**abl_position** (sentences [0])

> Offutt was my first assignment, worked at AFWA.

<details><summary>Document</summary>

  0 R    Offutt was my first assignment, worked at AFWA.  
  1 O★   On the sponsor thing, if you can get a number for your gaining unit it might help.  
  2      My first assignment my sponsor contacted me way before I arrived.  
  3      My second PCS I contacted my sponsor about 4 weeks before I arrived and was told they were waiting for me to call.  
  4      (WTF?)  

</details>
