
```sql
CREATE TABLE `weather` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(100) NOT NULL,
  `temperature` decimal(10,0) NOT NULL,
  `wind_speed` decimal(10,0) NOT NULL,
  `date` timestamp NOT NULL,
  PRIMARY KEY (`id`)
)
```

### Start the project
```shell
docker-compose up
```

### Debugging
##### Running the code:
1. Open a shell
```shell
docker-compose exec app bash
```
2. Run the script (do this as many times as necessary when testing)
```shell
python main.py
```

#### Open Mysql Shell. Password is "password"
```shell
docker-compose exec db mysql -u app -p app 
```
