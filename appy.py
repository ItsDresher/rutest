#!/usr/bin/env python3
import os

# Define your buttons and their corresponding URLs
buttons = [
    {"label": "English", "url": "https://rochesteru.instructure.com/courses/2426"},
    {"label": "Vocation/Identity", "url": "https://rochesteru.instructure.com/courses/2652"},
    {"label": "Computing", "url": "https://rochesteru.instructure.com/courses/2582"},
    {"label": "Programming", "url": "https://rochesteru.instructure.com/courses/2590"},
    {"label": "Workshop", "url": "https://rochesteru.instructure.com/courses/2393"},
    {"label": "Information Systems", "url": "https://rochesteru.instructure.com/courses/2586"},
    {"label": "Dashboard", "url": "https://rochesteru.instructure.com/"},
    {"label": "RU Email", "url": "https://mail.google.com/mail/u/0/#inbox"},
    {"label": "Button 9", "url": "https://example9.com"},
    {"label": "Button 10", "url": "https://example10.com"},
]

# ASCII art
ascii_art = """
        *%#################################%/.             .&&&&&&&&&&&&&&&@,               
               ##########################################/           ,&&&&&&&&&&&&&&&%              
               #############################################.          &&&&&&&&&&&&&&&              
               ###############################################          @&&&&&&&&&&&&&              
               ################################################.         &&&&&&&&&&&&&              
               #################################################         (&&&&&&&&&&&&              
               #################################################*        ,&&&&&&&&&&&&              
               #################################################/        ,&&&&&&&&&&&&              
               #################################################         /&&&&&&&&&&&&              
               ################################################*         @&&&&&&&&&&&&              
               ###############################################*         &&&&&&&&&&&&&&              
               ##############################################          %&&&&&&&&&&&&&&              
               ###########################################,           &&&&&&&&&&&&&&&&              
               #######################################*             %&&&&&&&&&&&&&&&&&              
               #####################%                             %&&&&&&&&&&&&&&&&&&&              
               ########################*                       (&&&&&&&&&&&&&&&&&&&&&&              
               ###########################                 *@&&&&&&&&&&&&&&&&&&&&&&&&&              
               #############################*            %&&&&&&&&&&&&&&&&&&&&&&&&&&&%              
               (###############################            ,&&&&&&&&&&&&&&&&&&&&&&&&&*              
                #################################*            #&&&&&&&&&&&&&&&&&&&&&@               
                ,##################################%            .&&&&&&&&&&&&&&&&&&&                
                 (####################################*            #&&&&&&&&&&&&&&&/                
                  (#####################################%            .&&&&&&&&&&&&(                 
                   (#######################################*            %&&&&&&&&*                  
                     #########################################            ,&&&&&                    
                      /#########################################*            %*                     
                        *##########################################                                 
                           ##########################################*                              
                              *######################################%,                             
                                   /#############################*                                  
                                            .,*(#####/*,   
"""

def main():
    while True:
        os.system("clear")  # Clear the terminal screen

        # Display the ASCII art
        print(ascii_art)

        # Display buttons
        for idx, button in enumerate(buttons, start=1):
            print(f"   {idx}. {button['label']}")

        print("""
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃ Enter the number of the button to   ┃
┃ open the corresponding link, or    ┃
┃ Ctrl+C to exit.                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

        # Get user input
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(buttons):
                url = buttons[choice - 1]["url"]
                os.system(f"firefox {url} &")
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
