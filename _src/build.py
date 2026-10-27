"""Builds the Dwell Home Designs static site. Run: python3 _src/build.py (from the repo root)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://dwellhomedesigns.com"
EMAIL = "nicole.r.brittingham@gmail.com"
IG = "https://www.instagram.com/dwell.home.designs/"
AREA = "west Fort Worth, Benbrook, Aledo, Willow Park, Hudson Oaks, Weatherford and the greater DFW area"

NAV = [("index.html", "Home"), ("services.html", "Services"), ("process.html", "Process"),
       ("portfolio.html", "Portfolio"), ("about.html", "About")]


def page(fname, title, desc, body):
    links = "".join(
        f'<li><a href="{h}"{" class=\"active\"" if h == fname else ""}>{t}</a></li>' for h, t in NAV)
    canon = SITE + "/" + ("" if fname == "index.html" else fname)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/images/hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header>
  <div class="wrap nav">
    <a class="logo" href="index.html">Dwell<small>Home Designs</small></a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul>{links}<li><a class="btn" href="contact.html">Book a Consultation</a></li></ul>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="logo" href="index.html">Dwell<small>Home Designs</small></a>
        <p style="margin-top:18px;max-width:340px">Residential interior design for everyday families, from one room to the whole home. Based on the west side of Fort Worth, Texas.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}<li><a href="contact.html">Contact</a></li></ul>
      </div>
      <div>
        <h4>Say hello</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram @dwell.home.designs</a></li>
          <li>Serving Tarrant &amp; Parker counties</li>
        </ul>
      </div>
    </div>
    <div class="copy">
      <span>&copy; <span class="year">2026</span> Dwell Home Designs. All rights reserved.</span>
      <span>Proud founder of <a href="https://dwellinyourneighborhood.com" target="_blank" rel="noopener">Dwell In Your Neighborhood</a>, restoring veterans' homes.</span>
    </div>
  </div>
</footer>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer"><button aria-label="Close">&times;</button><img src="" alt=""><p></p></div>
<script src="js/main.js"></script>
</body>
</html>
"""
    (ROOT / fname).write_text(html)


CTA = """
<section class="cta">
  <div class="wrap">
    <span class="eyebrow">Let's talk</span>
    <h2>Ready to love your home?</h2>
    <p>Tell me about your space, and let's set up your free 30-minute discovery call.</p>
    <a class="btn light" href="contact.html">Start Your Project</a>
  </div>
</section>"""

# Portfolio photos: (file, caption, categories)
PHOTOS = [
    ("navy-family-room", "Navy shiplap family room", "living walls"),
    ("hero", "Board and batten living room", "living walls"),
    ("blue-grid-bedroom", "Blue grid wall bedroom", "bedrooms walls"),
    ("white-kitchen", "Bright white kitchen", "kitchens"),
    ("sage-bathroom", "Sage shiplap bathroom", "kitchens walls"),
    ("oak-wall-living", "Warm oak paneled living room", "living walls"),
    ("wood-plank-bedroom", "Reclaimed wood plank bedroom", "bedrooms walls"),
    ("cognac-living", "Cognac leather living room", "living"),
    ("navy-media-wall", "Navy shiplap media wall", "living walls"),
    ("teal-grid-bedroom", "Teal grid wall bedroom", "bedrooms walls"),
    ("charcoal-dining", "Charcoal paneled dining nook", "dining walls"),
    ("layered-living", "Layered neutral living room", "living walls"),
    ("sage-bedroom", "Sage paneled guest room", "bedrooms walls"),
    ("stone-fireplace", "Stacked stone fireplace wall", "living walls"),
    ("dark-attic-bedroom", "Moody attic bedroom", "bedrooms walls"),
    ("warm-bedroom", "Warm, layered primary bedroom", "bedrooms"),
    ("white-attic-bedroom", "Shiplap attic bunk room", "bedrooms walls"),
    ("checker-rug-living", "Checkered rug living room", "living"),
    ("navy-nursery", "Navy paneled nursery", "bedrooms walls"),
    ("white-panel-living", "White grid wall living room", "living walls"),
    ("tufted-bedroom", "Soft paneled primary bedroom", "bedrooms walls"),
    ("blue-panel-lounge", "Blue paneled sitting room", "living walls"),
    ("white-fireplace-wall", "Board and batten fireplace wall", "living walls"),
    ("farmhouse-dining", "Farmhouse dining room", "dining"),
    ("neutral-bedroom", "Calm neutral bedroom", "bedrooms"),
    ("sunlit-living", "Sunlit family room", "living"),
    ("navy-entry", "Navy wainscot entry drop zone", "dining walls"),
    ("rug-bedroom", "Vintage rug guest bedroom", "bedrooms"),
]


