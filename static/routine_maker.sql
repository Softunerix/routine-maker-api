--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8
-- Dumped by pg_dump version 16.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO billy;

--
-- Name: classes; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.classes (
    id integer NOT NULL,
    name character varying(200),
    shift_availability integer[]
);


ALTER TABLE public.classes OWNER TO billy;

--
-- Name: classes_id_seq; Type: SEQUENCE; Schema: public; Owner: billy
--

CREATE SEQUENCE public.classes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_id_seq OWNER TO billy;

--
-- Name: classes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: billy
--

ALTER SEQUENCE public.classes_id_seq OWNED BY public.classes.id;


--
-- Name: school_data; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.school_data (
    id integer NOT NULL,
    num_days integer,
    num_shifts integer[]
);


ALTER TABLE public.school_data OWNER TO billy;

--
-- Name: school_data_id_seq; Type: SEQUENCE; Schema: public; Owner: billy
--

CREATE SEQUENCE public.school_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.school_data_id_seq OWNER TO billy;

--
-- Name: school_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: billy
--

ALTER SEQUENCE public.school_data_id_seq OWNED BY public.school_data.id;


--
-- Name: subjects; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.subjects (
    id integer NOT NULL,
    class_id integer,
    name character varying(200),
    num_days integer
);


ALTER TABLE public.subjects OWNER TO billy;

--
-- Name: subjects_id_seq; Type: SEQUENCE; Schema: public; Owner: billy
--

CREATE SEQUENCE public.subjects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subjects_id_seq OWNER TO billy;

--
-- Name: subjects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: billy
--

ALTER SEQUENCE public.subjects_id_seq OWNED BY public.subjects.id;


--
-- Name: teacher_daily_constraint; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.teacher_daily_constraint (
    id integer NOT NULL,
    teacher_id integer,
    num_shifts character varying[]
);


ALTER TABLE public.teacher_daily_constraint OWNER TO billy;

--
-- Name: teacher_daily_constraint_id_seq; Type: SEQUENCE; Schema: public; Owner: billy
--

CREATE SEQUENCE public.teacher_daily_constraint_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teacher_daily_constraint_id_seq OWNER TO billy;

--
-- Name: teacher_daily_constraint_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: billy
--

ALTER SEQUENCE public.teacher_daily_constraint_id_seq OWNED BY public.teacher_daily_constraint.id;


--
-- Name: teacher_subject; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.teacher_subject (
    id integer NOT NULL,
    teacher_id integer,
    subject_id integer
);


ALTER TABLE public.teacher_subject OWNER TO billy;

--
-- Name: teacher_subject_id_seq; Type: SEQUENCE; Schema: public; Owner: billy
--

CREATE SEQUENCE public.teacher_subject_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teacher_subject_id_seq OWNER TO billy;

--
-- Name: teacher_subject_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: billy
--

ALTER SEQUENCE public.teacher_subject_id_seq OWNED BY public.teacher_subject.id;


--
-- Name: teachers; Type: TABLE; Schema: public; Owner: billy
--

CREATE TABLE public.teachers (
    id integer NOT NULL,
    name character varying(200)
);


ALTER TABLE public.teachers OWNER TO billy;

--
-- Name: teachers_id_seq; Type: SEQUENCE; Schema: public; Owner: billy
--

CREATE SEQUENCE public.teachers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teachers_id_seq OWNER TO billy;

--
-- Name: teachers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: billy
--

ALTER SEQUENCE public.teachers_id_seq OWNED BY public.teachers.id;


--
-- Name: classes id; Type: DEFAULT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.classes ALTER COLUMN id SET DEFAULT nextval('public.classes_id_seq'::regclass);


--
-- Name: school_data id; Type: DEFAULT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.school_data ALTER COLUMN id SET DEFAULT nextval('public.school_data_id_seq'::regclass);


--
-- Name: subjects id; Type: DEFAULT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.subjects ALTER COLUMN id SET DEFAULT nextval('public.subjects_id_seq'::regclass);


--
-- Name: teacher_daily_constraint id; Type: DEFAULT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_daily_constraint ALTER COLUMN id SET DEFAULT nextval('public.teacher_daily_constraint_id_seq'::regclass);


