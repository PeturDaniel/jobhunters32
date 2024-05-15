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
        if (job_title[2].includes(company)) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}

const filterCategory = (unique_categories) => {
    const category = unique_categories.value;
    const jobs = document.querySelectorAll(".well_job");

    jobs.forEach((job) => {
        job_category = job.innerText.trim().split('\n')
        if (job_category[1].includes(category)) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}