def figs(items):
    return "".join(
        f'<figure data-cat="{c}"><img src="images/{f}.jpg" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
        for f, cap, c in items)


# ---------------- HOME ----------------
featured = [p for p in PHOTOS if p[0] in ("navy-family-room", "blue-grid-bedroom", "sage-bathroom", "white-kitchen")]
page("index.html", "Dwell Home Designs | Residential Interior Design in Fort Worth, TX",
     "Residential interior design for everyday families in west Fort Worth, Aledo, Weatherford and across Tarrant and Parker counties. Design boards, furniture sourcing and styling. Book a free consultation.",
     f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Dwell Home Designs &middot; Fort Worth, TX</span>
      <h1>Homes that feel like you</h1>
      <p class="lead">Residential interior design for everyday families, from one room to the whole home.</p>
      <div class="btn-row"><a class="btn" href="contact.html">Book a Consultation</a><a class="btn ghost" href="portfolio.html">See My Work</a></div>
    </div>
    <div class="hero-img"><img src="images/hero.jpg" alt="Bright living room with white board and batten walls, rattan console and olive tree"></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap split">
    <div class="split-img"><img src="images/styling-bed.jpg" alt="Nicole styling pillows on a bed" loading="lazy"></div>
    <div>
      <span class="eyebrow">Hi, I'm Nicole</span>
      <h2>Beautiful design for real life</h2>
      <p>Since 2022, I've helped families turn tired, unfinished or overwhelming spaces into homes they love walking into. Whether it's one room, a full remodel or your whole house, I handle the details so you can enjoy the result.</p>
      <p>Based on the west side of Fort Worth, I serve Tarrant County, Parker County and the greater Dallas&ndash;Fort Worth area, with virtual design available anywhere.</p>
      <p style="margin-top:28px"><a class="btn ghost" href="about.html">My Story</a></p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap center">
    <span class="eyebrow">What I do</span>
    <h2>Design that fits your family and your budget</h2>
    <div class="tiles" style="text-align:left">
      <div class="tile" style="background:#36445a;border-color:#d9b48f"><h3>Whole-Home Design</h3><p style="color:#c9cfd6">A cohesive plan for your entire home, phased to fit your budget and timeline.</p><a href="services.html" style="color:#fff">Learn more</a></div>
      <div class="tile" style="background:#36445a;border-color:#d9b48f"><h3>Room by Room</h3><p style="color:#c9cfd6">Start with the space that needs it most, from a single room to a statement wall.</p><a href="services.html" style="color:#fff">Learn more</a></div>
      <div class="tile" style="background:#36445a;border-color:#d9b48f"><h3>Remodel Design</h3><p style="color:#c9cfd6">Finishes, layouts and selections, coordinated with your contractor.</p><a href="services.html" style="color:#fff">Learn more</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap center">
    <span class="eyebrow">Recent work</span>
    <h2>Rooms families love living in</h2>
    <p class="lead">Warm wood, soft textures and one bold wall: a few favorite spaces from recent projects.</p>
    <div class="gallery featured">{figs(featured)}</div>
    <p style="margin-top:40px"><a class="btn ghost" href="portfolio.html">View the Portfolio</a></p>
  </div>
</section>

<section style="background:var(--linen)">
  <div class="wrap center">
    <span class="eyebrow">How it works</span>
    <h2>Simple, clear and stress-free</h2>
    <p class="lead">A free discovery call, design boards you'll love, ordering handled for you, and a styling day where it all comes together.</p>
    <p style="margin-top:32px"><a class="btn" href="process.html">See the Process</a></p>
  </div>
</section>
{CTA}""")

# ---------------- SERVICES ----------------
page("services.html", "Services & Pricing | Dwell Home Designs, Fort Worth",
     "Residential interior design services for families in Fort Worth: whole-home design, room design packages, statement walls, remodel design and virtual design. Family-friendly pricing.",
     f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Services</span>
    <h1>Design services</h1>
    <p class="lead" style="margin-top:20px">Every project starts with a conversation about how you live, what you love and what you need your home to do. Whether it's your whole home or one tired room, I'll shape the plan around your family, your budget and your timeline.</p>
  </div>
</section>

<section style="padding-top:24px">
  <div class="wrap">
    <div class="service"><div class="num">01</div><div>
      <h3>Whole-Home Design</h3>
      <p>My favorite kind of project: making your whole house feel like one warm, connected home. We create a plan for every room, then tackle it all at once or in phases as your budget allows. You get the same design boards, ordering help and styling days, at a lower per-room rate.</p>
      <p class="price">Custom quote, with a lower per-room rate for 3+ rooms</p>
    </div></div>
    <div class="service"><div class="num">02</div><div>
      <h3>Room Design Package</h3>
      <p>The full treatment for the rooms that matter most. For each room you get:</p>
      <ul>
        <li>Initial consultation and measurements (in person or virtual)</li>
        <li>Design boards with mood, layout and furniture plan</li>
        <li>A feature wall concept: paint, wallpaper or wall treatment</li>
        <li>A curated shopping list with links and alternatives</li>
        <li>Ordering and delivery coordination, including returns and damage claims</li>
        <li>A styling day to install and style everything</li>
      </ul>
      <p class="price">$1,500 for your first room, $1,200 for each additional room. Includes one revision round.</p>
    </div></div>
    <div class="service"><div class="num">03</div><div>
      <h3>Remodel &amp; Renovation Design</h3>
      <p>Planning a remodel? I help you choose finishes, fixtures, layouts and materials, then work alongside your contractor so the design comes together as planned. When construction wraps, I come back to furnish and style.</p>
      <p class="price">$75 per hour, with an estimate before we start</p>
    </div></div>
    <div class="service"><div class="num">04</div><div>
      <h3>Virtual Design (E-Design)</h3>
      <p>Not local, or love a good DIY? Get design boards, a layout and a shopping list with links, plus video check-ins. You order and place; I guide you.</p>
      <p class="price">$350 per room</p>
    </div></div>
    <div class="service"><div class="num">05</div><div>
      <h3>Statement Wall Design</h3>
      <p>Board and batten, grid paneling, shiplap or wallpaper: a wall designed for your room, with the paint color and a materials list. DIY it or hand it to your contractor.</p>
      <p class="price">$200 per wall</p>
    </div></div>
    <div class="service"><div class="num">+</div><div>
      <h3>Add-on: Home Staging</h3>
      <p>Getting ready to sell? I'll help your home photograph beautifully and stand out online, using your own furniture plus my accessories.</p>
      <p class="price">Staging consultations from $175; staging days from $600</p>
    </div></div>
  </div>
</section>

<section style="background:var(--linen)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow">Pricing at a glance</span>
      <h2>Start small or go all in</h2>
      <p class="lead">Beautiful design shouldn't be only for big budgets.</p>
    </div>
    <table class="prices">
      <thead><tr><th>Service</th><th>What you get</th><th>Price</th></tr></thead>
      <tbody>
        <tr><td>Discovery call</td><td>30-minute call to talk through your space and goals</td><td>Free</td></tr>
        <tr><td>Design consultation</td><td>90-minute in-home visit with layout, paint and furniture ideas, plus written notes</td><td>$150, credited toward any package booked within 30 days</td></tr>
        <tr><td>Whole-Home Design</td><td>A plan for every room, done all at once or in phases</td><td>Custom quote</td></tr>
        <tr><td>Room Design Package</td><td>Full design, ordering coordination and a styling day</td><td>$1,500 first room, $1,200 each additional</td></tr>
        <tr><td>Remodel Design</td><td>Finishes, fixtures and layouts, working with your contractor</td><td>$75/hour, estimate up front</td></tr>
        <tr><td>Virtual Room Design</td><td>Design board, layout and shopping list with links</td><td>$350 per room</td></tr>
        <tr><td>Statement Wall Design</td><td>Wall design, paint color and materials list</td><td>$200 per wall</td></tr>
        <tr class="small"><td>Staging</td><td>Consultation with a room-by-room checklist, or a hands-on staging day</td><td>From $175</td></tr>
      </tbody>
    </table>
    <ul class="notes">
      <li>Add-ons: extra styling day $400, 3D rendering $250, extra revisions $75/hour.</li>
      <li>Furniture and decor are purchased directly by you; I handle the ordering and tracking.</li>
      <li>Furniture assembly isn't included. I can recommend help, or have it ready before styling day.</li>
      <li>Projects begin with a 50% deposit.</li>
    </ul>
  </div>
</section>
{CTA}""")

