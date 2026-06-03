from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ─── 10TH COMPLETED ───────────────────────────────────────────────────────────
QUESTIONS_10TH = [
    {"id":1,"text":"When you have a free afternoon, what would you most enjoy doing?",
     "options":["Tinkering with gadgets or fixing things","Drawing, painting, or crafting","Reading about history or current events","Solving math puzzles or riddles","Helping a friend with their problems"],
     "map":{"Tinkering with gadgets or fixing things":"technical","Drawing, painting, or crafting":"creative","Reading about history or current events":"humanities","Solving math puzzles or riddles":"analytical","Helping a friend with their problems":"empathy"}},
    {"id":2,"text":"Which school project would excite you the most?",
     "options":["Building a working model or circuit","Designing a poster or short film","Writing an essay on a social issue","Creating a math/science experiment","Organizing a fundraiser for a cause"],
     "map":{"Building a working model or circuit":"technical","Designing a poster or short film":"creative","Writing an essay on a social issue":"humanities","Creating a math/science experiment":"analytical","Organizing a fundraiser for a cause":"empathy"}},
    {"id":3,"text":"Which TV show type would you binge?",
     "options":["Tech & engineering shows","Art, cooking, or fashion","Crime, history, or politics","Science & discovery","Medical or social drama"],
     "map":{"Tech & engineering shows":"technical","Art, cooking, or fashion":"creative","Crime, history, or politics":"humanities","Science & discovery":"analytical","Medical or social drama":"empathy"}},
    {"id":4,"text":"Your dream work environment looks like?",
     "options":["Workshop or lab with tools","Studio with creative freedom","Office with books and debates","Research desk with data","Hospital or community center"],
     "map":{"Workshop or lab with tools":"technical","Studio with creative freedom":"creative","Office with books and debates":"humanities","Research desk with data":"analytical","Hospital or community center":"empathy"}},
    {"id":5,"text":"Which word describes you best among friends?",
     "options":["The fixer / tech guy","The artist / designer","The talker / leader","The brains / strategist","The listener / helper"],
     "map":{"The fixer / tech guy":"technical","The artist / designer":"creative","The talker / leader":"humanities","The brains / strategist":"analytical","The listener / helper":"empathy"}},
    {"id":6,"text":"What makes you feel most proud of yourself?",
     "options":["When something I built actually works","When my creative work gets appreciated","When I change someone's opinion","When I solve a really tough problem","When I genuinely help someone"],
     "map":{"When something I built actually works":"technical","When my creative work gets appreciated":"creative","When I change someone's opinion":"humanities","When I solve a really tough problem":"analytical","When I genuinely help someone":"empathy"}},
    {"id":7,"text":"Which future job title sounds coolest to you?",
     "options":["Engineer or Architect","Designer or Filmmaker","Lawyer, Journalist, or Politician","Scientist or Data Expert","Doctor, Counselor, or Social Worker"],
     "map":{"Engineer or Architect":"technical","Designer or Filmmaker":"creative","Lawyer, Journalist, or Politician":"humanities","Scientist or Data Expert":"analytical","Doctor, Counselor, or Social Worker":"empathy"}},
    {"id":8,"text":"Pick the subject you'd study even without exams:",
     "options":["How machines and electronics work","Visual arts or music theory","Philosophy, politics, or literature","Pure mathematics or physics","Biology or psychology"],
     "map":{"How machines and electronics work":"technical","Visual arts or music theory":"creative","Philosophy, politics, or literature":"humanities","Pure mathematics or physics":"analytical","Biology or psychology":"empathy"}},
    {"id":9,"text":"Which skill would you most want to master?",
     "options":["Coding or hardware building","Illustration or video production","Public speaking or writing","Problem solving and logic","Understanding human behavior"],
     "map":{"Coding or hardware building":"technical","Illustration or video production":"creative","Public speaking or writing":"humanities","Problem solving and logic":"analytical","Understanding human behavior":"empathy"}},
    {"id":10,"text":"In a group project, you naturally become?",
     "options":["The one who builds and implements","The one who designs and presents","The one who researches and writes","The one who plans strategy and data","The one who manages people and conflict"],
     "map":{"The one who builds and implements":"technical","The one who designs and presents":"creative","The one who researches and writes":"humanities","The one who plans strategy and data":"analytical","The one who manages people and conflict":"empathy"}},
]

