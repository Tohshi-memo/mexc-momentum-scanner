# Decision Report

- generated_at: 2026-07-22T14:47:00.050442+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9288**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=9288, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.10% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.88% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.59% | **+0.24%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.87% | **+0.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.19% | **+0.18%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.21% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$105.90** / 初期 $100.00 (+5.90%)
- 確定トレード: 132件 (TP 45 / SL 82 / EXP 5)
- 最新: PROM/USDT:USDT TP_HIT PnL +8.00% 残高後 $105.90
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$430.72** / 初期 $100.00 (+330.72%)
- 確定: 3285件 (Win 1037 / Loss 1056 / Flat 1192) / skip 2564件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $430.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1539件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0906 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.90** / 初期 $100.00 (+1.90%)
- 確定: 423件 (Win 142 / Loss 174 / Flat 107) / pending 5件 / skip 343件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.90

## 6. Latest Market Context

- 更新: 2026-07-22T14:46:42.567079+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=65636.7
- Funnel: target 890 → liquid 183 → pre 50 → checked 50 → surge 10 → strict 4
- Surge前reject: below_1h_threshold=40, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1, 4h RSI 79.4 >= 65=1, 4h RSI 73.4 >= 65=1, 4h RSI 72.0 >= 65=1, 4h RSI 74.8 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BROCCOLIF3B/USDT:USDT | +37.83% | $1,008,897.73 |
| RE/USDT:USDT | +30.71% | $15,009,953.38 |
| SMCISTOCK/USDT:USDT | +25.50% | $5,777,099.68 |
| BLESS/USDT:USDT | +23.99% | $2,406,954.60 |
| JIMOTHY/USDT:USDT | +23.30% | $3,508,789.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.76% | +5.20% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.52% | +4.95% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.91% | +4.34% |
| BROCCOLIF3B/USDT:USDT | below_1h_threshold | +3.44% | +3.87% |
| AKE/USDT:USDT | below_1h_threshold | +3.36% | +3.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
