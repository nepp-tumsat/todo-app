alias todo-back='docker-compose up --build backend'
alias todo-front='docker-compose up --build fronted'
alias todo-front-bash='docker exec -it todo_front bash'
alias todo-back-bash='docker exec -it todo_back bash'

alias init_migration="docker exec -it todo_back bash -c 'sh ./scripts/init.sh'"