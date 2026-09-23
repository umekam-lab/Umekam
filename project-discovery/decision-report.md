# Decision report: project discovery for Rune á Kamarinum

Prepared 22 September 2026. Status: **desk-research recommendation, not yet validated by customer behaviour.** Confidence in the winner is low to medium. The lead over the runner-up is narrow and depends on one assumption that 14 days of fieldwork can settle.

> **Update, 23 September 2026: market check.** Web search worked again, so I checked the supply route before sending any supplier emails. Sources are in `evidence.md` §3.6. What I found:
> - **HealSafe already has a Danish distributor: Arkisafe.** HealSafe's own distributors page lists it. The 22 September claim that "no Danish distributor was found" was wrong.
> - **Arkisafe also represents Teal LifeCare in Scandinavia** and already serves social settings, not only psychiatry. For example, it furnished Bo og Naboskab Sydlolland, a municipal residential unit for adults with developmental disabilities.
> - **Pineapple Contracts lists a distributor in Denmark.** Its name was not found.
> - **Affari of Sweden's "ROBUST" is a home-decor collection** made from recycled metal barrels. It is not care furniture and should not have been listed.
>
> **What this means:**
> - **Demand for A is stronger than I thought:** social settings do buy robust furniture.
> - **A's plan to become a distributor is mostly closed:** the specialist makers are already represented, mainly by the main competitor.
> - **The remaining routes for A all need your decision:**
>   1. become an agent or reseller *through* Arkisafe or Pineapple's Danish distributor, with a lower margin
>   2. an own-brand range made by Danish joiners, with more capital and testing
>   3. sell the walkthrough as a paid service and buy products from whoever supplies
> - **A and B are now tied:** 3.45 each at base weights, and B leads in four of the six weightings (`analysis/scoring.py`).
>
> **The evidence no longer picks a single winner.** Per the brief, the recommendation becomes the most valuable next experiment. That is the same 14-day sprint with the same buyers, now testing A and B as equals, plus partner terms for each: Arkisafe for A, Linucare for B. Three enquiry emails (Arkisafe, Pineapple, Linucare) are saved as **drafts** in your Gmail and have not been sent.
>
> Cold email to institutions is not an option: Danish law bans unsolicited marketing email to businesses as well as to consumers (markedsføringsloven § 10). Customer contact must be by phone or to people you know.
>
> The sections below keep the original 22 September analysis. Where the update contradicts them, the update wins.

Companion files: `evidence.md` (sources, calculations, gaps), `validation-plan.md` (the 14-day test, outreach, offer, criteria), `progress.md` (status and next step), `research_notes/` (raw scan notes, about 550 source URLs), `analysis/` (scoring and unit-economics scripts; run them to reproduce every number here).

---

## 1. Recommendation

**Lead project: robust, calm rooms for specialist settings.** Working name: *Robuste Rum* (check the name is free before using it).

- **What we sell:** fixed-price packages of robust but homely furniture and fixtures (bedroom, common room, calm corner). Each package starts with a paid walkthrough of the setting by someone who has done the job.
- **Who we sell to:** private and self-governing (*selvejende*) residential units (*opholdssteder*, *bosteder*), specialist schools and day-treatment units (*dagbehandlingstilbud*) that serve children, young people or adults with outward-reacting behaviour.
- **How it starts:** as a distributor or agent for established Nordic or UK makers, with no own manufacturing and no personal data.
- **How it can grow:** an own-brand range, municipal and regional customers, and other Nordic countries.

**Strongest supporting evidence** (all from search-result excerpts; see `evidence.md` for URLs and verification status):
1. **Buyers already pay for this category.** Danish regional psychiatry buys anti-ligature and robust furniture. Arkisafe has announced agreements with Region Hovedstaden, Region Sjælland and Region Nordjylland, and Daarbak Design has supplied the regions under the D5R framework since 1 April 2025.
2. **The law makes the physical setting part of violence prevention.** Arbejdstilsynet's violence guidance (At-vejledning D.4.3) tells employers to consider the *physical framework* when assessing violence risk. Violence is high where these units operate: 343 reported accidents per 10,000 employees in residential institutions and home care in 2023, mainly from violence and stress, and 27% of Socialpædagogerne members reported physical violence in the past 12 months (2023 survey). Institut for Menneskerettigheder reports rising violence and threats against residents of residential care (*botilbud*).
3. **Specialist budgets are large and growing, and settings pay for their physical environment.** Municipal spending on specialist schools and special classes rose from DKK 12.6bn (2019) to DKK 14.4bn (2024). Sensory rooms get funded from municipal budgets (Hedensted: DKK 500k in 2025) and foundations (a regional special school: DKK 172k).
4. **The private segment looks under-served and reachable.** The proven suppliers are built around regional frameworks and large psychiatry projects. The Swedish maker HealSafe says it sells directly only in Sweden and Norway and picks distributors for other countries. *(Corrected 23 Sep: its Danish distributor is Arkisafe, which also serves social settings, so this segment is less open than stated here.)* Almost every purchase in this segment falls far below the DKK 1,611,360 EU threshold for goods (2026–27). Private providers probably buy outside public frameworks, but that still needs a legal check.

