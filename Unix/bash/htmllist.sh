#!/bin/bash
# Last modification Time-stamp: <07/06/2005 01:46 seki@obelix.seki.fr>

# This file is free software, you can use it, modify it or distribute
# it with no restriction.
#
# Authors : Matthieu Moy     - initial release 
#                            - changes validations
#
#  S�bastien Kirche : hacks  - localization code 
#                            - support for links
#                            - filenames bugfixes & cosmetic changes

# no argument -> display usage

usage ()
{
	cat <<EOF
htmllist.sh - Auto generation of html index files from directories 
              with optional localized descriptions.

Usage : htmllist.sh <directory> [indexfile] [language]
        directory : directory to list
        indexfile : name of the generated index file (default : index.html)
        language  : if several versions of the meta files are present, 
                    version to read from (default : none)

Optional additional files :
 - index.meta      : text to add before the list
 - index-tail.meta : text to add after the list
 - index-head.meta : html code to embed in the head part of the file
 - xxx.meta        : description of the file xxx. For different versions 
                     of the meta files, add the language to the meta suffix.
                     i.e.: index.meta.en somefile.meta.de
 - xxx.link        : link description in the following format
                     1st line     - url
                     2nd line     - label for the link
                     rest of file - text to be displayed as a description
                     Links files may also exist in different languages like meta files.
 - .htmllistignore : list of files not to treat (one name per line)

Options :
        --help, -h	Show this message
        -r, --recursive	Recursively run on subdirectories
        -t, --type	Show file type (/ for directories, @ for links)
        --prefix ARG	Use ARG as a prefix in page titles
	--thumb		Use 'convert' to generate thumbnail images
	--validator	Insert W3C validator icon in the page
EOF
}

uniquify ()
{
    echo $1 | sed -e 's,//*\(\.\|\)//*,/,g'
}

recursive="no"
type="no"
dir="."
target="index.html"
locale=""
args=""
prefix=""
thumb="no"
validator_icon="no"

while test $# -ne 0; do
    case "$1" in
        "--help"|"-h")
            usage
            exit 0
            ;;
        "-r"|"--recursive")
            recursive="yes"
            args="$args $1"
            shift
            ;;
        "-t"|"--type")
            type="yes"
            args="$args $1"
            shift
            ;;
        "--prefix")
            shift
            prefix=$1
            shift
            ;;
	"--thumb")
	    thumb="yes"
	    shift
	    ;;
	"--validator")
	    validator_icon="yes"
	    shift
	    ;;
        *)
            if [[ $dir = "." ]]; then
                dir=$1
            elif [[ $target = "index.html" ]]; then
                target=$1
                args="$args $1"
            elif [[ $locale = "" ]]; then
                locale=".$1"
                args="$args $1"
            else
                echo "Too many arguments"
                exit 1
            fi
            shift
            ;;
    esac
done

# if more than 1 arg, use arg #2 as index file 
# else defaults to index.html

cd $dir;

# removes former index file
if [ -f "$target" ]
    then
    rm "$target"
fi

if [[ $dir != "." ]]; then
    if [[ $prefix != "" ]]; then
        listingfor=" for $prefix/$dir"
    else
        listingfor=" for $dir"
    fi
else
    listingfor=""
fi

# keep trace of output
exec > /tmp/htmllist.$$

# html file header
cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">
<!-- This page was generated by htmllist.sh -->
<!-- See http://www-verimag.imag.fr/~moy/utils/htmllist.sh -->
  <head>
EOF

# use localized index header if provided
# else use default header & title
if [ -f "index-head.meta$locale" ]
then
    cat "index-head.meta$locale"
else
    echo "<title>directory listing$listingfor</title>"
fi

# end of header
cat <<EOF
  </head>
  <body>
EOF

# use localized top if provided
# else place default link to parent directory
if [ -f "index.meta$locale" ]
then
    cat "index.meta$locale"
else
    echo "  <p><a href=\"..\">Parent directory : ../</a></p>"
    echo "  <h1>directory listing$listingfor</h1>"
fi

# begining of enumeration
echo '<ul>'

# read ignore list content if it exists
ignorelist=/tmp/ignore.$$
touch "$ignorelist"

if [ -f ".htmllistignore" ]
    then
    cat .htmllistignore | while read line
    do
        echo ./$line | tr ' ' '\n' >> "$ignorelist"
    done
fi

# enumeration loop

for file in *
do
	# ignore metafiles
	if echo $file | grep -q -e '.meta$' -e '.meta.[a-z]\{2\}$' -e '~$' -e '^#.*$' -e 'htmllist-thumbnail.png$'
	then
		continue
	fi
	
	# ignore ignored files
	if grep -q "^./$file\$" $ignorelist
	then
		continue
	fi

	if echo $file | grep -q -e '.link$' -e '.link.[a-z]\{2\}$'
	then
		url=`sed '1q;d' "$file"`
		caption=`sed '2q;d' "$file"`
                if [[ $locale != "" ]]; then
		    if echo $file |grep -q -e ".$locale\$"
		    then
			cat <<EOF
<li class="item"><a href="$url" class="itema"><span class="link">$caption</span>
EOF
			tail -n+3 "$file"
		    else
			continue
		    fi
		else
		    if echo $file | grep -q -v -e '.link.[a-z]\{2\}$'
		    then
			cat <<EOF
<li class="item"><a href="$url" class="itema"><span class="link">$caption</span>
EOF
			tail -n+3 "$file"
		    else
			continue
		    fi
		fi
	else
	    bname=`basename "$file"`
            typestr=""
            if [[ $type = "yes" ]]; then
                if [ -d "$file" ]; then
                    typestr="/"
                elif [ -L "$file" ]; then
                    typestr="@"
                fi
            fi
	    thumbfile="${bname}-htmllist-thumbnail.png"
	    if [ "$thumb" = "yes" ] &&
		convert -resize 64x64 "$file" "$thumbfile" &&
		[ -f "$thumbfile" ]; then
		htmlthumb="<img src=\"$thumbfile\" alt=\"$bname\"/>"
	    else
		htmlthumb=""
	    fi
	    cat <<EOF
<li class="item"><a href="$bname" class="itema">$htmlthumb<span class="filename">$bname$typestr</span>
EOF
	    if [ -f "$file.meta$locale" ]
	    then
		cat "$file.meta$locale"
	    fi
            if [[ $recursive = yes && -d $file ]]; then
                if [[ $prefix != "" ]]; then
                    passprefix=$(uniquify $prefix/$dir)
                else
                    passprefix=$dir
                fi
                echo htmllist.sh --prefix $passprefix $file $args >&2
                htmllist.sh --prefix $passprefix $file $args
            fi
	fi
	cat <<EOF
</a></li>
EOF
done
# end of enumeration

rm -f $ignorelist
echo '</ul>'

# use index bottom if provided
if [ -f "index-tail.meta$locale" ]
then
    cat "index-tail.meta$locale"
fi

if [ "$validator_icon" = "yes" ]; then
    cat <<\EOF
<p>
    <a class="invisible" href="http://validator.w3.org/check?uri=referer"><img
       class="linkimg" src="http://www.w3.org/Icons/valid-xhtml11"
        alt="Valid XHTML 1.1" height="31" width="88" /></a>
  </p>
EOF
fi

# end of file
cat <<EOF
  </body>
</html>
EOF

mv /tmp/htmllist.$$ $target

# Local variables:
# time-stamp-format: "%02d/%02m/%:y %02H:%02M %u@%s"
# End: