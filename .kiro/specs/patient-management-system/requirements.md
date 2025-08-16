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

**User Story:** As a healthcare professional, I want to create, view, edit, and delete comprehensive clinical records for pelvic floor patients, so that I can maintain detailed medical information and track treatment progress.

#### Acceptance Criteria

1. WHEN a user clicks "Add Patient" THEN the system SHALL display a comprehensive clinical form with 9 major sections: patient data, gynecological history, lifestyle habits, urinary function, bowel function, sexual history, physical examination, intracavitary examination, and coloproctologic examination
2. WHEN a user submits a complete patient form THEN the system SHALL save all clinical data and redirect to the patient detail view
3. WHEN a user submits an incomplete patient form THEN the system SHALL display validation errors for missing required fields (name, age, consultation reason)
4. WHEN a user views a patient detail THEN the system SHALL display all clinical information organized by sections and appointment history
5. WHEN a user edits patient information THEN the system SHALL update the record with all clinical data and confirm the changes
6. WHEN a user deletes a patient THEN the system SHALL remove the patient and all associated appointments after confirmation
7. WHEN a patient is pregnant THEN the system SHALL automatically calculate and display current pregnancy weeks based on registration data
8. WHEN viewing clinical data THEN the system SHALL organize information into logical sections with appropriate medical terminology

### Requirement 4

**User Story:** As a healthcare professional, I want to create, view, edit, and delete appointments for each patient with PERFECT test assessment, so that I can track sessions and maintain detailed treatment evaluations.

#### Acceptance Criteria

1. WHEN a user creates an appointment THEN the system SHALL require date/time, session description, additional notes, and PERFECT test scores
2. WHEN a user views a patient's appointments THEN the system SHALL display them chronologically with all appointment details including PERFECT test results
3. WHEN a user edits an appointment THEN the system SHALL update the record and maintain the association with the patient
4. WHEN a user deletes an appointment THEN the system SHALL remove it after confirmation
5. WHEN filling the PERFECT test THEN the system SHALL provide integer fields for P, E, R, F scores and dropdown (Sí/No) fields for E, C, T scores
6. WHEN viewing appointment history THEN the system SHALL display PERFECT test scores in an organized format
7. WHEN creating appointments THEN the system SHALL NOT include evaluation progress field (removed from previous version)

### Requirement 5

**User Story:** As a healthcare professional, I want the application to have a clean, calming interface with efficient navigation, so that I can work effectively with long clinical forms.

#### Acceptance Criteria

1. WHEN the application loads THEN the system SHALL use the defined color palette (soft lilac #d1a0f8, soft pink #f9c5d1, white #ffffff, neutral #f4effa)
2. WHEN displaying interactive elements THEN the system SHALL use strong lilac #a86ef4 for buttons and details
3. WHEN showing error messages THEN the system SHALL use soft red #f87171 for error notifications
4. WHEN the application is viewed on different screen sizes THEN the system SHALL maintain usability (responsive design)
5. WHEN displaying the logo THEN the system SHALL show "MakiMotion" as text with appropriate styling
6. WHEN working with long clinical forms THEN the system SHALL provide floating action buttons that remain fixed during scrolling
7. WHEN using floating buttons THEN the system SHALL hide them on mobile devices and show standard form buttons instead
8. WHEN organizing clinical data THEN the system SHALL use clear section headers, subsections, and appropriate medical icons

### Requirement 6

**User Story:** As a system administrator, I want the application to be deployable on Render, so that it can be accessed reliably in production.

#### Acceptance Criteria

1. WHEN deploying to production THEN the system SHALL use PostgreSQL as the database
2. WHEN running in development THEN the system SHALL use SQLite as the database
3. WHEN deploying THEN the system SHALL include requirements.txt, Procfile, and render.yaml files
4. WHEN configuring the application THEN the system SHALL use environment variables for database connection and secret key
5. WHEN the application starts THEN the system SHALL connect to the appropriate database based on the environment

### Requirement 7

**User Story:** As a pelvic floor specialist, I want comprehensive clinical data collection and management, so that I can maintain detailed medical records for specialized treatment.

#### Acceptance Criteria

1. WHEN collecting patient data THEN the system SHALL include pregnancy tracking with automatic week calculation based on registration date and selected counting day
2. WHEN recording gynecological history THEN the system SHALL capture detailed obstetric history (G-A-P), delivery information, and surgical history
3. WHEN documenting urinary function THEN the system SHALL include detailed symptom checkboxes and incontinence classification (IUE, IUU, IUM)
4. WHEN recording bowel function THEN the system SHALL include Bristol scale, evacuation patterns, and incontinence assessment
5. WHEN documenting sexual history THEN the system SHALL capture relevant symptoms and incontinence during sexual activity
6. WHEN performing physical examination THEN the system SHALL record detailed findings including NCP tone assessment and reflex testing
7. WHEN conducting intracavitary examination THEN the system SHALL document MEA assessment, pain evaluation (EVA scale), and muscle function
8. WHEN performing coloproctologic examination THEN the system SHALL include Oxford test results, tone assessment, and pujo evaluation
9. WHEN organizing clinical data THEN the system SHALL provide "Others" fields in each section for additional notes

### Requirement 8

**User Story:** As a pelvic floor specialist, I want to use the PERFECT test assessment in appointments, so that I can systematically evaluate patient progress using standardized measurements.

#### Acceptance Criteria

1. WHEN creating or editing an appointment THEN the system SHALL provide a "Test PERFECT" section with 7 specific fields
2. WHEN filling P (Power) field THEN the system SHALL accept integer values for muscle power assessment
3. WHEN filling E (Endurance) field THEN the system SHALL accept integer values for endurance measurement
4. WHEN filling R (Repetitions) field THEN the system SHALL accept integer values for repetition count
5. WHEN filling F (Fast contractions) field THEN the system SHALL accept integer values for fast contraction assessment
6. WHEN filling E (Every contraction) field THEN the system SHALL provide dropdown with "Sí/No" options
7. WHEN filling C (Co-contraction) field THEN the system SHALL provide dropdown with "Sí/No" options
8. WHEN filling T (Timing) field THEN the system SHALL provide dropdown with "Sí/No" options
9. WHEN viewing appointment details THEN the system SHALL display PERFECT test results in a clear, organized format
10. WHEN the form is submitted THEN the system SHALL validate that PERFECT test fields are properly filled

### Requirement 9

**User Story:** As a healthcare professional, I want user management to be scalable, so that the system can grow with my practice needs.

#### Acceptance Criteria

1. WHEN the system is initially deployed THEN it SHALL support single-user access to their own patient data
2. WHEN the database is designed THEN it SHALL use a structure that can be extended to multi-user scenarios
3. WHEN a user accesses the system THEN they SHALL only see their own patients and appointments
4. WHEN using Django admin THEN administrators SHALL be able to view and manage system data during development
5. WHEN the system grows THEN the user model SHALL support extension to multi-tenant architecture