# ---------------- PROCESS ----------------
page("process.html", "How It Works | Dwell Home Designs",
     "From a free 30-minute discovery call to design boards, ordering and styling day: here's what working with Dwell Home Designs looks like.",
     f"""
<section class="page-head">
  <div class="wrap split">
    <div>
      <span class="eyebrow">The process</span>
      <h1>How it works</h1>
      <p class="lead" style="margin-top:20px">A clear, simple process so you always know what's next.</p>
    </div>
    <div class="split-img"><img src="images/styling-sofa.jpg" alt="Nicole styling pillows on a cognac leather sofa"></div>
  </div>
</section>
<section style="padding-top:24px">
  <div class="wrap">
    <ol class="steps">
      <li><div><h3>Discovery call</h3><p>We talk through your space, your style, your budget and your timeline. <em>Free, 30 minutes.</em></p></div></li>
      <li><div><h3>Consultation &amp; proposal</h3><p>I visit or video-walk your home, take measurements and photos, then send a proposal. A 50% deposit reserves your spot.</p></div></li>
      <li><div><h3>Design boards</h3><p>In about a week, I present mood boards, layouts and product links for each room. You get revisions until it feels right.</p></div></li>
      <li><div><h3>Ordering &amp; delivery</h3><p>Once you approve, I order everything, track deliveries and handle returns or damage claims.</p></div></li>
      <li><div><h3>Styling day</h3><p>I arrive to place, layer and style every piece. You walk into a finished room. <em>Furniture should be assembled before this day.</em></p></div></li>
    </ol>
  </div>
</section>
{CTA}""")

