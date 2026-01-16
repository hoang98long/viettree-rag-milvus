def build_prompt(context: str, question: str) -> str:
    return f"""
Bạn chỉ được trả lời dựa trên thông tin sau:

{context}

Câu hỏi:
{question}

Nếu không có thông tin, hãy nói: "Không tìm thấy dữ liệu phù hợp".
"""
