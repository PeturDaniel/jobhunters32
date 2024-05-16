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

document.getElementById('order_publish_date').addEventListener('click', function () {
    updateURL('publish_date');
    orderJobs('publish_date');
})

document.getElementById('order_due_date').addEventListener('click', function () {
    updateURL('due_date');
    orderJobs('due_date');
})

const orderJobs = (order_by) => {
    console.log('Fetching jobs sorted by:', order_by)
    fetch('/lausstorf/?order_by=' + {order_by})
        .then(response =>
            response.text()
        )
        .then(data => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, 'text/html');
            const ordered_job_offers = doc.querySelector('#job_offers_for')
            ordered_job_offers.innerHTML = data;
        })

}

function updateURL(order_by) {
    const url = new URL(window.location.href);
    url.searchParams.set('order_by', order_by);
    window.history.pushState({}, '', url);
}

const filterApplied = () => {
    const checkbox = document.getElementById("checkbox")
    const bla = document.querySelectorAll(".application")
    const applied_jobs = bla[0].innerText.slice(2, -1).split(", ")
    const jobs = document.querySelectorAll(".well_job");

    jobs.forEach((job) => {
        if (checkbox.checked == true && applied_jobs.indexOf(job.id) !== -1) {
            job.classList.remove("hidden")
        }
        else if (checkbox.checked == false) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}
