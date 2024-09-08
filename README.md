# Interactive Storytelling Platform with Branching Narratives

## Overview

The Interactive Storytelling Platform is a web application that allows users to create, read, and interact with stories featuring branching narratives. Authors can design stories with multiple paths and choices, while readers can experience unique stories based on their choices. The platform also provides authors with valuable analytics on reader interactions.

### Core Features

- **Story Creation & Editing**: 
  - Create and edit stories with multiple branching paths.
  - Visual editor to see and manage story structure.
  - Preview mode to test stories as readers.

- **Branching Narrative Structure**:
  - Create stories with multiple paths based on user choices.

- **Story Consumption**:
  - Interactive reading where choices determine the story path.
  - Save progress and resume later.
  - Track endings and branches explored.

- **Analytics for Authors**:
  - Track choice popularity and reader engagement.
  - Measure time spent on each section and overall story completion rate.

- **User Profiles**:
  - Reader accounts for saving stories, viewing history, and tracking paths.
  - Author accounts for story management and analytics.

- **Community & Sharing**:
  - Share stories via links or social media.
  - Rate stories and provide feedback.
  - Discover stories through search and filtering options.

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- Bootstrap 5.x

### Setup

1. **Clone the repository:**

   git clone https://github.com/yourusername/storytelling-platform.git
   cd storytelling-platform
   
2. **Create a virtual environment:**
  python -m venv venv
   venv\Scripts\activate

3. **Install dependencies:**
  pip install -r requirements.txt

4. **Apply Migrations:**
  python manage.py migrate

5. **Create a superuser(optional for admin access):**
  python manage.py createsuperuser

6. **Run the development server:**
   python manage.py runserver

Navigate to http://127.0.0.1:8000/ in your browser to view the application.







