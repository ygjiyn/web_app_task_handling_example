console.log('Hello, this is resultDetails.');

const taskResultElement = document.getElementById('taskResult') as HTMLDivElement;
const taskStatusElement = document.getElementById('taskStatus') as HTMLDivElement;
const taskId = taskResultElement.dataset.taskId;

function delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function updateTaskResult(totalNumOfTry: number = 6, intervalMs: number = 10000) {
    for (let i = 0; i < totalNumOfTry; ++i) {
        const taskResultResponse = await fetch(`/api/get_task_result_by_id/${taskId}/`);
        const taskResult = await taskResultResponse.json();
        taskResultElement.textContent = `Result: ${taskResult.result}, Status: ${taskResult.status}`;
        taskStatusElement.textContent = taskResult.status;
        await delay(intervalMs);
    }
}

updateTaskResult();
