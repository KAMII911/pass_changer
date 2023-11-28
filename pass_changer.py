import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    import ps
    ps.run()
elif "32" in a:
    import ps32
    ps32.run()