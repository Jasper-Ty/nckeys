mod word;

pub trait Degree {
    fn degree(&self) -> usize;
}

pub use word::*;