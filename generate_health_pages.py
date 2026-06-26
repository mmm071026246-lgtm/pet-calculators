import json
import pathlib

pages = [
    {
        'filename': 'dog-infectious-disease-symptoms.html',
        'title': 'Dog Infectious Disease Symptoms',
        'description': 'Recognize the key symptoms of infectious diseases in dogs, including fever, respiratory signs, and digestive changes.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-infectious-disease-symptoms.jpg',
        'sections': [
            ('Understanding infectious disease symptoms', 'Infectious diseases can affect multiple systems in the body. This section explains how infections may present and when to seek veterinary care.', [
                'Fever, low energy, and lack of appetite',
                'Persistent coughing or nasal discharge',
                'Diarrhea, vomiting, or abdominal pain',
                'Sudden weakness or collapse',
                'Skin lesions, swelling, or discharge'
            ]),
            ('Respiratory infection signs', 'Respiratory infections often start with mild symptoms and can progress quickly in dogs.', [
                'Coughing, sneezing, and throat irritation',
                'Nasal discharge that becomes thick or bloody',
                'Labored breathing or open-mouth breathing at rest',
                'Loss of appetite with breathing difficulty',
                'Watery or red eyes'
            ]),
            ('Gastrointestinal infection signs', 'Digestive infections can cause rapid fluid loss and discomfort.', [
                'Vomiting that persists or contains blood',
                'Loose stool, diarrhea, or mucus in the stool',
                'Abdominal tenderness or bloating',
                'Reluctance to eat or drink',
                'Signs of dehydration such as dry gums'
            ]),
            ('When to contact a veterinarian', 'If you see multiple infection signs or deterioration, prompt veterinary attention is critical.', [
                'High fever lasting more than a day',
                'Severe vomiting or diarrhea',
                'Difficulty breathing or blue gums',
                'Weakness, collapse, or unresponsiveness',
                'Signs of pain when touched'
            ])
        ]
    },
    {
        'filename': 'dog-skin-disease-symptoms.html',
        'title': 'Dog Skin Disease Symptoms',
        'description': 'Learn the signs of skin disease in dogs, from itching and redness to hair loss, sores, and infection.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-skin-disease-symptoms.jpg',
        'sections': [
            ('Early skin disease indicators', 'Skin problems often begin with subtle changes and progress if left untreated.', [
                'Intense itching or licking of the skin',
                'Red, inflamed patches or rashes',
                'Dry, flaky, or scaly skin',
                'Hair loss in localized or widespread areas',
                'Areas that appear darker or thicker than normal'
            ]),
            ('Common irritation and infection signs', 'Skin disease can lead to secondary infections that require veterinary treatment.', [
                'Pus, crusts, or discharge from affected skin',
                'Foul odor coming from the coat or skin folds',
                'Open sores or raw spots',
                'Swollen or painful skin areas',
                'Excessive rubbing against surfaces'
            ]),
            ('Signs from environmental or allergic causes', 'Environmental and food allergies often show as chronic skin symptoms.', [
                'Seasonal flares of itching and redness',
                'Recurring ear infections or head shaking',
                'Swollen lips, eyelids, or paw pads',
                'Repeated hot spots or inflamed skin folds',
                'Persistent chewing of the feet'
            ]),
            ('When to seek veterinary help', 'If skin symptoms worsen or persist despite grooming, get professional evaluation.', [
                'Rapid spread of irritation or hair loss',
                'Painful, bleeding, or infected lesions',
                'Signs of fever or general illness',
                'Skin that feels hot or has unusual texture',
                'Behavioral changes from discomfort'
            ])
        ]
    },
    {
        'filename': 'dog-arthritis-symptoms.html',
        'title': 'Dog Arthritis Symptoms',
        'description': 'Discover the signs of arthritis in dogs, including stiffness, limping, and changes in mobility.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-arthritis-symptoms.jpg',
        'sections': [
            ('Recognizing arthritis in dogs', 'Arthritis affects joint comfort and movement, especially in older or large-breed dogs.', [
                'Stiffness after resting or napping',
                'Reluctance to climb stairs or jump',
                'Slow, guarded movements',
                'Favoring one leg or shifting weight',
                'Limping that comes and goes'
            ]),
            ('Behavioral signs of joint pain', 'Joint pain can change how a dog behaves even before obvious limping appears.', [
                'Irritability when touched on the back or hips',
                'Less interest in play or walks',
                'Restlessness at night',
                'Difficulty settling into a comfortable position',
                'Avoiding hard surfaces or cold floors'
            ]),
            ('Visible changes in gait', 'Arthritis often changes a dog’s typical walking style.', [
                'Short, choppy strides',
                'Dragging paws or toe scuffing',
                'Uneven muscle tone in legs',
                'Slower turns and movements',
                'Hesitation before standing up'
            ]),
            ('How vets diagnose arthritis', 'A veterinarian evaluates movement and may use imaging to confirm arthritis.', [
                'Joint swelling or tenderness on exam',
                'Reduced range of motion in one or more joints',
                'Pain response when flexing the limb',
                'Changes in posture or stance',
                'History of previous injury or age-related wear'
            ])
        ]
    },
    {
        'filename': 'dog-digestive-disease-symptoms.html',
        'title': 'Dog Digestive Disease Symptoms',
        'description': 'Understand the symptoms of digestive disease in dogs, including vomiting, diarrhea, pain, and appetite changes.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-digestive-disease-symptoms.jpg',
        'sections': [
            ('Symptoms of digestive stress', 'Digestive disease can present as subtle or dramatic changes in eating and bathroom habits.', [
                'Vomiting or retching',
                'Diarrhea or loose stool',
                'Loss of appetite',
                'Increased gas or bloating',
                'Abdominal discomfort'
            ]),
            ('Signs of serious digestive trouble', 'Certain symptoms suggest more urgent gastrointestinal problems.', [
                'Blood in vomit or stool',
                'Repeated vomiting over hours',
                'Failure to keep water down',
                'Distended or painful abdomen',
                'Weakness or collapse from dehydration'
            ]),
            ('Chronic digestive disease clues', 'Chronic conditions often show recurring or long-term digestive issues.', [
                'Frequent bouts of upset stomach',
                'Weight loss despite a normal diet',
                'Changes in stool consistency over time',
                'Excessive hunger with poor condition',
                'Recurrent nausea or soft stool'
            ]),
            ('When to get veterinary support', 'If digestive symptoms persist, a veterinarian can identify the cause and treat it safely.', [
                'Long-term weight changes',
                'Persistent digestive upset despite diet change',
                'Lethargy and dehydration',
                'Straining or discomfort when defecating',
                'Unexplained behavioral changes'
            ])
        ]
    },
    {
        'filename': 'dog-respiratory-infection-symptoms.html',
        'title': 'Dog Respiratory Infection Symptoms',
        'description': 'Know the symptoms of respiratory infection in dogs, from coughing and discharge to breathing difficulty and fever.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-respiratory-infection-symptoms.jpg',
        'sections': [
            ('Common respiratory symptoms', 'Respiratory infection often starts with mild irritation and can worsen quickly.', [
                'Dry or wet cough',
                'Sneezing and nasal discharge',
                'Wheezing or crackling sounds',
                'Rapid or labored breathing',
                'Decreased appetite or energy'
            ]),
            ('Nasal and throat signs', 'Signs in the nose and throat can show whether the upper airway is involved.', [
                'Clear or colored nasal discharge',
                'Nasal congestion or sneezing',
                'Throat clearing or gagging',
                'Red or watery eyes',
                'Loss of smell or interest in food'
            ]),
            ('When breathing becomes urgent', 'Severe respiratory symptoms demand immediate action.', [
                'Open-mouth breathing at rest',
                'Blue or pale gums',
                'Inability to lie down comfortably',
                'Extended neck and head posture',
                'Fainting or collapsing'
            ]),
            ('How vets evaluate respiratory disease', 'A veterinarian can determine the cause and prescribe treatments for breathing issues.', [
                'Auscultation of lung sounds',
                'Chest imaging when needed',
                'Temperature and oxygen assessment',
                'Swab or culture for pathogens',
                'Monitoring response to therapy'
            ])
        ]
    },
    {
        'filename': 'dog-vomiting-diarrhea-symptoms.html',
        'title': 'Dog Vomiting and Diarrhea Symptoms',
        'description': 'Identify the most important vomiting and diarrhea symptoms in dogs, and know when veterinary care is needed.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-vomiting-diarrhea-symptoms.jpg',
        'sections': [
            ('What causes vomiting and diarrhea', 'Many conditions can cause digestive upset, from diet issues to infections and toxins.', [
                'Dietary indiscretion or new food',
                'Parasites or bacterial infection',
                'Toxin or foreign object ingestion',
                'Inflammatory bowel disease',
                'Stress or sudden environment changes'
            ]),
            ('Warning signs of severe problems', 'Some vomiting and diarrhea symptoms indicate a medical emergency.', [
                'Blood in vomit or stool',
                'Repeated episodes causing weakness',
                'Collapse or severe lethargy',
                'Persistent vomiting lasting more than 24 hours',
                'Signs of dehydration'
            ]),
            ('How to support your dog at home', 'Mild cases can be supported with rest, fluids, and careful diet management.', [
                'Offer small, frequent water sips',
                'Switch to a bland diet when tolerated',
                'Avoid treats and fatty foods',
                'Monitor stool and vomiting closely',
                'Keep the dog comfortable and quiet'
            ]),
            ('When to call the veterinarian', 'Consult your vet if symptoms do not improve or worsen quickly.', [
                'No improvement after 12-24 hours',
                'Weight loss or continued poor appetite',
                'Problem behavior or discomfort',
                'Blood in vomit or stool',
                'Dehydration symptoms'
            ])
        ]
    },
    {
        'filename': 'dog-urinary-tract-infection-symptoms.html',
        'title': 'Dog Urinary Tract Infection Symptoms',
        'description': 'Spot urinary tract infection symptoms in dogs, including frequent urination, straining, and blood in the urine.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-urinary-tract-infection-symptoms.jpg',
        'sections': [
            ('Key UTI symptoms', 'UTIs often begin with subtle changes in bathroom habits and can become painful quickly.', [
                'Frequent urination with small amounts',
                'Straining or discomfort when urinating',
                'Blood or cloudiness in the urine',
                'Accidents indoors despite housetraining',
                'Increased licking of the urinary area'
            ]),
            ('Pain and behavior changes', 'Urinary discomfort can affect your dog’s mood and activity.', [
                'Whining or restlessness',
                'Reluctance to go outside',
                'Decreased appetite',
                'Lethargy or low energy',
                'Changes in posture while eliminating'
            ]),
            ('When infection spreads', 'A urinary infection can affect the kidneys if left untreated.', [
                'Fever or elevated temperature',
                'Back or flank pain',
                'Vomiting or nausea',
                'General weakness',
                'Stronger odor in urine'
            ]),
            ('Testing and treatment', 'Veterinarians use urine testing and antibiotics to treat UTIs safely.', [
                'Urinalysis to identify bacteria',
                'Antibiotics selected for the infection',
                'Follow-up testing after treatment',
                'Fluid support if dehydrated',
                'Diet changes for recurrent infections'
            ])
        ]
    },
    {
        'filename': 'dog-ear-infection-symptoms.html',
        'title': 'Dog Ear Infection Symptoms',
        'description': 'Recognize dog ear infection symptoms, such as scratching, discharge, odor, and head shaking.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-ear-infection-symptoms.jpg',
        'sections': [
            ('Common ear infection signs', 'Ear infections typically cause discomfort and visible changes in the ear canal.', [
                'Frequent head shaking',
                'Pawing at or rubbing the ears',
                'Red or swollen ear flaps',
                'Sticky or foul-smelling discharge',
                'Changes in ear color or texture'
            ]),
            ('Discharge and odor explained', 'Discharge and odor often indicate an ongoing infection.', [
                'Yellowish or brown discharge',
                'Dark, waxy buildup in the ear',
                'Wet or greasy residue around the ear',
                'Strong, unpleasant smell',
                'Crusts or scabs near the ear opening'
            ]),
            ('Balance and behavior changes', 'Severe ear infections can affect balance and comfort.', [
                'Head tilt or circling',
                'Reluctance to be touched near the head',
                'Loss of appetite due to discomfort',
                'Irritability or restlessness',
                'Stumbling or unsteady walking'
            ]),
            ('What your vet will do', 'A veterinarian examines the ear and prescribes targeted treatment.', [
                'Visual exam of the ear canal',
                'Cleaning the ear before treatment',
                'Topical or oral medication',
                'Follow-up evaluation for chronic cases',
                'Advice on preventing recurrence'
            ])
        ]
    },
    {
        'filename': 'dog-eye-infection-symptoms.html',
        'title': 'Dog Eye Infection Symptoms',
        'description': 'Learn how to identify eye infection symptoms in dogs, including redness, discharge, squinting, and swelling.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-eye-infection-symptoms.jpg',
        'sections': [
            ('Eye infection warning signs', 'Eye infections can be painful and may threaten vision if untreated.', [
                'Red or bloodshot eyes',
                'Thick, colored discharge',
                'Squinting or holding the eye closed',
                'Swollen eyelids or third eyelid',
                'Increased tear production'
            ]),
            ('Discomfort and light sensitivity', 'Infected eyes often become sensitive and uncomfortable.', [
                'Blinking more than usual',
                'Avoiding bright light',
                'Rubbing the face with paws',
                'Head shaking or rubbing against furniture',
                'Behavioral changes due to pain'
            ]),
            ('When serious eye symptoms appear', 'Some symptoms indicate a more urgent ophthalmic issue.', [
                'Cloudy or hazy cornea',
                'Bleeding in the eye',
                'Vision loss or disorientation',
                'Bulging eyeball',
                'Severe swelling around the eye'
            ]),
            ('Veterinary diagnosis and treatment', 'A vet can determine the cause and protect your dog’s eye health.', [
                'Eye exam with careful observation',
                'Stain tests to assess corneal damage',
                'Prescription drops or ointments',
                'Anti-inflammatory medications when needed',
                'Advice on preventing recurrence'
            ])
        ]
    },
    {
        'filename': 'dog-allergy-symptoms.html',
        'title': 'Dog Allergy Symptoms',
        'description': 'Identify dog allergy symptoms such as itching, skin irritation, respiratory signs, and digestive upset.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-allergy-symptoms.jpg',
        'sections': [
            ('Common allergy symptoms', 'Allergies can affect a dog’s skin, breathing, and digestion in different ways.', [
                'Persistent scratching or licking',
                'Red, irritated skin',
                'Sneezing or nasal discharge',
                'Frequent ear infections',
                'Vomiting or diarrhea after meals'
            ]),
            ('Skin and coat signs', 'Skin symptoms are the most common manifestation of allergies.', [
                'Hot spots and raw areas',
                'Hair loss or thinning coat',
                'Bumps or rashes on the body',
                'Dry, flaky skin',
                'Discoloration from repeated licking'
            ]),
            ('Respiratory and eye symptoms', 'Allergies may also cause irritation in the airway and eyes.', [
                'Watery, itchy eyes',
                'Coughing or wheezing',
                'Sneezing or sniffling',
                'Nasal discharge or congestion',
                'Irritated ears or repeated ear problems'
            ]),
            ('How veterinarians manage allergies', 'A vet can identify triggers and create a treatment plan for long-term relief.', [
                'Allergy testing for food and environmental triggers',
                'Prescription diets or elimination feeding',
                'Medications for itching and inflammation',
                'Topical therapy for irritated skin',
                'Maintenance strategies to reduce flare-ups'
            ])
        ]
    }
]

