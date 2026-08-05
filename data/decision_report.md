# Decision Report

- generated_at: 2026-08-05T14:41:29.817787+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10412**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=10412, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.71% | **+1.54%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.58% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.00% | **+0.70%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.37%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.18% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3204件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.55** / 初期 $100.00 (+43.55%)
- 確定: 1319件 (Win 374 / Loss 310 / Flat 635) / skip 2504件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0660 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $143.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.15** / 初期 $100.00 (+18.15%)
- 確定: 1140件 (Win 365 / Loss 442 / Flat 333) / pending 2件 / skip 747件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.15

## 6. Latest Market Context

- 更新: 2026-08-05T14:41:18.717504+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=64297.8
- Funnel: target 948 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=1, 4h RSI 73.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +85.67% | $29,032,764.54 |
| BLESS/USDT:USDT | +85.37% | $63,187,983.99 |
| HFT/USDT:USDT | +65.73% | $4,517,771.70 |
| CASHCAT/USDT:USDT | +38.61% | $1,016,186.17 |
| BICO/USDT:USDT | +28.56% | $16,645,772.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +4.71% | +4.85% |
| AMGNSTOCK/USDT:USDT | below_1h_threshold | +4.54% | +4.68% |
| 1000RATS/USDT:USDT | below_1h_threshold | +4.42% | +4.55% |
| EVAA/USDT:USDT | below_1h_threshold | +3.10% | +3.24% |
| NVIDIA/USDT:USDT | below_1h_threshold | +2.79% | +2.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
