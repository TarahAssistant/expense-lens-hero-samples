#!/usr/bin/env python3
"""Assemble a.html .. d.html from src/ partials. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
STORE = "https://apps.apple.com/us/app/expense-lens-scan-track/id6789503509"

def read(name): return (SRC / name).read_text()

BADGE = f'<a href="{STORE}" class="store-badge inline-block w-full sm:w-auto shrink-0"><img src="assets/app-store-badge.svg" alt="Download on the App Store" width="168" height="52"></a>'
QR = f'<a href="{STORE}" aria-label="Open Expense Lens on the App Store"><img src="assets/app-store-qr.svg" alt="QR code linking to the App Store listing"></a>'

def h1(align):
    t = read("_h1.html")
    return t.replace("{{ALIGN}}", "items-center" if align == "center" else "items-start") \
            .replace("{{JUSTIFY}}", "justify-center" if align == "center" else "justify-start")

FEATURES = [
    ("lucide:languages", "Multi-Language AI", "Receipts in French? German? Japanese? Azerbaijani? Our AI reads receipts in dozens of languages and extracts everything in English, no manual translation needed."),
    ("lucide:mail", "Email-In Receipts", "Every account gets a unique email address. Forward any receipt or invoice and it's automatically scanned, extracted, and categorized. No app needed."),
    ("lucide:sparkles", "Smart Categories", "The AI learns your habits. It remembers your patterns and gets better at categorizing the more you use it."),
    ("lucide:download", "PDF &amp; CSV Export", "Generate expense reports as clean PDFs or detailed CSVs. Compatible with QuickBooks and Xero via standard headers. Download and share with your accountant."),
    ("lucide:car", "Mileage Tracker", "Track business trips by GPS or manual address entry. Set tiered reimbursement rates in km or miles. All trips logged alongside your expenses for clean tax reporting."),
    ("lucide:message-circle", "Lens AI Assistant", "Ask questions about your spending in plain language. Lens knows your data: category breakdowns, monthly comparisons, budget status, and answers without the dashboard clicks."),
    ("lucide:bar-chart-2", "Analytics &amp; Insights", "Spending trends, monthly comparisons, category breakdowns, top merchants, and budget vs actual, all in one visual dashboard. See exactly where your money goes."),
    ("lucide:folder", "Projects", "Separate expenses by client, project, or trip. Each project gets its own currency, budget, and report. Perfect for freelancers juggling multiple clients."),
]
def feature(icon, title, body):
    return f'''          <div class="dark:bg-[#0A0A0A] border border-subtle p-8 flex flex-col gap-4 group hover:border-[#14B8A6]/50 transition-colors shadow-sm bg-white">
            <div class="w-10 h-10 bg-[#F5F5F5] dark:bg-[#1A1A1A] rounded-full flex items-center justify-center text-[#14B8A6] group-hover:scale-110 transition-transform"><iconify-icon icon="{icon}" class="text-xl"></iconify-icon></div>
            <div><h3 class="text-lg font-sans-display text-[#171717] dark:text-[#EDEDED] mb-2 font-medium">{title}</h3><p class="text-xs text-[#595959] dark:text-[#A1A1AA] font-sans-body leading-relaxed">{body}</p></div>
          </div>'''

PLANS = [
    ("Free Trial", None, None, "5 scans to try it out", ["5 AI receipt scans", "AI-powered extraction", "Basic expense tracking", "1 project"], "Start Free", False),
    ("Starter", "4.99", "49", "For individuals getting started", ["30 receipt scans/month", "AI-powered extraction", "158 currencies", "1 project", "CSV export"], "Get Started", False),
    ("Value", "9.99", "99", "For freelancers and expats", ["75 receipt scans/month", "Everything in Starter", "3 projects", "Reports &amp; analytics", "Email receipt forwarding", "Priority support"], "Get Started", True),
    ("Pro", "19.99", "199", "For power users and small teams", ["200 receipt scans/month", "Everything in Value", "Unlimited projects", "Smart category learning", "Recurring expense detection", "Weekly spending digest"], "Get Started", False),
]
def plan(name, monthly, annual, blurb, items, cta, popular):
    li = "".join(f'<li class="flex items-start gap-2 text-sm font-sans-body"><iconify-icon icon="lucide:check" class="text-[#14B8A6] mt-0.5" style="flex-shrink:0;"></iconify-icon>{i}</li>' for i in items)
    price = '<span class="text-4xl font-sans-display font-bold text-[#171717] dark:text-[#EDEDED]">$0</span>' if monthly is None else \
        f'<span class="text-4xl font-sans-display font-bold text-[#171717] dark:text-[#EDEDED]"><span class="price-symbol">$</span><span data-monthly="{monthly}" data-annual="{annual}">{monthly}</span></span><span class="text-sm font-sans-body text-[#595959] dark:text-[#A1A1AA]" data-period>/mo</span>'
    box = 'border rounded-lg p-6 flex flex-col bg-[#FFFFFF] dark:bg-[#0A0A0A] relative animate-on-scroll" style="border-color:#14B8A6;box-shadow:0 0 0 1px #14B8A6,0 8px 32px rgba(20,184,166,0.15);' if popular else 'border border-subtle rounded-lg p-6 flex flex-col bg-[#FFFFFF] dark:bg-[#0A0A0A] animate-on-scroll'
    tag = '<div class="absolute left-1/2" style="top:-12px;transform:translateX(-50%);"><span class="text-[10px] uppercase tracking-widest font-sans-body font-bold px-3 py-1 rounded-full bg-[#14B8A6] text-white">Most Popular</span></div>' if popular else ''
    title_c = 'text-[#14B8A6]' if popular else 'text-[#595959] dark:text-[#A1A1AA]'
    btn = 'bg-[#14B8A6] text-white hover:bg-[#0D9488]' if popular else 'border border-subtle text-[#171717] dark:text-[#EDEDED] hover:border-[#14B8A6] hover:text-[#14B8A6]'
    return f'''          <div class="{box}">{tag}
            <div class="mb-6"><h3 class="text-sm uppercase tracking-widest font-sans-body font-semibold mb-3 {title_c}">{name}</h3><div class="flex items-end gap-1">{price}</div><p class="text-xs font-sans-body mt-2 text-[#595959] dark:text-[#A1A1AA]">{blurb}</p></div>
            <ul style="flex-grow:1;" class="space-y-3 mb-8 text-[#171717] dark:text-[#EDEDED]">{li}</ul>
            <a href="https://app.expense-lens.com/signup" class="block w-full text-center py-2.5 px-4 rounded text-xs uppercase tracking-widest font-sans-body font-semibold {btn} transition-colors">{cta}</a>
          </div>'''

FAQS = [
    ("How accurate is the AI extraction?", "Expense Lens uses a multi-model AI system including Google Gemini for extraction. Accuracy depends on receipt quality: clear photos give the best results. The AI handles most formats, languages, and receipt conditions. It also learns your patterns over time, so categories get smarter the more you use it."),
    ("Which currencies are supported?", "158 currencies. The AI automatically detects the currency on the receipt and converts it to your home currency using the exchange rate from the date of the purchase, via Open Exchange Rates."),
    ("Can I export my expense data?", "Yes. Expense Lens generates PDF reports (including a tax-ready report with multi-currency breakdowns) and CSV exports with headers compatible with QuickBooks and Xero. Download and import, no API connection needed."),
    ("Do I need to connect my bank account?", "No. Expense Lens works by scanning receipts, not by accessing your bank data. Your financial accounts stay completely private."),
]
def faq(q, a):
    return f'''          <div class="faq-item dark:bg-[#0A0A0A] border border-subtle bg-white">
            <button class="w-full flex items-center justify-between p-6 text-left group focus:outline-none" onclick="toggleFaq(this)"><span class="text-base font-sans-display text-[#171717] dark:text-[#EDEDED]">{q}</span><span class="text-[#595959] dark:text-[#A1A1AA] text-xl font-light transition-transform duration-300 icon-plus">+</span></button>
            <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-out faq-content"><div class="overflow-hidden"><p class="px-6 pb-6 text-xs text-[#595959] dark:text-[#A1A1AA] font-sans-body leading-relaxed">{a}</p></div></div>
          </div>'''

VARIANTS = {
    "a": "Keep the hero, add the install row",
    "b": "Split hero with the phone",
    "c": "QR code in the lens",
    "d": "Compact headline plus install panel",
}

sections = read("sections.html") \
    .replace("{{FEATURES}}", "\n".join(feature(*f) for f in FEATURES)) \
    .replace("{{PRICING}}", "\n".join(plan(*p) for p in PLANS)) \
    .replace("{{FAQ}}", "\n".join(faq(*f) for f in FAQS)) \
    .replace("{{BADGE}}", BADGE)

for letter, title in VARIANTS.items():
    head = read("head.html").replace("{{LETTER}}", letter.upper()).replace("{{TITLE}}", title)
    for v in VARIANTS:
        head = head.replace("{{ON_%s}}" % v.upper(), 'class="on"' if v == letter else "")
    hero = read(f"hero-{letter}.html") \
        .replace("{{LENS}}", read("_lens.html")) \
        .replace("{{STATS}}", read("_stats.html")) \
        .replace("{{H1_CENTER}}", h1("center")).replace("{{H1_LEFT}}", h1("left")) \
        .replace("{{BADGE}}", BADGE).replace("{{QR}}", QR).replace("{{STORE}}", STORE)
    (ROOT / f"{letter}.html").write_text(head + read("nav.html") + hero + sections)
    print("wrote", f"{letter}.html")
