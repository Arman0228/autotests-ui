from pathlib import Path

import pytest
from playwright.sync_api import Page

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self,courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self,courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", max_score="0", min_score="0", description="", estimated_time=""
        )

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright",
            estimated_time="2 weeks"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

        def test_edit_course(
                self,
                page: Page,
                courses_list_page: CoursesListPage,
                create_course_page: CreateCoursePage
        ):
            # Test data
            original_data = {
                "title": "Playwright Course",
                "max_score": "100",
                "min_score": "50",
                "description": "Original course about Playwright",
                "estimated_time": "2 weeks"
            }

            edited_data = {
                "title": "Advanced Playwright",
                "max_score": "90",
                "min_score": "60",
                "description": "Updated advanced Playwright course",
                "estimated_time": "3 weeks"
            }

            # Path to test image
            image_path = str(Path(__file__).parent / "testdata/files/image.png")

            # Step 1: Create initial course
            create_course_page.visit(
                "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
            create_course_page.create_course_toolbar_view.check_visible()

            # Upload image and fill form
            create_course_page.image_upload_widget.upload_preview_image(image_path)
            create_course_page.create_course_form.fill(**original_data)

            # Verify create button is enabled before clicking
            create_course_page.create_course_toolbar_view.create_course_button.check_enabled()
            create_course_page.create_course_toolbar_view.click_create_course_button()

            # Step 2: Verify course was created
            courses_list_page.course_view.check_visible(
                index=0,
                title=original_data["title"],
                max_score=original_data["max_score"],
                min_score=original_data["min_score"],
                estimated_time=original_data["estimated_time"]
            )

            # Step 3: Open edit form through course menu
            courses_list_page.course_view.menu.open_menu(index=0)
            courses_list_page.course_view.menu.click_edit_option()

            # Step 4: Edit course
            create_course_page.create_course_form.check_visible(
                title=original_data["title"],
                max_score=original_data["max_score"],
                min_score=original_data["min_score"],
                description=original_data["description"],
                estimated_time=original_data["estimated_time"]
            )

            create_course_page.create_course_form.fill(**edited_data)

            # Verify update button is enabled before clicking
            create_course_page.create_course_toolbar_view.create_course_button.check_enabled()
            create_course_page.create_course_toolbar_view.click_create_course_button()

            # Step 5: Verify changes
            courses_list_page.course_view.check_visible(
                index=0,
                title=edited_data["title"],
                max_score=edited_data["max_score"],
                min_score=edited_data["min_score"],
                estimated_time=edited_data["estimated_time"]
            )

    def test_edit_course(
            self,
            page: Page,
            courses_list_page: CoursesListPage,
            create_course_page: CreateCoursePage
    ):
        # Test data
        original_data = {
            "title": "Playwright Course",
            "max_score": "100",
            "min_score": "50",
            "description": "Original course about Playwright",
            "estimated_time": "2 weeks"
        }

        edited_data = {
            "title": "Advanced Playwright",
            "max_score": "90",
            "min_score": "60",
            "description": "Updated advanced Playwright course",
            "estimated_time": "3 weeks"
        }

        # Path to test image
        image_path = str(Path(__file__).parent / "testdata/files/image.png")

        # Step 1: Create initial course
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view.check_visible()

        # Upload image and fill form
        create_course_page.image_upload_widget.upload_preview_image(image_path)
        create_course_page.create_course_form.fill(**original_data)

        # Verify create button is enabled before clicking
        create_course_page.create_course_toolbar_view.create_course_button.check_enabled()
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Step 2: Verify course was created
        courses_list_page.course_view.check_visible(
            index=0,
            title=original_data["title"],
            max_score=original_data["max_score"],
            min_score=original_data["min_score"],
            estimated_time=original_data["estimated_time"]
        )

        # Step 3: Open edit form through course menu
        courses_list_page.course_view.menu.open_menu(index=0)
        courses_list_page.course_view.menu.click_edit_option()

        # Step 4: Edit course
        create_course_page.create_course_form.check_visible(
            title=original_data["title"],
            max_score=original_data["max_score"],
            min_score=original_data["min_score"],
            description=original_data["description"],
            estimated_time=original_data["estimated_time"]
        )

        create_course_page.create_course_form.fill(**edited_data)

        # Verify update button is enabled before clicking
        create_course_page.create_course_toolbar_view.create_course_button.check_enabled()
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Step 5: Verify changes
        courses_list_page.course_view.check_visible(
            index=0,
            title=edited_data["title"],
            max_score=edited_data["max_score"],
            min_score=edited_data["min_score"],
            estimated_time=edited_data["estimated_time"]
        )


