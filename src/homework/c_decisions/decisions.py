def get_options_ratio(option, total):
    ratio = option/total
    return ratio

def get_faculty_rating(ratio):
    
    rating_statement = ""

    if(ratio >= 0.9 and ratio <= 1.0 ):
        rating_statement = "Excellent"
        
    elif(ratio >= 0.8 and ratio < .9):
        rating_statement = "Very Good"

    elif(ratio >= 0.7 and ratio < .8):
        rating_statement = "Good"

    elif(ratio >= 0.6 and ratio < .7):
        rating_statement = "Needs Improvement"
        
    elif(ratio >= 0 and ratio < 0.6):
        rating_statement = "Unacceptable"
    
    else:
        rating_statement = "Non Existant"
    
    return rating_statement
