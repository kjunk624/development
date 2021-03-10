import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog

root = Tk()
root.title("PhotoManager")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택 하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),\
        initialdir=r"D:\Python\PyExcise\pygame_project\images") 
        # 최초에 D:/...경로를 보여줌 'r'을 사요하면 이후의 모든 것을 string으로 인식
    
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)  

# 선택 삭제
def del_file():
    #print(list_file.curselection())

    for index in reversed(list_file.curselection()): 
        # 뒤에서 부터 지워야 앞에서 인덱스가 다시 0이 되어 엉뚱한 것이 지워지는 일이 없게 하기 위함
        list_file.delete(index)

# 저장 경로(폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None : # 사용자가 취소를 누를 때
        return
    #print(folder_selected)
    txt_dest_path.delete(0,END) # 기존 것은 지워줌(entry:0,END / text:"0.1", END)
    txt_dest_path.insert(0,folder_selected)

# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로 넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일몰록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return  # 더이상 진행 하지 못하게...
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 추가하세요")
        return


#파일 프레임(파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, background="yellow", padx=5, pady=5, width=12, text="화일 추가",command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, background="blue", padx=5, pady=5, width=12,text="선택 삭제",command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollar = Scrollbar(list_frame)
scrollar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollar.config(command=list_file.yview)


#저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=6) # Entry높이 증가 


btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right")

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack()

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left")

# 가로 넓이 콤보
opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left")

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left")

# 3. 파일 포맷 옵션
# 파일 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left")

# 파일 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

# 진행 상황 progress Bar
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x")

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right")



root.resizable(False,False) #x(너비),y(높이) 값 변경 불가(창 변경 불가)
root.mainloop()