**Why you:**
- **You know the problem from inside.** You have spent over ten years in specialist education and day treatment. You know what gets thrown, what gets broken, what staff strip out of rooms, and what Arbejdstilsynet and the social inspectorate (*Socialtilsynet*) look at. You speak the buyer's language and can run a walkthrough that a furniture salesperson cannot.
- **The buyers are the NÆRVÆRK buyers.** Leaders and boards of specialist settings are the people you will meet for NÆRVÆRK anyway, so the two sales efforts support each other.
- **It runs in parallel with NÆRVÆRK.** Unlike every software-shaped alternative, it involves no personal data, no GDPR work and no 24/7 service, so it can move while NÆRVÆRK waits on its consultants.
- **It is the physical product you asked for.** It uses existing, tested products rather than invention.

**What is not proven:** that small private settings spend enough on damage-driven replacement, and will pay a premium for robust packages, to support a distributor. This is the decisive unknown. The 14-day plan tests it directly, with a paid step, and tests the runner-up with the same buyers at almost no extra cost.

**Two alternatives:**
- **Alternative 1: staff safety alarms with incident follow-up.** Same buyers. This has the strongest demand evidence of all 20 candidates. It lost on liability, 24/7 operations, the GDPR overlap with NÆRVÆRK, and weak differentiation against established suppliers.
- **Alternative 2: coordinated estate clearance and senior moves.** Demand is strong and deadline-driven. It lost on thin margins, no insider advantage, and work that must be done within days, which clashes with limited weekly time.

---

## 2. Materials inspected and research limits

- **Inspected:** the brief (`Claude_Code_Project_Discovery_Rune.txt`). The repository `umekam-lab/Umekam` was empty: no commits, files, NÆRVÆRK materials or workspace instructions. No ChatGPT history or other accounts were available.
- **Web research:** six parallel research streams covered 20 problem/opportunity pairs on 22 September 2026. The session had a 200-search cap, which ran out during the scan. The network policy blocked every direct page fetch. **Every cited fact therefore comes from search-engine result extracts, not from reading the source page.** Each claim in `evidence.md` carries that status. None of the planned deep-dive fetches (supplier price lists, Tilbudsportalen counts, Arkisafe and HealSafe terms) could be run. The deep dives below combine the scan evidence with explicit assumptions, and the checks that could not be run have become first tasks in the validation plan.
- **Confidentiality:** no founder, family, employer or student information was used in any search.

---

## 3. Where you have an advantage

| Asset | Status | Business advantage it creates |
|---|---|---|
| 10+ years in specialist education and day treatment: social pedagogy, teaching, documentation, board work | **Demonstrated** (founder statement, consistent history) | Credibility with leaders and staff; knowledge of incident patterns, room use and the work-environment and inspection rules; a walkthrough service others cannot copy quickly |
| Board work | **Demonstrated** | Understands how self-governing settings approve spending; can speak to boards |
| NÆRVÆRK product ownership (Lovable, Supabase, testing, GDPR coordination) | **Demonstrated as product ownership with AI-assisted building**; no engineering credentials or commercial traction yet | Can build simple quoting and catalogue tools and documentation packs; knows the buyer's documentation burden |
| Network across schools and treatment organisations | **Plausible, size unknown** | Warm introductions to the first 10 customers. Must be measured in week 1 |
| Direct sales, persistence, negotiation, recruiting specialists | **Self-reported**; not demonstrated in a new market | Must show up as conversion rates in the validation plan |
| PADI instructor | **Demonstrated, recreational** | No commercial diving in Denmark without a Søfartsstyrelsen commercial diver certificate (30 m course ≈ DKK 49k ex VAT) |
| Father's drones | **Unconfirmed** | The DK-STS-03 transitional declaration expired on 1 January 2026, and Remote-ID is proposed from 2027. Older drones may not be usable for commercial work in towns |
| Property-related work | **Unspecified** | Not relied on |
| Capital | **Unspecified** | Options staged: validate (<25k), pilot (<170k), scale (quoted separately) |

**Capabilities to hire or prove:**
- furniture engineering and testing documentation (comes from the supplier)
- installation (freelance carpenter)
- product-liability and distributor contract review
- logistics
- accounting
- later, industrial design for an own-brand range

**Assumptions about you that could distort this recommendation:**
1. **Insider bias.** What hurts at one setting may not hurt everywhere. The validation plan interviews settings other than your own.
2. **Sales strength is self-reported.** The plan measures meeting and paid-step conversion instead of assuming them.
3. **Daytime availability.** Walkthroughs happen in working hours. If you are employed full-time with no flexibility, the plan slows to about 2 walkthroughs a month.
4. **Conflict of interest with your employer.** Selling to peers in the same sector may need disclosure and must never draw on employer or student information. Check your contract's rules on side businesses (*bibeskæftigelse*).
5. **NÆRVÆRK's state.** If NÆRVÆRK suddenly needs full attention, a distributor model can pause without stranding customers. A 24/7 alarm service could not.

---

## 4. The 20 problem/opportunity pairs scanned

Evidence strength: **S** = observed spend or published prices plus sales signals, **M** = several competitors with public prices, **W** = opinion, anecdote or nothing found. Details and sources are in `research_notes/`.

