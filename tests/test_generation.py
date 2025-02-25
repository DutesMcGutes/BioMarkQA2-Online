from biomarkqa2.generation import generate_answer

def test_generation():
    response = "Biomarkers such as troponin and CRP are associated with cardiovascular disease."
    answer = generate_answer(response)

    assert "Biomarker" in answer, "Failed to format the answer."
    print("✅ Answer generation test passed.")

if __name__ == "__main__":
    test_generation()
