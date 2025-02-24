def generate_answer(response):
    """
    Formats the retrieved response into a readable answer.

    Args:
        response (str): The retrieved text response.

    Returns:
        str: A formatted answer.
    """
    return f"Extracted Biomarker Information:\n\n{response}"
