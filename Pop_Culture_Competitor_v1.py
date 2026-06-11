
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#

student_name   = 'Hamidullah Rezae' 
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
#--------------------------------------------------------------------#



#-----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            print("Warning - Request to server does not reveal client's true identity.")
            print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print(f"\nCannot find requested document '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print(f"\nAccess denied to document at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except URLError as message: # probably the wrong server address
        print(f"\nCannot access web server at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              f"the document at URL '{str(url)}'")
        print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL " + \
              f"'{url}' as '{char_set}' characters")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              f"the document from URL '{url}'")
        print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print(f"\nUnable to write to file '{target_filename}'")
            print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#
#
# Put your solution below.

# Create the main window
main_window = Tk()
# Your code goes here

# The title of the window
main_window.title('Pop Culture Competitors')

# Creating regular expression for extracting the title of the tv show
pattern1 = 'tbl-cell-name.*?\">([^<]+)'
# Creating regular expression for extracting the runtime of the tv show
pattern11 = '<td.class=\"pb-2.tbl-cell.tbl-cell-runtime.*?inline-block\">([^<]+)'
# Creating regular expression for extracting the title of animes
pattern2 = '<a href="[^"]+"[^>]*class="hoverinfo_trigger"[^>]*>([^<]+)</a>'
# Creating regular expression for extracting the scores of animes
pattern22 = r'<span class="text on score-label[^>]*>(\d+\.\d+)</span>'
# Creating regular expression for extracting the title of the songs
pattern3 =  r'data-title="([^"]+)"'
# Creating regular expression for extracting the artists
pattern33 =  r'ata-artist="([^\&"]+)"'

# The link to the first website
url1 = 'https://www.netflix.com/tudum/top10/'
# The link to the second website
url2 = 'https://myanimelist.net/topanime.php?type=airing'
# The link to the third website
url3 = 'https://www.officialcharts.com/charts/singles-chart/'

# Introducing a string variable that can store values for radiobuttons
# the value = 0 when no button is chosen 
select_button = StringVar(value = 0)

# Defining some helpful global variables
data_source = ''
ranking = ''
identifier = ''
data_property = ''

# Defining a function to update the radiobuttons
def update_status():

    global data_source

    # Getting the values of select_button and assigning it to selected_button
    selected_button = select_button.get()
    
    if selected_button == 'Button A':
        page1 = download(url = url1)
        
    elif selected_button == 'Button B':
        page2 = download(url = url2)
    else:
        page3 = download(url = url3)

# Creating functions for the button responsible for showing the top three items
# and saving them into the database

select_button = StringVar(value = 0)

def top_three():

    global data_source, identifier, data_property
    
    # Getting the values of select_button and assigning it to selected_button
    selected_button = select_button.get()
    
    if selected_button == 'Button A':
        # Code to catch the errors
        try:   
            page1 = download(url = url1)
            title = findall(pattern1, page1)
            runtime = findall(pattern11, page1)
            data_source = "US TV Guide's Trending TV Shows (Title and Runtime)"
            identifier = title
            data_property = runtime

            # Displaying the result as string in the output_text area
            output_text['text'] = f'''
    US TV Guide's Trending TV Shows (Title and Runtime):
    1. {title[0]}- {runtime[0]}
    2. {title[1]} - {runtime[1]}
    3. {title[2]} - {runtime[2]}
    '''
        except:
            output_text['text'] = 'Connection Failure: Connect to the Internet'
    elif selected_button == 'Button B':
        # Code to catch the errors
        try:
            page2 = download(url = url2)
            animes = findall(pattern2, page2)
            score= findall(pattern22, page2)
            data_source = 'Top Three Airing Animes on MyAnimeList (Title and Score)'
            identifier = animes
            data_property = score
            output_text['text'] = f'''
    Top Three Airing Animes on MyAnimeList (Title and Score):
    1. {animes[0]} - {score[0]}
    2. {animes[1]} - {score[1]}
    3. {animes[2]} - {score[2]}
    '''
        except:
            output_text['text'] = 'Connection Failure: Connect to the Internet'
            
    elif selected_button == 'Button C':
        # Code to catch the errors
        try:
            page3 = download(url = url3)
            songs = findall(pattern3, page3)
            artist = findall(pattern33, page3)
            data_source = 'Most popular songs on Official Charts (Artist and Song)'
            identifier = songs
            data_property = artist
            output_text['text'] = f'''
    Most popular songs on Official Charts (Artist and Song):
    1. {songs[0]} - {artist[0]}
    2. {songs[1]} - {artist[1]}
    3. {songs[2]} - {artist[2]}
    '''
        except:
            output_text['text'] = 'Connection Failure: Connect to the Internet'
    else:
        output_text['text'] = 'Please select an option first'

# Introducing a string variable that can store values for radiobuttons
# the value = 0 when no button is chosen    
select_button = StringVar(value = 0)

# Defining a function for the data source button 
def data_source():

    selected_button = select_button.get()
    # When the first button is selected, display the link for the first website
    if selected_button == 'Button A':
        try:
            urldisplay(url1)
        except:
            output_text['text'] = 'Failed Connection: Please check your connnection.'
    # When the second button is selected, display the link for the second website
    elif selected_button == 'Button B':
        try:
            urldisplay(url2)
        except:
            output_text['text'] = 'Failed Connection: Please check your connnection.'
    # When the third  button is selected, display the link for the third website
    elif selected_button == 'Button C':
        try:
            urldisplay(url3)
        except:
            output_text['text'] = 'Failed Connection: Please check your connnection.'
    # Otherwise, choose a button to view first
    else:
        output_text['text'] = 'Please choose one option first.'
        
# Defining a function for to save the first winner to the database
  
def first_1(): 
    global data_source, identifier, data_property

    try:
        # 1. Make a connection to the saved_rankings database
        connection = connect(database = 'saved_rankings.db')
                             
        # 2. Get a cursor on the database
        cursor = connection.cursor()

        # 3. Construct the SQLite insert statement (keeping in mind that the
        #    strings appearing in the SQLite statement must have single quotes
        #    around them)
        t = (data_source, '1', identifier[0], data_property[0])
        
        # 4. Execute the query
        cursor.execute(f'INSERT INTO rankings VALUES (?, ?, ?, ?)', t)
        
        # 5. Get the count of the number of rows inserted
        rows_inserted = cursor.rowcount

        # 6. Commit the changes to the database
        connection.commit()
        
        # 7. Close the cursor and connection
        cursor.close()
        connection.close()
        output_text['text'] += '\n' + 'Database updated successfully'
    except:
        output_text['text'] = 'Index Error: Please select an option to view'

# Defining a function for to save the second winner to the database 
def second_2():
    global data_source, identifier, data_property

    try:
        # 1. Make a connection to the saved_rankings database
        connection = connect(database = 'saved_rankings.db')
                             
        # 2. Get a cursor on the database
        cursor = connection.cursor()

        # 3. Construct the SQLite insert statement (keeping in mind that the
        #    strings appearing in the SQLite statement must have single quotes
        #    around them)
        t = (data_source, '2', identifier[1], data_property[1])
       
        # 4. Execute the query
        cursor.execute(f'INSERT INTO rankings VALUES (?, ?, ?, ?)', t)
        
        # 5. Get the count of the number of rows inserted
        rows_inserted = cursor.rowcount

        # 6. Commit the changes to the database
        connection.commit()
        
        # 7. Close the cursor and connection
        cursor.close()
        connection.close()
        output_text['text'] += '\n' + 'Database updated successfully'
    except:
        output_text['text'] = 'Index Error: Please select an option to view'

# Defining a function for to save the third winner to the database         
def third_3():
    global data_source, identifier, data_property

    try:
        # 1. Make a connection to the saved_rankings database
        connection = connect(database = 'saved_rankings.db')
                             
        # 2. Get a cursor on the database
        cursor = connection.cursor()

        # 3. Construct the SQLite insert statement (keeping in mind that the
        #    strings appearing in the SQLite statement must have single quotes
        #    around them)
        t = (data_source, '3', identifier[2], data_property[2])

        # 4. Execute the query
        cursor.execute(f'INSERT INTO rankings VALUES (?, ?, ?, ?)', t)
        
        # 5. Get the count of the number of rows inserted
        rows_inserted = cursor.rowcount

        # 6. Commit the changes to the database
        connection.commit()
        
        # 7. Close the cursor and connection
        cursor.close()
        connection.close()
        output_text['text'] += '\n' + 'Database updated successfully'
    except:
        output_text['text'] = 'Index Error: Please select an option to view'
    
#Importing the image file
sale_image = PhotoImage(file = 'file66.gif')
Label(main_window, bg = 'seagreen', image = sale_image).\
                 grid(row = 1, column = 1, columnspan = 2)

# Creating a label frame to choose and view a ranking
choose_and_view = LabelFrame(main_window, text = 'Choose and view a ranking',
                             bg = 'seagreen',
                             font = ('Arial', 20))

# Creating a label frame to save a winner
save_winner = LabelFrame(main_window, bg = 'seagreen',
                         text = 'Save a winner',
                         font = ('Arial', 20))

messages_1 = LabelFrame(main_window, bg = 'seagreen',
                        text = 'Messages', 
                         font = ('Arial', 20))
output_text = Label(messages_1, bg = 'seagreen',
                    text = 'Please choose and view a ranking',
                    anchor = NW,  justify = LEFT, width = 65, height = 10, 
                    font = ('Arial', 18),
                    borderwidth = 2, relief = 'groove')

# Creating three radiobuttons for top three competitors
# The select_button refers to the variable used for storing string values
# We assign specific values to each radiobutton

TV_shows_b = Radiobutton(choose_and_view, bg = 'seagreen',
                         text = 'US TV Guide’s Trending TV shows',
                         variable = select_button, value = 'Button A',
                         command = update_status,
                         font = ('Arial', 20))

Downloaded_movies_b = Radiobutton(choose_and_view, bg = 'seagreen',
                                  text = 'Top Airing Animes on MyAnimeList',
                                  variable = select_button,
                                  value = 'Button B',
                                  command = update_status,
                                  font = ('Arial', 20))
            
Pop_songs_b = Radiobutton(choose_and_view, bg = 'seagreen',
                          text = 'Most popular songs on Official Charts',
                          variable = select_button, value = 'Button C',
                          command = update_status,
                          font = ('Arial', 20))
  
# Creating two push buttons for selecting top three and data sources 
top_three = Button(choose_and_view, bg = 'seagreen',
                   activeforeground = 'red', text = 'show top three',
                   font = ('Arial', 20), command = top_three)
data_source = Button(choose_and_view, fg = 'black',
                     bg = 'seagreen',
                     text = 'Show data source',
                     activeforeground = "red",
                     font = ('Arial', 20), command = data_source)

# Creating three push buttons for top three winners

first = Button(save_winner, bg = 'seagreen',
               text = 'First', font = ('Arial', 20),
               activeforeground = "red",
               command = lambda: first_1())
second = Button(save_winner,bg = 'seagreen',
                activeforeground = "red",
                text = 'Second', font = ('Arial', 20),
                command = second_2)
third = Button(save_winner, bg = 'seagreen',
               text = 'Third',
               activeforeground = "red",
               command = third_3,
               font = ('Arial', 20))

# Giving the main window a color

main_window.config(background = 'seagreen')
# Using grid manager to put radiobuttons in choose
#and view lable frame in the right place

TV_shows_b.grid(row = 2, column = 1, sticky = 'w')
Downloaded_movies_b.grid(row = 3, column = 1, sticky = 'w')
Pop_songs_b.grid(row = 4, column = 1, sticky = 'w')
top_three.grid(row = 5, column = 1,
               padx = 10, pady = 10, sticky = 'w')
data_source.grid(row = 5, column = 2, columnspan = 1,
                 padx = 10, pady = 10, sticky = 'e')

# Using grid manager to put buttons in main window

first.grid(row = 2, column = 2,
           sticky = 'w', padx = 20, pady = 5)
second.grid(row = 3, column = 2,
            sticky = 'w', padx = 20, pady = 5)
third.grid(row = 4, column = 2, sticky = 'w', padx = 20, pady = 5)
output_text.grid(row = 3, column = 1, columnspan = 2, rowspan = 2)

# Use grid to put widgets in main window

choose_and_view.grid(row = 2, column = 1, sticky = 'w',
                     padx = 5, pady = 5)
save_winner.grid(row = 2, column = 2, sticky='n',
                 padx =5, pady = 5)
messages_1.grid(row = 3, column = 1, columnspan = 2,
                padx = 5, sticky = 'w')

# Start the event loop to detect user inputs
main_window.mainloop()



