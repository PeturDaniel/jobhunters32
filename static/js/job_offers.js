const jobs = document.getElementsByClassName("job_offers")

const doSearchJobs = () => {
    const jobs = document.querySelectorAll(".well_job");
    const query = document.getElementById("search-box").value;

    jobs.forEach((job) => {
        job_title = job.innerText.trim().split('\n')
        if (job_title[0].toLowerCase().includes(query.trim().toLowerCase())) {
            job.classList.remove("hidden");
        }
        else {
            job.classList.add("hidden");
        }
    });
};

const filterCompany = () => {
    const companies = document.querySelectorAll("#companySelect")
    if ()
    console.log(companies)
}