| # | Problem / opportunity | User → buyer | Current alternative | Cost if unresolved | Reason to switch | Evidence | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Robust / anti-ligature furniture for social and specialist settings | Residents, pupils, staff → leader or owner (private); region (psychiatry) | Cheap furniture replaced often, stripped rooms, custom joinery, Arkisafe and Daarbak (psychiatry) | Injuries, replacement spend, institutional rooms (not quantified) | Robust *and* homely, small orders, advice from a practitioner | M (psychiatry) / W (social sector) | **Lead** |
| 2 | Low-stimulus booths for pupils with ADHD or autism | Pupils → school leader, municipal building budget | Screens DKK 2.35k–30.5k, corridors, office pods DKK 28k–66k | Disruption, exclusion | Child-safe booth priced between screens and pods | M (screens) / W (booths) | Not shortlisted: no evidence schools buy booths; heavy development |
| 3 | Phone storage for schools | Teachers → school leader | Phone in bag (free); phone lockers DKK 2.65k–3.9k | Distraction | Little | M | Rejected: the L 130 bill lapsed; the new ban is not yet law; commodity |
| 4 | Sensory and regulation rooms | Pupils, residents → leader, municipality, foundations | MultiCare, Ran-Play, Oliz, DIY | Poor regulation | Package led by pedagogy | M | Folded into the lead as an add-on (crowded, lumpy) |
| 5 | Staff safety alarms plus incident follow-up | Staff → leader and health-and-safety committee | CEKURA (DKK 169/month), Alarmselskabet (149–249), Linucare, Ascom (SKI) | Injury, sick leave, orders from Arbejdstilsynet | Reliability that can be proven; alarm-to-report link | S–M | **Alternative 1** |
| 6 | E-bike battery charging cabinets | Residents → board | Dedicated sockets, house rules, cabinets DKK 9k–73k | Rare but severe fires (143 in 2024) | Complete package for boards | M | Rejected: no mandate; commodity; low fit |
| 7 | Water-leak shut-off | Homeowner → homeowner / insurer | LeakBot DKK 60/month via insurer; free alerts from water utilities | DKK 25k–150k per claim | Little | S | Rejected: insurers already subsidise a competitor |
| 8 | Maintenance planning for housing co-operative boards | Board → board / administrator | Plan 1, Min Boligforening, Ejendom.com, Unyti, administrators | Stale plans, surprise costs | Plan kept up to date between reviews | M–S | Shortlisted (D) |
| 9 | Drone roof inspection | Boards, surveyors → same | 6+ providers at DKK 3k–9.5k per job; scaffolding DKK 15k–25k | Missed defects | Cheaper than scaffolding | M | Rejected as a stand-alone: crowded, rules tightening, drones unconfirmed |
| 10 | Home solar systems whose installer has gone | Homeowner | Local electrician | Lost output | Service package | W (DK) | Rejected: weak Danish evidence; needs electrical authorisation |
| 11 | Heat-pump service gap | Homeowner | Service agreements DKK 1.25k–3.5k/year; all-brand provider at DKK 1,795 | Breakdowns | None found | M | Rejected: no evidence of a gap; needs certified technicians |
| 12 | Brush boat-wash stations | Boat owner → marina | Copper paint (legal in Danish salt water) | Pollution | Environmental | W (DK) | Rejected: no Danish ban; kit costs DKK 0.34m–1.68m; main supplier shrinking |
| 13 | Mooring inspection by underwater drone | Harbour master → harbour / club | Dive firms at DKK 3,000/hour | Boats breaking loose | Cheaper visual check | W–M | Rejected: no inspection duty; small, seasonal jobs |
| 14 | Holiday-home monitoring plus inspection visits | Owner → owner | Weekly visits at DKK 695–1,150/year; alarm firms | Frost, leaks, break-ins (40% of break-ins happen Nov–Feb) | Real-time alerts plus someone who acts | M | Shortlisted (E) |
| 15 | Tool theft from vans | Tradesperson → owner | Lock installers at DKK 10k–14k, insurer-linked | ~DKK 40k–70k per theft | Little | S | Rejected: crowded; thefts down 20% in 2025; low fit |
| 16 | Cargo-bike service for daycare institutions | Staff → institution leader | Local bike shop, supplier | Lost outings, safety | Mobile scheduled service | W | Not shortlisted: no service-spend evidence (re-check later) |
| 17 | EV charging for housing associations | Residents → board | Clever, Monta, Spirii, others | — | — | W (unsourced) | Rejected: crowded, capital-heavy |
| 18 | Estate clearance and senior moves | Family → heirs / senior | Clearance firms (plejebolig DKK 4k–7k ex VAT), gig platforms, Lenore (DKK 560–595/h) | Rent until re-let, lost workdays, stress | One coordinator, transparent resale | M–S | **Alternative 2** |
| 19 | Mould monitoring in rental housing | Tenant → landlord | Surveys after complaints | Rent reductions, liability | Documenting the cause | W | Rejected: no evidence of spend; meter companies already present |
| 20 | Children's swimming (special-needs niche) | Child → parents | Clubs (DKK 1.8k–2.3k/season, waiting lists); private (DKK 4k–4.9k per 10 lessons) | Waiting lists up to about 12 months | Immediate start, adapted teaching | M | Not shortlisted: scarce pool time; your qualification unverified; hours-bound |

