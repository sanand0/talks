---
marp: true
title: Homelabbing with Bare Metal
author: Kiran Jonnalagadda
url: https://sanand0.github.io/talks/2025-09-20-kiran-homelabbing-with-bare-metal/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/c/68d4a615-7c50-8324-a9b7-65a60269a2ae
---

<style>
li { font-size: 95%; }
transcript { display: none; }
</style>

# Homelabbing with Bare Metal

[IndiaFOSS](https://fossunited.org/c/indiafoss/2025/cfp/4v6f8ek2n0) · 20 Sep 2025, 3:00 pm IST · [Bangalore](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)
[Kiran Jonnalagadda](https://www.linkedin.com/in/kiranjonna/) · Co-founder [Hasgeek](http://hasgeek.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-20-kiran-homelabbing-with-bare-metal/README.md)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-20-kiran-homelabbing-with-bare-metal/)

---

## Raspberry Pi basics & power

- I frame the **Raspberry Pi as a tiny, low-power PC**. Idle draw around _\~2–3W_ on Pi 4, much lower than typical desktops. ([pidramble.com][1])
- I ballpark cheaper Indian pricing and stress “slow but small” as the tradeoff. (No public price source cited; numbers are my talk’s estimates.)
- I contrast idle power with x86 desktops; full systems often idle far higher than Pis. (**Edit**: CPU-only idle can be lower than system idle.) ([RackSolutions][2])
- My point: leave it running for long periods without guilt.
- That low power is the foundation for always-on home projects.

<transcript>

Okay, I'm going to have a problem with this mic because I'm moving around a lot, but let's see if we can pull it off.

So, I'm going to talk about something very boring. There's something called a Raspberry Pi. This is a Raspberry Pi. I'm sure everybody in this room has encountered one, but on the assumption that you have not, it's essentially like a desktop PC motherboard, except it is very, very slow. But it's also very, very small, fairly cheap—I think this is the Raspberry Pi 4, it's about 3,000 rupees. You can get one for as low as 1,700 now. And it's extremely low power. It can run at like one to two watts idling, which is something that a normal Intel or AMD CPU cannot do. Those things are like 5 to 15 watts minimum idling. And that kind of adds up when you leave something running for a long time.

</transcript>

---

## Starter projects: Pi-hole & Home Assistant

- I recommend starting with **Pi-hole for whole-home ad blocking**; it even cleans up smart TV ads. See: [pi-hole.net](https://pi-hole.net/). ([Pi-hole][3])
- Next level: **Home Assistant automates the house**; private, local-first, huge community. See: [home-assistant.io](https://www.home-assistant.io/). ([Home Assistant][4])
- These give quick wins without custom hardware work.
- They show the “always-on, low-power” value clearly.
- From there, you can explore weirder, personal projects.

<transcript>

So, one of the questions that you have when you have a device like this is, what do you do with it? There are lots of projects for a Raspberry Pi that you can find online. The best one that most people should start with is something called a Pi-hole, which is DNS for your house. It removes ads from every computer on your home network, especially smart TVs. If you've not done Pi-hole, you're missing out on so much peace in life. So everybody should do that. Or if you want to upgrade, go to something like Home Assistant. That's kind of like Pi-hole but 10 times better. It automates everything in your house.

</transcript>

---

## Find “Pi-shaped” problems

- I ask: **how do I notice life problems a Pi can solve**?
- Ideas strike while daydreaming—not at the desk—so I avoid screens.
- Going to the PC derails me into Reddit/Discord/Twitter doom-scrolling.
- I want a capture workflow that survives distraction.
- The goal is a thinking rig that moves with me.

<transcript>

So now, those are nice ready-made projects. But let's say you want to challenge yourself and say, "I want to find something to do with this." Now, how do you find a Pi-shaped problem in your life to say, "Here, this is the solution to the problem"? And that's generally very hard to do when you're sitting at a screen, sitting at a computer. It's the kind of thing that kind of comes to you when you're chilling out. No screen, daydreaming, and thinking of all the tiny things that are bothering you, and hopefully thinking, "Maybe this is a thing that will help me deal with that kind of problem."

So, one of the things that tends to happen when you're in this ideal thinking mode of daydreaming is, my computer is somewhere there. The moment I go there and say, "Oh, I had an idea," the next thing I'm doing, I'm on Reddit, or Discord, or Twitter or somewhere. There is this problem with how do you imagine a problem that you can solve with this kind of device, and how do you stay focused on the damn thing? Because the moment you go to a regular desktop setup and continue working, it falls apart.

</transcript>

---

## Handheld “Hackberry Pi” idea

- I try a **BlackBerry-keyboard Pi handheld** to daydream without distractions.
- It’s _so slow_ that I literally can’t browse; perfect.
- But closed backs block GPIO, limiting tinkering imagination.
- Bare Pi setups become wire messes; portability dies.
- Net: inspiration up, but prototyping friction rises.

<transcript>

And so, one of the questions that I've been trying to deal with is, **can I build a workspace where this comes daydreaming with me, so that I'm not distracted when I'm trying to think about what is the correct way to solve any particular problem?** So, one of the ways that I've tried is, why don't you make a little phone mod? This is called a Hackberry Pi. You can buy it. I think this one is a discontinued model. But there's a new one which is based on the Raspberry Pi 5. I had one, but I forgot to bring it this morning. Maybe I can show it to you tomorrow if anybody's interested. So, this is kind of like a handheld computer using a BlackBerry keyboard and a Raspberry Pi. And now I can go sit daydreaming with my little cyberdeck. It is so slow, I can't go to Reddit. Which is great because then I'm not distracted on a device like this.

The problem I have, though, is if you look at the backside of the device, it's closed off. And one of the nice things about working with an open hardware piece like this is the GPIO, that you essentially are adding on things to it and tinkering with it. And it kind of gets a little tedious when you try something like this because it looks like a bit of a retail product. It again limits your imagination with what you can do with it.

So, typically when you start working with a Raspberry Pi, it starts looking like this. You've got all kinds of things sticking out. It's a huge mess of wires, and that's not portable anymore. So, once you're on your desk, once again you get busy with Googling stuff and saying, "Hey, what's this GPIO pin? Can I buy one more accessory?" Once again, not thinking about your actual problem.

</transcript>

---

## Lapdock: laptop shell, bring your CPU

- I test a **laptop shell (lapdock) where you bring your own CPU**—screen+keyboard via USB-C/HDMI. ([Wikipedia][5])
- Vendor Pi adapter leaves the board sticking out; add hats and it flops—portability lost.
- I experiment: stick the Pi on the laptop’s back (LEGO/pegboard).
- It works but only for flat, light bits; depth twists screens.
- Verdict: clever, but dead-end for real builds.

<transcript>

So, what I wanted was, if only I had something that was running on this Pi but felt a bit like a laptop because chilling out like this with a laptop on my lap, sure, I can do that. So I went looking for something of that sort, and I did find one. I have a device here. Let's see if I can open it up and show you. So, this is a product you can buy. It's roughly about 16,000 rupees if you can find supply, although it's completely sold out in India right now. And I have one. And maybe we can see it working.

So this is a device that's like a laptop without a CPU. **You bring your own CPU**. It's a laptop without a CPU. I can't power it on because there is no CPU. What you get instead is USB-C and HDMI and USB-A. Plug in your device, and effectively what it is is that it's a monitor and a keyboard in a laptop form factor, but the rest of the device is yours.

So now, this is kind of great, and the way it is meant to work is, this company offers you a standard accessory if you're trying to use a Raspberry Pi. And so it looks like this. This is like a little PCB accessory board, and you plug this into the side of the laptop, and you plug your Raspberry Pi on this, and then you've got a Pi sticking out of the side of your laptop, like this. Yes, I can sit here and work on it. Until I start doing accessories. And suddenly again it's flopping out over the side. So once again, it stops being portable. So this one was frustrating me a little bit, so I figured okay, why don't I try something radical that will potentially destroy this hardware, but you got to try it.

And so I did. And what I figured is the backside of your laptop, which is normally stickers, what if I put it over there and stick it on the back? Why can't I just stick my Pi on the back? And all you need is some kind of pegboard. Put a LEGO board, build a LEGO tower on the back of your laptop. As long as it's not too heavy, it's fine. So I tried doing that on this machine. And you can see it here. So this was one attempt at solving this problem. Here's the Pi on a multi-board. So all of your odds and ends hanging off the back of your laptop. This is a little bit of labor; every time you get a new device, I need to make a mount for it. It gets annoying a little fast. And this can only take flat things that don't add too much bulk. Because the moment it grows in depth, I can't do this. Then it starts falling off. It'll potentially damage my screen by twisting it too much. So this kind of became a dead end. It's great for the first few things to try, but then you need to try something else.

</transcript>

---

## DIN-rail tabletop rig

- I try a **DIN rail** mini-frame with multi-voltage power for clip-on modules. ([Wikipedia][6])
- It’s great for bench experiments with swappable clips.
- But… still missing a portable screen/keyboard flow.
- As a thinking rig, it’s another dead-end.
- Lesson: prototyping ease ≠ daydream-friendly workflow.

<transcript>

And so I tried something else. I kind of built a little table rack for keeping devices. This is what's called a DIN rail. There's one in everybody's house. This is where your MCB is for your main switch. The trippers are mounted on a rail like this. It's called a DIN rail. You can buy it on Amazon; it's quite cheap. And all I did was take four pieces, put them on a frame, and now this sits on a table. This is not my design. There's a guy on Printables called Iconic Fab who makes this design, and I just printed it. But you have a power inlet. From there, I do what I want. So for my experiments, I put in a whole bunch of power converters. So I have 12 volts, 5 volts, 24 volts, or mains, depending on what I'm doing here. And you can make clips for all kinds of equipment. So I can make a clip for a Raspberry Pi and put it over here. In fact, this one's on a clip. That's it.

So now this becomes a way to experiment with hardware, except... now what? Where's my keyboard, screen, and what not? So, eventually I realized that this approach was a bit of a dead end. And I had to take on some other way of doing it.

</transcript>

---

## Server racks: 19″ is weird; 10″ scarce

- I explore **server racks**; 19″ standard dates back \~1930s; mounting rail spacing **18.312″** causes fit variations. ([AudioRax][7])
- In India, small **10″ racks** are what I could actually find. ([Amazon][8])
- A 10″ frame cost \~₹16k—overkill for one Pi.
- The mismatch between need and standard offends my builder brain.
- Conclusion: time to DIY something saner.

<transcript>

So what I figured is, okay, why don't we try server racks? Those things are meant for mounting equipment, right? And so I went looking for a server rack. Now, usually what data centers use is what's called a 19-inch server rack. That means it's exactly 19 inches wide. And if you want to know why 19 inches, you're going to cry. So it's not worth getting into. But effectively, somewhere in the year 1920 or 1922, some people decided to settle on their conflict about office space and said, "Your telecom equipment rack can be exactly 19 inches wide, on the floor. You push it against the wall, next person gets next to that," and that's how they were renting out space. And it's got to do with how they build houses in America where they don't build with concrete, they build with wood, and those wood strips are 19 inches wide apart. **So it's a really weird standard, it's got nothing to do with logic**.

</transcript>

---

## DIY frame with aluminum extrusions

- I pivot to **aluminum extrusions** (3D-printer style) to build a half-size rack.
- Commodity, widely available, cut to length; bolts and brackets finish it.
- My cost beats the ₹16k box; even retail parts stay reasonable.
- With trial and error, I refine sizes to fit “not-rack” gear.
- DIY wins on price, adaptability, and joy.

<transcript>

So, I figured, okay, why don't I try using server racks? So I went looking for one. There's only one sold in this country that is the smaller standard, which is 10 inches. And I bought one, and I'm going to unbox it for you. Here we go. So at this point, or at least six months ago when I went into this, this was the only one sold in this country. This is what you get. I added a few accessories, but this is what it is. And so you can mount your equipment in these slots. It's a 1U slot just like commercial data center equipment, except it's only 10 inches wide instead of 19 inches. Now, what do you think this costs? 16,000. Yes.

Do you see this little slot over here? That's for a Raspberry Pi. And that's all the Raspberry Pi needs in terms of space. So what am I doing with all this space then? I mean, why am I buying a box this large for one Raspberry Pi? Just because it's the only one available. And it cost 16,000 rupees. For what? It's just a frame and some nice acrylic. It looks nice. I mean, yes, look at the YouTube reviews, everybody's raving about it. But what the hell? What does it cost so much for, and why do I need something this large? So this was a point where I forgot all about the daydreaming thing and said, you know, fuck it. **This is offending me. This cannot stand**. So let's fix it.

So I figured, okay, why don't I just buy some metal and make it myself? And what can it cost? And so what I did is I went to look at the 3D printing community for what they do. And aluminum is cheap. You can buy it anywhere. These are what's called aluminum extrusion. You can buy this anywhere in the world. And that's largely because windows are made of aluminum. You look at the glass window over there in the corner; it's made of an aluminum frame. So aluminum is a commodity. As a metal, it is cheap. This kind of extrusion of the metal is standard, available worldwide. And this particular form factor is popular because of the 3D printing community because they build the printers out of this.

If you look at the price, this is for one meter. It's 270 rupees per meter, plus tax, so that works out to about 320. And this is one meter of it. So I figured, okay, why don't I just use metal frames and build that? But I don't want that much space, so let's do half size.

So that's where my research began. And I wrote a blog post about how to do this. This became my exploration back in March, saying, "That's offending me. I want to do this for half the size. I have no idea how to work metal, so I'm going to see if I can buy it online by just buying all the pieces required." And so I built my first rack and documented all of the measurements and so on.

Exactly this, but half the size. See? It's exactly the same. So, this is roughly about two meters of metal. And if I had bought it from Misumi, that's 320 per meter. Twice is how much? 16,000 versus that. Obviously, that's not a full thing, right? You still need screws and stuff to join it. So it doesn't end with that little bit. But how much more can they be? They can't be 15,000 more, right? For screws?

So, this was not this price because I didn't know about Misumi at that time. And so because I had to buy from retail outlets, this actually cost me 4,000 rupees. But 16 versus four, it's already a victory, man. Why is anybody buying that? Just make it yourself. After all, it is just ordering online. You don't have to do any labor.

So I started with that, and then one of the things I realized quickly when working with this is that I was trying to use some large equipment and suddenly it didn't fit really well. Those things are not made for racks, so they don't fit the dimensions. So I tried different sizes to see what works for my purposes. So here's another. Now this one is a server rack, but it's thicker. And that's because the material that I used there is 20 mm by 20 mm, and so it's called 2020. This one is 20 by 40, so it's called 2040. What I tried was, instead of 2020, I used 2040, so that my actual internal is still 10 inches. But I can slide something bigger inside from this side. And this again is 10 inches. So now suddenly I made it a two-sided rack where now I can fit in things wherever there's space available. But while I was doing this, I also realized that when I make arbitrary decisions like this, they are meant for one idea in mind, but I'm still in the daydreaming phase of saying, "I don't actually know what my idea is." It's still something vague, that if I go in this direction, I will find something useful to do.

</transcript>

---

## From 2020 to 2040, then a cube

- I iterate from **2020 to 2040** profiles to fit larger bits.
- I discover rack depth isn’t standardized; only width is.
- I choose a **uniform cube** for mental simplicity and packing.
- EIA-310’s rail spacing is exact (18.312″), so gear uses elongated holes to tolerate cuts. ([RackSolutions][2])
- I round dimensions to practical mm; _256 mm_ happens to feel delightfully “8-bit.”

(**Edit**: The talk mentions “9.312″” for 10″—common _10″ class_ racks vary; EIA-310 doesn’t define a 10″ spec.) ([RackSolutions][2])

<transcript>

Eventually I realized that the server rack standard has absolutely no specification for how deep the rack is. It only specifies how wide. So everybody makes a rack of a different size. So then why am I following that guy's standard? That one measures 200 mm depth and 10 inches wide. It's two different units. This felt a little like, this is just confusing to me when I'm trying to install equipment because everything is a different size. So what if I just make them one uniform size in all directions?

And so I made it a cube. Now it's 10 inches in every dimension. But it's actually not exactly 10 inches because there's a little quirk to it. And that is, if you look at the spec—Wikipedia has a diagram for it of what is the actual spec for a server rack. Remember, they defined it as 19 inches on the floor. But when you're mounting, where is the screw hole? It's not on the edges, right? It's somewhere within its channel. What is the actual size? Guess. 18.312 inches. So it's an imperial standard in which they have three decimal places. You want the 10-inch version? 9.312 inches. 236.525 millimeters. That's the official standard. How do you cut metal to three-decimal-digit precision? The saw blade is 1 mm, right? You can't cut to anything less than 1 mm precision. It's going to be arbitrary. And therefore, you will find that any equipment that is meant to be rack-mounted has screw holes that are elongated. Because no rack from any two different manufacturers is actually the same size. This is not 10 inches wide, it's about 10.5. It's just that the screw holes have to be somewhere in that area.

So, if that's the case, then why do I care? I will just round it off, right? And so I figured I'm going to round it down to 236 because if it is too narrow, it's okay, you lose a little bit in the screw. But if it is too large, then I have to shave metal to tighten it. Right? So it is easier to be slightly smaller than slightly larger. So I said, okay, approximate 236.

And the material that we're dealing with here is 20 mm wide, and the mounting column, which is this channel in between, is in the middle. Which means that if I need to get to 236 with those columns in the middle, I have 10 mm extra on this side, 10 mm on that side. Which is 236 plus 10 plus 10, 256. And just this moment I'm looking at it and saying, "Hang on, 10 inches is 234 millimeters. But by some quirk of the material I'm using, I have arrived at 256 millimeters instead of 254 millimeters." **256 is like, you know, eight bits. This is very nice.** It's like a stroke of luck that I'm looking at the standard and saying, "What is this randomness? Yeah, round it off, it doesn't matter." And I got a nice number. And it just feels very satisfying, saying that I got a nice number that is just arbitrary and it actually works because the spec is so vague.

</transcript>

---

## Displays, ITX, and power: make your own PDU

- I add a 10″ display and mini-ITX: Tetris the cube space.
- Commercial “rack PDUs” don’t fit; I **build a modular power strip** from plug modules.
- I add an **earthing lug**; safer than many cheap strips.
- I can’t sell—needs India **BIS** certification—so I publish DIY instructions.
- Mounting vertical helps heavy EU plugs stay seated.

<transcript>

So, I made it as a cube. And all of the things that I've done in the process of trying to figure out how to make this, I had to find different ways. Here's something I made. This is a 10-inch display. It fits on the rack. I can attach it. Here's my little computer, it's a mini-ITX motherboard. So I can actually turn this into a PC case if I want to. And because I made it a cube, even though I'm out of space over here, I can put whatever I want over here because the display is after all hollow; it's got nothing behind it. So now this is nice because I can stuff this as I like. I can effectively play Tetris with this design and use up all the space. Except for one problem: how do I give this power? Now you need a power strip. So that became my next problem.

So these are the commercially available power strips. This is from MX. It does not fit the rack. It's sold as a rackmount power strip. Doesn't fit. Why? Because they made it a few millimeters longer and they put a cable on the side which bangs against it. Here's another one I bought. This one has a cable you can insert later. Doesn't fit. But I was looking at these modules and saying, "Hey, these look modular. Can I just buy those power modules and make my own power strip?" And so you can buy them. It's exactly the same one. You can buy it from MX. It's like 60 rupees each.

So I figured, okay, let's make one. So here's my power strip. Homemade. And it fits. See? So my idea of making it like this is to put it this way in and mount it from the bottom because all the bulky plugs that you get, which are for European plugs and not Indian plugs in India, if you try to put them horizontally, they'll fall off. You put them vertically, gravity will keep them there. So keep it like this, I've got power here. And I also made sure to put in this little piece of metal sticking out. Anyone wants to guess why? Earthing. It's metal. You don't want to kill yourself, and that's what's going to happen with one of those things. They have no grounding. So **I actually got a technically superior design which I can't sell for legal reasons because I don't have a BIS license. So instead, I can give you instructions on how to do it yourself.** So it's on GitHub.

</transcript>

---

## Buying in bulk, cutting waste

- Extrusions come in **4-meter factory lengths**; retail cuts waste material.
- I computed optimal cuts; bulk-ordered \~30 frames to lower cost and waste.
- I used most for experiments; a few spares went to friends.
- Anyone can still source retail; it’ll just cost a bit more.
- Takeaway: planning cuts beats chasing retail scraps.

<transcript>

Okay, so out there on the table, I have all of this stuff, you can come and inspect it. I also discovered in the process of buying parts that when you want to buy cheap, you buy lots. And part of the problem is that this frame is about 2.7 meters. I can commercially buy one meter. But I have to cut the full length. So what's going to happen is that those frames are 216 mm in length each. What is 216 into 4? It's almost at one meter, right? I'm going to have a little bit of it left, this much. What do I do with this extra piece? So typically the way to do this is the factories that make these things make them in four-meter lengths. And if you can get them cut at the factory, then I have very few of these extra small parts left. But I can't make a retail order and say, "Give me one stick with this many chops from the factory." So instead they say, "Please buy 40 meters at once or 50 meters." So what I did is I sat down one day with a calculator to say, "Given all my segment sizes and four-meter lengths, how many of these do I need to buy to have the minimum wastage?" and I ended up at about 30. And so I bought 30 racks from the factory because they were a fraction of the price of buying a commercial one. And I used that for my experiments, but I have some spare. I think about 15 people have already bought my spares. I have a few left over from my first bulk purchase to optimize my price.

So that's available if you feel like it, but that's completely optional because you can buy it all yourself. It will cost you more though, because I've got the benefit of bulk discounts. But that's it.

</transcript>

---

## Q\&A: Mobility and power

- **Battery/UPS?** Yes; current pack: _three 18650 cells_, \~8 hours at low idle draw; flight-safe under typical IATA limits when <100 Wh. ([IATA][9])
- **ITX board?** Mine uses an **Arm SoC**, keeping power low like the Pi.
- **Flying with it?** I stack frames using screw “feet” and nuts; simple transport hack.
- **Bigger batteries?** Unneeded so far; low-power boards sip watts.
- **General tip:** design for airline rules and modular swaps.

<transcript>

**Question**: I have another question. Any plans of making it more mobile? Like, having a UPS or some power source?
**Answer**: Yes. You see that thing there? That's a battery. It's not in this yet. It's still on my table.

**Question**: But there are batteries of the size of 10 inches, right? You can put them in the space that you have there to last longer for maybe when you have power cuts.
**Answer**: So this one is lasting me about eight hours. And it's just three 18650s. This is the nice thing about working with Arm; it's so low power. My idling on that machine—that's a Rockchip, that's not a Raspberry Pi—but the idling on that is like two and a half watts. So just with three 18650 batteries, I can get eight hours out of it. So like, why do I need bigger batteries? This is at least flight safe.

**Question**: Uh, what about the ITX board?
**Answer**: The ITX board is also an Arm chip, it is not Intel.

**Question**: Hi. Do you carry this around on flights?
**Answer**: I just brought them in here. What I typically do is... you see these holes? No hole. So what I've been trying to do is, the moment I have some equipment sticking out of it, I can't simply keep them on top of each other because then it's on the equipment. So what I've figured I will do is take a little 5-millimeter screw, put a couple of nuts on it. So now I just have to adjust the nuts to the correct size, and it sits there. And just support them. And that's my transport solution. And that's why I have a drill.

</transcript>

---

## Q\&A: DIN rails & mounting

- **DIN-rail mounting?** Feet support rails, nails, or **French cleats**; DIN needs weight checks. ([Wikipedia][6])
- For fast iteration, I use a **universal hole grid + cable ties**.
- That avoids custom mounts every experiment.
- Once the layout stabilizes, I print a custom bracket.
- Modularity > perfection during early exploration.

<transcript>

**Question**: I think I myself have gone through this kind of rabbit hole. I started with Raspberry Pis to mini-PCs to finally sticking on to like laptop motherboards. But I have to custom-print the mounts for this. One solution that I am suffering with is stacking and wall mounting. I want to mount it on a DIN rail. Is there a possibility to mount the whole of this on a DIN rail and take it out?
**Answer**: Yeah, this one. That's meant for mounting on a DIN rail, hanging on a nail, hanging on a French cleat. I haven't done DIN rail yet because I'm not sure DIN rails can take the weight for this kind of load. But a regular wall hook, the foot is meant for that. This one's ABS. For the equipment itself, one of the things I realized is that if I keep iterating on hardware, it's painful to make custom mounts every time. It's easier to just do cable ties. And so I made my own design. I kind of made a Raspberry Pi-sized design, but I also made a generic grid of holes. And with this, you just put whatever you want, cable tie it down. And that makes it very easy to iterate and figure out what you want, and then you can make a custom mount for it.

</transcript>

---

# Homelabbing with Bare Metal

[IndiaFOSS](https://fossunited.org/c/indiafoss/2025/cfp/4v6f8ek2n0) · 20 Sep 2025, 3:00 pm IST · [Bangalore](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)
[Kiran Jonnalagadda](https://www.linkedin.com/in/kiranjonna/) · Co-founder [Hasgeek](http://hasgeek.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-20-kiran-homelabbing-with-bare-metal/README.md) · [Video](https://www.youtube.com/live/FtF-I0-wJGo?t=3460s)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-20-kiran-homelabbing-with-bare-metal/)

---

## Quiz

- Why did the lapdock + Pi adapter kill portability once accessories were added?
- What problem does a uniform cube solve that standard racks didn’t?
- Why do rack-mount devices often have elongated mounting holes?
- In what ways does vertical PDU mounting help heavy plugs?
- How does daydream-friendly design change device and workflow choices?

---

## Errata

- **x86 idle comparison.** My contrast was qualitative. CPU-only idle can be low, but _system_ idle is often much higher than a Pi; EIA-310 is about rail spacing (18.312″). ([RackSolutions][2])
- **10″ rack spec.** EIA-310 defines 19″ mounting geometry; “10-inch” small racks exist commercially, but a single universal 10″ mounting spec is not canonical EIA. ([Newegg.com][10])
- **Pi power.** Pi 4 idle around \~2.7 W; my “1–2 W” remark is optimistic for Pi 4; earlier Pis or tuned configs can be lower. (**Edit**: \~2.7 W typical). ([pidramble.com][1])
- **Flight safety.** Lithium batteries under 100 Wh are generally allowed in cabin baggage with conditions; always check airline rules. ([IATA][9])
- **Lapdock concept.** Lapdocks are CPU-less laptop shells relying on a phone/mini-PC; examples include NexDock. ([Wikipedia][5])

---

## Counterpoints

<small>

- **“Just DIY a rack.”** Premade racks include EMI, airflow, and safety testing; DIY frames skip these guardrails. Consider certified enclosures for production. ([RackSolutions][2])
- **“Pi-hole solves ads.”** Some in-app ads come from the same domains as content; DNS-level blocking can break services or miss CDN-based ads. Test allow-lists. ([Pi-hole][3])
- **“Home Assistant solves all.”** HA’s power comes with maintenance overhead; vendor API changes break integrations without notice. (Recent coverage underscores fragility of community integrations.) ([The Verge][11])
- **“Lapdock is perfect.”** Lapdocks depend on device OS modes (e.g., DeX); latency, driver quirks, and trackpad quality vary widely. ([Wikipedia][5])
- **“Any battery is fine.”** National regulators add stricter rules beyond IATA (e.g., Korea); verify route-specific limits. ([Reuters][12])

</small>

---

## Feedback

- Mark measurements in one unit (mm) and summarize “why this size” early.
- Add a 1-slide diagram comparing dead-ends vs. the cube’s benefits.
- Quantify idle power for each board in a table; cite sources.
- Show a BOM with vendors and cut plan; separate “must-have” vs “nice-to-have.”
- Close with a “build in 90 minutes” quick-start checklist + repo links.

[1]: https://www.pidramble.com/wiki/benchmarks/power-consumption?utm_source=chatgpt.com "Power Consumption Benchmarks"
[2]: https://www.racksolutions.com/news/data-center-optimization/eia-310-definition/?srsltid=AfmBOoq0rVxA5bF-hsNCpD02vXJcuTT5DdUJug8LCAntcAe2i9mN6ViH&utm_source=chatgpt.com "EIA-310: What Does It Mean?"
[3]: https://pi-hole.net/?utm_source=chatgpt.com "Pi-hole – Network-wide Ad Blocking"
[4]: https://www.home-assistant.io/?utm_source=chatgpt.com "Home Assistant"
[5]: https://en.wikipedia.org/wiki/Lapdock?utm_source=chatgpt.com "Lapdock"
[6]: https://en.wikipedia.org/wiki/DIN_rail?utm_source=chatgpt.com "DIN rail"
[7]: https://www.audiorax.com/rack-rail-hole-spacing-explained?srsltid=AfmBOook98M3KXuxhNkIxu3zSHKUdu3Z8dH9JkwnFsNvLLP04wAkl-nI&utm_source=chatgpt.com "Rack Rail Hole Spacing Explained"
[8]: https://www.amazon.com/stores/NavePoint/page/4B05A581-DB09-4D31-98A5-37201761F96B?utm_source=chatgpt.com "NavePoint: 10-Inch Width Series"
[9]: https://www.iata.org/contentassets/6fea26dd84d24b26a7a1fd5788561d6e/lithium-battery-vehicles-cargo.pdf?utm_source=chatgpt.com "Passengers Travelling with Lithium Batteries Guidance ..."
[10]: https://www.newegg.com/p/pl?d=10+inch+network+rack&srsltid=AfmBOoph4blgivX7OFmLnYfMUHSwHq3kyBfCBoO_K0DMHixplu0ELoRW&utm_source=chatgpt.com "10 inch network rack"
[11]: https://www.theverge.com/news/634336/switchbot-home-assistant-45-device-integrations-coming-soon?utm_source=chatgpt.com "SwitchBot adds robot vacuums, smart shades, and its new Hub 3 to Home Assistant"
[12]: https://www.reuters.com/business/aerospace-defense/skoreas-new-lithium-battery-rules-planes-highlight-growing-risk-aviation-2025-02-28/?utm_source=chatgpt.com "SKorea's new lithium battery rules on planes highlight growing risk for aviation"
