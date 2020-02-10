# TrashTalk

## To recycle or not to recylce? We let the computer's vision decide! 


Dataset and trained model : https://drive.google.com/open?id=1eawx4aqh4sTnZ2XCFqeUMTWf3FwMXQLX

trashnet-extended is the zip file with all images.
the data folder contains the same images, split up into training, validation and test sets
The data folder also contains a trained model- export.pkl


## Inspiration
During the early hours of HackBeanpot, we were happily surprised by the focus towards sustainability shown by the organizers and the overall community. Walking around, we noticed a lot of help-text specifying what materials go into which bin. However, many people(including us) aren't used to sorting their waste in an organized manner, so it was a little confusing and we had to keep referring to these help-text sheets. That is where we had the idea to develop a tool that makes this decision process infinitely easier for us.

## What it does
The application we built to demo our classifier is very easy to use. The user clicks a picture of an item to be analyzed, and the application specifies which bin the item belongs to.  

## How we built it
We found a dataset of images labeled according to the material it is made of - [TrashNet](https://github.com/garythung/trashnet). We then tried a few different models to train the classifier and ultimately settled upon a Resnet34 CNN which gave us an accuracy of ~91%. We also added the Microsoft Azure Computer Vision API to focus our model on the primary object in the picture in case there are multiple. Since the API also provides a label for the object, we incorporated its classification confidence, but with a lower weightage since we wish to focus on the material rather than the object itself.  

## Challenges we ran into
The TrashNet dataset did not offer any data for compostable substances, but we were able to extend it to classify some food items as well.
The CNN itself took a lot of time to run with limited resources, so we were not able to make some changes due to time constraints.
The dataset is also biased towards plastic since it contains a significantly higher number of pictures labeled plastic. We were, however, able to increase the accuracy of other materials by clicking pictures of random waste items around the hackathon and adding it to the database. 

## Accomplishments that we are proud of
We were able to extend the dataset significantly, by adding a larger variety of items in the existing materials, as well as creating a new label for food items.
After a few tries, we attained an accuracy of ~91% (with 50/25/25 split) with our CNN, which was quite an exciting moment, given that the original paper had an accuracy of 75%.

## What we learned
This was our first time working with CNN, Computer Vision and CUDA. It was a challenging experience and would definitely be useful to us in the future.

## What's next for TrashTalk
This hackathon was spent with more focus on the classifier itself, so we made a web-app to showcase it.
The next steps would be to have it available on a device that can be mounted near the bins so users can scan their items then and there.
The dataset needs to be extended further to accurately identify all types of food since our focus was on fruits for this iteration.