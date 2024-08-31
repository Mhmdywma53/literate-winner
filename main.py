from flet import *

def main(page: Page):
    page.title = "تطبيق متعدد الصفحات"

    def show_login():
        page.clean()
        page.add(
            Column([
                Text("تسجيل الدخول", size=30),
                TextField(label="البريد الإلكتروني"),
                TextField(label="كلمة المرور", password=True),
                Row([
                    ElevatedButton("تسجيل الدخول", on_click=lambda _: show_home()),
                    ElevatedButton("إنشاء حساب", on_click=lambda _: show_signup())
                ])
            ])
        )

    def show_signup():
        page.clean()
        page.add(
            Column([
                Text("إنشاء حساب", size=30),
                TextField(label="البريد الإلكتروني"),
                TextField(label="كلمة المرور", password=True),
                Row([
                    ElevatedButton("إنشاء حساب", on_click=lambda _: show_login()),
                    ElevatedButton("عودة إلى تسجيل الدخول", on_click=lambda _: show_login())
                ])
            ])
        )

    def show_home():
        page.clean()
        page.add(
            Column([
                Text("الصفحة الرئيسية", size=30),
                Text("مرحباً بك في التطبيق!"),
                ElevatedButton("تسجيل الخروج", on_click=lambda _: show_login())
            ])
        )

    show_login()

app(target=main)
