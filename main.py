from flet import *
from flet_core import*
from pdf2docx import Converter
from random import sample
import os
v_theme = 0
v_conv=0
def main(page:Page):
    def theme_mode(e):
        global v_theme
        v_theme+=1
        if v_theme== 2:
            e.control.checked = page.theme_mode=ThemeMode.DARK
            page.appbar=AppBar(actions=[IconButton(icons.SUNNY,on_click=theme_mode)])
            page.update()
            v_theme-=2
        else:
            e.control.checked = page.theme_mode=ThemeMode.LIGHT 
            page.appbar=AppBar(actions=[IconButton(icons.DARK_MODE,on_click=theme_mode)])   
            page.update()  
    
    alert1=AlertDialog(content= Text("PDF لم يتم اختيار اي ملف",size=20,color=colors.RED_ACCENT))
    
    def on_result(e:FilePickerResultEvent):
        global v_conv
        if v_conv ==1 :
            v_conv -= 1
            page.clean()
            main_2()
            page.update()

        num1 ="0987654321"
        num2="0123456789"
        sum_num= num1+num2
        pdf_num=''.join(sample(sum_num,5))
   
        class Pdf:
            def pdf_to_docx(e):
                global v_conv
                try: 
                    t="\t"
                    pro=ProgressRing(color=colors.GREEN_ACCENT_700,width=100,height=100)
                    alert4=AlertDialog(modal=True,title=Text(f" {t*4}.... جاري التحويل ....",size=32,font_family="Adobe Arabic",color=colors.GREEN_700),
                                      actions=[pro],actions_alignment=MainAxisAlignment.CENTER)
                    page.open(alert4)
                    alert4.open=True
                    page.update()
        
                    conv=Converter(file_pdf)

                    if t_f.value== '':
                        #os.chdir(r"C:\\Users\\mwale\\Downloads")
                        os.makedirs((r"PDF To Word"),exist_ok=True)
                        conv.convert(rf"PDF To Word\PDF-Word_{pdf_num}.docx")
                        conv.close()
                        alert4.open=False
                    else:
                        #os.chdir(r"C:\\Users\\mwale\\Downloads")
                        os.makedirs((r"PDF To Word"),exist_ok=True)
                        conv.convert(rf"PDF To Word\{t_f.value}.docx")
                        conv.close()
                        alert4.open=False     
                    
                    alert2=AlertDialog(title=Text(f"{t*12}DONE",color=colors.GREEN_700),
                                      content=Icon(icons.DONE_SHARP,size=150,color=colors.GREEN_900))
                    page.open(alert2)
                    alert2.open=True
                    page.update()

                    if v_conv ==1 :
                        v_conv -= 1
                        page.clean()
                        main_2()
                        page.update()
                except :
                    alert4.open=False
                    alert3=AlertDialog(title=Text("صيغة الملف غير مدعومة",size=17,color=colors.RED_ACCENT),
                                       content=Text("\"PDF\"تاكد من ان الملف المختار بصيغة",size=15))
                    page.open(alert3)
                    alert3.open=True
                    
                    if v_conv ==1 :
                        v_conv -= 1
                        page.clean()
                        main_2()
                        page.update()
        if e.files is not None: 
            v_conv+=1
            for f in e.files:
                file_pdf=f.path
                l_1=Text("----------------------------------------------------------",color=colors.GREEN)
                t=Text(f.name,size=17,color=colors.RED)
                l_2=Text("----------------------------------------------------------",color=colors.GREEN)
                t_f=TextField(label=" الاسم المراد لملف word ",rtl=True,icon=icons.FILE_COPY,height=38)
                btn_1=ElevatedButton("docx التحويل الى",style=ButtonStyle(bgcolor=colors.BLUE,color="white",padding=17)
                    ,on_click=Pdf.pdf_to_docx)
                
        try:
                page.add(l_1,t,l_2,t_f,btn_1) 
                page.update() 
        except UnboundLocalError:
                page.open(alert1)
                alert1.open=True
                page.update()             
    ## window
    page.window.top=1
    page.window.left=960
    page.window.width=390
    page.window.height=740
    page.window.resizable=False
    page.window.title_bar_hidden=False
    page.horizontal_alignment='center'
    page.vertical_alignment=15
    page.theme_mode=ThemeMode.SYSTEM
    
    def main_2():
    # --- file picker -----
        file_picker=FilePicker(on_result=on_result)
        page.overlay.append(file_picker)

        # --- appbar ----
        page.appbar=AppBar(actions=[IconButton(icons.SUNNY,on_click=theme_mode)])

        # -- --- --- ---
        page.add(
        Text("PDF --> Word",size=33,font_family="Consolas"),
        Row([
        Icon(icons.PICTURE_AS_PDF_SHARP,size=120,color=colors.RED_ACCENT_700),
        Icon(icons.ARROW_RIGHT_ALT_ROUNDED,size=50,color=colors.GREEN),
        Image(src='assets/word.png',width=120)
        ],alignment=MainAxisAlignment.CENTER),
        ElevatedButton("PDF اختار ملف",style=ButtonStyle(bgcolor=colors.RED_ACCENT_700,color="white",padding=17),
        on_click=lambda _:file_picker.pick_files(allow_multiple=True)
        ))

        page.navigation_bar=CupertinoNavigationBar(
            destinations=[
            NavigationBarDestination(label="V . 0 . 0")]
        )
        page.update()
    main_2()    
app(main,assets_dir="assets/")    
