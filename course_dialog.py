"""
===========================
@Time : 2024/9/15 下午6:39
@Author : Entropy.Xu
@File : course_dialog.py
@Software: PyCharm
============================
"""
# course_dialog.py

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class CourseDialog(QDialog):
    def __init__(self, parent=None, day=None, period=None, course_data=None):
        super().__init__(parent)
        self.setWindowTitle("编辑课程" if course_data else "添加课程")
        self.resize(400, 300)

        self.day = day
        self.period = period
        self.course_data = course_data

        layout = QVBoxLayout()

        # 课程名称
        name_label = QLabel("课程名称:")
        self.name_edit = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)

        # 上课地点
        location_label = QLabel("上课地点:")
        self.location_edit = QLineEdit()
        layout.addWidget(location_label)
        layout.addWidget(self.location_edit)

        # 重复周数
        weeks_label = QLabel("周数 (如: 1-16 或 1,3,5):")
        self.weeks_edit = QLineEdit()
        layout.addWidget(weeks_label)
        layout.addWidget(self.weeks_edit)

        # 课程老师
        teacher_label = QLabel("课程老师:")
        self.teacher_edit = QLineEdit()
        layout.addWidget(teacher_label)
        layout.addWidget(self.teacher_edit)

        # 按钮
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # 连接信号
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # 如果是编辑模式，填充现有数据
        if course_data:
            self.populate_fields()

    def populate_fields(self):
        """填充现有课程数据"""
        self.name_edit.setText(self.course_data['name'])
        self.location_edit.setText(self.course_data['location'])
        self.weeks_edit.setText(format_weeks(self.course_data['weeks']))
        self.teacher_edit.setText(self.course_data.get('teacher', ''))

    def get_data(self):
        return {
            'name': self.name_edit.text(),
            'location': self.location_edit.text(),
            'weeks': self.weeks_edit.text(),
            'teacher': self.teacher_edit.text(),
            'start_time': self.course_data['start_time'] if self.course_data else None,
            'end_time': self.course_data['end_time'] if self.course_data else None
        }

def format_weeks(weeks):
    """将周数列表格式化为字符串"""
    if not weeks:
        return ""
    weeks = sorted(weeks)
    result = []
    start = weeks[0]
    prev = start
    
    for week in weeks[1:]:
        if week != prev + 1:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = week
        prev = week
    
    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")
    
    return ",".join(result)
