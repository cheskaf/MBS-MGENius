# Landing Page
LANDING_PAGE = ""

# Admin
ADMIN_LOGIN = "admin/login"
ADMIN_LOGOUT = "admin/logout"
ADMIN_DASHBOARD = "admin"

# Modules
MODULE_LIST = "admin/webinars?type=course",
MODULE_LIST_PENDING = "admin/webinars?type=course&filter=pending"
MODULE_LIST_PUBLISHED = "/admin/webinars?type=course&filter=published"
MODULE_LIST_UNPUBLISHED = "admin/webinars?type=course&filter=unpublished"
MODULE_CREATE = "admin/webinars/create",
MODULE_EDIT = "admin/webinars/{id}/edit",
MODULE_EMPLOYEES = "admin/webinars/{id}/students",
MODULE_SEND_NOTIFICATION = "admin/webinars/{id}/sendNotification",
MODULE_QUIZZES = "admin/quizzes/create/{id}",
MODULE_QUIZ_RESULTS = "admin/quizzes/{id}",
MODULE_QUIZ_ANSWERS = "public/admin/quizzes/{quiz_id}/{attempt_id}/view",

MODULE_PREVIEW = "course/{slug}",
MODULE_LEARNING_PAGE = "course/learning/{slug}"

# Categories
CATEGORY_LIST = "admin/categories"
CATEGORY_CREATE = "admin/categories/create"
CATEGORY_EDIT = "admin/categories/{id}/edit"

# Users
ADMIN_LIST = "admin/staffs"
EMPLOYEE_LIST = "admin/students"
TRAINER_LIST = "admin/instructors"
CREATE_USER = "admin/users/create"
EDIT_USER = "admin/users/{id}/edit"
INDIVIDUAL_REPORT = "admin/users/badges/{id}"
ALL_EMPLOYEES_REPORT = "public/admin/viewall"
USER_ROLES = "admin/roles"

# Groups
GROUP_LIST = "admin/users/groups"
GROUP_CREATE = "admin/users/groups/create"
GROUP_EDIT = "admin/users/groups/{id}/edit"

# Notifications
NOTIFICATIONS_RECEIVED = "public/admin/notifications"
NOTIFICATIONS_POSTED = "admin/notifications/posted"
SEND_NOTIFICATION = "admin/notifications/send"

# Settings
CHANGE_PASSWORD = "admin/users/{id}/editPassword"

# Employee
EMPLOYEE_LOGIN = "login"
EMPLOYEE_LOGOUT = "logout"
EMPLOYEE_DASHBOARD = "panel"

# Notifications
EMPLOYEE_NOTIFICATIONS = "panel/notifications"

# Modules
EMPLOYEE_MODULES_LIST = "panel/webinars/purchases"
EMPLOYEE_MODULE_PREVIEW = "course/{slug}"
EMPLOYEE_MODULE_LEARNING_PAGE = "course/learning/{slug}"

# Quizzes
EMPLOYEE_QUIZ_TAKING = "panel/quizzes/{id}/start"
EMPLOYEE_QUIZ_STATUS = "panel/quizzes/{id}/status"
EMPLOYEE_QUIZ_RESULTS = "panel/quizzes/my-results"

# Settings
EMPLOYEE_STEP_1 = "panel/setting"
EMPLOYEE_STEP_2 = "panel/setting/step/2"
EMPLOYEE_STEP_3 = "panel/setting/step/3"
EMPLOYEE_STEP_4 = "panel/setting/step/4"
EMPLOYEE_STEP_5 = "panel/setting/step/5"