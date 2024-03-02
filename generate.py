import json

with open('me.json') as f:
    talaman = json.load(f)

def generate_md(data,filepath):
    with open(filepath, 'w') as f:
        f.write(f"# {data['name']} ({data['alias']})\n")
        f.write(f"{data['title']}\n\n")
        f.write(f"- {data['age']} years old\n")
        f.write(f"- Currently based in {data['location']}\n")
        f.write(f"- Phone: [{data['contact']['phone']}](tel:{data['contact']['phone']})\n")
        f.write(f"- Email: [{data['contact']['email']}](mailto:{data['contact']['email']})\n")
        f.write(f"- Website: [{data['contact']['website']}](https://{data['contact']['website']})\n\n")
        f.write(f"## PERSONAL STATEMENT\n\n")
        f.write(f"{data['personal_statement']}\n\n")
        f.write(f"## SKILLS AND EXPERIENCE\n\n")
        f.write(f"{data['skills_and_experience']}\n\n")
        f.write(f"## PERSONAL INTERESTS\n\n")
        f.write(f"{data['personal_interests']}\n\n")
        f.write(f"## EDUCATION\n\n")
        for education in data['education']:
            f.write(f"- {education['degree']}, {education['institution']}, {education['year']}.\n")
        f.write(f"\n## RELEVANT WORK HISTORY\n\n")
        for job in data['work_history']:
            website = f" ({job['website']})" if job['website'] else ""
            f.write(f"### {job['title']}, {job['company']}{website}, {job['location']}. {job['period']}\n\n")
            f.write(f"{job['description']}\n\n")
        f.write(f"## My stack of interest includes\n\n")
        f.write(f"{data['stack_of_interest']}\n\n")
        f.write(f"I'm skilled in {data['skills']}\n\n")
        f.write(f"## LANGUAGES\n\n")
        for language in data['languages']:
            f.write(f"- {language['language']}, {language['level']}.\n")
        f.write(f"\n## REFERENCES\n\n")
        for reference in data['references']:
            f.write(f"{reference['name']}, {reference['title']}, {reference['company']}.\n")
            f.write(f"LinkedIn: {reference['linkedin']}\n")
            f.write(f"Phone: {reference['phone']}\n\n")

generate_md(talaman, 'me.md')
generate_md(talaman, 'me.txt')

import subprocess

subprocess.run(["mdpdf", "-o", "me.pdf", "me.md"])