RESULTS_10TH = {
    "technical": {"stream":"Science (PCM)","icon":"⚙️","color":"#e63946",
        "why":"Your love for building and problem-solving makes PCM your launchpad.",
        "careers":["Software Engineer","Mechanical Engineer","Civil Engineer","Electrical Engineer","Robotics Engineer","Game Developer"],
        "paths":["PCM → B.Tech/BE → Core Engineering / IT Industry","PCM → B.Tech CSE → Software / AI / Robotics","PCM → Diploma → Polytechnic → Industry"]},
    "analytical":{"stream":"Science (PCM or PCB)","icon":"🔬","color":"#4361ee",
        "why":"You think in patterns and love discovering how things really work.",
        "careers":["Data Scientist","Research Scientist","Physicist","Mathematician","Economist","Actuary"],
        "paths":["PCM → B.Tech → Data Science / Research","PCM → BSc Physics/Maths → MSc → Research","PCM → Core Science or Engineering"]},
    "creative":  {"stream":"Humanities or Commerce with Arts","icon":"🎨","color":"#f4a261",
        "why":"You see the world through expression, beauty, and storytelling.",
        "careers":["Graphic Designer","Filmmaker","Architect","Fashion Designer","Illustrator","UX Designer"],
        "paths":["Arts/Humanities → BFA / Design School → Creative Industry","Humanities → Mass Communication → Media / Film","Commerce → BDes → Product or UX Design"]},
    "humanities":{"stream":"Humanities (Arts)","icon":"📚","color":"#2a9d8f",
        "why":"You love ideas, debate, and shaping how people think.",
        "careers":["Lawyer / Judge","Journalist","Politician / IAS Officer","Author","HR Manager","Diplomat"],
        "paths":["Humanities → BA → LLB → Legal Career","Humanities → BA → UPSC → IAS / IPS / IFS","Humanities → Mass Comm → Journalism / Media"]},
    "empathy":   {"stream":"Science (PCB) or Humanities","icon":"💚","color":"#06d6a0",
        "why":"You genuinely care about people — that's your superpower.",
        "careers":["Doctor / Surgeon","Psychologist","Nurse / Physiotherapist","Social Worker","NGO Leader","Counselor"],
        "paths":["PCB → NEET → MBBS → Doctor","PCB → BSc Nursing / Allied Health","Humanities → BSW → Social Work / NGO"]},
}

