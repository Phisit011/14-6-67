from kivy.uix.gesturesurface import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

KV = '''
ScreenManager:
    MenuScreen:
    RegisterScreen:

<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        md_bg_color: 203,171,228
        Image:
            source: '1.jpg'
            size_hint: (1, 0.5)

        MDRaisedButton:
            text: 'เข้าสู่ระบบ'
            md_bg_color: (1, 1, 0, 1)
            font_size: '20sp'
            size_hint: (1, 0.1)
            on_release: app.switch_to_register_screen()
            font_name: 'tahoma'

        MDRaisedButton:
            text: 'ลงทะเบียนใหม่'
            md_bg_color: (0.5, 0, 0.5, 1)
            font_size: '20sp'
            size_hint: (1, 0.1)
            on_release: app.switch_to_register_screen()
            font_name: 'tahoma'

        MDRaisedButton:
            text: 'For Foreigner'
            md_bg_color: (0, 0.5, 1, 1)
            font_size: '20sp'
            size_hint: (1, 0.1)
            on_release: app.switch_to_register_screen()

        Image:
            source: 'Line.png'
            size_hint: (1, 0.1)
            size: (50, 50)

        MDLabel:
            text: 'Copyrights © สงวนลิขสิทธิ์ © 2021\\nกรมการขนส่งทางบก | dlt.go.th'
            font_size: '12sp'
            size_hint: (1, 0.1)
            halign: 'center'
            font_name: 'tahoma'

<RegisterScreen>:
    name: 'register'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10

        MDTextField:
            id: citizen_id
            hint_text: 'รหัสประชาชน'
            size_hint_x: None
            width: 300
            pos_hint: {'center_x': 0.5}
            font_name: 'tahoma'

        MDTextField:
            id: phone_number
            hint_text: 'เบอร์โทร'
            size_hint_x: None
            width: 300
            pos_hint: {'center_x': 0.5}
            font_name: 'tahoma'

        MDTextField:
            hint_text: 'ระบุอีเมล'
            size_hint_x: None
            width: 300
            pos_hint: {'center_x': 0.5}
            font_name: 'tahoma'

        MDTextField:
            hint_text: 'Input 4'
            size_hint_x: None
            width: 300
            pos_hint: {'center_x': 0.5}
            font_name: 'tahoma'

        MDRaisedButton:
            text: 'ดำเนินการต่อ'
            pos_hint: {'center_x': 0.5}
            on_release: app.process_inputs()
            font_name: 'tahoma'
        MDRaisedButton:
            text: 'Go Back'
            pos_hint: {'center_x': 0.5}
            on_release: app.switch_to_menu_screen()
            font_name: 'tahoma'
'''

class MenuScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class MyApp(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def switch_to_register_screen(self):
        self.root.current = 'register'

    def switch_to_menu_screen(self):
        self.root.current = 'menu'

    def process_inputs(self):
        register_screen = self.root.get_screen('register')
        citizen_id = register_screen.ids.citizen_id.text
        phone_number = register_screen.ids.phone_number.text

        if len(citizen_id) != 13 or not citizen_id.isdigit():
            self.show_dialog("รหัสประชาชนไม่ถูกต้อง", "กรุณากรอกรหัสประชาชนให้ครบ 13 หลัก")
        elif len(phone_number) != 10 or not phone_number.isdigit():
            self.show_dialog("เบอร์โทรไม่ถูกต้อง", "กรุณากรอกเบอร์โทรให้ครบ 10 หลัก")
        else:
            self.show_dialog("ข้อมูลถูกต้อง", "รหัสประชาชนและเบอร์โทรถูกต้อง")

    def show_dialog(self, title, text):
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=text,
                size_hint=(0.8, 1),
                buttons=[
                    MDRaisedButton(
                        text="ตกลง",
                        on_release=lambda x: self.dialog.dismiss()
                    
                    )
                ],
            )
        else:
            self.dialog.title = title
            self.dialog.text = text

        self.dialog.open()

if __name__ == '__main__':
    MyApp().run()