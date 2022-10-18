#Example Config for my servers livemap, replace the data by your own.

url = "http://okmeis.minecraft.best:8100/"
mapname = "MainMap_Beta_0_2_3"

#relevant for the url, changes when zooming and when moving on the map.
anotherParameter = "-1_3/"

#These are not coordinates, but name fragments of the seperate images of the map.
#To figure out your own numbers inspect the HTML elements of your livemap in a browser.
down  = 98
top   = 111
left  = -16
right = 1

#to get a channels or users ID: activate Developer Mode and right click a user or channel

#channelID = ID of the channel you want the bot to post your map, WARNING: don't use the ID
#of a channel that contains other messages than the image this bot is posting else you'll
#lose all these messages.
channelID = 1031661649855258684

#your and your admins IDs, for multiple IDs: [id1, id2, id3, ....]
botAdminIDs = [238807093371600897]

#time until the map gets updated, but don't set it too low, consider the download time
repeatInMinutes = 10