# ─── 12TH COMPLETED ───────────────────────────────────────────────────────────
QUESTIONS_12TH = [
    {"id":1,"text":"Which of these activities sounds like a dream Saturday to you?",
     "options":["Coding a side project or app","Sketching logos or editing videos","Debating politics or writing articles","Running experiments or analyzing data","Volunteering or mentoring juniors"],
     "map":{"Coding a side project or app":"tech","Sketching logos or editing videos":"design","Debating politics or writing articles":"social","Running experiments or analyzing data":"science","Volunteering or mentoring juniors":"care"}},
    {"id":2,"text":"What kind of problems do you most want to solve in life?",
     "options":["Build smarter technology","Make things look and feel better","Fix broken systems in society","Discover new scientific truths","Help people live healthier or happier lives"],
     "map":{"Build smarter technology":"tech","Make things look and feel better":"design","Fix broken systems in society":"social","Discover new scientific truths":"science","Help people live healthier or happier lives":"care"}},
    {"id":3,"text":"If you had to pick a college club, which one?",
     "options":["Coding / Robotics Club","Design / Photography Club","Debate / Model UN","Science / Research Club","NSS / Community Service"],
     "map":{"Coding / Robotics Club":"tech","Design / Photography Club":"design","Debate / Model UN":"social","Science / Research Club":"science","NSS / Community Service":"care"}},
    {"id":4,"text":"Where do you see yourself at 30?",
     "options":["Working at a top tech company or running a startup","Running a creative agency or making films","Leading policy changes or running an NGO","Publishing research or working in a lab","Helping patients, students, or communities"],
     "map":{"Working at a top tech company or running a startup":"tech","Running a creative agency or making films":"design","Leading policy changes or running an NGO":"social","Publishing research or working in a lab":"science","Helping patients, students, or communities":"care"}},
    {"id":5,"text":"Pick one word that describes how you want to impact the world:",
     "options":["Innovate","Create","Reform","Discover","Heal"],
     "map":{"Innovate":"tech","Create":"design","Reform":"social","Discover":"science","Heal":"care"}},
    {"id":6,"text":"Which type of content do you consume most?",
     "options":["Tech tutorials, startups, AI news","Design inspiration, films, photography","News, politics, social issues","Science journals, documentaries, research","Health, motivation, human stories"],
     "map":{"Tech tutorials, startups, AI news":"tech","Design inspiration, films, photography":"design","News, politics, social issues":"social","Science journals, documentaries, research":"science","Health, motivation, human stories":"care"}},
    {"id":7,"text":"What does success look like to you?",
     "options":["Building a product used by millions","Creating art that moves people","Making laws or systems fairer","Winning a prestigious research award","Transforming someone's life directly"],
     "map":{"Building a product used by millions":"tech","Creating art that moves people":"design","Making laws or systems fairer":"social","Winning a prestigious research award":"science","Transforming someone's life directly":"care"}},
    {"id":8,"text":"Your friends come to you when they need?",
     "options":["Technical help or advice","Aesthetic feedback or ideas","Honest opinions on life decisions","Logical analysis of a situation","Emotional support or guidance"],
     "map":{"Technical help or advice":"tech","Aesthetic feedback or ideas":"design","Honest opinions on life decisions":"social","Logical analysis of a situation":"science","Emotional support or guidance":"care"}},
    {"id":9,"text":"Which environment makes you most productive?",
     "options":["A coding setup with multiple screens","A studio with creative tools everywhere","A library or policy think-tank","A research lab or data center","A hospital, school, or field setting"],
     "map":{"A coding setup with multiple screens":"tech","A studio with creative tools everywhere":"design","A library or policy think-tank":"social","A research lab or data center":"science","A hospital, school, or field setting":"care"}},
    {"id":10,"text":"Which of these projects would you be most excited to do?",
     "options":["Build an AI chatbot or mobile app","Design a brand identity or short film","Write a policy paper or start a movement","Conduct original research and publish it","Run a mental health or education program"],
     "map":{"Build an AI chatbot or mobile app":"tech","Design a brand identity or short film":"design","Write a policy paper or start a movement":"social","Conduct original research and publish it":"science","Run a mental health or education program":"care"}},
]

RESULTS_12TH = {
    "tech":   {"stream":"B.Tech / BCA / BSc Computer Science","icon":"💻","color":"#4361ee",
        "why":"You're wired to build and innovate with technology.",
        "careers":["Software Engineer","AI/ML Engineer","Cybersecurity Analyst","Product Manager","Full-Stack Developer","Cloud Architect"],
        "paths":["B.Tech CSE → Software / AI / Product Companies","BCA → MCA → IT Industry","BSc CS → MSc / MTech → Research or Industry"]},
    "design": {"stream":"BDes / BA Design / Mass Communication","icon":"🎨","color":"#f4a261",
        "why":"You think visually and communicate through creativity.",
        "careers":["UX/UI Designer","Brand Designer","Filmmaker / Director","Animator","Art Director","Content Strategist"],
        "paths":["BDes → Design Agency / Product Startups","BA Mass Comm → Media / Film / Advertising","BFA → Creative Industry / Freelance"]},
    "social": {"stream":"BA / BBA / Law / Journalism","icon":"🌍","color":"#2a9d8f",
        "why":"You want to change systems and influence how the world works.",
        "careers":["IAS / IPS Officer","Lawyer / Advocate","Journalist","Policy Analyst","HR Manager","Diplomat"],
        "paths":["BA → UPSC → Civil Services","BA/BBA → LLB → Legal Career","BJourn → Journalism / Media / Digital"]},
    "science":{"stream":"BSc / B.Tech with Research focus","icon":"🔬","color":"#7209b7",
        "why":"You want to push the boundaries of human knowledge.",
        "careers":["Research Scientist","Data Scientist","Biotech Engineer","Environmental Scientist","Economist","Actuary"],
        "paths":["BSc Physics/Chem/Bio → MSc → PhD → Research","B.Tech → GATE → MTech / Research Labs","BSc Stats/Maths → Data Science / Finance"]},
    "care":   {"stream":"MBBS / BSc Nursing / BSW / BEd","icon":"💚","color":"#06d6a0",
        "why":"Helping people isn't just a career for you — it's a calling.",
        "careers":["Doctor / Surgeon","Psychologist / Counselor","Nurse / Physiotherapist","Social Worker","School Teacher","Child Development Specialist"],
        "paths":["PCB → NEET → MBBS → Doctor","BSc Nursing / Allied Health → Healthcare","BSW → Social Work / NGO / Government"]},
}

