import smtplib

sender_email = "aafeefarahman@gmail.com"
app_password = "add your password"

companies = {
     "Algorand Foundation": "community@algorand.foundation",
    "Solana Foundation": "events@solana.org",
    "Stream": "support@getstream.io",
    "Supabase": "support@supabase.com",
    "Neon": "partners@neon.tech",
    "Clerk": "partnerships@clerk.com",
    "Convex": "founders@convex.dev"
    # Add more companies here
}

subject = "Sponsorship Opportunity – National AI & Innovation Hackathon at IIIT Hyderabad"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

for company, email in companies.items():

    body = f"""
Dear Team,

I hope you are doing well.

I am reaching out on behalf of the organizing team of an upcoming hackathon to be hosted at IIIT Hyderabad, one of India's leading technology institutions.

The event is expected to bring together approximately 300–350 highly motivated students, developers, researchers, and innovators from across the country to collaborate and build solutions in emerging technology domains.

EVENT HIGHLIGHTS:

Venue: IIIT Hyderabad
Participants: 300–350

Themes:
• Agentic AI
• Vision-Language Agents (VLA) & Robotics
• Cybersecurity
• Computer Vision
• Open Innovation

Event Poster:
https://drive.google.com/file/d/1qQSfc7eGWaG4MBH0XYVzFbGyV-22VSfp/view?usp=sharing

We would be honored to explore a sponsorship and collaboration opportunity with your organization. Your support can significantly enhance the participant experience through prizes, credits, mentorship, workshops, merchandise, internship opportunities, cloud credits, API credits, internship opportunities, or other forms of partnership.

In return, we would be happy to provide:
• Brand visibility across event promotions and social media
• Logo placement on event materials and website
• Direct engagement with top student talent
• Recognition during the event and closing ceremony
• Recruitment and community outreach opportunities

We would be delighted to discuss potential collaboration models and provide additional event details at your convenience.

Thank you for your time and consideration. We look forward to the possibility of partnering with {company} to make this event a meaningful experience for the next generation of innovators.

Best Regards,

Afeefa Rahman
TEAM AI FOUNDRY
"""

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(sender_email, email, message.encode("utf-8"))
    print(f"✓ Sent to {company}")

server.quit()

print("All emails sent successfully!")