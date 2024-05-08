function findMaxK(nums: number[]): number{
     
    const arr:string[] =nums.sort((a,b)=>b-a).map(String)
    for(let i=0; i<arr.length;i++){
        if(arr.includes(`-${arr[i]}`)){
            return Number(arr[i]);
        }
    }   
    return -1
    };