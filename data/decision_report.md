# Decision Report

- generated_at: 2026-05-17T15:48:31.930180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4409**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4409, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.07% | **+0.05%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.09% | **+0.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.32%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.26% | **+0.63%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.81** / 初期 $100.00 (+18.81%)
- 確定: 406件 (Win 104 / Loss 138 / Flat 164) / skip 564件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $118.81

## 4. Latest Market Context

- 更新: 2026-05-17T15:48:27.593071+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=78006.1
- Funnel: target 760 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +69.16% | $3,261,394.65 |
| BSB/USDT:USDT | +48.30% | $18,237,256.99 |
| AIA/USDT:USDT | +26.01% | $21,027,659.81 |
| SUPRA/USDT:USDT | +24.39% | $1,014,416.07 |
| KAIA/USDT:USDT | +20.26% | $3,430,981.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +2.67% | +2.67% |
| KAIA/USDT:USDT | below_1h_threshold | +2.43% | +2.43% |
| BEAT/USDT:USDT | below_1h_threshold | +1.40% | +1.40% |
| SUPRA/USDT:USDT | below_1h_threshold | +1.32% | +1.33% |
| APE/USDT:USDT | below_1h_threshold | +1.18% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
