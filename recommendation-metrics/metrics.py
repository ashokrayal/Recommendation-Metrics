def precision(actual, predicted, k = 5 ):
    """ Computes precision for recommendation systems using actual items and predicated items at k

        If the argument `k` isn't passed in, the default k 5 is used.

        Parameters
        ----------
        actual : list
            actual items used/brought by user

        predicted : list
            items recommended by system

        k : int
            The items number at which precision is calculated (default is 5)
        
        Returns
        ----------
        score : double
            the precision over actual items and recommended items
    """
    act_set = set(actual)
    pred_set = set(predicted[:k])
    result = len(act_set & pred_set) / float(k)
    return result

def recall(actual, predicted, k=5):
    """ Computes recall for recommendation systems using actual items and predicated items at k

        If the argument `k` isn't passed in, the default k 5 is used.

        Parameters
        ----------
        actual : list
            actual items used/brought by user

        predicted : list
            items recommended by system

        k : int
            The items number at which recall is calculated (default is 5)
            
                
        Returns
        ----------
        score : double
            the recall over actual items and recommended items
    """
    act_set = set(actual)
    pred_set = set(predicted[:k])
    result = len(act_set & pred_set) / float(len(act_set))
    return result

if __name__ == "__main__":
    actuals = [1,2,3]
    predicted = [1,2]
    print(precision(actuals,predicted,5))