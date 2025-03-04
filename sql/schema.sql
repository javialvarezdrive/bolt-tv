-- SQL script to create the database schema in Supabase

-- Create the 'agents' table
CREATE TABLE IF NOT EXISTS agents (
    id SERIAL PRIMARY KEY,
    nip VARCHAR(6) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellidos VARCHAR(25