---

## 5. The five candidates in depth

All DKK figures exclude VAT unless marked. "Fact" means seen in a search extract with a source in `evidence.md`. "Assumption" means a working number to be tested. The calculations are in `analysis/economics.py`.

### A. Robust, calm rooms for specialist settings (LEAD)

**Problem, frequency, severity, trigger.**
- **Problem:** in units for outward-reacting children, young people and adults, furniture and fixtures get broken, thrown, used as weapons or used as ligature points. Staff respond by stripping rooms bare, which makes them feel institutional and can itself raise arousal, or by buying cheap furniture again and again.
- **Severity:** injuries to staff and residents, replacement spend, and poor living conditions. Arbejdstilsynet counts the physical framework as part of the violence risk assessment (fact). The social inspectorate's quality model assesses physical surroundings (*fysiske rammer*) (background knowledge, verify).
- **Frequency:** incident-driven, likely monthly in high-intensity units (assumption).
- **Purchase triggers:** damage after an incident, a new high-risk resident, an Arbejdstilsynet visit or order, a new unit or renovation, the start of the budget year.

**Initial segment and budget holder.**
- **Segment:** private and self-governing residential units, children's residential institutions (*døgninstitutioner*), specialist schools and day-treatment units within 1.5 hours' drive of you.
- **Budget holder:** the leader or owner in private units; the leader plus board in self-governing ones. The health-and-safety representative influences the purchase.
- **Later segments:** municipal units, which buy under their own agreements and SKI (the public joint purchasing body), and regional psychiatry, which buys through framework tenders.
- **Size of the target list:** not retrieved. Get it from Tilbudsportalen and danskeskoler.dk in week 1.

**Evidence of spend and willingness to pay.**
- **Medium for the category:** regional psychiatry buys through agreements with Arkisafe and Daarbak.
- **Weak for this segment:** there is anecdote (young residents throwing tables and chairs; source: Altinget) and context (violence rates, specialist budgets, sensory-room spending). No transaction, price or damage-cost data was found for private settings.

**Competition and alternatives.**
- **Direct:** Arkisafe (Danish; distributes Teal LifeCare, UK, and HealSafe, Sweden, furniture for "challenged environments"; anti-ligature curtains and fittings; regional agreements; already furnishes municipal social settings such as Bo og Naboskab Sydlolland), Daarbak Design (health sector; SKI 50.30 and 03.13; D5R framework), Pineapple Contracts (UK; lists a Danish distributor), Broda and Norix (US). Norwegian health and institution furniture makers such as Haugstad Fabrikker are possible further sources. *(Affari of Sweden "ROBUST" was removed on 23 Sep: it is home decor.)*
- **Indirect:** standard contract furniture through SKI (Lekolar Leika, Kinnarps and others), retail flat-pack, local joinery, sensory-room suppliers (MultiCare, Ran-Play and others).
- **Doing nothing:** strip rooms and replace as things break.
- **Prices:** no robust-range prices were public in the extracts, so supplier price lists are a day-1 task.
- **Customer feedback:** none found.

**Our improvement, and why incumbents would struggle to erase it.**
1. A **practitioner-led walkthrough** (about 2 hours) that turns incident patterns into a room plan tied to the violence risk assessment and the inspectorate's view of the physical surroundings.
2. **Fixed-price packages for one room at a time**, so a 6–12-place unit can buy without a tender.
3. **Homely rather than clinical** products chosen for social settings, not psychiatry.
4. **Fast delivery, installation, and a repair-or-replace service.**
5. A **documentation pack** (before and after, plus what changed) for the board, the safety representative and inspections.

The incumbents are organised around regional framework tenders and large psychiatry projects. Serving hundreds of small private buyers needs a trust-based, visit-heavy sales approach they do not currently show. **Be honest about the moat: it is channel trust and practitioner credibility, not product IP.** Arkisafe could copy the offer if the segment proves attractive. The response is speed: win the first 30 settings and their references.

**First version: what you do versus partners.**
- **You:** sales, walkthroughs, room plans, quotes, customer relationships, before-and-after documentation.
- **Partners:**
  - one or two makers under an agent or distributor agreement. *Corrected 23 Sep: HealSafe and Teal LifeCare are already distributed in Denmark by Arkisafe, and Pineapple lists a Danish distributor. Realistic routes are agent or reseller terms through Arkisafe or Pineapple's Danish distributor, or an own-brand range from a Danish joiner.*
  - a freelance carpenter or installer
  - an accountant
  - an insurance broker for product and business liability
- **Specialists later:** a furniture designer for an own-brand range.
- **No manufacturing, tooling or stock at the start.**
  - Landed cost: Swedish goods arrive VAT-reverse-charged within the EU with no customs. UK goods pass customs; under the EU–UK trade agreement, UK-origin goods usually pay no duty (background knowledge, verify).
  - Product liability: an importer of non-EU goods is treated as the producer. The new EU Product Liability Directive (2024/2853) widens this (background knowledge, verify).
  - Standards: use only products with documented strength and fire tests, for example EN 16139 / EN 1728 (non-domestic seating), EN 15372 (tables) and EN 1021 (upholstery ignitability). These references are unverified. Never make suicide-prevention claims beyond what the maker has certified.
  - Quality control: check the maker's test certificates and inspect on delivery. Returns: pass through the maker's terms.

