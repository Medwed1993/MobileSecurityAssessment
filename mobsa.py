import json
import requests # pip3 install requests
from json2html import * # pip3 install json2html
from requests_toolbelt.multipart.encoder import MultipartEncoder # pip3 install requests_toolbelt
import os # pip3 install os0
from colorama import init, Fore # pip3 install colorama
import subprocess # pip3 install subprocess32
from bs4 import BeautifulSoup # pip3 install bs4
import threading
import sys
import re


class Json_from_mobsf:
    def banner(self):
        init(autoreset = True)
        print("############################")
        print("# MobileSecurityAssessment #")
        print("#         1.0.1            #")
        print("############################")

    def linux(self):
        self.user = os.getlogin()
        init(autoreset = True)

        def adb():
            apk_file = sys.argv[1]
            print(Fore.GREEN + "[+] Working...")
            subprocess.check_output(f"adb install {apk_file}", shell = True)
            subprocess.check_output(f"adb pull /data/app /home/{self.user}/Desktop/app", shell = True)
            apk = os.listdir(f"/home/{self.user}/Desktop/app")
            self.apk_f = apk[0]

        def mobsf():
            subprocess.check_output("docker run -d -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest", shell = True)

        def pars_api_key():
            while True:
                try:
                    requests.get("http://0.0.0.0:8000")
                    break
                except:
                    pass

            response = requests.get("http://0.0.0.0:8000/api_docs").text
            soup = BeautifulSoup(response, "lxml")
            soup_1 = soup.find("div", class_ = "card-body")
            self.api_key = soup_1.find("code").text

        def get_json():
            server = "http://0.0.0.0:8000" # "http://127.0.0.1:8000"
            file = f"/home/{self.user}/Desktop/app/{self.apk_f}/base.apk"

            def upload():
                """Upload File"""
                print(Fore.GREEN + "[+] Uploading...")
                multipart_data = MultipartEncoder(fields = {"file": (file, open(file, "rb"), "application/octet-stream")})
                headers = {"Content-Type": multipart_data.content_type, "Authorization": self.api_key}
                response = requests.post(server + "/api/v1/upload", data = multipart_data, headers = headers)
                return response.text

            def scan(data):
                """Scan the file"""
                print(Fore.GREEN + "[+] Scanning...")
                post_dict = json.loads(data)
                headers = {"Authorization": self.api_key}
                response = requests.post(server + "/api/v1/scan", data = post_dict, headers = headers)

            def json_resp(data):
                """Generate JSON Report"""
                print(Fore.GREEN + "[+] Generate JSON report")
                headers = {"Authorization": self.api_key}
                data = {"hash": json.loads(data)["hash"]}
                response = requests.post(server + "/api/v1/report_json", data = data, headers = headers).text
                with open(f"/home/{self.user}/Desktop/data.json", "w", encoding = "utf-8") as flip:
                    flip.write(response)

            def delete(data):
                """Delete Scan Result"""
                print(Fore.GREEN + "[+] Deleting...")
                headers = {"Authorization": self.api_key}
                data = {"hash": json.loads(data)["hash"]}
                response = requests.post(server + "/api/v1/delete_scan", data = data, headers = headers)

            resp = upload()
            scan(resp)
            json_resp(resp)
            delete(resp)

        def docker():
            res = subprocess.check_output("docker ps", shell = True).decode("utf-8")
            con_id = re.search(r"(\b[A-Fa-f0-9]{12}\b)", res).group(0)
            subprocess.check_output(f"docker kill {con_id}", shell = True)


        def write_json():
            with open(f"/home/{self.user}/Desktop/data.json", "r", encoding = "utf-8") as file:
                data_json = json.load(file)

            manifest_analysis = data_json["manifest_analysis"]
            permissions = data_json["permissions"]
            code_analysis = data_json["code_analysis"]
            domains = data_json["domains"]
            certificate_analysis = data_json["certificate_analysis"]

            with open(f"/home/{self.user}/Desktop/information.json", "w", encoding = "utf-8") as file:
                file.write("""{
""")
                file.write('"manifest_analysis":')
                json.dump(manifest_analysis, file, indent = 4)

                file.write(''',
"permissions":''')
                json.dump(permissions, file, indent = 4)

                file.write(''',
"code_analysis":''')
                json.dump(code_analysis, file, indent = 4)

                file.write(''',
"domains":''')
                json.dump(domains, file, indent = 4)

                file.write(''',
"certificate_analysis":''')
                json.dump(certificate_analysis, file, indent = 4)
                file.write("""
}""")

        def html():
            with open(f"/home/{self.user}/Desktop/information.json", "r", encoding = "utf-8") as file:
                data_html = json.load(file)

            html = json2html.convert(json = data_html)

            with open(f"/home/{self.user}/Desktop/data.html", "w", encoding = "utf-8") as file:
                file.write(html)

            print(Fore.GREEN + "Success, file on Desktop")

        adb()
        mobsf()
        pars_api_key()
        get_json()
        docker()
        write_json()
        html()
        
    def run(self):
        self.banner()
        self.linux()


