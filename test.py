import errno, os, stat, shutil

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

PATH = os.path.join(os.curdir, 'test')
print(PATH) #./data

for file in os.listdir():
	shutil.rmtree(file, ignore_errors=False, onerror=handleRemoveReadonly)

print('Database Erased...!')
print('''

--create new Database using command,
	python3 run.py record''')