--
-- Name: teacher_subject id; Type: DEFAULT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_subject ALTER COLUMN id SET DEFAULT nextval('public.teacher_subject_id_seq'::regclass);


--
-- Name: teachers id; Type: DEFAULT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teachers ALTER COLUMN id SET DEFAULT nextval('public.teachers_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.alembic_version (version_num) FROM stdin;
3390ca40607c
\.


--
-- Data for Name: classes; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.classes (id, name, shift_availability) FROM stdin;
1	Class 1	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
2	Class 2	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
3	Class ----3	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
\.


--
-- Data for Name: school_data; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.school_data (id, num_days, num_shifts) FROM stdin;
1	6	{3,3,3,3,3,3}
\.


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.subjects (id, class_id, name, num_days) FROM stdin;
1	1	Math	6
2	1	English	6
3	1	Bengali	6
4	2	Physics	3
5	2	H. Math	2
6	2	Math	6
9	3	BGS	3
10	3	ICT	3
11	3	Biology	3
\.


--
-- Data for Name: teacher_daily_constraint; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.teacher_daily_constraint (id, teacher_id, num_shifts) FROM stdin;
1	1	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
2	2	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
3	3	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
4	4	{{1,3},{1,3},{1,3},{1,3},{1,3},{1,3}}
\.


--
-- Data for Name: teacher_subject; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.teacher_subject (id, teacher_id, subject_id) FROM stdin;
1	1	2
2	1	3
3	1	5
4	2	1
5	2	6
6	3	10
7	3	11
8	4	4
9	4	9
\.


--
-- Data for Name: teachers; Type: TABLE DATA; Schema: public; Owner: billy
--

COPY public.teachers (id, name) FROM stdin;
1	Alice
2	Bob
3	Jolly
4	Mark
\.


--
-- Name: classes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: billy
--

SELECT pg_catalog.setval('public.classes_id_seq', 3, true);


--
-- Name: school_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: billy
--

SELECT pg_catalog.setval('public.school_data_id_seq', 1, true);


--
-- Name: subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: billy
--

SELECT pg_catalog.setval('public.subjects_id_seq', 11, true);


--
-- Name: teacher_daily_constraint_id_seq; Type: SEQUENCE SET; Schema: public; Owner: billy
--

SELECT pg_catalog.setval('public.teacher_daily_constraint_id_seq', 4, true);


--
-- Name: teacher_subject_id_seq; Type: SEQUENCE SET; Schema: public; Owner: billy
--

SELECT pg_catalog.setval('public.teacher_subject_id_seq', 9, true);


--
-- Name: teachers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: billy
--

SELECT pg_catalog.setval('public.teachers_id_seq', 4, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: classes classes_name_key; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.classes
    ADD CONSTRAINT classes_name_key UNIQUE (name);


--
-- Name: classes classes_pkey; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.classes
    ADD CONSTRAINT classes_pkey PRIMARY KEY (id);


--
-- Name: school_data school_data_pkey; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.school_data
    ADD CONSTRAINT school_data_pkey PRIMARY KEY (id);


--
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (id);


--
-- Name: teacher_daily_constraint teacher_daily_constraint_pkey; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_daily_constraint
    ADD CONSTRAINT teacher_daily_constraint_pkey PRIMARY KEY (id);


--
-- Name: teacher_daily_constraint teacher_daily_constraint_teacher_id_key; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_daily_constraint
    ADD CONSTRAINT teacher_daily_constraint_teacher_id_key UNIQUE (teacher_id);


--
-- Name: teacher_subject teacher_subject_pkey; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_subject
    ADD CONSTRAINT teacher_subject_pkey PRIMARY KEY (id);


--
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (id);


--
-- Name: subjects subjects_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id);


--
-- Name: teacher_daily_constraint teacher_daily_constraint_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_daily_constraint
    ADD CONSTRAINT teacher_daily_constraint_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES public.teachers(id);


--
-- Name: teacher_subject teacher_subject_subject_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_subject
    ADD CONSTRAINT teacher_subject_subject_id_fkey FOREIGN KEY (subject_id) REFERENCES public.subjects(id);


--
-- Name: teacher_subject teacher_subject_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: billy
--

ALTER TABLE ONLY public.teacher_subject
    ADD CONSTRAINT teacher_subject_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES public.teachers(id);


--
-- PostgreSQL database dump complete
--