# ---------------- PORTFOLIO ----------------
page("portfolio.html", "Portfolio | Dwell Home Designs, Fort Worth Interior Design",
     "Living rooms, bedrooms, kitchens, baths and statement walls designed by Nicole Brittingham of Dwell Home Designs in Fort Worth, Texas.",
     f"""
<section class="page-head center">
  <div class="wrap">
    <span class="eyebrow">Portfolio</span>
    <h1>A few homes I've had the joy of designing</h1>
    <div class="filters">
      <button class="on" data-filter="all">All</button>
      <button data-filter="living">Living Rooms</button>
      <button data-filter="bedrooms">Bedrooms</button>
      <button data-filter="kitchens">Kitchens &amp; Baths</button>
      <button data-filter="dining">Dining &amp; Entry</button>
      <button data-filter="walls">Statement Walls</button>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap"><div class="gallery">{figs(PHOTOS)}</div></div>
</section>
{CTA}""")

# ---------------- ABOUT ----------------
page("about.html", "About Nicole | Dwell Home Designs",
     "Meet Nicole Brittingham, founder of Dwell Home Designs in Fort Worth and of Dwell In Your Neighborhood, a nonprofit restoring veterans' homes.",
     f"""
<section class="page-head">
  <div class="wrap split">
    <div>
      <span class="eyebrow">About</span>
      <h1>Hi, I'm Nicole</h1>
      <p class="lead" style="margin-top:20px">I started Dwell Home Designs in January 2022 with a simple belief: your home should be a peaceful, beautiful place you love walking into.</p>
      <p style="margin-top:20px">I design for real life. That means rooms that work for busy families, finishes that hold up, and spaces that still feel personal. I handle the boards, the shopping, the deliveries and the styling, so you get to enjoy the fun part.</p>
      <p>And I'm not afraid to pick up a paintbrush or a hammer. Every project is a whole-home, whole-heart effort, and I'm flexible about meeting your family where you are.</p>
      <p style="margin-top:28px"><a class="btn" href="contact.html">Work With Me</a></p>
    </div>
    <div class="split-img"><img src="images/nicole-painting.jpg" alt="Nicole painting a navy board and batten wall" style="aspect-ratio:auto"></div>
  </div>
</section>
<section class="band">
  <div class="wrap split rev">
    <div class="split-img"><img src="images/nicole-hammer.jpg" alt="Nicole holding a hammer in safety glasses" loading="lazy"></div>
    <div>
      <span class="eyebrow">Design with a bigger purpose</span>
      <h2>Dwell In Your Neighborhood</h2>
      <p class="lead">I'm also the founder of Dwell In Your Neighborhood, a nonprofit that restores veterans' homes with help from local businesses, volunteers and friends.</p>
      <p style="margin-top:16px;color:#c9cfd6">It's so much bigger than houses. It's about restoring hope and honoring those who served.</p>
      <p style="margin-top:28px"><a class="btn light" href="https://dwellinyourneighborhood.com" target="_blank" rel="noopener">Learn About DIYN</a></p>
    </div>
  </div>
</section>
{CTA}""")

