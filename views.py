from django.shortcuts import render

class TeamMember:
    def __init__(self, full_name, student_id, email=None):
        self.full_name = full_name
        self.student_id = student_id
        self.email = email

def about_page(request):
    # Dummy data for demonstration, replace this with your actual data retrieval logic
    team_members = [
        TeamMember(full_name='Amar Tamang', student_id='s368248', email='amartamang12334@example.com'),
        TeamMember(full_name='Md Arafat Islam Taluker', student_id='s361203', email='arafattalukder211@example.com'),
        TeamMember(full_name='Mohammed Jawad Jafar Rafi', student_id='s365058', email='jawadjafar20114@example.com'),
        TeamMember(full_name='Md Badrul Hasan Bhuiyan', student_id='s361204', email='badrulhasan7564@example.com'),
        TeamMember(full_name='Ricky Bobby', student_id='s321512', email='trickyrick321@example.com'),
        # Add more team members as needed
    ]

    