# Decision Report

- generated_at: 2026-07-18T04:51:19.135972+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8913**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=8913, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.83% | **+0.75%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.72% | **+1.22%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.93% | **+0.79%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.55% | **+0.39%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.34% | **+0.29%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$363.79** / 初期 $100.00 (+263.79%)
- 確定: 3028件 (Win 940 / Loss 963 / Flat 1125) / skip 2446件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $363.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.27** / 初期 $100.00 (+11.27%)
- 確定: 875件 (Win 205 / Loss 178 / Flat 492) / skip 1449件
- 成長率目線: 平均log +0.000122 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0033 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $111.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.64** / 初期 $100.00 (-0.36%)
- 確定: 171件 (Win 54 / Loss 90 / Flat 27) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000253 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.64

## 6. Latest Market Context

- 更新: 2026-07-18T04:51:12.566514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63926.9
- Funnel: target 885 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +65.10% | $12,149,885.89 |
| AKE/USDT:USDT | +38.36% | $49,545,851.69 |
| TRADOOR/USDT:USDT | +14.96% | $1,391,091.40 |
| BSB/USDT:USDT | +9.70% | $1,133,638.04 |
| VVV/USDT:USDT | +8.65% | $2,785,465.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.83% | +2.93% |
| XEC/USDT:USDT | below_1h_threshold | +2.48% | +2.58% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.44% | +2.54% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.91% | +2.00% |
| BSB/USDT:USDT | below_1h_threshold | +1.91% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
