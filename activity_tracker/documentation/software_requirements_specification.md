#  Software Requirements Specification

## 1. Introduction
Topic of the project: Fitness Activity Tracker

### 1.1. Purpose

The purpose of the software is to provide a comprehensive fitness activity tracking system that allows users to log, monitor, and analyze their physical activities and body weight over time. The application serves as a personal fitness diary that helps users maintain motivation and track their progress toward fitness goals. 

### 1.2. Intended audience

The Fitness Activity Tracker will provide an interface for a main user that is the single user type of the software. The audience consists of anyone who is interested in tracking their fitness activities, monitoring their progress, and maintaining a personal fitness log. This includes fitness enthusiasts, people starting their fitness journey, athletes, and anyone looking to maintain an active lifestyle.  


## 2. Overall description

### 2.1. Key functionality

#### 2.1.1. Before logging in:

- User can create a username in the system
  - Username must be unique and at least 5 characters long
  - User can log into the system
  - Login succeeds when entering an existing username and password in the login form
  - If the user doesn't exist or the password doesn't match, the system notifies about this

#### 2.1.2. After logging in:

- The user can view their activity dashboard with a summary of recent activities
- The user can see all their past activity logs in chronological order
- The user can add new fitness activities with detailed information:
  - Activity type (running, cycling, yoga, swimming, weightlifting, etc.)
  - Date and time of the activity
  - Duration (in minutes)
  - Intensity level (1-10 scale)
  - Distance (for applicable activities like running, cycling)
  - Additional notes or comments
- The user can track their weight over time:
  - Add weight entries with date
  - View weight progress chart
  - Set weight goals
- The user can view activity statistics and progress
- The user can log out from the system
- All data is private and visible only to the user

#### 2.1.3. Draft layout of User Interface

The application consists of the following main views:

1. **Login/Registration View**
   - Username and password input fields
   - Login button
   - Link to registration form

2. **Registration View**
   - Username and password input fields
   - Password confirmation
   - Create account button
   - Link back to login

3. **Main Dashboard**
   - Welcome message with username
   - Quick stats (total activities this week, current weight)
   - Recent activities list
   - Add new activity button
   - Weight tracking section
   - Logout button

4. **Add Activity View**
   - Activity type dropdown (running, cycling, yoga, swimming, weightlifting, etc.)
   - Date and time picker
   - Duration input (minutes)
   - Intensity slider (1-10)
   - Distance input (for applicable activities)
   - Notes text area
   - Save and Cancel buttons

5. **Activity History View**
   - Chronological list of all activities
   - Filter options (by activity type, date range)
   - Edit/Delete options for each activity

6. **Weight Tracking View**
   - Current weight display
   - Weight entry form
   - Weight progress chart
   - Goal setting section


The application opens to a login view, from which
- it's possible to navigate to a new user creation view or, upon successful login,
- to the logged-in user's activity list.


### 2.2. Further development

Some ideas for further development are:

- **Data Export/Import**: Allow users to export their data to CSV or import from other fitness apps
- **Achievement System**: Badges and milestones for reaching certain targets
- **Advanced Analytics**: Detailed charts and insights about fitness trends
- **Photo Attachments**: Add photos to activity logs


## 3. Technical Requirements

### 3.1. Functional Requirements

#### 3.1.1. User Management
- FR-001: System shall allow users to create unique accounts with username and password
- FR-002: System shall validate username uniqueness and minimum length (5 characters)
- FR-003: System shall authenticate users during login
- FR-004: System shall provide secure logout functionality

#### 3.1.2. Activity Tracking
- FR-005: System shall allow users to log fitness activities with the following data:
  - Activity type (running, cycling, yoga, swimming, weightlifting, hiking, etc.)
  - Date and time
  - Duration in minutes
  - Intensity level (1-10 scale)
  - Distance (for applicable activities)
  - Personal notes
- FR-006: System shall display all logged activities in chronological order
- FR-007: System shall allow users to edit or delete existing activity entries
- FR-008: System shall provide filtering options for activity history

#### 3.1.3. Weight Tracking
- FR-009: System shall allow users to log weight entries with date
- FR-010: System shall display weight progress over time
- FR-011: System shall allow users to set weight goals
- FR-012: System shall calculate and display weight change trends

#### 3.1.4. Data Management
- FR-013: System shall ensure data privacy - users can only access their own data
- FR-014: System shall persist all user data between sessions
- FR-015: System shall provide data validation for all input fields


## 4. Data Model

### 4.1. User Entity
- user_id (Primary Key)
- username (Unique)
- password_hash
- created_at
- last_login

### 4.2. Activity Entity
- activity_id (Primary Key)
- user_id (Foreign Key)
- activity_type
- activity_date
- duration_minutes
- intensity_level
- distance_km
- notes
- created_at
- updated_at

### 4.3. Weight Entry Entity
- weight_id (Primary Key)
- user_id (Foreign Key)
- weight_kg
- entry_date
- created_at

## References














