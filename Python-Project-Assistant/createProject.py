#!/usr/bin/env python3

# ======================================================================================================================
#   Python Project Assistant
#   Copyright (C) 2017  Kevin Ziegler <ziegler.kevin@outlook.de>
#
#   This program is free software; you can redistribute it and/or modify it under the terms of
#   the GNU General Public License as published by the Free Software Foundation; either version
#   3 of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#   without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#   See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along with this program;
#   if not, see <http://www.gnu.org/licenses/>.
# ======================================================================================================================

import sys, os, shutil

print( 'Usage: python parameter.py [...] [...] [...] ....|[crDir, crClass, crRelease, crInstall]!' )


class Param:
	def __init__( self, script_name=' ', version=' ', description=' ', url=' ', author=' ', author_email=' ',
				  licenses=' ' ):
		self._script_name = script_name
		self._version = version
		self._description = description
		self._url = url
		self._author = author
		self._author_email = author_email
		self._licenses = licenses

	def create_dir( self ):
		print( 'Create a new project ' )

		self.script_name = input( 'Project Name: ' )
		self.version = input( 'Version: ' )
		self.description = input( 'Description: ' )
		self.url = input( 'URL: ' )
		self.author = input( 'Author: ' )
		self.author_email = input( 'Author Email: ' )
		self.path = ("./" + self.script_name)
		self.licenses = input( 'Lizenz: ' )
		os.makedirs( self.path )

		os.chdir( self.path )
		# Setup file
		setup = open( "setup.py", 'w' )
		setup.write( "#!/usr/bin/env python" )
		setup.write( "\n" )
		setup.write( "\n" )
		setup.write( "from distutils.core import setup" )
		setup.write( "\n" )
		setup.write( "\n" )
		setup.write( "setup(name='" + self.script_name + "',\n\t"
                                "version='" + self.version + "',\n\t"
                                "description='" + self.description + "',\n\t"
                                "url='" + self.url + "',\n\t"
                                "author='" + self.author + "',\n\t"
                                "author_email='" + self.author_email + "',\n\t"
                                "license='" + self.licenses + "',)" )
		setup.close( )
		readme = open( "README.rst", "w" )
		lizenz = open( "LICENSE", "w" )

		if self.licenses == "gpl":
			shutil.copy( '../GPLv3', './LICENSE' )
		else:
			exit( )

		os.makedirs( "./bin/" + self.script_name.lower( ) )

		os.makedirs( "./" + self.script_name.lower( ) + "/test/" )
		os.chdir( "./" + self.script_name.lower( ) + "/" )
		init = open( "__init__.py", "w" )
		mainfile = open( "main.py", "w" )

		os.chdir( "./test" )
		test_init = open( "__init__.py", "w" )
		test_main = open( "test_main.py", "w" )

	def create_class( self ):
		class_name = input( "Klassen Name" )
		os.chdir( "../" )
		# print(os.path.abspath("."))
		test = open( "main.py", "w" )
		test.write( "#!/usr/bin/env python" )
		test.write( "\n \n" )
		test.write( "class " + class_name + ":\n\tpass" )
		test.close( )

	def abfrage( self ):
		try:
			if CRDIR == 'crDir':
				self.create_dir( )
				print( 'Grundstrucktur wurde angelegt!' )
			else:
				print( 'Grundstrucktur wurde NICHT angelegt!' )

			if CRCLASS == 'crClass':
				print( 'Klasse wurde angelegt' )
			else:
				print( 'Klasse wurde NICHT angelegt!' )

			if CRRELEASE == 'crRelease':
				print( 'Release wurde angelegt' )
			else:
				print( 'Release wurde NICHT angelegt!' )

			if CRINSTALL == 'crInstall':
				print( 'Installer wurde angelegt' )
			else:
				print( 'Installer wurde NICHT angelegt!' )
		except ValueError:
			print( 'Fehler' )

<<<<<<< HEAD
=======
print('Usage: python parameter.py [...] [...] [...] ....|[crDir, crClass, crRelease, crInstall]!')