# ---------------- CONTACT ----------------
CHECKS = ["Whole-home design", "Room design", "Remodel design", "Virtual design", "Statement wall", "Staging", "Not sure yet"]
page("contact.html", "Contact | Book a Free Consultation | Dwell Home Designs",
     "Tell Nicole about your home and book a free 30-minute discovery call. Serving west Fort Worth, Aledo, Weatherford and the DFW area.",
     f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Let's talk about your home</h1>
    <p class="lead" style="margin-top:20px">Share a few details and I'll reply within two business days to set up your free 30-minute discovery call.</p>
  </div>
</section>
<section style="padding-top:16px">
  <div class="wrap contact-grid">
    <form action="https://formsubmit.co/{EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="New inquiry from dwellhomedesigns.com">
      <input type="hidden" name="_next" value="{SITE}/thank-you.html">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="form-grid">
        <div><label for="name">Name *</label><input id="name" name="Name" required autocomplete="name"></div>
        <div><label for="email">Email *</label><input id="email" type="email" name="email" required autocomplete="email"></div>
        <div><label for="phone">Phone</label><input id="phone" type="tel" name="Phone" autocomplete="tel"></div>
        <div><label for="city">City *</label><input id="city" name="City" required placeholder="e.g. Aledo"></div>
        <fieldset class="full"><label>What can I help with? *</label>
          <div class="checks">{"".join(f'<label><input type="checkbox" name="Services" value="{c}"> {c}</label>' for c in CHECKS)}</div>
        </fieldset>
        <div><label for="rooms">Which rooms?</label><input id="rooms" name="Rooms"></div>
        <div><label for="timeline">Ideal timeline</label><select id="timeline" name="Timeline"><option>ASAP</option><option>1&ndash;3 months</option><option>3&ndash;6 months</option><option>Just exploring</option></select></div>
        <div><label for="budget">Approximate budget</label><select id="budget" name="Budget"><option>Under $2,500</option><option>$2,500&ndash;$5,000</option><option>$5,000&ndash;$10,000</option><option>$10,000+</option><option>Not sure yet</option></select></div>
        <div><label for="heard">How did you hear about me?</label><select id="heard" name="Heard about"><option>Instagram</option><option>Referral</option><option>Google</option><option>Houzz</option><option>Other</option></select></div>
        <div class="full"><label for="msg">Tell me about your space</label><textarea id="msg" name="Message"></textarea></div>
        <div class="full"><button class="btn" type="submit">Send</button></div>
      </div>
    </form>
    <aside class="contact-side">
      <h3>Good to know</h3>
      <p>Your first call is free and takes about 30 minutes.</p>
      <p>Serving {AREA}. Virtual design available anywhere.</p>
      <p>Prefer email? <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>Instagram: <a href="{IG}" target="_blank" rel="noopener">@dwell.home.designs</a></p>
    </aside>
  </div>
</section>""")

# ---------------- THANK YOU ----------------
page("thank-you.html", "Thank You | Dwell Home Designs", "Thanks for reaching out to Dwell Home Designs.", f"""
<section class="page-head center" style="padding:120px 0">
  <div class="wrap">
    <span class="eyebrow">Message sent</span>
    <h1>Thank you!</h1>
    <p class="lead" style="margin:24px auto 36px">I can't wait to hear more about your home. I'll be in touch within two business days. In the meantime, find inspiration on Instagram.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn" href="{IG}" target="_blank" rel="noopener">@dwell.home.designs</a><a class="btn ghost" href="portfolio.html">Browse the Portfolio</a></div>
  </div>
</section>""")

# ---------------- extras ----------------
(ROOT / "CNAME").write_text("dwellhomedesigns.com\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"<url><loc>{SITE}/{'' if f == 'index.html' else f}</loc></url>"
               for f in ["index.html", "services.html", "process.html", "portfolio.html", "about.html", "contact.html"])
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
(ROOT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#2E3A4B"/><text x="32" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="38" fill="#F7F4EF">D</text></svg>')
print("built")
