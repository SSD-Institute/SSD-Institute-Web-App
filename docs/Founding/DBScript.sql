
/* Stretch goal and most likely will not get to this, but it is theoretical for future sprints.*/

CREATE DATABASE SSDInstituteDB;
USE SSDInstituteDB;

CREATE TABLE Role (
  role_id INT PRIMARY KEY AUTO_INCREMENT,
  role_name VARCHAR(50) NOT NULL,
  permissions TEXT NOT NULL
);

CREATE TABLE User (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  role_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash CHAR(64) NOT NULL,
  join_date DATE NOT NULL,
  status ENUM('active', 'inactive', 'banned') DEFAULT 'active',
  FOREIGN KEY (role_id) REFERENCES Role(role_id)
);

CREATE TABLE Document (
  doc_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200) NOT NULL,
  author_id INT NOT NULL,
  description TEXT,
  data_type VARCHAR(50),
  created_at DATETIME NOT NULL,
  updated_at DATETIME,
  FOREIGN KEY (author_id) REFERENCES User(user_id)
);

CREATE TABLE Dataset (
  dataset_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200) NOT NULL,
  source VARCHAR(200),
  created_at DATETIME NOT NULL,
  owner_id INT NOT NULL,
  license VARCHAR(100),
  provenance TEXT,
  tags VARCHAR(200),
  FOREIGN KEY (owner_id) REFERENCES User(user_id)
);

CREATE TABLE Version (
  version_id INT PRIMARY KEY AUTO_INCREMENT,
  dataset_id INT NOT NULL,
  version_number VARCHAR(10),
  changelog TEXT,
  created_at DATETIME NOT NULL,
  FOREIGN KEY (dataset_id) REFERENCES Dataset(dataset_id)
);

CREATE TABLE CivicImpact (
  impact_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(150) NOT NULL,
  description TEXT,
  impact_score DECIMAL(5,2),
  related_region VARCHAR(100),
  updated_at DATETIME
);

CREATE TABLE Concept (
  concept_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(150) NOT NULL,
  description TEXT,
  civic_impact_id INT,
  created_at DATETIME NOT NULL,
  FOREIGN KEY (civic_impact_id) REFERENCES CivicImpact(impact_id)
);

CREATE TABLE Visualization (
  vis_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  dataset_id INT,
  concept_id INT,
  vis_type VARCHAR(50),
  data_source VARCHAR(200),
  created_at DATETIME NOT NULL,
  updated_at DATETIME,
  status ENUM('draft', 'published', 'archived') DEFAULT 'draft',
  FOREIGN KEY (user_id) REFERENCES User(user_id),
  FOREIGN KEY (dataset_id) REFERENCES Dataset(dataset_id),
  FOREIGN KEY (concept_id) REFERENCES Concept(concept_id)
);

CREATE TABLE Simulation (
  sim_id INT PRIMARY KEY AUTO_INCREMENT,
  vis_id INT NOT NULL,
  parameters TEXT,
  results TEXT,
  timestamp DATETIME,
  FOREIGN KEY (vis_id) REFERENCES Visualization(vis_id)
);

CREATE TABLE Feedback (
  feed_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  vis_id INT NOT NULL,
  rating TINYINT CHECK (rating BETWEEN 1 AND 5),
  comment TEXT,
  created_at DATETIME,
  FOREIGN KEY (user_id) REFERENCES User(user_id),
  FOREIGN KEY (vis_id) REFERENCES Visualization(vis_id)
);

CREATE TABLE BlogPost (
  blog_id INT PRIMARY KEY AUTO_INCREMENT,
  author_id INT NOT NULL,
  doc_id INT,
  title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  created_at DATETIME NOT NULL,
  category VARCHAR(50),
  status ENUM('draft', 'review', 'published')
)