**Route to the first ten paying customers.**
1. **Warm network:** 20–30 leaders you can call personally. Expect 3–5 customers.
2. **Referrals and case studies** from pilot customers.
3. **LOS (the association of private social providers) and Selveje Danmark:** newsletters, regional meetings, conference stands. Both exist (background knowledge); member counts need verifying.
4. **Phone outreach** to leaders, using lists from Tilbudsportalen. *(23 Sep: not cold email or LinkedIn messages, because markedsføringsloven § 10 bans unsolicited electronic marketing to businesses.)*
5. **Arbejdstilsynet's public smiley register:** a unit with a recent order about violence has a live trigger (verify that it can be searched this way).
6. **Health-and-safety consultants** who advise after an Arbejdstilsynet order, as referrers.

**Sales cycles (assumptions):**
- private units: 2–8 weeks
- self-governing units: 1–3 months
- municipal units: 3–9 months

**Likely objections:**
- "too expensive compared with IKEA"
- "we must use the municipality's agreement"
- "it will look institutional"
- "no budget left this year"
- "who installs it and what if it breaks?"
- "we already use Arkisafe"

**Price hypothesis and unit economics** (assumptions; `analysis/economics.py`).
- **Walkthrough and room plan:** DKK 2,500, credited in full against an order within 60 days.
- **Packages:** robust bedroom DKK 18k–40k; calm common room DKK 35k–90k. First order DKK 30k / 45k / 80k (low / mid / high).
- **Distributor discount:** 25% / 32% / 38% off list. Freight 7% / 5% / 3%. Installation 2–4 hours at DKK 450. A 2% reserve for returns and warranty.
- **Contribution per order:** DKK 3.0k / 9.9k / 25.5k, a margin of 10% / 22% / 32%. At 10–15 founder hours per order, that is DKK 200 / 825 / 2,550 per founder hour.
- **Fixed costs:** DKK 45k–80k a year (insurance, accounting, web, demo-stock depreciation, travel). Break-even takes 27 / 6 / 2 orders a year.
- **Year 1 with 10 customers, 40% of them reordering DKK 15k:** revenue DKK 360k / 510k / 860k; contribution after fixed costs DKK −44k / +52k / +229k.
- **The model only works if supplier terms land in the middle or high case.** A maker offering 25% on small orders makes it unviable. That is why supplier terms are a stop criterion.
- **Own-brand stage:** a 45–55% gross margin raises contribution on a DKK 45k order to about DKK 17k–22k.

**Capital required** (assumptions to verify).

| Stage | One-off | Recurring | Working capital | Total |
|---|---|---|---|---|
| Validate (14 days) | Mileage DKK 3k–6k; 1–2 samples or deposit DKK 0–8k; printing and domain DKK 1.5k; optional supplier visit DKK 3k–6k | — | — | **DKK 5k–20k** |
| First paid pilot (3–5 delivered orders, days 15–90) | Company set-up (sole trader: almost nil; ApS: share capital, verify current minimum); demo kit DKK 25k–60k (resaleable); web and catalogue DKK 5k–15k | Insurance DKK 6k–15k/year; accounting DKK 5k–10k/year | Supplier prepayment on 3 overlapping orders, with 30% customer deposits: ≈ DKK 40k–80k | **DKK 80k–170k** |
| Scale as distributor (months 4–24) | Show van or showroom DKK 100k–250k; trade fairs and tender bids DKK 50k–150k | Part-time salesperson or installer DKK 250k–450k/year | Stock of fast movers DKK 150k–400k | **DKK 0.4m–1.2m** |
| Ambitious own-brand range | Design DKK 100k–300k; prototypes DKK 50k–150k; strength and fire tests DKK 50k–150k per product family; wood and steel need jigs rather than moulds | — | First production run (minimum order unknown) DKK 300k–1m | **+DKK 0.8m–2.5m** |

**Time, workload, complexity, expansion.**
- **Time to first revenue:** paid walkthroughs in weeks 2–4. First order in weeks 6–12, with delivery 4–8 weeks later (supplier lead time, assumption).
- **Workload:** 10–12 hours a week during validation; 8–12 hours a week during the pilot, including 2–4 daytime visits a month.
- **Complexity:** low to moderate (logistics, installation, occasional returns).
- **Expansion:** municipal units (below threshold, positioned as special equipment outside the frameworks), regional psychiatry (partner or bid), special classes in state schools, other Nordic countries through the makers, an own-brand range.
- **Adjacent offers:** calm and sensory corners, a staff-alarm partner offer, and documentation of reduced incidents (the natural bridge to NÆRVÆRK).

**Why it could fail:**
1. The segment accepts damage as a running cost and buys cheap.
2. No maker gives viable terms for small orders.
3. Arkisafe or an SKI supplier already serves small private units with similar packages.
4. Purchases are one-off and lumpy, so volume needs many accounts.
5. Budget pressure on private units delays spending.
6. Your daytime availability caps the number of walkthroughs.
7. A product involved in a self-harm incident creates liability and reputational risk.

### B. Staff safety alarms with incident follow-up (Alternative 1)

