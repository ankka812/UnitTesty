import pytest
from unittest.mock import patch, mock_open
from task1 import add_student, remove_student, export_students, check_students, import_students


class Test:

    def test_add_student(self):
        # Given
        file_lista_studentow = "students.txt"
        students_list = {}

        with patch("builtins.input", return_value="Ola Nowak"):
            # When
            got = add_student(students_list, file_lista_studentow)

        # Then
        want = {"Ola Nowak": True}
        assert got == want

    def test_remove_student(self):
        # Given
        file_lista_studentow = "students.txt"
        students_list = {"Ola Nowak": True, "Natalia Nowak": True}

        with patch("builtins.input", return_value="Ola Nowak"):
            # When
            remove_student(file_lista_studentow, students_list)

        # Then
        got = students_list
        want = {"Natalia Nowak": True}
        assert got == want

    def test_check_students(self):
        # Given
        students_list = {"Ola Nowak": True, "Natalia Nowak": False}

        with patch("builtins.input", side_effect=["T", "T"]):
            # When
            check_students(students_list)

        # Then
        got = students_list
        want = {"Ola Nowak": True, "Natalia Nowak": True}
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
        mock_file().write.assert_any_call("Ola Nowak                 - nieobecny\n")
        mock_file().write.assert_any_call("Natalia Nowak             - obecny\n")

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
