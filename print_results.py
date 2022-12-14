#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Abraham Chua
# DATE CREATED: 08/12/2022
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    # Print the type of pretrained model used in this classification
    print("The model used for this classification is {}".format(model))
    # Formatting
    print("")
    print("Result statistics of the classification")
    # Print the corresponding values inside the result statistics dictionary
    for k, v in results_stats_dic.items():
        if k[0] == "p":
            print("% {} has the value of {}".format(k[4:].replace("_", " "), v))
        else:
            print("number of {} is {}".format(k[2:].replace("_", " "), v))
    
         
    # Check if the user wants to check for incorrectly classified images and if there any misclassified images. 
    # The second statement was added to remove unnecessary runtime for code block to check everything if there are no misclassified images
    if print_incorrect_dogs and (results_stats_dic["pct_correct_dogs"] < 100 or results_stats_dic["pct_correct_notdogs"] < 100):
        # Formatting
        print("") 
        print("Misclassified images")
        for k, v in results_dic.items():
            # Check the values if it's misclassified
            if v[3] != v[4]:
                print("The image {} has been misclassified".format(k))
    # Check if the user wants to check for incorrectly classified dog breeds and if there are any.
    if print_incorrect_breed and results_stats_dic["pct_correct_breed"] < 100:
        # Formatting
        print("") 
        print("Misclassified dog breeds")
        for k, v in results_dic.items():
            if sum(v[3:]) == 2 and v[2] == 0:
                # print(results_dic[k])
                print("The breed of the dog in the image {} has been misclassified".format(k))