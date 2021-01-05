from src.reSolved import ReSolved
resolved = ReSolved('0fdd7a34-16ff-4ab7-a28b-566ff425c12c', '264f06d413e71211d66a4ff42b2076')
task = resolved.createTask('6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz', 'https://www.supremenewyork.com/checkout',  'reCaptcha', 'v2Invis', False, False, '')
taskID = task['data']['taskID']
token = resolved.getToken()
print(token)
