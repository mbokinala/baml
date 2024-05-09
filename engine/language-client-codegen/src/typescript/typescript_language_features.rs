use crate::dir_writer::LanguageFeatures;
use internal_baml_core::ir::TypeValue;

#[derive(Default)]
pub(super) struct TypescriptLanguageFeatures {}

impl LanguageFeatures for TypescriptLanguageFeatures {
    fn content_prefix(&self) -> &'static str {
        // "typed: strict" is set on a per-file basis in Typescript
        r#"
/*************************************************************************************************

Welcome to Baml! To use this generated code, please run one of the following:

$ npm install baml_ts
$ yarn add baml_ts
$ pnpm add baml_ts

*************************************************************************************************/

// This file was generated by BAML: do not edit it. Instead, edit the BAML
// files and re-generate this code.
//
// tslint:disable
// @ts-nocheck
// biome-ignore format: autogenerated code
/* eslint-disable */
        "#
        .trim()
    }

    fn to_file_path(&self, name: &str) -> std::path::PathBuf {
        std::path::PathBuf::from(name.to_lowercase()).with_extension("ts")
    }
}

pub(super) trait ToTypescript {
    fn to_typescript(&self) -> String;
}

impl ToTypescript for TypeValue {
    fn to_typescript(&self) -> String {
        match self {
            TypeValue::Bool => "boolean".to_string(),
            TypeValue::Float => "number".to_string(),
            TypeValue::Int => "number".to_string(),
            TypeValue::String => "string".to_string(),
            TypeValue::Null => "null".to_string(),
            TypeValue::Char => "string".to_string(),
            TypeValue::Image => "baml_ts.Image".to_string(),
        }
    }
}
