import openai

def generate_comic_panels(story):
    prompt = f"""
    Convert the following story into a structured comic book format. Each panel should include:
    - Scene Description
    - Dialogue
    - Panel Type (Close-up, Action, Wide, etc.)
    
    Story:
    {story}
    
    Output format:
    Panel 1:
    Scene: [Scene Description]
    Dialogue: [Dialogue]
    Type: [Panel Type]
    
    Panel 2:
    Scene: [Scene Description]
    Dialogue: [Dialogue]
    Type: [Panel Type]
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert comic script formatter."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message["content"]

# Example usage
if __name__ == "__main__":
    story = "A brave little rabbit finds a magic carrot and fights a hungry fox."
    panels = generate_comic_panels(story)
    print(panels)
