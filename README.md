# jobhunters32

X Layout site
    X Navigation bar 
    X Footer

X Edit profile
    X Name
    X Profile image

● Job offer site - lists available job offerings
    ○ Filter by category, e.g. Software Engineering, Data Science, etc.
    ○ Filter by company
    ○ Filter by already applied job offerings
    ~ Search (based on name)
    ○ Order by
        ■ Date of offering
        ■ Due date of offering

● Job offering detail site - shows more information about a certain product
    X Title of job offering
    X Information whether it is a full time or part time job
    ? Location of the job offering (address of the company associated with the job
    offering)
    X Job category
    X Due date
    X Starting date
    ? Description of job offering (displayed as HTML)
    X Company information
        X Name
        X Address
        X Link to company page
    ~ Button to apply for the job offering / Status of the job application
        X If the job offering has not been applied for the button should say “Apply”
        ■ If the job offering has been applied for instead of displaying a button -
            information should be displayed about when the job offering was applied
            for along with the status of the job application.

● Company detail site
    X Title of the company
    X Address of the company
    X Logo of the company
    X Cover image of the company
    ? Description of the company (displayed as HTML)
    X A list of all non due job offerings the company has
        X Each job offering listed should provide a link to navigate to the link
            offering

● Job applications page
    ○ A list of all job applications
    ○ Each job application should have the following:
        ■ Job title
        ■ Date of application
        ■ Status of application
        ■ Company
        ■ Full time / part time

● Applying for a job - should be a multi step phase
    ○ Contact information
        ■ Full name
        ■ Street name
        ■ House number
        ■ City
        ■ Country (displayed as a <select> HTML element)
        ■ Postal code
    ○ Cover letter
        ■ A text section to write a cover letter
    ○ Experiences
        ■ A list of experiences related to previous jobs
            ● Place of work
            ● Role
            ● Start date
            ● End date
    ○ Recommendations
        ■ A list of contacts which can be contacted for recommendations
            ● Name
            ● Email address
            ● Phone number
            ● Checkbox whether they may be contacted or not
            ● Role, e.g. Manager at Reykjavik Seafood
    ○ Review - this is a read-only site where a user can review what he is buying and
        what information he has already typed in
    ○ Confirmation - this is the final step where a user gets a confirmation that
        everything was successful, you cannot go back when you have arrived to this
        step
    ○ Easy navigation between steps - it should be easy to navigate between the steps
        in the job application phase