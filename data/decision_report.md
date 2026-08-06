# Decision Report

- generated_at: 2026-08-06T11:56:43.494989+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10591**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=10591, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.24% | **+0.43%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +4.23% | **+1.69%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.76% | **+0.69%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.95% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$596.41** / 初期 $100.00 (+496.41%)
- 確定: 3795件 (Win 1203 / Loss 1249 / Flat 1343) / skip 3357件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $596.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.04** / 初期 $100.00 (+43.04%)
- 確定: 1424件 (Win 396 / Loss 336 / Flat 692) / skip 2578件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0179 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $143.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 922件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000117 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T11:56:29.014705+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64573.9
- Funnel: target 955 → liquid 190 → pre 50 → checked 50 → surge 6 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.4 >= 65=1, 4h RSI 95.5 >= 65=1, 4h RSI 69.7 >= 65=1, 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +62.87% | $74,003,550.57 |
| CTSI/USDT:USDT | +57.92% | $1,565,050.78 |
| HFT/USDT:USDT | +50.33% | $4,815,522.04 |
| CASHCAT/USDT:USDT | +44.44% | $1,382,377.53 |
| ZBT/USDT:USDT | +41.71% | $3,471,227.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.41% | +4.44% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.39% | +4.42% |
| RESOLV/USDT:USDT | below_1h_threshold | +3.55% | +3.58% |
| UB/USDT:USDT | below_1h_threshold | +2.85% | +2.88% |
| ALLO/USDT:USDT | below_1h_threshold | +2.15% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
