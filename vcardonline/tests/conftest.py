import pytest
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.images import ImageFile

from users.models.customuser import CustomUser

from cv.models.cv import Cv
from cv.models.experience import Experience
from cv.models.hobbies import Hobbies
from cv.models.formation import Formation

from skill.models.softskill import SoftSkill
from skill.models.technology import Technology
from skill.models.language import Language

from project.models.project import Project

@pytest.fixture
def mock_presentation_file(tmpdir):
    file_content = (
        'fichier test'
    )
    temp_presentation_file = tmpdir.join('presentation.txt')
    temp_presentation_file.write_text(file_content, encoding='utf-8')
    return temp_presentation_file

@pytest.fixture
def mock_documentation_file(tmpdir):
    file_content = (
        'fichier test'
    )
    temp_documentation_file = tmpdir.join('documentation.txt')
    temp_documentation_file.write_text(file_content, encoding='utf-8')
    return temp_documentation_file

@pytest.fixture
def mock_image_file(tmpdir):
    img = Image.new("RGB", (800, 600), color=(256, 0, 0))
    img_file = BytesIO()
    img.save(img_file, 'JPEG')
    file = ImageFile(img_file)
    return file

@pytest.fixture
def get_datas(mock_documentation_file, mock_image_file, mock_presentation_file):

    # partie utilisateur de test

    user1 = CustomUser.objects.create_user(
        username='user1',
        password='P@s$4TestAp1',
        email='user1@test.net',
        first_name='user',
        last_name='1',
        phone='0323456789',
        mobile='0612345678',
        birth_date='1986-09-01',
        number='1',
        street='route des marrons',
        city='Little Town',
        state='FR',
        zip_code='89140',
        country='France',
        linkedin_url='https://www.linkedin.com/in/util1',
        git_url='https://github.com/util1'

    )

    user2 = CustomUser.objects.create_user(
        username='user2',
        password='P@s$4TestAp1',
        email='user2@test.net',
        first_name='user',
        last_name='2',
        phone='0123456789',
        mobile='0687654321',
        birth_date='1986-09-01',
        number='2',
        street='rue du lavoir',
        city='Big Town',
        state='FR',
        zip_code='77140',
        country='France',
        linkedin_url='https://www.linkedin.com/in/util2',
        git_url='https://github.com/util2'


    )

    # partie skills

    language1 = Language.objects.create(
        title='Langue1',
        user=user1,
    )

    language2 = Language.objects.create(
        title='Langue2',
        user=user1,
    )

    softskill1 = SoftSkill.objects.create(
        title='softskill1',
        summary='resumé softskill1',
        user=user1
    )

    softskill2 = SoftSkill.objects.create(
        title='softskill2',
        summary='resumé softskill2',
        user=user1
    )

    technologie1 = Technology.objects.create(
        title='technologie1',
        user=user1
    )

    technologie2 = Technology.objects.create(
        title='technologie2',
        user=user1
    )

    # partie projet

    test_presentation_file = mock_presentation_file
    test_documentation_file = mock_documentation_file
    test_image_file = mock_image_file

    projet1 = Project.objects.create(
        title='projet1',
        description='description projet1',
        date_started='2023-09-21',
        date_end='2023-10-21',
        tasks='tache1-tache2-tache3',
        link_git='https://github.com/util1/projet1',
        user=user1,
        can_be_display=True
    )
    projet1.technologies.add(technologie1, technologie2)
    projet1.softskills.add(softskill1, softskill2)
    projet1.save()
    projet1.presentation_file = SimpleUploadedFile('test_presentation_file.txt', b'content')
    projet1.documents = SimpleUploadedFile('test_documentation_file.txt', b'content')
    projet1.image = test_image_file

    projet2 = Project.objects.create(
        title='projet2',
        description='description projet2',
        date_started='2023-11-21',
        date_end='2023-12-21',
        tasks='tache1-tache2-tache3',
        link_git='https://github.com/util1/projet2',
        user=user1
    )
    projet2.technologies.add(technologie1, technologie2)
    projet2.softskills.add(softskill1, softskill2)
    projet2.save()
    projet2.presentation_file = SimpleUploadedFile('test_presentation_file.txt', b'content')
    projet2.documents = SimpleUploadedFile('test_documentation_file.txt', b'content')
    projet2.image = test_image_file

    # partie CV de test

    experience1 = Experience.objects.create(
        title='experience1',
        company_name='company1',
        location='location1',
        date_started='2023-10-01',
        date_end='2023-12-01',
        tasks='tache1-tache2-tache3',
        user=user1,
    )

    experience2 = Experience.objects.create(
        title='experience2',
        company_name='company2',
        location='location2',
        date_started='2023-01-01',
        date_end='2023-09-30',
        tasks='tache1-tache2-tache3',
        user=user1,
    )

    formation1 = Formation.objects.create(
        title='formation1',
        school_name='school1',
        location='location1',
        date_started='1999-01-01',
        date_end='2000-01-01',
        user=user1,
    )

    formation2 = Formation.objects.create(
        title='formation2',
        school_name='school2',
        location='location2',
        date_started='2001-01-01',
        date_end='2002-01-01',
        user=user1,
    )

    hobbie1 = Hobbies.objects.create(
        title='hobbie 1',
        description="description hobbie 1",
        user=user1
    )

    hobbie2 = Hobbies.objects.create(
        title='hobbie 2',
        description="description hobbie 2",
        user=user1
    )

    cv1 = Cv.objects.create(
        title='cv1',
        profil='profil user1',
        user=user1,
        can_be_display=True
    )
    cv1.experiences.add(experience1, experience2)
    cv1.softskills.add(softskill1, softskill2)
    cv1.languages.add(language1, language2)
    cv1.hobbies.add(hobbie1, hobbie2)
    cv1.formations.add(formation1, formation2)
    cv1.technologies.add(technologie1, technologie2)

    return locals()
