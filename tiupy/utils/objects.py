from bs4 import BeautifulSoup
from dataclasses import dataclass, field, asdict
from typing import List, Optional
import json

@dataclass
class PersonalInfo:
    """Represents detailed personal information of a student."""
    
    gender: Optional[str] = None
    status: Optional[str] = None
    tuition_type: Optional[str] = None
    registration_date: Optional[str] = None
    registration_reason: Optional[str] = None
    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    birth_date: Optional[str] = None
    phones: List[str] = field(default_factory=list)
    father_phone: Optional[str] = None
    mother_phone: Optional[str] = None
    graduating_phone: Optional[str] = None

    def from_html(self, html: str) -> None:
        """Parse personal information from HTML content."""
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")
        self._extract_personal_data(soup)
        self._extract_phone_data(soup)

    def _extract_personal_data(self, soup: BeautifulSoup) -> None:
        """Extract basic personal information from the soup object."""
        labels_map = {
            'Gender': 'gender',
            'Status': 'status',
            'Tuition/Scholarship Student': 'tuition_type',
            'Date of Registration': 'registration_date',
            'Reason of Registration': 'registration_reason',
            'Name of Father': 'father_name',
            'Name of Mother': 'mother_name',
            'Date of Birth': 'birth_date'
        }

        for row in soup.select('table tr'):
            columns = row.find_all('td')
            if len(columns) >= 2:
                label = columns[0].text.strip(':')
                if label in labels_map:
                    setattr(self, labels_map[label], columns[1].text.strip())

    def _extract_phone_data(self, soup: BeautifulSoup) -> None:
        """Extract phone numbers from the soup object."""

        phone_fields = ['cep_tel', 'ika_tel', 'kef_tel', 'kef_cep_tel', 
                       'kef_is_tel', 'ceptel', 'evtel']
        phone_inputs = soup.find_all('input', {
            'name': lambda x: x and x in phone_fields
        })
        self.phones = [input_['value'] for input_ in phone_inputs if input_.get('value')]


        father_phone = soup.find('input', {'name': 'babatel'})
        mother_phone = soup.find('input', {'name': 'anatel'})
        graduating_phone = soup.find('input', {'name': 'mezuntel'})

        self.father_phone = father_phone['value'] if father_phone and father_phone.get('value') else None
        self.mother_phone = mother_phone['value'] if mother_phone and mother_phone.get('value') else None
        self.graduating_phone = graduating_phone['value'] if graduating_phone and graduating_phone.get('value') else None

    def to_dict(self) -> dict:
        """Convert personal info to a dictionary."""
        return asdict(self)

    def to_json(self) -> str:
        """Convert personal info to a JSON string."""
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class Course:
    """Represents a single course with its details."""
    
    course_code: str
    course_name: str
    credits: str
    grade: str

    def to_dict(self) -> dict:
        """Convert course data to a dictionary."""
        return asdict(self)

    def to_json(self) -> str:
        """Convert course data to a JSON string."""
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class CourseData:
    """Collection of courses with methods for data manipulation."""
    
    courses: List[Course] = field(default_factory=list)

    def from_html(self, html: str) -> None:
        """Parse course data from HTML content."""
        soup = BeautifulSoup(html, "html.parser")
        self.courses = self._extract_courses_data(soup)

    def _extract_courses_data(self, soup: BeautifulSoup) -> List[Course]:
        """Extract course information from the soup object."""
        course_list = []
        for row in soup.select('tr'):
            cells = row.find_all('td')
            if len(cells) == 5:
                course_code, course_name, credits, grade = [
                    cell.text.strip() for cell in cells[:4]
                ]
                if all([course_code, course_name, credits, grade]):
                    course_list.append(Course(course_code, course_name, credits, grade))
        return course_list

    def to_dict_list(self) -> List[dict]:
        """Convert all courses to a list of dictionaries."""
        return [course.to_dict() for course in self.courses]

    def to_json(self) -> str:
        """Convert all courses to JSON format."""
        return json.dumps(self.to_dict_list(), indent=2)


@dataclass
class UserProfile:
    """Represents a user's profile with all associated information."""
    
    image: Optional[str] = None
    name: Optional[str] = None
    curriculum: Optional[str] = None
    department: Optional[str] = None
    student_id: Optional[str] = None
    last_login: Optional[str] = None
    grade: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None
    gpa: Optional[str] = None
    year: Optional[str] = None
    term: Optional[str] = None
    type: Optional[str] = None
    somestr: Optional[str] = None
    info_board: List[str] = field(default_factory=list)
    personal_info: Optional[PersonalInfo] = None

    def from_html(self, html: str) -> None:
        """Parse user profile data from HTML content."""
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")
        self.image = self._extract_image(soup)
        self._extract_user_data(soup)
        self.info_board = self._extract_info_board(soup)

    def _extract_image(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract profile image URL from the soup object."""
        img_tag = soup.select_one('img[src*="https://my.tiu.edu.iq/myresim/"]')
        return img_tag.get("src") if img_tag else None

    def _extract_user_data(self, soup: BeautifulSoup) -> None:
        """Extract user information from the soup object."""
        labels_map = {
            'Name Surname': 'name',
            'CURRICULUM': 'curriculum',
            'Department': 'department',
            'Student ID': 'student_id',
            'Last Login': 'last_login',
            'GRADE': 'grade',
            'E-mail': 'email',
            'Mobile': 'mobile',
            'GPA': 'gpa',
            'Year': 'year',
            'Term': 'term',
            'Type': 'type',
            'Somestr': 'somestr'
        }

        for row in soup.select('table tr'):
            columns = row.find_all('td')
            if len(columns) >= 2:
                label = columns[0].text.strip(':')
                if label in labels_map:
                    setattr(self, labels_map[label], columns[1].text.strip())

    def _extract_info_board(self, soup: BeautifulSoup) -> List[str]:
        """Extract info board links from the soup object."""
        return [
            link['href'] for link in 
            soup.select('a.box[href^="https://my.tiu.edu.iq/pages/p401.php?id="]')
        ]

    def to_dict(self) -> dict:
        """Convert user profile to a dictionary."""
        data = asdict(self)
        if self.personal_info:
            data['personal_info'] = self.personal_info.to_dict()
        return data

    def to_json(self) -> str:
        """Convert user profile to JSON format."""
        return json.dumps(self.to_dict(), indent=2)
