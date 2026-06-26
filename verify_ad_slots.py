from pathlib import Path
files = [
    'dog-blog/health/dog-emergency-symptoms.html',
    'dog-blog/health/dog-first-aid-basics.html',
    'dog-blog/health/dog-choking-emergency.html',
    'dog-blog/health/dog-bloat-emergency-signs.html',
    'dog-blog/health/dog-poisoning-emergency-response.html',
    'dog-blog/health/dog-heatstroke-emergency.html',
    'dog-blog/health/dog-trauma-first-aid.html',
    'dog-blog/health/dog-burn-injury-first-aid.html',
    'dog-blog/health/dog-allergic-reaction-emergency.html',
    'dog-blog/health/dog-seizure-first-aid.html',
]
for f in files:
    p = Path(f)
    if not p.exists():
        print(f + ': MISSING')
        continue
    text = p.read_text(encoding='utf-8')
    print(f + ': ' + str(text.count('data-ad-slot=')))
