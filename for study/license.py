def main():
    import subprocess as subpro
    import os
    a=str(subpro.run(("wmic csproduct get uuid"),capture_output=True,check=False).stdout[41:-8])[2:-1]
    if os.path.exists("new_license.lc"):
        with open("new_license.lc","w+") as lic:
            lic.write(a)
    else:
        with open("new_license.lc","a+") as lic:
            lic.write(a)
main()
