import win10toast
class toast:
    def __init__(self):
        self.toast=win10toast.ToastNotifier()
    def message(self,title,message,return_time=0,icon="main.ico"):
        try:
            result=self.toast.show_toast(title,
                                         message,
                                         icon_path=icon,
                                         duration=return_time
                                         )
        except TypeError:
            return result
