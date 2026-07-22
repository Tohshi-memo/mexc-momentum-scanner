# Decision Report

- generated_at: 2026-07-22T14:51:56.933481+00:00
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

- 更新: 2026-07-22T14:51:40.018110+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=65725.4
- Funnel: target 890 → liquid 184 → pre 50 → checked 50 → surge 9 → strict 3
- Surge前reject: below_1h_threshold=41, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1, 4h RSI 79.7 >= 65=1, 4h RSI 73.3 >= 65=1, 4h RSI 72.2 >= 65=1, 4h RSI 74.0 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BROCCOLIF3B/USDT:USDT | +39.32% | $1,019,657.39 |
| RE/USDT:USDT | +29.47% | $15,143,261.92 |
| SMCISTOCK/USDT:USDT | +26.10% | $5,837,038.69 |
| BLESS/USDT:USDT | +24.12% | $2,446,818.64 |
| JIMOTHY/USDT:USDT | +21.45% | $3,517,590.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.76% | +5.06% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +4.93% |
| BROCCOLIF3B/USDT:USDT | below_1h_threshold | +4.56% | +4.86% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.52% | +4.81% |
| BANK/USDT:USDT | below_1h_threshold | +4.15% | +4.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
