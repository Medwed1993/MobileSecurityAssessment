import subprocess


class Result():
	def clear(self, command):
		# remove extra text and run command
		result = str(subprocess.check_output(f"objection --gadget com.middleware.winbank run '{command}'", shell = True, universal_newlines = True))
		result = result[330:-52]
		print(result)

	def run(self):
		# run commands
		self.clear("android clipboard monitor")
		self.clear("android deoptimize")
		self.clear("android heap print methods")
		self.clear("android heap print fields")
		# self.clear("android heap execute --return-string")
		self.clear("android keystore list")
		self.clear("android keystore watch")
		self.clear("android root simulate")
		self.clear("android root disable")
		self.clear("android shell_exec cat /etc/passwd")
		self.clear("android sslpinning disable --quiet")
		self.clear("android sslpinning disable")

if __name__ == '__main__':
	result = Result()
	result.run()