class param:
    def __init__( self, script_name=" ", version=" ", description=" ", url=" ", author=" ", author_email=" ", path=" ",
                  licenses=" " ):
        self.script_name = script_name
        self.version = version
        self.description = description
        self.url = url
        self.author = author
        self.author_email = author_email
        self.path = path
        self.licenses = licenses

    def create_dir( self ):
        print( 'Create a new project ' )
        self.script_name = input( 'Project Name: ' )
        self.version = input( 'Version: ' )
        self.description = input( 'Description: ' )
        self.url = input( 'URL: ' )
        self.author = input( 'Author: ' )
        self.author_email = input( 'Author Email: ' )
        self.path = ("./" + self.script_name)
        self.licenses = input( 'Lizenz: ' )
        os.makedirs( self.path )

        os.chdir( self.path )
        # Setup file
        setup = open( "setup.py", 'w' )
        setup.write( "#!/usr/bin/env python" )
        setup.write( "\n" )
        setup.write( "\n" )
        setup.write( "from distutils.core import setup" )
        setup.write( "\n" )
        setup.write( "\n" )
        setup.write( "setup(name='" + self.script_name + "',\n\t"
                                                 "version='" + self.version + "',\n\t"
                                                  "description='" + self.description + "',\n\t"
                                                   "url='" + self.url + "',\n\t"
                                                    "author='" + self.author + "',\n\t"
                                                     "author_email='" + self.author_email + "',\n\t"
                                                      "license='" + self.licenses + "',)" 
                    )
        
        setup.close( )
        readme = open( "README.rst", "w" )
        lizenz = open( "LICENSE", "w" )

        if self.licenses == "gpl":
            shutil.copy( '../GPLv3', './LICENSE' )
        else:
            exit( )

        os.makedirs( "./bin/" + self.script_name.lower( ) )

        os.makedirs( "./" + self.script_name.lower( ) + "/test/" )
        os.chdir( "./" + self.script_name.lower( ) + "/" )
        init = open( "__init__.py", "w" )
        mainfile = open( "main.py", "w" )

        os.chdir( "./test" )
        test_init = open( "__init__.py", "w" )
        test_main = open( "test_main.py", "w" )

    def create_class( self ):
        class_name = input( "Klassen Name" )
        os.chdir( "../" )
        # print(os.path.abspath("."))
        test = open( "main.py", "w" )
        test.write( "#!/usr/bin/env python" )
        test.write( "\n \n" )
        test.write( "class " + class_name + ":\n\tpass" )
        test.close( )


    def abfrage(self):
        try:
            if CRDIR == 'crDir':
                self.create_dir( )
                print( 'Grundstrucktur wurde angelegt!')
            else:
                print('Grundstrucktur wurde NICHT angelegt!')

            if CRCLASS == 'crClass':
                print('Klasse wurde angelegt')
            else:
                print('Klasse wurde NICHT angelegt!')

            if CRRELEASE == 'crRelease':
                print('Release wurde angelegt')
            else:
                print('Release wurde NICHT angelegt!')

            if CRINSTALL == 'crInstall':
                print('Installer wurde angelegt')
            else:
                print('Installer wurde NICHT angelegt!')
        except ValueError:
            print('Fehler')
>>>>>>> ff8295dd3e8e9eb289d6b7d479f702efa8f58d40

try:
	CRDIR = str( sys.argv[ 1 ] )
except IndexError:
	CRDIR = None

try:
	CRCLASS = str( sys.argv[ 2 ] )
except IndexError:
	CRCLASS = None

try:
	CRRELEASE = str( sys.argv[ 3 ] )
except IndexError:
	CRRELEASE = None

try:
	CRINSTALL = str( sys.argv[ 4 ] )
except IndexError:
	CRINSTALL = None


def main( ):
	create = Param( )
	create.__init__()
	create.create_dir()


if __name__ == "__main__":
	main( )
