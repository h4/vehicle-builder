--
-- PostgreSQL database dump
--

-- Dumped from database version 11.0 (Debian 11.0-1.pgdg90+2)
-- Dumped by pg_dump version 11.0 (Debian 11.0-1.pgdg90+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: ltree; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS ltree WITH SCHEMA public;


--
-- Name: EXTENSION ltree; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION ltree IS 'data type for hierarchical tree-like structures';


--
-- Name: productionstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.productionstatus AS ENUM (
    'UNKNOWN',
    'DESIGN',
    'PRODUCTION',
    'ORDERED',
    'IN_STOCK',
    'DEPRECATED'
);


ALTER TYPE public.productionstatus OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: component_properties; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.component_properties (
    id integer NOT NULL,
    property_name character varying(32),
    value character varying(32),
    component_id integer NOT NULL
);


ALTER TABLE public.component_properties OWNER TO postgres;

--
-- Name: component_properties_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.component_properties_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.component_properties_id_seq OWNER TO postgres;

--
-- Name: component_properties_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.component_properties_id_seq OWNED BY public.component_properties.id;


--
-- Name: components; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.components (
    id integer NOT NULL,
    title character varying(32),
    cad_model character varying(32),
    sku character varying(16),
    provider character varying(16),
    weight numeric(3,0),
    price numeric(2,0),
    production_status public.productionstatus NOT NULL
);


ALTER TABLE public.components OWNER TO postgres;

--
-- Name: components_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.components_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.components_id_seq OWNER TO postgres;

--
-- Name: components_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.components_id_seq OWNED BY public.components.id;


--
-- Name: features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.features (
    id integer NOT NULL,
    title character varying(32),
    parent_id integer NOT NULL
);


ALTER TABLE public.features OWNER TO postgres;

--
-- Name: features_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.features_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.features_id_seq OWNER TO postgres;

--
-- Name: features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.features_id_seq OWNED BY public.features.id;


--
-- Name: functions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.functions (
    id integer NOT NULL,
    title character varying(32),
    feature_id integer NOT NULL
);


ALTER TABLE public.functions OWNER TO postgres;

--
-- Name: functions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.functions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.functions_id_seq OWNER TO postgres;

--
-- Name: functions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.functions_id_seq OWNED BY public.functions.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.groups (
    id integer NOT NULL,
    title character varying(32),
    parent_id integer,
    path public.ltree,
    is_set boolean DEFAULT false NOT NULL,
    CONSTRAINT ck_groups__ck_groups__set_has_parent CHECK (((is_set = false) OR (parent_id IS NOT NULL)))
);


ALTER TABLE public.groups OWNER TO postgres;

--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.groups_id_seq OWNER TO postgres;

--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: interfaces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.interfaces (
    id integer NOT NULL,
    title character varying(32)
);


ALTER TABLE public.interfaces OWNER TO postgres;

--
-- Name: interfaces_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.interfaces_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.interfaces_id_seq OWNER TO postgres;

--
-- Name: interfaces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.interfaces_id_seq OWNED BY public.interfaces.id;


--
-- Name: vehicle_configurations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehicle_configurations (
    id integer NOT NULL,
    vehicle_id integer NOT NULL,
    feature_id integer NOT NULL
);


ALTER TABLE public.vehicle_configurations OWNER TO postgres;

--
-- Name: vehicle_configurations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vehicle_configurations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vehicle_configurations_id_seq OWNER TO postgres;

--
-- Name: vehicle_configurations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vehicle_configurations_id_seq OWNED BY public.vehicle_configurations.id;


--
-- Name: vehicle_connections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehicle_connections (
    id integer NOT NULL,
    vehicle_function_id integer NOT NULL,
    component_id integer NOT NULL,
    interface_id integer NOT NULL
);


ALTER TABLE public.vehicle_connections OWNER TO postgres;

--
-- Name: vehicle_connections_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vehicle_connections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vehicle_connections_id_seq OWNER TO postgres;

--
-- Name: vehicle_connections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vehicle_connections_id_seq OWNED BY public.vehicle_connections.id;


--
-- Name: vehicle_functions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehicle_functions (
    id integer NOT NULL,
    vehicle_id integer NOT NULL,
    function_id integer NOT NULL,
    is_frozen boolean DEFAULT false NOT NULL
);


ALTER TABLE public.vehicle_functions OWNER TO postgres;

--
-- Name: vehicle_functions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vehicle_functions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vehicle_functions_id_seq OWNER TO postgres;

--
-- Name: vehicle_functions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vehicle_functions_id_seq OWNED BY public.vehicle_functions.id;


--
-- Name: vehicle_properties; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehicle_properties (
    id integer NOT NULL,
    property_name character varying(32),
    value character varying(32),
    vehicle_id integer NOT NULL
);


ALTER TABLE public.vehicle_properties OWNER TO postgres;

--
-- Name: vehicle_properties_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vehicle_properties_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vehicle_properties_id_seq OWNER TO postgres;

--
-- Name: vehicle_properties_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vehicle_properties_id_seq OWNED BY public.vehicle_properties.id;


--
-- Name: vehicles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehicles (
    id integer NOT NULL,
    title character varying(32),
    range integer
);


ALTER TABLE public.vehicles OWNER TO postgres;

--
-- Name: vehicles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vehicles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vehicles_id_seq OWNER TO postgres;

--
-- Name: vehicles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vehicles_id_seq OWNED BY public.vehicles.id;


--
-- Name: component_properties id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component_properties ALTER COLUMN id SET DEFAULT nextval('public.component_properties_id_seq'::regclass);


--
-- Name: components id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.components ALTER COLUMN id SET DEFAULT nextval('public.components_id_seq'::regclass);


--
-- Name: features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features ALTER COLUMN id SET DEFAULT nextval('public.features_id_seq'::regclass);


--
-- Name: functions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.functions ALTER COLUMN id SET DEFAULT nextval('public.functions_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Name: interfaces id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interfaces ALTER COLUMN id SET DEFAULT nextval('public.interfaces_id_seq'::regclass);


--
-- Name: vehicle_configurations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_configurations ALTER COLUMN id SET DEFAULT nextval('public.vehicle_configurations_id_seq'::regclass);


--
-- Name: vehicle_connections id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_connections ALTER COLUMN id SET DEFAULT nextval('public.vehicle_connections_id_seq'::regclass);


--
-- Name: vehicle_functions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_functions ALTER COLUMN id SET DEFAULT nextval('public.vehicle_functions_id_seq'::regclass);


--
-- Name: vehicle_properties id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_properties ALTER COLUMN id SET DEFAULT nextval('public.vehicle_properties_id_seq'::regclass);


--
-- Name: vehicles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicles ALTER COLUMN id SET DEFAULT nextval('public.vehicles_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
9f6b21727930
\.


--
-- Data for Name: component_properties; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.component_properties (id, property_name, value, component_id) FROM stdin;
\.


--
-- Data for Name: components; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.components (id, title, cad_model, sku, provider, weight, price, production_status) FROM stdin;
2	BMS Module	a	abcd123	Lao	1	1	DESIGN
1	Batteries	a	abcd125	Lao	1	1	DESIGN
3	Inverter	a	abcded	Zinghao	1	1	IN_STOCK
\.


--
-- Data for Name: features; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.features (id, title, parent_id) FROM stdin;
1	HV Battery	11
2	HV Battery Management	12
3	Base Steering	17
4	Progressive Steering	17
5	HV Battery Maintenance	12
6	Drivetrain	13
\.


--
-- Data for Name: functions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.functions (id, title, feature_id) FROM stdin;
1	HV Battery	1
2	HV Battery Current Management	2
3	HV Battery Voltage Management	2
4	HV Battery Management	2
6	Traction Inverter Control	6
7	Traction Inverter Coolant IN	6
8	Traction Inverter Coolant OUT	6
10	Motor Stator Temperature	6
11	Motor Resolver	6
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.groups (id, title, parent_id, path, is_set) FROM stdin;
1	Powertrain	\N	1	f
2	Suspension	\N	2	f
3	Steering	\N	3	f
12	HV Battery Management	1	1.2	f
13	Drivetrain	1	1.3	f
11	HV Battery	1	1.1	f
15	Pneumatic	2	2.2	t
16	Mechanical	3	3.1	t
17	Electrical	3	3.2	t
14	Hydraulic	2	2.1	t
\.


--
-- Data for Name: interfaces; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.interfaces (id, title) FROM stdin;
1	CAN
2	LIN
\.


--
-- Data for Name: vehicle_configurations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehicle_configurations (id, vehicle_id, feature_id) FROM stdin;
\.


--
-- Data for Name: vehicle_connections; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehicle_connections (id, vehicle_function_id, component_id, interface_id) FROM stdin;
1	1	1	1
2	2	2	2
4	2	2	2
\.


--
-- Data for Name: vehicle_functions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehicle_functions (id, vehicle_id, function_id, is_frozen) FROM stdin;
1	1	1	f
2	1	2	f
3	1	3	f
4	1	4	f
5	1	6	f
6	1	7	f
7	1	8	f
8	1	10	f
9	1	11	f
\.


--
-- Data for Name: vehicle_properties; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehicle_properties (id, property_name, value, vehicle_id) FROM stdin;
1	color	red	1
2	engine_type	v8	1
4	wheels_count	4	1
\.


--
-- Data for Name: vehicles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehicles (id, title, range) FROM stdin;
1	My Car	100500
\.


--
-- Name: component_properties_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.component_properties_id_seq', 1, false);


--
-- Name: components_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.components_id_seq', 3, true);


--
-- Name: features_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.features_id_seq', 6, true);


--
-- Name: functions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.functions_id_seq', 11, true);


--
-- Name: groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.groups_id_seq', 17, true);


--
-- Name: interfaces_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.interfaces_id_seq', 2, true);


--
-- Name: vehicle_configurations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vehicle_configurations_id_seq', 1, false);


--
-- Name: vehicle_connections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vehicle_connections_id_seq', 4, true);


--
-- Name: vehicle_functions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vehicle_functions_id_seq', 10, true);


--
-- Name: vehicle_properties_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vehicle_properties_id_seq', 4, true);


--
-- Name: vehicles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vehicles_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: component_properties pk_component_properties; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component_properties
    ADD CONSTRAINT pk_component_properties PRIMARY KEY (id);


--
-- Name: components pk_components; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.components
    ADD CONSTRAINT pk_components PRIMARY KEY (id);


--
-- Name: features pk_features; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT pk_features PRIMARY KEY (id);


--
-- Name: functions pk_functions; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.functions
    ADD CONSTRAINT pk_functions PRIMARY KEY (id);


--
-- Name: groups pk_groups; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT pk_groups PRIMARY KEY (id);


--
-- Name: interfaces pk_interfaces; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interfaces
    ADD CONSTRAINT pk_interfaces PRIMARY KEY (id);


--
-- Name: vehicle_configurations pk_vehicle_configurations; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_configurations
    ADD CONSTRAINT pk_vehicle_configurations PRIMARY KEY (id);


--
-- Name: vehicle_connections pk_vehicle_connections; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_connections
    ADD CONSTRAINT pk_vehicle_connections PRIMARY KEY (id);


--
-- Name: vehicle_functions pk_vehicle_functions; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_functions
    ADD CONSTRAINT pk_vehicle_functions PRIMARY KEY (id);


--
-- Name: vehicle_properties pk_vehicle_properties; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_properties
    ADD CONSTRAINT pk_vehicle_properties PRIMARY KEY (id);


--
-- Name: vehicles pk_vehicles; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicles
    ADD CONSTRAINT pk_vehicles PRIMARY KEY (id);


--
-- Name: component_properties uq_component_properties__component_property_name; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component_properties
    ADD CONSTRAINT uq_component_properties__component_property_name UNIQUE (component_id, value);


--
-- Name: components uq_components__sku; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.components
    ADD CONSTRAINT uq_components__sku UNIQUE (sku);


--
-- Name: vehicle_configurations uq_vehicle_configurations__vehicle_feature; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_configurations
    ADD CONSTRAINT uq_vehicle_configurations__vehicle_feature UNIQUE (vehicle_id, feature_id);


--
-- Name: vehicle_functions uq_vehicle_configurations__vehicle_function; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_functions
    ADD CONSTRAINT uq_vehicle_configurations__vehicle_function UNIQUE (vehicle_id, function_id);


--
-- Name: vehicle_properties uq_vehicle_properties__vehicle_property_name; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_properties
    ADD CONSTRAINT uq_vehicle_properties__vehicle_property_name UNIQUE (vehicle_id, value);


--
-- Name: ix_component_properties_component_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_component_properties_component_id ON public.component_properties USING btree (component_id);


--
-- Name: ix_components_production_status; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_components_production_status ON public.components USING btree (production_status);


--
-- Name: ix_features_parent_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_features_parent_id ON public.features USING btree (parent_id);


--
-- Name: ix_features_tree_path_btree; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_features_tree_path_btree ON public.groups USING btree (path);


--
-- Name: ix_features_tree_path_gist; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_features_tree_path_gist ON public.groups USING gist (path);


--
-- Name: ix_functions_feature_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_functions_feature_id ON public.functions USING btree (feature_id);


--
-- Name: ix_groups_parent_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_groups_parent_id ON public.groups USING btree (parent_id);


--
-- Name: component_properties fk_component_properties__component_id__components; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.component_properties
    ADD CONSTRAINT fk_component_properties__component_id__components FOREIGN KEY (component_id) REFERENCES public.components(id) ON DELETE CASCADE;


--
-- Name: features fk_features__parent_id__groups; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT fk_features__parent_id__groups FOREIGN KEY (parent_id) REFERENCES public.groups(id) ON DELETE CASCADE;


--
-- Name: functions fk_functions__feature_id__features; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.functions
    ADD CONSTRAINT fk_functions__feature_id__features FOREIGN KEY (feature_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: groups fk_groups__parent_id__groups; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT fk_groups__parent_id__groups FOREIGN KEY (parent_id) REFERENCES public.groups(id) ON DELETE CASCADE;


--
-- Name: vehicle_configurations fk_vehicle_configurations__feature_id__features; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_configurations
    ADD CONSTRAINT fk_vehicle_configurations__feature_id__features FOREIGN KEY (feature_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: vehicle_configurations fk_vehicle_configurations__vehicle_id__vehicles; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_configurations
    ADD CONSTRAINT fk_vehicle_configurations__vehicle_id__vehicles FOREIGN KEY (vehicle_id) REFERENCES public.vehicles(id) ON DELETE CASCADE;


--
-- Name: vehicle_connections fk_vehicle_connections__component_id__components; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_connections
    ADD CONSTRAINT fk_vehicle_connections__component_id__components FOREIGN KEY (component_id) REFERENCES public.components(id) ON DELETE CASCADE;


--
-- Name: vehicle_connections fk_vehicle_connections__interface_id__interfaces; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_connections
    ADD CONSTRAINT fk_vehicle_connections__interface_id__interfaces FOREIGN KEY (interface_id) REFERENCES public.interfaces(id) ON DELETE CASCADE;


--
-- Name: vehicle_connections fk_vehicle_connections__vehicle_function_id__vehicle_functions; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_connections
    ADD CONSTRAINT fk_vehicle_connections__vehicle_function_id__vehicle_functions FOREIGN KEY (vehicle_function_id) REFERENCES public.vehicle_functions(id) ON DELETE CASCADE;


--
-- Name: vehicle_functions fk_vehicle_functions__function_id__functions; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_functions
    ADD CONSTRAINT fk_vehicle_functions__function_id__functions FOREIGN KEY (function_id) REFERENCES public.functions(id) ON DELETE CASCADE;


--
-- Name: vehicle_functions fk_vehicle_functions__vehicle_id__vehicles; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_functions
    ADD CONSTRAINT fk_vehicle_functions__vehicle_id__vehicles FOREIGN KEY (vehicle_id) REFERENCES public.vehicles(id) ON DELETE CASCADE;


--
-- Name: vehicle_properties fk_vehicle_properties__vehicle_id__vehicles; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vehicle_properties
    ADD CONSTRAINT fk_vehicle_properties__vehicle_id__vehicles FOREIGN KEY (vehicle_id) REFERENCES public.vehicles(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

