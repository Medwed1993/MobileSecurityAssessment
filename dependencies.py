import subprocess # pip3 install subprocess32
import os # pip3 install os0
import requests # pip3 install requests


class Dep_installer():
	def folder_user(self):
		self.user = os.getlogin() # username
		subprocess.call("apt update", shell = True) # update packages

	def python_modules(self):
		# install modules for python script
		subprocess.call("pip3 install requests", shell = True) # install module requests
		subprocess.call("pip3 install json2html", shell = True) # install module json2html
		subprocess.call("pip3 install requests_toolbelt", shell = True) # install module requests_toolbelt
		subprocess.call("pip3 install os0", shell = True) # install module os
		subprocess.call("pip3 install colorama", shell = True) # install module colorama
		subprocess.call("pip3 install pyfiglet", shell = True) # install module pyfiglet

	def docker(self):		
		# install docker
		subprocess.call("apt install apt-transport-https ca-certificates curl software-properties-common", shell = True)
		subprocess.call("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -", shell = True)
		subprocess.call("add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'", shell = True)
		subprocess.call("apt update", shell = True)
		subprocess.call("apt-cache policy docker-ce", shell = True)
		subprocess.call("apt install docker-ce", shell = True)
		subprocess.call(f"usermod -aG docker {self.user}", shell = True)

	def adb(self):	
		# install adb
		subprocess.call("apt-get install scrcpy", shell = True)

	def mobsf(self):
		# install mobsf
		subprocess.call("docker pull opensecurity/mobile-security-framework-mobsf", shell = True)

	def objection(self):
		# install objection
		subprocess.call("pip3 install -U objection", shell = True)

	def frida(self):
		# install frida on virtual machine
		url = "https://github.com/frida/frida/releases/download/14.2.13/frida-server-14.2.13-android-x86.xz" # install frida server
		response = requests.get(url).content

		with open(f"/home/{self.user}/frida-server-14.2.13-android-x86.xz", "wb") as file: # write frida server
			file.write(response)

		url = "https://github.com/frida/frida/releases/download/14.2.13/frida-inject-14.2.13-android-x86.xz" # install frida inject
		response = requests.get(url).content

		with open(f"/home/{self.user}/frida-inject-14.2.13-android-x86.xz", "wb") as file: # write frida inject
			file.write(response)

		subprocess.call(f"unxz /home/{self.user}/frida-server-14.2.13-android-x86.xz", shell = True) # extract frida server
		subprocess.call(f"unxz /home/{self.user}/frida-inject-14.2.13-android-x86.xz", shell = True) # extract frida inject

		subprocess.call(f"adb push /home/{self.user}/frida-server-14.2.13-android-x86 /data/local/tmp", shell = True) # install frida server on virtual machine
		subprocess.call(f"adb push /home/{self.user}/frida-inject-14.2.13-android-x86 /data/local/tmp", shell = True) # install frida inject on virtual machine

	def run(self):
		self.folder_user()
		self.python_modules()
		self.docker()
		self.adb()
		self.mobsf()
		self.objection()
		self.frida()

if __name__ == '__main__':
	dep_installer = Dep_installer()
	dep_installer.run()