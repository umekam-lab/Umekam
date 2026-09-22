# Progress log: project discovery for Rune á Kamarinum

Last updated: 22 September 2026.

## Status in one line

Desk research is complete and a lead project has been recommended: **robust, calm rooms for specialist settings**, with staff safety alarms and estate clearance as the two alternatives. It is **not yet validated**. Next comes the 14-day validation in `validation-plan.md`, which only you can run.

## Materials inspected

- `Claude_Code_Project_Discovery_Rune.txt`: the brief, uploaded to this session.
- Repository `umekam-lab/Umekam`: it was empty, with no commits, files, NÆRVÆRK materials, prior research or workspace instructions. No ChatGPT history or other accounts were available.

## Completed work

1. **Workspace and brief reviewed.** Working assumptions recorded:
   - 8–15 hours a week
   - capital unspecified, so options are staged
   - drones unconfirmed
   - PADI is recreational only
   - no confidential information in any search
2. **Broad scan of 20 problem/opportunity pairs** in six parallel streams covering:
   - specialist-setting products
   - safety and prevention
   - property and drones
   - marine and holiday homes
   - mobility and trades
   - everyday services

   Raw notes: `research_notes/Rune venture discovery Denmark/r1`–`r6`.
3. **Shortlist of five, analysed in depth:**
   - A: robust, calm rooms
   - B: staff alarms
   - C: estate clearance
   - D: board maintenance planning
   - E: holiday-home monitoring
4. **Weighted comparison with uncertainty ranges and six sensitivity scenarios**, in `analysis/scoring.py`. A leads under every weighting, ties B when demand evidence dominates, and loses to B if its own demand evidence fails.
5. **Unit economics and capital by stage for all five**, in `analysis/economics.py`.
6. **Deliverables written:**
   - `decision-report.md`: recommendation, founder fit, all 20 pairs, the five in depth, comparison, stress test, questions
   - `evidence.md`: claims register with sources and verification status, calculations, gaps
   - `validation-plan.md`: offer, 14-day plan, interview guide, outreach, supplier enquiry, paid pilot proposal, demonstration, criteria, 30/60/90 plan, first three actions

## Limitations to keep in mind

- **Every cited fact comes from a search-engine extract. No source page was opened.** The session's 200-search cap ran out during the scan, and the network policy blocked all direct page fetches (retsinformation.dk, dst.dk, at.dk, ski.dk, supplier sites, Wikipedia and others).
- The planned deep-dive fetches could not run. These include supplier price lists, target-list counts from Tilbudsportalen, and Arkisafe's and HealSafe's terms. They are now tasks in the validation plan.
- Exchange rates other than the EUR peg are assumptions.
- Legal and standards points marked "B" (background knowledge) in `evidence.md` have not been verified.

## Open questions for you (answers would change the plan)

1. How many hours a week, and which daytime slots, can you give from October to December 2026? Does your employment contract restrict side businesses or selling to other providers in the sector?
2. How much cash will you put at risk before the first paid order: up to DKK 25k, up to DKK 170k, or more?
3. Roughly how many leaders of other private or self-governing specialist settings could you call personally this week?

## Verification backlog, in priority order

1. Supplier price lists and distributor terms (HealSafe, Affari, Pineapple, Broda, Norix), and Arkisafe's position in the social sector.
2. Count of target settings (Tilbudsportalen, danskeskoler.dk).
3. Whether private and self-governing providers are bound by municipal or SKI agreements (legal check).
4. Spend per setting on damage-driven replacement (interviews only).
5. Re-open every ★ claim in `evidence.md`.
6. Product standards and liability for robust and anti-ligature furniture. Check the Danish transposition of the EU Product Liability Directive (2024/2853).
7. Membership and events of LOS and Selveje Danmark; the social inspectorate's text on physical surroundings; whether Arbejdstilsynet's smiley register can be searched for enforcement orders.

## Precise next step

**Tomorrow, you:** follow section 11 of `validation-plan.md`.
1. Check your contract, then build the list of 60 settings, marking the warm ones.
2. Send the supplier enquiry to four makers.
3. Contact your 10 warmest leaders and book five interviews for days 3–5.

**On day 14:** fill in the section 8 scorecard, then continue, revise or stop.

**If you resume this work with Claude:** bring the day-14 interview and supplier logs (no personal data about residents or pupils). The next session should re-score A and B with the real numbers, update `analysis/economics.py` with actual supplier terms, and, if the result is continue, draft the distributor agreement checklist and the first package price sheets.
