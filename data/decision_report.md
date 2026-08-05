# Decision Report

- generated_at: 2026-08-05T11:31:27.336709+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10400**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=10400, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +2.43% | **+1.70%** |
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.84% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.61% | **+0.21%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.10% | **-0.05%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.38% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3192件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.35** / 初期 $100.00 (+43.35%)
- 確定: 1316件 (Win 372 / Loss 310 / Flat 634) / skip 2495件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0522 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.36** / 初期 $100.00 (+18.36%)
- 確定: 1138件 (Win 365 / Loss 441 / Flat 332) / pending 4件 / skip 735件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000082 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $118.36

## 6. Latest Market Context

- 更新: 2026-08-05T11:31:16.392217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64027.1
- Funnel: target 945 → liquid 179 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.0 >= 65=1, 4h RSI 86.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +96.53% | $45,282,416.42 |
| HFT/USDT:USDT | +82.31% | $3,543,866.64 |
| HEI/USDT:USDT | +82.16% | $22,171,987.70 |
| CASHCAT/USDT:USDT | +47.01% | $1,009,652.39 |
| GRVT/USDT:USDT | +29.83% | $7,094,112.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.55% | +4.56% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.11% | +4.12% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.09% | +4.10% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +3.52% | +3.53% |
| CAP/USDT:USDT | below_1h_threshold | +2.77% | +2.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
