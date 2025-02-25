def generate_answer(response):
    """
    Formats the retrieved response into a structured, readable answer.

    Args:
        response (str): The retrieved text response.

    Returns:
        str: A formatted, structured response.
    """
    return f"### Extracted Biomarker Information ###\n\n{response}"
