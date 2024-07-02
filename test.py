from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
import time 



html = """<a href="/r/AITAH/comments/1dt03zf/aita_for_telling_my_husband_either_he_comes_home/" class="hover:no-underline no-underline pointer-events-none text-neutral-content visited:text-neutral-content-weak" slot="text-body">
       <div class="  mb-xs " data-post-click-location="text-body">
          <div id="t3_1dt03zf-post-rtjson-content" class="md feed-card-text-preview text-ellipsis line-clamp-3 xs:line-clamp-6 text-14" style="--emote-size: 20px">
             <p>
                I've been with my husband for 9 years now. I just gave birth to our son 5 months after years of infertility. We underwent 3 rounds of IVF before we had a pregnancy that "stuck" (4 miscarriages). This was such a a big turning point in our marriage. We got unbelievably closer, despite all the grief, and for the first 3.5 months of our sons life he was easily the most attentive and helpful man I have ever in my life met. Life was happy.
             </p>
             <p>
                Well, his mom all the sudden came back in to his life when our son was 3.5 months old. She moved back to our state (she moved to Canada without him when he was 13 and has barely seen him or his siblings for 17 years). There have been multiple occasions where her presence has made me incredibly uncomfortable. Like she has come here a good 5-6 times since our son was 3.5 months old, never held the baby either. When my husband says "look, it's grammie", his mom will raise her eyebrows and say "hi" before looking away. 99% of the time that she comes here, she asks my husband to go outside with her (away from me and the baby) and she's started to ask my husband A LOT to go to her place and needless to say, me and the baby are never invited. He says that she's "just trying to catch up" with him and make up for lost time but I'm honestly just done with it.
             </p>
             <p>
                Today was his only day off this week. The baby has a spiked fever and is super cranky. I had to call out of work for the past 3 days due to this (I work from home). The house is an absolute mess. I haven't showered in 4 days. I can't put the baby down without him screaming. I need help. Well, around 10am his mom calls and says she "needs" him because she has a surgery and needs a ride to and from. So, he leaves. There was no prior notice. Well, he called me and hour ago and told me that her boyfriend is there too so I asked him why he is still there when she clearly has a ride and a support system? He says that she just asked him to be there and he wanted to be there for her. Well, he just called me again 10 minutes ago and tells me that she's in recovery and asked him not to leave. I told him that I really needed his help and that ever since his mother has popped back up, he's been MIA and I feel like I'm doing everything alone. He told me he's sorry I feel that way and that he "wants" to be home with us but his mother needs him. I guess something inside me just broke when he said that. Because I'm telling him I need him and his mom "needing" him is more important. So I told him if he didn't come home I was done. I would file for divorce. I'm not playing second to a 'mother' who ditched her kids off 17 years ago and has seen them all of twice since. Me needing his help is more important than his mother wanting him there when she already has support with her. He says "are you fucking serious?" And I just hung up. I hardly see this man any more because of this woman and I don't want to live a life like this anymore, even though it's only been a month and a half since this started happening. AITA? The hospital is only 15 minutes from us so if he's not back in 30 minutes, I'm packing my stuff.
             </p>
             <p>
                ETA: I own a property that I rent out for AirBNB. That's where I will be going. No, I don't have a support system. I grew up in foster care. My biological mother died during child birth and my dad didn't want me. I was never adopted out. My best friend moved 2 years ago. It's just me, and used to be my husband.
             </p>
             <p>
                Edit: on my way to the AirBNB now. The last phone call I received was him telling me his mother would be discharged within the hour and he would be home after dropping her off. Her boyfriend (who lives with her) is still at the hospital. He could drive her. But mommy wants her precious son to. So, I'm leaving. Thank you everyone who took the time to comment. I will update as the night progresses.
             </p>
          </div>
       </div>
    </a>"""




soup = BeautifulSoup(html, "html.parser")

content = soup.div.div.get_text()
# join all text in content
print(content)


   

