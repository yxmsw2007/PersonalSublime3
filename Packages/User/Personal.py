import sublime
import sublime_plugin
import datetime
import sys
import os
		
class FileHeaderCommentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",
            {
                "contents": "/************************************************************""\n"
                " * @FileName   : ${1:FileName}\n"
                " * @Author     : ${2:yexiaoming} \n"
				" * @Email      : ${3:xiaoming.ye@cnlaunch.com} \n"
				" * @Vsersion   : ${4:V1.0.0} \n"
                " * @DateTime   : ${5:%s}"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                " * @Description: ${6:Description}\n"
                " ************************************************************/"
            }
        )
		
class FileHeaderCommentsCNCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",
            {
                "contents": "/************************************************************""\n"
                " * @文件名: ${1:FileName}\n"
                " * @作  者: ${2:yexiaoming} \n"
				" * @邮  箱: ${3:xiaoming.ye@cnlaunch.com} \n"
				" * @版  本: ${4:V1.0.0} \n"
                " * @日  期: ${5:%s}"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                " * @描  述: ${6:Description}\n"
                " ************************************************************/"
            }
        )


		