# ─── B.TECH ───────────────────────────────────────────────────────────────────
QUESTIONS_BTECH = [
    {"id":1,"text":"Which kind of work genuinely excites you day-to-day?",
     "options":["Writing code and solving algorithmic problems","Designing systems and infrastructure","Working with data to find patterns","Building user-facing products and interfaces","Leading teams and strategy"],
     "map":{"Writing code and solving algorithmic problems":"dev","Designing systems and infrastructure":"systems","Working with data to find patterns":"data","Building user-facing products and interfaces":"product","Leading teams and strategy":"management"}},
    {"id":2,"text":"Which course or topic do you engage with most in college?",
     "options":["DSA, OOPS, or competitive programming","Networks, OS, or cloud systems","Machine Learning, statistics, or databases","Web/app development or design","Management, finance, or entrepreneurship"],
     "map":{"DSA, OOPS, or competitive programming":"dev","Networks, OS, or cloud systems":"systems","Machine Learning, statistics, or databases":"data","Web/app development or design":"product","Management, finance, or entrepreneurship":"management"}},
    {"id":3,"text":"You just got 3 free hours. What do you actually do?",
     "options":["Solve problems on LeetCode / Codeforces","Set up a Linux server or learn DevOps","Explore a Kaggle dataset or train a model","Build a personal project or design a UI","Read startup stories or watch business content"],
     "map":{"Solve problems on LeetCode / Codeforces":"dev","Set up a Linux server or learn DevOps":"systems","Explore a Kaggle dataset or train a model":"data","Build a personal project or design a UI":"product","Read startup stories or watch business content":"management"}},
    {"id":4,"text":"Which internship would you fight for?",
     "options":["Backend / software dev role at a product company","Cloud or infrastructure role at AWS/Google","Data science or ML internship","Frontend or full-stack at a startup","Business analyst or product intern at a unicorn"],
     "map":{"Backend / software dev role at a product company":"dev","Cloud or infrastructure role at AWS/Google":"systems","Data science or ML internship":"data","Frontend or full-stack at a startup":"product","Business analyst or product intern at a unicorn":"management"}},
    {"id":5,"text":"Which sentence describes your ideal career output?",
     "options":["Clean, efficient code that ships features","Reliable infrastructure that never goes down","Insights that drive decisions with data","A product that users love using","A company or team that I've built and led"],
     "map":{"Clean, efficient code that ships features":"dev","Reliable infrastructure that never goes down":"systems","Insights that drive decisions with data":"data","A product that users love using":"product","A company or team that I've built and led":"management"}},
    {"id":6,"text":"What's your biggest strength honestly?",
     "options":["I write very clean, logical code","I'm great at architecture and infrastructure","I turn messy data into clear stories","I build things people actually want to use","I get people aligned and moving forward"],
     "map":{"I write very clean, logical code":"dev","I'm great at architecture and infrastructure":"systems","I turn messy data into clear stories":"data","I build things people actually want to use":"product","I get people aligned and moving forward":"management"}},
    {"id":7,"text":"In a hackathon, which role do you naturally take?",
     "options":["Core backend developer","DevOps / infra setup","Data pipeline and model builder","Frontend / UI and product flow","Team lead, presenter, and idea generator"],
     "map":{"Core backend developer":"dev","DevOps / infra setup":"systems","Data pipeline and model builder":"data","Frontend / UI and product flow":"product","Team lead, presenter, and idea generator":"management"}},
    {"id":8,"text":"Which certification or course would you take right now?",
     "options":["System design or advanced DSA","AWS / GCP / Kubernetes certification","Coursera ML or fast.ai deep learning","Full-stack bootcamp or UI/UX course","MBA prep or product management course"],
     "map":{"System design or advanced DSA":"dev","AWS / GCP / Kubernetes certification":"systems","Coursera ML or fast.ai deep learning":"data","Full-stack bootcamp or UI/UX course":"product","MBA prep or product management course":"management"}},
    {"id":9,"text":"Which company type is your dream employer?",
     "options":["FAANG / top product company as SDE","Cloud-first company like Cloudflare or HashiCorp","Data-heavy company like a quant firm or AI lab","Startup where I own full product decisions","Consulting firm or my own startup"],
     "map":{"FAANG / top product company as SDE":"dev","Cloud-first company like Cloudflare or HashiCorp":"systems","Data-heavy company like a quant firm or AI lab":"data","Startup where I own full product decisions":"product","Consulting firm or my own startup":"management"}},
    {"id":10,"text":"What do you want people to say about your work 5 years from now?",
     "options":["Their code is rock solid and elegant","Their systems never fail","Their analysis changed how we think","Their product changed how users experience it","They built something from nothing"],
     "map":{"Their code is rock solid and elegant":"dev","Their systems never fail":"systems","Their analysis changed how we think":"data","Their product changed how users experience it":"product","They built something from nothing":"management"}},
]

