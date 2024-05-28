import React from "react";
import { render, fireEvent } from "@testing-library/react";
import SearchUsers from "./SearchUsers";

describe("SearchUsers Component", () => {
  it("renders without errors", () => {
    render(<SearchUsers />);
  });

  it("updates search input value on change", () => {
    const { getByPlaceholderText } = render(<SearchUsers />);
    const inputElement = getByPlaceholderText("Search users..");
    fireEvent.change(inputElement, { target: { value: "John" } });
    expect(inputElement.value).toBe("John");
  });

  it("clears search input on icon click", () => {
    const { getByTestId, getByPlaceholderText } = render(<SearchUsers />);
    const inputElement = getByPlaceholderText("Search users..");
    fireEvent.change(inputElement, { target: { value: "John" } });
    const iconElement = getByTestId("close-icon");
    fireEvent.click(iconElement);
    expect(inputElement.value).toBe("");
  });
});
