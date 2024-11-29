import pytest
from unittest.mock import patch, mock_open
from datetime import datetime
from task1 import add_student, remove_student, export_students, check_students, import_students


class Test:

    def test_add_student(self):
        # Given
        file_list_of_students = "students.txt"
        students_list = {}

        with patch("builtins.input", return_value="Ola Nowak"):
            # When
            got = add_student(students_list, file_list_of_students)

        # Then
        want = {"Ola Nowak": True}
        assert got == want

    def test_add_existing_student(self):
        # Given
        file_list_of_students = "students.txt"
        students_list = {"Ola Nowak": True}

        with patch("builtins.input", return_value="Ola Nowak"):
            # When
            got = add_student(students_list, file_list_of_students)

        # Then
        want = {"Ola Nowak": True}
        assert got == want

    def test_remove_student(self):
        # Given
        file_list_of_students = "students.txt"
        students_list = {"Ola Nowak": True, "Natalia Nowak": True}

        with patch("builtins.input", return_value="Ola Nowak"):
            # When
            remove_student(file_list_of_students, students_list)

        # Then
        got = students_list
        want = {"Natalia Nowak": True}
        assert got == want

    def test_remove_nonexistent_student(self):
        # Given
        file_list_of_students = "students.txt"
        students_list = {"Natalia Nowak": True}

        with patch("builtins.input", return_value="Ola Nowak"):
            # When
            remove_student(file_list_of_students, students_list)

        # Then
        got = students_list
        want = {"Natalia Nowak": True}
        assert got == want

    def test_check_students(self):
        # Given
        students_list = {"Ola Nowak": True, "Natalia Nowak": False}

        with patch("builtins.input", side_effect=["Y", "Y"]):
            # When
            check_students(students_list)

        # Then
        got = students_list
        want = {"Ola Nowak": True, "Natalia Nowak": True}
        assert got == want

    def test_check_students_with_invalid_input(self):
        # Given
        students_list = {"Ola Nowak": True, "Natalia Nowak": False}

        with patch("builtins.input", side_effect=["X", "N"]):
            # When
            check_students(students_list)

        # Then
        got = students_list
        want = {"Ola Nowak": False, "Natalia Nowak": False}
        assert got == want

    def test_export_students(self):
        # Given
        students_list = {"Ola Nowak": False, "Natalia Nowak": True}
        mock_file = mock_open()

        with patch("builtins.open", mock_file):
            # When
            export_students("students.txt", students_list)

        # Then
        mock_file.assert_called_once_with("students.txt", "w")
        mock_file().write.assert_any_call("Ola Nowak                 - absent\n")
        mock_file().write.assert_any_call("Natalia Nowak             - present\n")

    def test_export_empty_student_list(self):
        # Given
        students_list = {}
        mock_file = mock_open()

        with patch("builtins.open", mock_file):
            # When
            export_students("students.txt", students_list)

        # Then
        mock_file.assert_called_once_with("students.txt", "w")
        mock_file().write.assert_called_with(f"{datetime.now()}\n")

    def test_import_students(self):
        # Given
        mock_file_content = "Ola Nowak,Natalia Nowak,\n"
        mock_file = mock_open(read_data=mock_file_content)

        with patch("builtins.open", mock_file):
            # When
            got = import_students("students.txt")

        # Then
        want = {"Ola Nowak": True, "Natalia Nowak": True}
        assert got == want

    def test_import_empty_file(self):
        # Given
        mock_file_content = ""
        mock_file = mock_open(read_data=mock_file_content)

        with patch("builtins.open", mock_file):
            # When
            got = import_students("students.txt")

        # Then
        want = {}
        assert got == want
