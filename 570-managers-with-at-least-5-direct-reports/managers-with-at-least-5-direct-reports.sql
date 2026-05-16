select e.name from Employee as e 
join
Employee as emp
on 
e.id=emp.managerId
group by e.id,e.name
having count(*)>=5