# Decision Report

- generated_at: 2026-08-25T10:41:25.845337+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12596**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=12596, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.02% | **+0.36%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.02%** |
| LIMIT_BB3S | 2/15 | 13.3% | -0.89% | **-0.12%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.35% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.84% | **+0.83%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.26% | **+0.82%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.75% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.22% | **+0.43%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.38% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.34** / 初期 $100.00 (+608.34%)
- 確定: 4576件 (Win 1392 / Loss 1500 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $708.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4030件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0339 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.26** / 初期 $100.00 (+15.26%)
- 確定: 1926件 (Win 564 / Loss 733 / Flat 629) / pending 6件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000147 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.26

## 6. Latest Market Context

- 更新: 2026-08-25T10:41:14.298828+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79270.4
- Funnel: target 1023 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +74.15% | $4,781,552.72 |
| JIMOTHY/USDT:USDT | +61.52% | $1,362,601.12 |
| ONG/USDT:USDT | +39.90% | $7,617,514.38 |
| TAC/USDT:USDT | +37.75% | $6,276,815.85 |
| BR/USDT:USDT | +19.36% | $3,441,094.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +4.89% | +4.75% |
| H/USDT:USDT | below_1h_threshold | +4.19% | +4.05% |
| TAC/USDT:USDT | below_1h_threshold | +3.38% | +3.24% |
| SNXX/USDT:USDT | below_1h_threshold | +3.01% | +2.87% |
| SOXL/USDT:USDT | below_1h_threshold | +2.03% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
