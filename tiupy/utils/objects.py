from bs4 import BeautifulSoup
from dataclasses import dataclass, field, asdict
from typing import List, Optional
import json

@dataclass
class UserProfile:
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

    def from_html(self, html: str):
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")
        self.image = self._extract_image(soup)
        self._extract_user_data(soup)
        self.info_board = self._extract_info_board(soup)

    def _extract_image(self, soup) -> Optional[str]:
        img_tag = soup.select_one('img[src*="https://my.tiu.edu.iq/myresim/"]')
        return img_tag.get("src") if img_tag else None

    def _extract_user_data(self, soup):
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

    def _extract_info_board(self, soup) -> List[str]:
        return [link['href'] for link in soup.select('a.box[href^="https://my.tiu.edu.iq/pages/p401.php?id="]')]


@dataclass
class Course:
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
    courses: List[Course] = field(default_factory=list)

    def from_html(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        self.courses = self._extract_courses_data(soup)

    def _extract_courses_data(self, soup) -> List[Course]:
        course_list = []
        for row in soup.select('tr'):
            cells = row.find_all('td')
            if len(cells) == 5:
                course_code, course_name, credits, grade = [cell.text.strip() for cell in cells[:4]]
                if all([course_code, course_name, credits, grade]):
                    course_list.append(Course(course_code, course_name, credits, grade))
        return course_list

    def to_dict_list(self) -> List[dict]:
        """Convert all courses to a list of dictionaries."""
        return [course.to_dict() for course in self.courses]

    def to_json(self) -> str:
        """Convert all courses to JSON format."""
        return json.dumps(self.to_dict_list(), indent=2)