base_style = '''body{font-family:Arial,sans-serif;max-width:920px;margin:0 auto;padding:24px;background:#ffffff;color:#1f2937;line-height:1.75;}
html{background:#f8fafc;}
a{color:#2563eb;text-decoration:none;}a:hover{text-decoration:underline;}
.breadcrumb{margin-bottom:24px;color:#6b7280;font-size:14px;}.breadcrumb a{color:#2563eb;}
h1{font-size:32px;margin-bottom:18px;}
h2{font-size:24px;margin-top:36px;margin-bottom:14px;}
h3{font-size:20px;margin-top:28px;margin-bottom:12px;}p{margin:16px 0;}ul{margin:16px 0 16px 24px;}li{margin:10px 0;}table{width:100%;border-collapse:collapse;margin:24px 0;}th,td{border:1px solid #d1d5db;padding:14px;vertical-align:top;}th{background:#eff6ff;}.notice{background:#eff6ff;border-left:4px solid #2563eb;padding:18px;margin:28px 0;border-radius:8px;}.ad-box{margin:34px 0;text-align:center;}.related-box{background:#f8fafc;padding:22px;border-radius:10px;margin-top:42px;}.related-box ul{margin:0;padding-left:20px;}.footer-note{color:#6b7280;font-size:14px;margin-top:42px;text-align:center;}
'''

