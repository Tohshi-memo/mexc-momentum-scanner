# Decision Report

- generated_at: 2026-07-14T10:56:23.219783+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8687**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8687, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S | 3/11 | 27.3% | +0.48% | **+0.13%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.27% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +2.95% | **+2.63%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.11% | **+1.16%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.23% | **+1.13%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.45% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$328.48** / 初期 $100.00 (+228.48%)
- 確定: 2855件 (Win 891 / Loss 926 / Flat 1038) / skip 2393件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $328.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.49** / 初期 $100.00 (+5.49%)
- 確定: 685件 (Win 161 / Loss 162 / Flat 362) / skip 1413件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0536 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 59件 (Win 19 / Loss 39 / Flat 1) / pending 0件 / skip 98件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SXT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T10:56:12.319624+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=62808.3
- Funnel: target 864 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +56.97% | $23,114,042.64 |
| AIOT/USDT:USDT | +31.54% | $8,468,509.50 |
| SXT/USDT:USDT | +24.38% | $6,604,296.14 |
| HEI/USDT:USDT | +20.32% | $1,079,351.11 |
| BSB/USDT:USDT | +18.27% | $3,781,685.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.17% | +3.85% |
| HEI/USDT:USDT | below_1h_threshold | +2.67% | +2.35% |
| ENA/USDT:USDT | below_1h_threshold | +1.90% | +1.57% |
| BSB/USDT:USDT | below_1h_threshold | +1.81% | +1.48% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
