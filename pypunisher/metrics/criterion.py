"""

     Information Criterion
     ~~~~~~~~~~~~~~~~~~~~~

"""


def aic(model, data):
    """Compute the Akaike Information Criterion (AIC)

    Args:
        model : sklearn model object)
            A sklearn model.
        data : ndarray
            The data used to train `model`.

    Returns:
        float: ...

    References:
        * https://en.wikipedia.org/wiki/Akaike_information_criterion

    """
    pass


def bic(model, data):
    """Compute the Bayesian Information Criterion (BIC)

    Args:
        model : sklearn model object)
            A sklearn model.
        data : ndarray
            The data used to train `model`.

    Returns:
        float: ...

    References:
        * https://en.wikipedia.org/wiki/Bayesian_information_criterion

    """
    pass


def compute_score(model, criterion):
    """Get the score of a model.

    Args:
        model : sklearn model
            Model to obtain the score of.
        criterion : str
            Criterion to use.
            One of: 'aic', 'bic', None
            If none, call `.score()`.

    Returns:
        float :
            model score.
    """
    pass
