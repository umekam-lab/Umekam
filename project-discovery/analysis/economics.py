"""Unit economics and capital sketches for the five shortlisted candidates.

Every input is an ASSUMPTION unless marked otherwise in evidence.md. All DKK, ex VAT.
Run: python3 economics.py
"""


def band(label, low, mid, high, unit="DKK"):
    print(f"  {label:<58} {low:>10,.0f} {mid:>10,.0f} {high:>10,.0f}  {unit}")


def header(title):
    print(f"\n### {title}\n  {'':<58} {'low':>10} {'mid':>10} {'high':>10}")


# ---------------------------------------------------------------- A
header("A. Robust environments: contribution per order (distributor model)")
order = (30_000, 45_000, 80_000)                  # first order value (assumption)
supplier_discount = (0.25, 0.32, 0.38)           # distributor discount off list (assumption)
freight = (0.07, 0.05, 0.03)                     # share of order (assumption)
install_hours, install_rate = (4, 3, 2), 450     # freelance carpenter (assumption)
reserve = 0.02                                   # warranty/returns/payment reserve (assumption)
contrib = []
for o, d, f, h in zip(order, supplier_discount, freight, install_hours):
    c = o * d - o * f - h * install_rate - o * reserve
    contrib.append(c)
band("Order value", *order)
band("Contribution before founder time", *contrib)
band("Contribution margin", *(c / o * 100 for c, o in zip(contrib, order)), unit="%")
founder_hours = (15, 12, 10)
band("Contribution per founder hour", *(c / h for c, h in zip(contrib, founder_hours)), unit="DKK/h")
fixed = (80_000, 60_000, 45_000)  # insurance, accounting, web, demo depreciation, travel (assumption)
band("Annual fixed costs", *fixed)
band("Orders to break even on fixed costs", *(f / c for f, c in zip(fixed, contrib)), unit="orders")
# Year 1: 10 first orders + repeat orders from 40% of customers at 15k
y1_rev = [10 * o + 10 * 0.4 * 15_000 for o in order]
y1_con = [10 * c + 10 * 0.4 * 15_000 * (c / o) for c, o in zip(contrib, order)]
band("Year-1 revenue (10 customers, 40% reorder 15k)", *y1_rev)
band("Year-1 contribution", *y1_con)
band("Year-1 contribution after fixed costs", *(c - f for c, f in zip(y1_con, fixed)))

header("A. Own-brand variant (scale stage): contribution per 45k order")
for label, gm in (("gross margin 45%", .45), ("gross margin 55%", .55)):
    print(f"  {label}: contribution ≈ {45_000 * (gm - .05 - .02):,.0f} DKK "
          f"(after 5% freight, 2% reserve)")

# ---------------------------------------------------------------- B
header("B. Staff alarms: per-site economics (12 devices)")
devices = 12
price = (149, 199, 249)          # observed public price points, DKK/device/month (CEKURA, Alarmselskabet)
reseller_share = (0.15, 0.25, 0.30)  # assumption
setup_fee = (5_000, 10_000, 15_000)  # implementation/training (assumption), 60% margin
band("Monthly subscription per site", *(devices * p for p in price))
band("Reseller margin per site per year", *(devices * p * 12 * s for p, s in zip(price, reseller_share)))
band("Setup-service contribution (60%)", *(s * .6 for s in setup_fee))
band("Year-1 contribution per site (reseller)",
     *(devices * p * 12 * s + f * .6 for p, s, f in zip(price, reseller_share, setup_fee)))

# ---------------------------------------------------------------- C
header("C. Estate clearance: coordinator-led jobs")
# plejebolig clearance: observed 4,000-7,000 ex VAT (Nordsjællands Borydning); half-day crew 3,600 ex VAT
price_c = (6_000, 7_500, 9_500)
sub = (4_500, 4_500, 5_000)
coord_hours, coord_wage = (6, 4, 3), 250
band("Plejebolig job price", *price_c)
band("Contribution after subcontractor + coordinator wage",
     *(p - s - h * coord_wage for p, s, h in zip(price_c, sub, coord_hours)))
price_h = (15_000, 20_000, 28_000)                # house clearance incl. coordination (assumption)
sub_h = (11_000, 13_000, 16_000)
band("House job contribution (12 h coordinator)", *(p - s - 12 * coord_wage for p, s in zip(price_h, sub_h)))

# ---------------------------------------------------------------- D
header("D. Board 'living plan': per-association economics")
arr = (1_500, 3_000, 5_000)
setup = (3_000, 5_000, 8_000)
band("Annual subscription", *arr)
band("Year-1 revenue incl. setup", *(a + s for a, s in zip(arr, setup)))
band("Associations needed for 500k DKK ARR", *(500_000 / a for a in arr), unit="assoc.")

# ---------------------------------------------------------------- E
header("E. Holiday-home monitoring: per-subscriber economics")
fee = (99, 129, 149)                   # DKK/month (assumption)
cost = (55, 45, 35)                    # SIM + platform + support DKK/month (assumption)
kit_price, kit_cost = 1_495, (1_200, 950, 700)
cac = (1_000, 700, 400)
band("Monthly contribution", *(f - c for f, c in zip(fee, cost)))
band("Kit margin (one-off)", *(kit_price - k for k in kit_cost))
band("Months to recover CAC", *(max(c - (kit_price - k), 0) / (f - co)
                                for c, k, f, co in zip(cac, kit_cost, fee, cost)), unit="months")
band("Subscribers for 500k DKK annual contribution",
     *(500_000 / ((f - c) * 12) for f, c in zip(fee, cost)), unit="subs")
