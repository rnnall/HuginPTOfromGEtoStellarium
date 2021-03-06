# Hugin Poject file from Google Earth KML to Stellarium Landscape

Inspired by the following YouTube Video [Using Google Earth terrain in Stellarium](https://www.youtube.com/watch?v=5TrRE5wUeAk). Is there an easir way to do this.

**Goal:** Write a script preferirble in `Python` to take KML file and convert it to Hugin Poject file. Automate image download based on KML file output.

# Intorduciton

By no means am I a programer or an expert with these tools. Just made some gernal observations in my exploration how to make this easier and was intrested in creating panoramic images withg Google Earth Pro, just happend to find this video.

## Getting Started

You will need the following software downlaoded installed or data pulled from. Assuming know how to do this.

* [Hugin](http://hugin.sourceforge.net/)
* [Stellarium](https://stellarium.org/)
* [Google Earth Pro](https://www.google.com/earth/versions/#earth-pro)
* [Make Stellarium panoramas from Google Earth](https://homepage.univie.ac.at/Georg.Zotti/php/panoCam.php)


# Hugin's Project file

The Hugin's project file can be opned with a text editor such as `Notepad`. To change the `Pitch` and `Yaw` as recomended in the video look for `p-90 y0` so this could be scripted to do the calculation based on output from [Make Stellarium panoramas from Google Earth](https://homepage.univie.ac.at/Georg.Zotti/php/panoCam.php) I do not believe this is necssary as if KML outputs the same each time then all you need is the project file [example.pto](example.pto) file. Just make sure your image captures match the filenames in the [example.pto](example.pto) file.

## Example .pto file

Download [example.pto](example.pto) to saved photo directory. That should be it....


## Editing .pto File

These numbers might be different, see example below. Now assuming that the `0-0.jpg to 150-324.jpg` do not change you can use the same pto file and the `pitch` and `yaw` should line up the photos.

*Note:* When moving Hugin's `.pto` file it want's to relink if the photos are not already in the diretory.


*Example .pto file:*

![Pitch & Yaw](https://github.com/rnnall/HuginPTOfromGEtoStellarium/blob/master/images/pitchyaw.gif)

*Hugin Configuraton File*

```
# image lines
#-hugin  cropFactor=1
i w4800 h2987 f0 v60 Ra0 Rb0 Rc0 Rd0 Re0 Eev0 Er1 Eb1 r0 p-90 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a0 b0 c0 d0 e0 g0 t0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0  Vm5 n"0-0.jpg"

#-hugin  cropFactor=1
i w4800 h2987 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p-65 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"25-0.jpg"
```
## Example Pano Created

This was created with flat blue sky files. Not the best example, but it does create pano image. All the files are named and match Hugin Project file.

![Example JPG](https://github.com/rnnall/HuginPTOfromGEtoStellarium/blob/master/example/example.jpg)

## TODO's

TODO: Script to calculate `yaw` and `pitch` look at [Hugin .pto File Parser](https://github.com/smidm/huginpto-py)

TODO: Script gathering Google Images. Possible Google Earth Engine API? Or Google Street View API's?? Researching...

## Google Earth Studio (GES)

### Python Scripts

TODO: Clean up scripts

* `mapl.py` - Creates mapping list of the image files based on Google Studio extracted images `mapl.txt`
* `mlist.py` -  Joins the master image names `master.txt` with `master.txt` into a mapping list to be used with `rename_files.py` to convert the names of the files from the Google Earth Studio output zip

TODO: Fix Image Size with [GES](https://www.google.com/earth/studio)

![Google Earth Studio](https://github.com/rnnall/HuginPTOfromGEtoStellarium/blob/master/images/GES.gif)

TODO: Explore translation of `.kml` to GES `.esp` file to edit and transfer Keyframes.

**Sample Code below:**

```html
{"modelVersion":16,"settings":{"name":"Location","frameRate":30,"dimensions":{"width":3840,"height":2160},"duration":450,"timeFormat":"frames"},
....

```
## Authors

* **rnull** - *Initial work* - [rnnall](https://github.com/rnnall)


## Acknowledgments

* [Hugin .pto File Parser](https://github.com/smidm/huginpto-py)

# Addtional Resoucres

* [THE PHOTOGRAPHER'S EPHEMERIS](https://app.photoephemeris.com)

# License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