related_links = [
    ('Dog Preventive Care Guide', 'dog-preventive-care-guide.html'),
    ('Annual Dog Wellness Exam', 'annual-dog-wellness-exam.html'),
    ('Dog Health Screening Guide', 'dog-health-screening-guide.html'),
    ('Dog Vaccine Side Effects', 'dog-vaccine-side-effects.html'),
    ('Dog First Aid Basics', 'dog-first-aid-basics.html')
]

common_sections = [
    {
        'heading': 'How symptoms commonly develop',
        'intro': 'Understanding how these symptoms typically progress helps you recognize when a dog is improving and when it may need urgent care.',
        'bullets': [
            'Symptoms can begin subtly and worsen over hours or days.',
            'Watch for changes in frequency, intensity, and overall behavior.',
            'Rapid progression often means a faster response is needed.',
            'Some conditions alternate between mild and more severe episodes.',
            'Improvement should be steady once treatment begins.'
        ]
    },
    {
        'heading': 'What your veterinarian will evaluate',
        'intro': 'Veterinarians use the symptom pattern, physical exam, and diagnostic tests to determine the underlying cause.',
        'bullets': [
            'A thorough history of when symptoms began and what changed.',
            'A physical exam focused on the affected organs or systems.',
            'Diagnostic tests like blood work, imaging, or cultures when needed.',
            'Assessment of hydration, pain, and overall wellness.',
            'A plan that balances treatment speed with long-term care.'
        ]
    },
    {
        'heading': 'Treatment approaches and what to expect',
        'intro': 'A successful recovery plan combines immediate care, follow-up treatment, and support at home.',
        'bullets': [
            'Initial treatment may focus on stabilizing the dog and reducing discomfort.',
            'Medication often includes antibiotics, anti-inflammatories, or supportive therapy.',
            'Some cases improve with diet change, rest, and careful monitoring.',
            'Your veterinarian may recommend follow-up visits or rechecks.',
            'Long-term management may include lifestyle adjustments or ongoing medication.'
        ]
    },
    {
        'heading': 'Prevention and long-term care',
        'intro': 'Preventing recurrence starts with understanding triggers and maintaining good daily care.',
        'bullets': [
            'Maintain a balanced diet and avoid sudden food changes.',
            'Keep up with preventive treatments that lower disease risk.',
            'Monitor your dog for early symptoms and act quickly.',
            'Reduce exposure to known irritants or infectious agents.',
            'Keep regular wellness exams on the schedule.'
        ]
    }
]

faq_template = [
    {
        'question': 'What should I do first when I notice these symptoms?',
        'answer': 'Start by observing your dog closely, remove any immediate hazards, and contact your veterinarian if symptoms are severe, persistent, or getting worse.'
    },
    {
        'question': 'Can some symptoms be treated at home?',
        'answer': 'Mild symptoms may improve with rest, fluid support, and diet changes, but it is important to consult your vet before trying home treatment.'
    },
    {
        'question': 'How can I prevent these symptoms from coming back?',
        'answer': 'Prevention depends on the condition, but common steps include good nutrition, regular checkups, stress reduction, and avoiding known triggers.'
    }
]

extra_sections = [
    {
        'heading': 'Age-specific warning signs',
        'intro': 'Puppies, adult dogs, and seniors may show symptoms differently. Pay attention to what is normal for your dog’s life stage.',
        'bullets': [
            'Puppies may decline quickly due to smaller reserves.',
            'Adult dogs may hide pain until the condition worsens.',
            'Senior dogs often show slower recovery from even mild episodes.',
            'Young dogs can be more susceptible to infectious disease.',
            'Older dogs may have chronic conditions that complicate symptoms.'
        ]
    },
    {
        'heading': 'What to track at home',
        'intro': 'Daily tracking gives your veterinarian useful information and helps you spot improvement or decline.',
        'bullets': [
            'Record how often symptoms occur and their intensity.',
            'Note any changes in appetite, energy, or thirst.',
            'Write down any triggers such as food, exercise, or environment.',
            'Track medication or treatment responses carefully.',
            'Share your notes with the veterinarian on the next visit.'
        ]
    },
    {
        'heading': 'Environmental and seasonal factors',
        'intro': 'Certain symptoms may be linked to seasonal allergies, temperature changes, or environmental exposures.',
        'bullets': [
            'Hot weather can make dehydration and heat-related symptoms worse.',
            'Seasonal pollen may cause sneezing and skin irritation.',
            'New plants or cleaning chemicals can trigger reactions.',
            'Lifestyle changes like travel may increase infection risk.',
            'Stress from moving or boarding affects symptom patterns.'
        ]
    },
    {
        'heading': 'How to comfort your dog during recovery',
        'intro': 'A calm, supportive environment helps your dog recover more quickly.',
        'bullets': [
            'Provide a quiet place to rest away from noise and activity.',
            'Offer small, frequent meals if your dog tolerates food.',
            'Keep a consistent routine to reduce anxiety.',
            'Stay close enough to monitor, but avoid overhandling.',
            'Use gentle encouragement rather than forcing movement or food.'
        ]
    },
    {
        'heading': 'Potential complications if symptoms continue',
        'intro': 'Left untreated, some conditions can lead to more serious health problems.',
        'bullets': [
            'Chronic inflammation can damage organs over time.',
            'Infection may spread from one system to another.',
            'Dehydration can affect kidney and heart function.',
            'Ongoing pain reduces quality of life and mobility.',
            'Delayed treatment may require longer, costlier care.'
        ]
    },
    {
        'heading': 'Questions to ask your veterinarian',
        'intro': 'Preparing questions helps you get clear direction and understand the best course of action.',
        'bullets': [
            'What is the likely cause of these symptoms?',
            'What tests do you recommend to diagnose the issue?',
            'How should I manage care at home while we wait?',
            'When should I bring the dog back for follow-up?',
            'Are there any changes I should make to diet or activity?'
        ]
    },
    {
        'heading': 'What not to do after symptoms begin',
        'intro': 'Avoid common mistakes that can make symptoms worse or delay proper diagnosis.',
        'bullets': [
            'Do not give any medication without veterinary approval.',
            'Avoid sudden diet changes unless directed by the vet.',
            'Do not let the dog drink large amounts of water all at once.',
            'Avoid applying human creams or treatments to the dog.',
            'Do not ignore subtle changes in behavior or appetite.'
        ]
    },
    {
        'heading': 'How to support recovery over several days',
        'intro': 'Recovery can take time, and consistent care makes a big difference.',
        'bullets': [
            'Offer gentle exercise as your dog starts to feel better.',
            'Keep meals light and easy to digest during recovery.',
            'Encourage rest and reduce activity until symptoms improve.',
            'Continue monitoring for new or returning signs.',
            'Follow the veterinarian’s care plan closely through recovery.'
        ]
    },
    {
        'heading': 'A safe aftercare checklist',
        'intro': 'Use a checklist after the initial treatment to track recovery and prevent relapse.',
        'bullets': [
            'Confirm all medications were administered correctly.',
            'Check that appetite and drinking habits are normalizing.',
            'Watch for improved energy and willingness to move.',
            'Note any new symptoms right away.',
            'Schedule follow-up visits as recommended by your vet.'
        ]
    },
    {
        'heading': 'When to call your veterinarian immediately',
        'intro': 'Some signs require immediate veterinary contact rather than delayed follow-up.',
        'bullets': [
            'Sudden collapse or fainting.',
            'Difficulty breathing or blue gums.',
            'Severe or bloody vomiting or diarrhea.',
            'Persistent shaking, trembling, or seizures.',
            'Signs of extreme pain or distress.'
        ]
    },
    {
        'heading': 'Why early care matters',
        'intro': 'Addressing symptoms early often leads to faster recovery and fewer complications.',
        'bullets': [
            'Early treatment can prevent the condition from worsening.',
            'It reduces the risk of secondary infections.',
            'It lowers the chance of long-term organ damage.',
            'Early care also reduces stress for your dog.',
            'Prompt veterinary attention can save time and cost in the long run.'
        ]
    },
    {
        'heading': 'How to use this guide with your veterinarian',
        'intro': 'Bring the most relevant observations from this guide to your vet visit to improve communication and care.',
        'bullets': [
            'Share the exact timing of when symptoms began.',
            'Explain any recent changes to diet or environment.',
            'Describe behavior changes and energy levels.',
            'Note any prior history of similar problems.',
            'Ask the vet to clarify the next steps and follow-up plan.'
        ]
    }
]