class Json_from_android():
    def work_with_files(self):
        self.user = os.getlogin() # username

        os.mkdir(f"/home/{self.user}/Desktop/result_from_android") # create folder
        os.mkdir(f"/home/{self.user}/Desktop/result_from_android/result_json") # create folder

        subprocess.check_output(f"adb pull '/data/user/0/com.middleware.winbank/files/' '/home/{self.user}/Desktop/result_from_android/files'", shell = True) # pars json
        subprocess.check_output(f"adb pull '/data/user/0/com.middleware.winbank/files/.com.google.firebase.crashlytics' '/home/{self.user}/Desktop/result_from_android/files_1'", shell = True) # pars json
        
        dire = os.listdir(f"/home/{self.user}/Desktop/result_from_android/files_1/report-persistence/sessions") # find directory
        self.direc = dire[0]
        os.chdir(f"/home/{self.user}/Desktop/result_from_android/files_1/report-persistence/sessions/{self.direc}") # enter in directory
        os.renames("report", "report.json") # rename file

        dire_1 = os.listdir(f"/home/{self.user}/Desktop/result_from_android/files") # find directory
        self.direc_1 = dire_1[0]

    def read_and_save_files(self):
        with open(f"/home/{self.user}/Desktop/result_from_android/files_1/com.crashlytics.settings.json", "r", encoding = "utf-8") as file: # read json file
            data = json.load(file)

        with open(f"/home/{self.user}/Desktop/result_from_android/result_json/com.crashlytics.settings.json", "w", encoding = "utf-8") as file: # write json file
            json.dump(data, file, indent = 4)

        with open(f"/home/{self.user}/Desktop/result_from_android/files_1/report-persistence/sessions/{self.direc}/report.json", "r", encoding = "utf-8") as file: # read json file
            data = json.load(file)

        with open(f"/home/{self.user}/Desktop/result_from_android/result_json/report.json", "w", encoding = "utf-8") as file: # write json file
            json.dump(data, file, indent = 4)

        with open(f"/home/{self.user}/Desktop/result_from_android/files/{self.direc_1}", "r", encoding = "utf-8") as file: # read json file
            data = json.load(file)

        with open(f"/home/{self.user}/Desktop/result_from_android/result_json/{self.direc_1}.json", "w", encoding = "utf-8") as file: # write json file
            json.dump(data, file, indent = 4)

        init(autoreset = True)

        print(Fore.GREEN + f"Succes path to files /home/{self.user}/Desktop/result_from_android/result_json")

    def server(self):
        home = os.getcwd()
        subprocess.call(f"python3 {home}/server.py", shell = True)

    def run(self):
        self.work_with_files()
        self.read_and_save_files()
        self.server()
    

if __name__ == '__main__':
    json_from_mobsf = Json_from_mobsf()
    json_from_mobsf.run()

    json_from_android = Json_from_android()
    json_from_android.run()
