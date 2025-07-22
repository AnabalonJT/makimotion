# Requirements Document

## Introduction

MakiMotion is a web application designed for healthcare professionals (therapists, psychologists, kinesiologists, etc.) to manage patient records, appointments, and evaluations. The system will provide a clean, user-friendly interface for registering, organizing, and tracking patient data and appointments. The application will be built with Django and deployed on Render with a soft color palette (lilac, pink, white) for a calming professional environment.

## Requirements

### Requirement 1

**User Story:** As a healthcare professional, I want to securely log into the system, so that I can access my patient data privately and securely.

#### Acceptance Criteria

1. WHEN a user accesses the login page THEN the system SHALL display a clean login form with username/password fields and MakiMotion logo
2. WHEN a user enters valid credentials THEN the system SHALL authenticate them and redirect to the dashboard
3. WHEN a user enters invalid credentials THEN the system SHALL display an error message and remain on the login page
4. WHEN a user clicks logout THEN the system SHALL securely end their session and redirect to the login page
5. IF admin disables registration THEN the system SHALL not display registration options to users

### Requirement 2

**User Story:** As a healthcare professional, I want to view a dashboard with all my patients, so that I can quickly access patient information and see recent activity.

#### Acceptance Criteria

1. WHEN a user successfully logs in THEN the system SHALL display a dashboard with a list of all patients
2. WHEN viewing the patient list THEN the system SHALL display patient cards showing name, age, and brief diagnosis
3. WHEN a user selects name sorting THEN the system SHALL order patients alphabetically (A-Z or Z-A)
4. WHEN a user selects last appointment sorting THEN the system SHALL order patients by most recent to oldest appointment or vice versa
5. WHEN a patient has no appointments THEN the system SHALL still display the patient card with appropriate indication

### Requirement 3

**User Story:** As a healthcare professional, I want to create, view, edit, and delete patient records, so that I can maintain accurate patient information.

#### Acceptance Criteria

1. WHEN a user clicks "Add Patient" THEN the system SHALL display a form with required fields: full name, age, diagnosis, and general notes
2. WHEN a user submits a complete patient form THEN the system SHALL save the patient and redirect to the patient detail view
3. WHEN a user submits an incomplete patient form THEN the system SHALL display validation errors for missing required fields
4. WHEN a user views a patient detail THEN the system SHALL display all patient information and appointment history
5. WHEN a user edits patient information THEN the system SHALL update the record and confirm the changes
6. WHEN a user deletes a patient THEN the system SHALL remove the patient and all associated appointments after confirmation

### Requirement 4

**User Story:** As a healthcare professional, I want to create, view, edit, and delete appointments for each patient, so that I can track sessions and maintain treatment history.

#### Acceptance Criteria

1. WHEN a user creates an appointment THEN the system SHALL require date/time, session description, evaluation, and additional notes
2. WHEN a user views a patient's appointments THEN the system SHALL display them chronologically with all appointment details
3. WHEN a user edits an appointment THEN the system SHALL update the record and maintain the association with the patient
4. WHEN a user deletes an appointment THEN the system SHALL remove it after confirmation
5. WHEN viewing appointment history THEN the system SHALL show evaluation scales or categories clearly

### Requirement 5

**User Story:** As a healthcare professional, I want the application to have a clean, calming interface, so that it creates a professional and pleasant working environment.

#### Acceptance Criteria

1. WHEN the application loads THEN the system SHALL use the defined color palette (soft lilac #d1a0f8, soft pink #f9c5d1, white #ffffff, neutral #f4effa)
2. WHEN displaying interactive elements THEN the system SHALL use strong lilac #a86ef4 for buttons and details
3. WHEN showing error messages THEN the system SHALL use soft red #f87171 for error notifications
4. WHEN the application is viewed on different screen sizes THEN the system SHALL maintain usability (responsive design)
5. WHEN displaying the logo THEN the system SHALL show "MakiMotion" as text with appropriate styling

### Requirement 6

**User Story:** As a system administrator, I want the application to be deployable on Render, so that it can be accessed reliably in production.

#### Acceptance Criteria

1. WHEN deploying to production THEN the system SHALL use PostgreSQL as the database
2. WHEN running in development THEN the system SHALL use SQLite as the database
3. WHEN deploying THEN the system SHALL include requirements.txt, Procfile, and render.yaml files
4. WHEN configuring the application THEN the system SHALL use environment variables for database connection and secret key
5. WHEN the application starts THEN the system SHALL connect to the appropriate database based on the environment

### Requirement 7

**User Story:** As a healthcare professional, I want user management to be scalable, so that the system can grow with my practice needs.

#### Acceptance Criteria

1. WHEN the system is initially deployed THEN it SHALL support single-user access to their own patient data
2. WHEN the database is designed THEN it SHALL use a structure that can be extended to multi-user scenarios
3. WHEN a user accesses the system THEN they SHALL only see their own patients and appointments
4. WHEN using Django admin THEN administrators SHALL be able to view and manage system data during development
5. WHEN the system grows THEN the user model SHALL support extension to multi-tenant architecture