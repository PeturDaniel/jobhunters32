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


const filterCompany = (unique_employers) => {
    const company = unique_employers.value;
    const jobs = document.querySelectorAll(".well_job");

    jobs.forEach((job) => {
        job_title = job.innerText.trim().split('\n')
        console.log(job_title)
        if (job_title[1].includes(company)) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}
