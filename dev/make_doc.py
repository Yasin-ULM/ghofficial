'''
Python script to make datalists (hints) for the editor,
copy/paste the output


<span class='api_def'>len</span>(s)
<div class='api_doc'>Return the length (the number of items) of an object.</div>
'''

# look for public API
is_doc=False
with open('../index.html') as sourcecode:
    for line in sourcecode.readlines():
        if line.strip().startswith('class'):
            print("<div class='api_doc'> class <span class='api_def'>"+line.strip().strip('class')+'</span></div>')

        if line.strip().startswith('def'):
            is_doc=True
            name, args = line.strip().strip('def').strip('):').strip().split('(')
            final_args = []
            for arg in (i.strip() for i in args.split(',')):
                if '=' in arg:
                     arg = arg.replace('=', "=<span class='api_num'>")
                     arg+='</span>'
                final_args.append(arg)  
            print(f'''<span class='api_def'>{name}</span>( {", ".join(final_args)} ):''')          
        elif is_doc:
            if line.strip() == "'''":
                print("</div>") 
                is_doc=False
            else:    
                if line.strip().startswith("'''"):
                    print("<div class='api_doc'>") 
                
                print( line.strip().strip("'''") )    
                
                if line.strip().endswith("'''"):    
                    print("</div>") 
                    is_doc=False