for page in pages:
    path = pathlib.Path('dog-blog/health') / page['filename']
    content = []
    content.append('<!DOCTYPE html>')
    content.append('<html lang="en">')
    content.append('<head>')
    content.append('<meta charset="UTF-8">')
    content.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    content.append(f'<title>{page["title"]} | Dog Health</title>')
    content.append(f'<meta name="description" content="{page["description"]}" />')
    content.append('<meta name="robots" content="index,follow,max-image-preview:large">')
    content.append(f'<link rel="canonical" href="https://mmm071026246-lgtm.github.io/dog-blog/health/{page["filename"]}">')
    content.append(f'<meta property="og:title" content="{page["title"]} | Dog Health">')
    content.append(f'<meta property="og:description" content="{page["description"]}">')
    content.append('<meta property="og:type" content="article">')
    content.append(f'<meta property="og:url" content="https://mmm071026246-lgtm.github.io/dog-blog/health/{page["filename"]}">')
    content.append('<meta property="og:site_name" content="Pet Calculators">')
    content.append('<meta property="og:locale" content="en_US">')
    content.append(f'<meta property="og:image" content="{page["image"]}">')
    content.append(f'<meta property="og:image:alt" content="{page["title"]} image">')
    content.append('<meta name="twitter:card" content="summary_large_image">')
    content.append(f'<meta name="twitter:title" content="{page["title"]} | Dog Health">')
    content.append(f'<meta name="twitter:description" content="{page["description"]}">')
    content.append(f'<meta name="twitter:image" content="{page["image"]}">')
    content.append('<meta name="theme-color" content="#2563eb">')
    content.append('')
    content.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755" crossorigin="anonymous"></script>')
    content.append('')
    content.append('<script type="application/ld+json">')
    blog_posting = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": page["title"],
        "description": page["description"],
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://mmm071026246-lgtm.github.io/dog-blog/health/{page['filename']}"
        },
        "author": {
            "@type": "Organization",
            "name": "Pet Calculators"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Pet Calculators"
        },
        "image": page["image"],
        "articleSection": "Dog Health",
        "keywords": [
            page["title"].lower(),
            "canine health",
            "dog care",
            "dog illness signs",
            "dog health guide"
        ]
    }
    content.append(json.dumps(blog_posting, indent=2))
    content.append('</script>')
    content.append('')
    content.append('<script type="application/ld+json">')
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq_template[0]["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_template[0]["answer"]
                }
            },
            {
                "@type": "Question",
                "name": faq_template[1]["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_template[1]["answer"]
                }
            },
            {
                "@type": "Question",
                "name": faq_template[2]["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_template[2]["answer"]
                }
            }
        ]
    }
    content.append(json.dumps(faq, indent=2))
    content.append('</script>')
    content.append('')
    content.append('<style>')
    content.append(base_style)
    content.append('</style>')
    content.append('</head>')
    content.append('<body>')
    content.append('')
    content.append('<nav class="breadcrumb" aria-label="breadcrumb">')
    content.append('    <a href="../index.html">Dog Health Hub</a> ›')
    content.append('    <a href="index.html">Health Guides</a> ›')
    content.append(f'    <span>{page["title"]}</span>')
    content.append('</nav>')
    content.append('')
    content.append(f'<h1>{page["title"]}</h1>')
    content.append('')
    content.append(f'<p>{page["description"]}</p>')
    content.append('')
    content.append(f'<p>{page["description"]} This article provides in-depth guidance for dog owners who want to understand important symptoms and respond with confidence.</p>')
    content.append('')
    content.append('<div class="notice">')
    content.append('    <strong>Key point:</strong> Early recognition helps you get treatment sooner and improves your dog’s chances of a full recovery.')
    content.append('</div>')
    content.append('')
    content.append('<div class="ad-box">')
    content.append('    <ins class="adsbygoogle"')
    content.append('    style="display:block"')
    content.append('    data-ad-client="ca-pub-9374368296307755"')
    content.append('    data-ad-slot="8079351163"')
    content.append('    data-ad-format="auto"')
    content.append('    data-full-width-responsive="true"></ins>')
    content.append('    <script>')
    content.append('    (adsbygoogle = window.adsbygoogle || []).push({});')
    content.append('    </script>')
    content.append('</div>')
    content.append('')

    # Add extra descriptive sections before main symptom sections
    for section in common_sections[:2]:
        content.append(f'<h2>{section["heading"]}</h2>')
        content.append(f'<p>{section["intro"]}</p>')
        content.append('<ul>')
        for bullet in section['bullets']:
            content.append(f'    <li>{bullet}</li>')
        content.append('</ul>')
        content.append('<p>These patterns often help distinguish between mild issues and conditions that require faster intervention.</p>')
        content.append('')

    for idx, (heading, intro, bullets) in enumerate(page['sections']):
        content.append(f'<h2>{heading}</h2>')
        content.append(f'<p>{intro}</p>')
        content.append('<ul>')
        for item in bullets:
            content.append(f'    <li>{item}</li>')
        content.append('</ul>')
        content.append('<h3>What this means</h3>')
        content.append('<p>These symptoms can indicate anything from a mild irritation to a condition that requires prompt veterinary support. Monitoring severity and change over time is important.</p>')
        content.append('<p>When in doubt, note the pattern and call your vet for advice rather than waiting too long.</p>')
        content.append('')
        if idx == 1:
            content.append('<div class="ad-box">')
            content.append('    <ins class="adsbygoogle"')
            content.append('    style="display:block"')
            content.append('    data-ad-client="ca-pub-9374368296307755"')
            content.append('    data-ad-slot="8079351163"')
            content.append('    data-ad-format="auto"')
            content.append('    data-full-width-responsive="true"></ins>')
            content.append('    <script>')
            content.append('    (adsbygoogle = window.adsbygoogle || []).push({});')
            content.append('    </script>')
            content.append('</div>')
            content.append('')

    content.append('<h2>How to interpret symptom severity</h2>')
    content.append('<p>Some symptoms are less urgent, while others require immediate veterinary care. This table helps you distinguish between levels of concern.</p>')
    content.append('<table>')
    content.append('    <thead>')
    content.append('        <tr>')
    content.append('            <th>Symptom category</th>')
    content.append('            <th>What it may indicate</th>')
    content.append('            <th>Action to take</th>')
    content.append('        </tr>')
    content.append('    </thead>')
    content.append('    <tbody>')
    content.append('        <tr>')
    content.append('            <td>Intermittent or mild</td>')
    content.append('            <td>May indicate mild upset or stress.</td>')
    content.append('            <td>Monitor closely and support with rest.</td>')
    content.append('        </tr>')
    content.append('        <tr>')
    content.append('            <td>Persistent or worsening</td>')
    content.append('            <td>Suggests a more serious underlying condition.</td>')
    content.append('            <td>Contact your veterinarian soon.</td>')
    content.append('        </tr>')
    content.append('        <tr>')
    content.append('            <td>Severe or sudden</td>')
    content.append('            <td>May require urgent or emergency care.</td>')
    content.append('            <td>Seek veterinary help immediately.</td>')
    content.append('        </tr>')
    content.append('    </tbody>')
    content.append('</table>')
    content.append('<p>Even mild symptoms should not be ignored if they persist. A follow-up appointment is often the best way to rule out more serious causes.</p>')
    content.append('<p>Discuss any symptom changes with your veterinarian and ask whether additional monitoring or treatment is needed.</p>')
    content.append('')

    for section in extra_sections:
        content.append(f'<h2>{section["heading"]}</h2>')
        content.append(f'<p>{section["intro"]}</p>')
        content.append('<ul>')
        for bullet in section['bullets']:
            content.append(f'    <li>{bullet}</li>')
        content.append('</ul>')
        content.append('<p>As you follow this guidance, keep in mind that every dog recovers at its own pace and that close monitoring helps avoid surprises.</p>')
        content.append('<p>Review these points with your veterinarian and adjust your care plan as your dog improves.</p>')
        content.append('')

    content.append('<h2>Frequently asked questions</h2>')
    for item in faq_template:
        content.append(f'<h3>{item["question"]}</h3>')
        content.append(f'<p>{item["answer"]}</p>')
    content.append('')
    content.append('<h2>Health tools and resources</h2>')
    content.append('<p>These tools can help you keep track of your dog’s overall wellness while you manage symptoms and recovery.</p>')
    content.append('<ul>')
    content.append('    <li><a href="../../dog/dog-age-calculator.html">Dog Age Calculator</a> — Helps you match care to your dog’s life stage.</li>')
    content.append('    <li><a href="../../dog/dog-ideal-weight-calculator.html">Dog Ideal Weight Calculator</a> — Helps maintain healthy body condition during recovery.</li>')
    content.append('    <li><a href="../../dog/dog-water-intake-calculator.html">Dog Water Intake Calculator</a> — Ensures hydration remains consistent after illness.</li>')
    content.append('    <li><a href="../../dog/dog-food-calculator.html">Dog Food Calculator</a> — Supports balanced nutrition as your dog recovers.</li>')
    content.append('</ul>')
    content.append('')
    content.append('<p>Using these resources alongside veterinary guidance helps you stay proactive and informed about your dog’s health.</p>')
    content.append('')
    content.append('<div class="related-box">')
    content.append('    <h3>Related guides:</h3>')
    content.append('    <ul>')
    for title, href in related_links[:4]:
        content.append(f'        <li><a href="{href}">{title}</a></li>')
    content.append('    </ul>')
    content.append('</div>')
    content.append('')
    content.append('<h2>Final takeaways</h2>')
    content.append('<p>Recognizing symptoms early and working with your veterinarian are the best ways to help your dog recover quickly and safely.</p>')
    content.append('<p>Every dog is unique, so tailor the approach to your pet’s needs and refer to this guide for ongoing monitoring and prevention.</p>')
    content.append('')
    content.append('<footer class="footer-note">')
    content.append('    Pet Calculators © . Always consult a licensed veterinarian for personalized medical advice.')
    content.append('</footer>')
    content.append('')
    content.append('</body>')
    content.append('</html>')

    path.write_text('\n'.join(content), encoding='utf-8')
    print(f'Wrote {path}')
