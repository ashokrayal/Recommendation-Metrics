import numpy as np

def precision(actual, predicted, k = 5):
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

def recall(actual, predicted, k = 5):
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


def apk(actual, predicted, k = 5):
    """ Computes average precision for recommendation systems using actual items and predicated items at k

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
            the average precision over actual items and recommended items
    """
    
    # return 0 is no item in actuals list
    if not actual:
        return 0.0

    if len(predicted)>k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i,p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)

    return score / min(len(actual), k)

def mapk(actual, predicted, k = 5):
    """ Computes mean average precision for recommendation systems using actual items and predicated items at k

        If the argument `k` isn't passed in, the default k 5 is used.

        Parameters
        ----------
        actual : list
                A list of lists of elements that are to be predicted 
                (order doesn't matter in the lists)

        predicted : list
            A list of lists of predicted elements
                (order matters in the lists)

        k : int
            The items number at which mean average precision is calculated (default is 5)
        
        Returns
        ----------
        score : double
            the mean average precision over actual items and recommended items
    """
    return np.mean([apk(a,p,k) for a,p in zip(actual, predicted)])

def global_precision(actual, predicted, k = 5):
    """ Computes global precision for recommendation systems using actual items and predicated items at k

        If the argument `k` isn't passed in, the default k 5 is used.

        Parameters
        ----------
        actual : list
                A list of lists of elements that are to be predicted 
                (order doesn't matter in the lists)

        predicted : list
            A list of lists of predicted elements
                (order matters in the lists)

        k : int
            The items number at which mean average precision is calculated (default is 5)
        
        Returns
        ----------
        score : double
            the global precision over actual items and recommended items
    """
    return np.mean([precision(a,p,k) for a,p in zip(actual, predicted)])

def global_recall(actual, predicted, k = 5):
    """ Computes global recall for recommendation systems using actual items and predicated items at k

        If the argument `k` isn't passed in, the default k 5 is used.

        Parameters
        ----------
        actual : list
                A list of lists of elements that are to be predicted 
                (order doesn't matter in the lists)

        predicted : list
            A list of lists of predicted elements
                (order matters in the lists)

        k : int
            The items number at which global recall is calculated (default is 5)
        
        Returns
        ----------
        score : double
            the global recall over actual items and recommended items
    """
    return np.mean([recall(a,p,k) for a,p in zip(actual, predicted)])

if __name__ == "__main__":
    actuals = [1,2,3]
    predicted = [1,2]
    print(precision(actuals,predicted,5))