RESULTS_BTECH = {
    "dev":       {"stream":"Software Development / SDE Track","icon":"💻","color":"#4361ee",
        "why":"You're built for clean code, algorithms, and shipping products that scale.",
        "careers":["Software Development Engineer (SDE)","Backend Engineer","Full-Stack Developer","Open Source Contributor","Competitive Programmer → FAANG"],
        "paths":["Master DSA + System Design → SDE-1 at Product Company","B.Tech → Internship → FAANG / top MNC","B.Tech → Startup SDE → Build your own product"]},
    "systems":   {"stream":"DevOps / Cloud / Infrastructure Engineering","icon":"☁️","color":"#7209b7",
        "why":"You love building the invisible backbone that keeps everything running.",
        "careers":["DevOps Engineer","Cloud Architect","Site Reliability Engineer (SRE)","Network Engineer","Cybersecurity Engineer"],
        "paths":["B.Tech → AWS/GCP Cert → Cloud/DevOps Role","B.Tech → SRE at Big Tech","B.Tech → Cybersecurity cert → InfoSec career"]},
    "data":      {"stream":"Data Science / AI / ML Engineering","icon":"🤖","color":"#e63946",
        "why":"Numbers, models, and insights are your native language.",
        "careers":["Data Scientist","ML Engineer","AI Researcher","Business Intelligence Analyst","Quantitative Analyst"],
        "paths":["B.Tech → Kaggle / Projects → Data Science role","B.Tech → MTech/MS in AI → Research / Big Tech","B.Tech → CFA + Quant skills → Finance / FinTech"]},
    "product":   {"stream":"Product Management / Full-Stack / UX","icon":"🚀","color":"#f4a261",
        "why":"You build what users want and make the experience beautiful and seamless.",
        "careers":["Product Manager","Full-Stack Developer","UX Engineer","Startup Founder","Growth Hacker"],
        "paths":["B.Tech → APM Program → PM at Tech Company","B.Tech → Full-stack projects → Startup / Freelance","B.Tech → UX Bootcamp → Product Design role"]},
    "management":{"stream":"MBA / Entrepreneurship / Business Track","icon":"👑","color":"#2a9d8f",
        "why":"You see the big picture and know how to move people and resources toward a goal.",
        "careers":["Entrepreneur / Startup Founder","Product Manager (Senior)","Business Analyst","Management Consultant","Venture Capitalist"],
        "paths":["B.Tech → CAT/GMAT → IIM → Management Career","B.Tech → Build startup → Raise funding","B.Tech → Consulting firm → Strategy roles"]},
}

# ─── ROUTES ───────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/questions/<level>")
def get_questions(level):
    if level == "10th":  return jsonify(QUESTIONS_10TH)
    if level == "12th":  return jsonify(QUESTIONS_12TH)
    if level == "btech": return jsonify(QUESTIONS_BTECH)
    return jsonify([]), 404

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    level   = data.get("level")
    answers = data.get("answers", {})

    if level == "10th":   questions, results = QUESTIONS_10TH, RESULTS_10TH
    elif level == "12th": questions, results = QUESTIONS_12TH, RESULTS_12TH
    elif level == "btech":questions, results = QUESTIONS_BTECH, RESULTS_BTECH
    else: return jsonify({"error": "Invalid level"}), 400

    if len(answers) < len(questions):
        return jsonify({"error": "Answer all questions"}), 400

    scores = {}
    for q in questions:
        qid = str(q["id"])
        if qid in answers:
            trait = q["map"].get(answers[qid])
            if trait:
                scores[trait] = scores.get(trait, 0) + 1

    dominant = max(scores, key=scores.get) if scores else list(results.keys())[0]
    return jsonify({"result": results[dominant], "scores": scores, "dominant": dominant})

if __name__ == "__main__":
    app.run(debug=True, port=5050)