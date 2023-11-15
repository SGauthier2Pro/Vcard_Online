from world import Human
from brain import Knowledges, QuickLearning


class Developer(Human):

    first_name = "Sylvain"
    last_name = "Gauthier"
    birthday_date = "21/09/1979"
    skills = ['curiosity', 'ingeneering', 'autonomy', 'arrangement',
              'communication', 'creativity', 'rigor', 'teamWork']
    technologies = ['Docker', 'Python', 'SQL', 'Javascript', 'Django',
                    'CSS', 'Sass', 'HTML', 'Git', 'PostgreSQL']

    def analyse_skills_needed(self, customer_needs):
        for customer_need in customer_needs:
            for skill in self.skills:
                if customer_need == skill:
                    return "I'm you man !"
                else:
                    new_skill = Knowledges(customer_need)
                    Quicklearning.learn(new_skill)
                    self.skills.append(new_skill)
                    return "I'll do my best to adapt !"

    def analyse_technologies_needed(self, customer_needs):
        for customer_need in customer_needs:
            for technology in self.technologies:
                if customer_need == technology:
                    return "I'm you man !"
                else:
                    new_technology = Knowledges(customer_need)
                    Quicklearning.learn(new_technology)
                    self.technologies.append(new_technology)
                    return "I'll do my best to make the job !"
