import base64
with open('frames/frame_0150.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
    
with open('c:/Users/Admin/.gemini/antigravity-ide/brain/c2b84cfc-8a15-417e-a660-73c5d942d051/scratch/test.html', 'w') as f:
    f.write(f'<img src="data:image/png;base64,{b64}" />')
