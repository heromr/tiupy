from bs4 import BeautifulSoup

class UserProfile:
    def __init__(self, html):
        self.image = self.name = self.curriculum = self.department = self.student_id = None
        self.last_login = self.grade = self.email = self.mobile = self.gpa = self.year = None
        self.term = self.type = self.somestr = None
        self.info_board = []

        if not html:
            return

        self.soup = BeautifulSoup(html, "html.parser")
        self._extract_image()
        self._extract_user_data()
        self._extract_info_board()

    def _extract_image(self):
        img_tag = self.soup.select_one('img[src*="https://my.tiu.edu.iq/myresim/"]')
        if img_tag:
            self.image = img_tag.get("src")

    def _extract_user_data(self):
        labels = {
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

        table = self.soup.find('table')
        if table:
            for row in table.find_all('tr'):
                columns = row.find_all('td')
                if len(columns) >= 2:
                    label = columns[0].text.strip(':')
                    if label in labels:
                        value = columns[1].text.strip()
                        setattr(self, labels[label], value)

    def _extract_info_board(self):
        table = self.soup.find('table')
        if table:
            for row in table.find_all('tr'):
                link = row.select_one('a.box[href^="https://my.tiu.edu.iq/pages/p401.php?id="]')
                if link:
                    self.info_board.append(link['href'])

class CourseData:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")
        self.data = self._extract_courses_data()

    def _extract_courses_data(self):
        course_data = []
        for row in self.soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 5:
                course_code, course_name, credits, grade = [cell.text.strip() for cell in cells[:4]]
                if course_code and course_name and credits and grade:
                    course_data.append({
                        'Course Code': course_code,
                        'Name of Course': course_name,
                        'Credits': credits,
                        'Grade': grade
                    })
        return course_data