- **Problem:** staff facing violence need help within seconds and need to trust that the alarm works.
  - Arbejdstilsynet has ordered a residential unit to secure "fast and effective help", concluding that police arrive too late and staff need an internal alarm (fact).
  - On 31 May 2026, alarms failed during an assault at Aalborg forensic psychiatry and four staff were sick-listed (fact).
  - After each incident, leaders fill in the work-accident report (via EASY), internal registration and, for residents, use-of-force (*magtanvendelse*) forms, with monthly reports due by the 5th (fact). Double registration is a hypothesised pain.
- **Segment and budget holder:** the same settings as A. Budget holder: the leader, with the health-and-safety committee. Municipal units often buy through SKI (Ascom is on SKI's welfare-technology agreement).
- **Evidence of spend: Strong–Medium.** Public prices:
  - CEKURA from DKK 169 per device a month, 6-month minimum, 90+ business and municipal customers
  - Alarmselskabet DKK 149–249 a month
  - an unnamed provider from DKK 199 a month
  - Linucare app and button (safety package DKK 590)
  - Ascom through a framework

  Enforcement orders and violence statistics create recurring pressure.
- **Competitors:** the names above plus Intelligent Care, CS Vagt and Reactio. Tunstall, Zenitel and TeleCare Nordic were not researched. No structured reviews were found.
- **Improvement:** a team alarm within the building with room-level location, automatic self-tests with a log you can show Arbejdstilsynet, an alarm-to-incident-report flow, and pricing for 5–60-staff settings.
  - **Why incumbents would not struggle:** they own the hardware and alarm centres and can add a form. Differentiation is weak unless it comes from deep workflow integration, which is really a NÆRVÆRK feature.
- **First version:** resell or partner with an existing provider, plus your implementation service (risk review, alarm plan, drills, incident template). Later, integrate the incident follow-up into NÆRVÆRK.
- **Route to first 10:** the same channels as A. Arbejdstilsynet orders are a sharp trigger. Sales cycle 1–3 months (private), 6–12 months (municipal).
  - **Likely objections:** "we have Ascom or CEKURA", "the contract runs to 2027", "staff do not want location tracking".
- **Price and unit economics:** for 12 devices at DKK 149 / 199 / 249 a month, a reseller share of 15–30% plus a DKK 5k–15k set-up fee at 60% margin gives **year-1 contribution per site of DKK 6.2k / 13.2k / 19.8k**. An own platform could reach 70–80% software margins but needs hardware, firmware, certification and 24/7 operations.
- **Capital:**
  - validate: DKK 5k–15k
  - reseller pilot: DKK 30k–80k (demo kits, insurance, training material)
  - own platform: DKK 3m–10m (assumption)
- **Time and workload:** first revenue in 1–3 months if a partner agrees. Ongoing support escalation, installation, and data-protection work (staff location data needs a data protection impact assessment (DPIA) and involvement of the staff cooperation committee).
- **Why it could fail:**
  1. Life-safety liability: a failure during an assault is catastrophic.
  2. 24/7 obligations clash with part-time capacity.
  3. It is a second GDPR-heavy system competing with NÆRVÆRK for the same consultants and attention.
  4. Reseller margins are thin.
  5. Incumbents copy the incident flow.
  6. Alarms aimed at residents fall under the Social Services Act and are legally sensitive (the Ombudsman criticised door alarms in a residential unit).

### C. Coordinated estate clearance and senior moves (Alternative 2)

- **Problem:** when a parent moves into a care home (*plejebolig*) or dies, relatives, often living far away, must empty a home fast.
  - Care homes want units cleared "within a few days".
  - The notice period is usually 3 months, or 1 month on a death with no co-resident, and the estate pays rent until the unit is re-let (fact).
  - There were about 58,000 deaths in 2025 and about 42,000 care-home places (fact). Estimated 14,000–21,000 moves into care homes a year (assumption).
- **Segment and budget holder:** adult children or heirs, paid from the estate or the senior's own money. Referrers: care-home staff, undertakers, estate lawyers.
- **Evidence of spend: Medium–Strong.** Published prices:
  - care-home unit clearance DKK 4k–7k ex VAT
  - house clearance DKK 75–99/m² plus DKK 27/m² cleaning
  - half-day crew DKK 3,600
  - senior-move assistant DKK 560–595/hour incl. VAT
  - gig-platform average ≈ DKK 2,050 for a care-home move (23 tasks)
- **Competitors:**
  - clearance firms: Hamers, Nordsjællands Borydning (dozens of town-specific web pages), Rydbo, Borydning Danmark, Borydderen (Trustpilot 4.7)
  - auction houses: Lauritz, Campen
  - gig platform: Handyhand
  - senior-move assistant: Lenore
- **Improvement:** one coordinator for relatives far away. Video walkthrough, photo inventory, sharing heirlooms among siblings, transparent pass-through of resale proceeds (clearance firms' margin often comes from buying the valuables), a fixed price with a deadline guarantee, and a documented handover to the care home. The coordinator layer is easy to copy.
- **First version:** you coordinate; 2–3 clearance and moving firms do the physical work.
- **Route to first 10:** care-home leaders, undertakers, Ældre Sagen local networks, Google Ads (expensive against firms running dozens of town pages). Sales cycle: days.
- **Unit economics:**
  - care-home unit job at DKK 6k / 7.5k / 9.5k, less a subcontractor (DKK 4.5k–5k) and coordinator wages (DKK 250/h): **contribution DKK 0 / 2.0k / 3.75k per job**
  - coordinated house job: DKK 1k / 4k / 9k
  - reaching DKK 500k contribution needs roughly 150–250 jobs a year
- **Capital:** validate DKK 10k–20k; pilot DKK 30k–80k; scale with employed coordinators DKK 150k–400k.
- **Time and workload:** first revenue within weeks, but jobs demand presence within days, which clashes with limited weekly time unless you hire coordinators early.
- **Why it could fail:** thin margins; buying ads against search-optimised incumbents; gig-platform prices set the anchor; disputes over valuables; no insider advantage; growth is local and tied to labour.

### D. Maintenance planning for housing co-operative boards

- **Problem:** volunteer boards of housing co-operatives (*andelsboligforeninger*) and owners' associations (*ejerforeninger*) own a maintenance plan that goes stale between updates every 3–5 years, lose knowledge when board members change, and struggle to document the building's condition to buyers and valuers.
- **Legal driver:** a statutory 15-year plan, updated every 5 years, applies only to housing co-operatives founded on or after 1 July 2018. For older co-operatives and owners' associations the duty comes indirectly, through bylaws.
- **Evidence:** Medium–Strong.
  - Plans cost DKK 8k–60k.
  - About 9,000–9,151 housing co-operatives with about 210,000 homes; ABF has about 5,450 member associations.
  - Administration fees average DKK 1,546 per share per year.
- **Competitors:**
  - Plan 1 (digital for about 10 years)
  - Min Boligforening
  - Ejendom.com (used by MMAKE)
  - Unyti
  - administrators such as DEAS, Newsec, OADV and Qvortrup
  - engineering firms
- **Improvement:** a plan kept current with AI intake of old PDFs, invoices and photos, contractor follow-up, and automatically filled key-information forms (*nøgleoplysninger*) and handover packs. Plan 1 or Ejendom.com can add this easily.
- **Unit economics:** DKK 1.5k–5k a year plus DKK 3k–8k set-up. Reaching DKK 500k of annual recurring revenue needs 100–333 associations.
- **Capital:** validate under DKK 25k; MVP DKK 25k–150k.
- **Why it lost:**
  - the category is crowded and has a digital leader
  - administrators control the channel
  - boards pay little and decide slowly
  - you have no network among housing boards
  - it is another software product competing with NÆRVÆRK for build and GDPR attention
- **Drone inspection** (DKK 3k–9.5k per job) fits only as a feature here.

### E. Holiday-home monitoring plus partner inspection visits

- **Problem:** owners who live far from their holiday home (*sommerhus*) find frost bursts, leaks, break-ins and mould late. More than 40% of holiday-home break-ins happen November–February (fact). About 224,000 families own one (fact).
- **Evidence:** Medium. Weekly inspection sells for DKK 695–1,150 a year (≈ DKK 20–40 per visit). Falck sells a national product (price unclear). Verisure Norway starts at NOK 549 a month.
- **Offer:** a sensor kit (leak, temperature, humidity, power) with a 4G hub, an app, and local partner call-outs.
- **Unit economics:** a DKK 1,495 kit plus DKK 99–149 a month gives a monthly contribution of DKK 44–114. Customer acquisition cost (CAC) is recovered in 0–16 months. DKK 500k a year of contribution needs 365–947 subscribers.
- **Capital:** validate DKK 15k–30k (10 pilot kits); pilot DKK 50k–150k; scale DKK 0.5m–2m.
- **Why it lost:** you have no founder edge; consumer acquisition is costly; willingness to pay for visits is low; Falck and alarm firms have strong brands; hardware support and winter call-outs peak together; it needs local route density.

---

## 6. Weighted comparison

**Weights.**
- **Demand evidence, 20%:** a real, paid-for problem matters most.
- **Ability to reach buyers, 15%:** you have limited time, so channel access decides speed.
- **Founder fit, 15%:** your advantage is the reason to do this at all.
- **10% each:** contribution margin, differentiation, execution feasibility (including founder time, 24/7 duties, regulation), capital exposure (5 = least capital at risk), growth potential.

Uncertainty is scored separately as a low–high range on the criteria where evidence is thinnest. `analysis/scoring.py` reproduces the tables.

| Candidate | Demand | Reach | Fit | Margin | Differentiation | Feasibility | Capital | Growth | **Weighted** | Range | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A Robust, calm rooms | 3 | 4 | 5 | 3 | 3 | 4 | 4 | 3 | **3.65** | 3.20–3.95 | low |
| B Staff alarms + incident follow-up | 4 | 4 | 5 | 3 | 2 | 2 | 3 | 3 | **3.45** | 3.25–3.75 | medium |
| C Estate clearance and senior moves | 4 | 3 | 3 | 3 | 2 | 2 | 5 | 2 | **3.10** | 2.85–3.25 | medium |
| D Board maintenance planning | 3 | 2 | 3 | 3 | 1.5 | 3 | 4 | 3 | **2.80** | 2.60–2.95 | medium |
| E Holiday-home monitoring | 3 | 2 | 2 | 2.5 | 3 | 3 | 3 | 3 | **2.65** | 2.40–2.90 | medium-low |

**Sensitivity:**

| Scenario | A | B | C | D | E | Winner |
|---|---|---|---|---|---|---|
| Base weights | 3.65 | 3.45 | 3.10 | 2.80 | 2.65 | A |
| Demand-heavy (demand 30%, fit 10%, feasibility 5%) | 3.50 | 3.50 | 3.25 | 2.80 | 2.70 | **Tie A/B** |
| Growth-heavy | 3.45 | 3.40 | 2.90 | 2.75 | 2.70 | A (narrow) |
| Capital ignored | 3.55 | 3.45 | 2.90 | 2.62 | 2.65 | A |
| Founder fit ignored | 3.40 | 3.25 | 3.15 | 2.75 | 2.72 | A |
| Equal weights | 3.62 | 3.25 | 3.00 | 2.81 | 2.69 | A |
| **Stress case: A's demand drops to 2, B's feasibility rises to 3** | 3.45 | **3.55** | — | — | — | **B** |

**Reading the tables:**
- A wins under every weighting tried, but only by 0.05–0.37 points, and ties B when demand evidence dominates.
- **A realistic change in the evidence flips the winner:** if interviews show little damage-driven spend, and a partner removes most of B's delivery burden, B leads.
- C, D and E never come close.
- The decision is therefore between A and B, and the validation plan tests both with the same buyers.

---

## 7. Why the lead fits you, and why the alternatives lost

**A fits you specifically** for four reasons:
- The sale is won in a walkthrough where your practice knowledge is the product.
- The buyers are the people you already know, and the NÆRVÆRK buyers.
- It needs no software build, no personal data and no on-call duty, so it runs alongside NÆRVÆRK without competing for GDPR consultants or engineering.
- It is the physical-product direction you asked to prioritise, done by improving and bundling existing products rather than inventing.

**B lost despite stronger demand evidence** because:
1. **Liability is asymmetric.** An alarm that fails during an assault (as at Aalborg in May 2026) is catastrophic for a part-time founder. A robust chair that wears out is not.
2. **The workload doesn't fit your hours.** 24/7 support and installation conflict with them.
3. **It overlaps NÆRVÆRK's bottleneck.** Staff location and incident data would put a second GDPR-heavy system on the same consultants.
4. **A reseller adds little that incumbents can't copy.** They own the hardware and alarm centres. Its best idea, the alarm-to-report flow, belongs inside NÆRVÆRK as an integration.

**Revisit B** if validation shows alarm pain clearly outranks furniture pain and a provider will carry the 24/7 and certification burden.

**C lost** on:
- margins of DKK 0–3.75k per care-home job
- deadline-driven fieldwork that your time cannot support
- no insider edge
- growth that is local and tied to labour

C would suit a founder with free daytime hours and a care-home referral network.

---

## 8. Stress test of the lead

**The strongest evidence against A:**
- **No observed spend in the target segment.** The only proven spend is regional psychiatry, which frameworks lock to Arkisafe and Daarbak.
- **Arkisafe already distributes furniture for "challenged environments".** It could serve, or may already serve, private units.
- **The low-case economics lose money:** DKK 30k orders at a 25% discount give a 10% contribution.
- **Purchases are infrequent.**
- **You have no demonstrated sales record** outside your own organisation.

**The three most dangerous assumptions:**
1. **Willingness to pay:** private and self-governing settings spend at least DKK 10k–15k a year on replacement driven by damage or safety, and will pay a premium for a robust package (first order ≥ DKK 25k).
2. **Supply:** at least one credible maker offers a distributor discount of 30% or more (at least 25% as the floor), orders as small as a single room, lead times of 8 weeks or less, and test documentation.
3. **Channel and time:** at least 30% of warm contacts take a meeting and at least 20% of meetings lead to a paid step, with you working about 10 hours a week.

**What would reverse the recommendation:**
- fewer than 4 of 10 interviewed settings report meaningful spend
- no paid walkthrough or signed letter of intent after 12 or more conversations
- no maker offers a discount of 25% or more
- evidence that incumbents already sell comparable packages to small private units at similar prices
- alarm pain clearly stronger (5 or more of 10 report a recent alarm failure or a contract ending within 12 months, and at least 2 accept a paid alarm review): switch to B through a partner
- your employment terms prevent selling to peers

---

## 9. Desk research versus validated business

This is a ranking built from public information: search extracts that could not be opened in full, plus stated assumptions. **No customer has paid or promised anything, and no supplier has confirmed terms.** Treat A as the best hypothesis, not a proven business.

**The next experiment (`validation-plan.md`):**
- 12–15 interviews with leaders of private and self-governing specialist settings
- 4–6 supplier term requests
- a paid walkthrough offer

**It decides, within 14 days:** continue with A, switch to B through a partner, or stop both and move to C. Its cost: DKK 5k–20k and about 25 founder hours.

---

## 10. Questions whose answers would change the plan

1. How many hours a week, and which daytime slots, can you give from October to December 2026? Does your employment contract restrict side businesses or selling to other providers?
2. How much cash will you put at risk before the first paid order: up to DKK 25k, up to DKK 170k, or more?
3. Roughly how many leaders of other private or self-governing specialist settings could you call personally this week?
