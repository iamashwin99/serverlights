from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingsModel")


@_attrs_define
class SettingsModel:
    """Model for protocol settings.

    Attributes:
        dali_ping (Union[Unset, bool]): Enable/Disable the periodic sending of a ping command over the DALI bus Default:
            False.
    """

    dali_ping: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dali_ping = self.dali_ping

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dali_ping is not UNSET:
            field_dict["dali_ping"] = dali_ping

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dali_ping = d.pop("dali_ping", UNSET)

        settings_model = cls(
            dali_ping=dali_ping,
        )

        settings_model.additional_properties = d
        return settings_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
