# Decision Report

- generated_at: 2026-09-05T22:56:24.574031+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13780**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=13780, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.68% | **+0.17%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.87% | **+0.55%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.62% | **+0.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$861.15** / 初期 $100.00 (+761.15%)
- 確定: 5086件 (Win 1525 / Loss 1658 / Flat 1903) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $861.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.27** / 初期 $100.00 (+88.27%)
- 確定: 2525件 (Win 703 / Loss 597 / Flat 1225) / skip 4666件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0397 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: OP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.73** / 初期 $100.00 (+19.73%)
- 確定: 2397件 (Win 711 / Loss 909 / Flat 777) / pending 6件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: OP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.73

## 6. Latest Market Context

- 更新: 2026-09-05T22:56:13.854977+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=79768.6
- Funnel: target 1050 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.0 >= 65=1, 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +36.52% | $67,033,484.76 |
| 4/USDT:USDT | +21.34% | $23,871,428.07 |
| SUSHI/USDT:USDT | +20.63% | $3,585,495.59 |
| BASECAT/USDT:USDT | +18.22% | $1,856,255.40 |
| UNI/USDT:USDT | +11.90% | $55,077,281.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +2.67% | +2.80% |
| INTUSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.44% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.26% | +2.39% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.22% | +2.34% |
| STRK/USDT:USDT | below_1h_threshold | +1.87% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
