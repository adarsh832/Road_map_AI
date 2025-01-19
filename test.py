stream = chat(
    model='llama3.2',
    messages=[
         {
            'role': 'system',
            'content': 'You are a AI that help people to get roadmap for learning.give them a step by step guide to learn.',
            'role': 'user',
            'content': f'I want to leant {learn} in {time} and I am {level} level. give me a roadmap to learn. step by step guide.',


            },
            
        ],
    stream=True,
    )
    for chunk in stream:
      output = chunk['message']['content']

      for word in output.split(" "):
        yield word + " "
        tm.sleep(0.02)