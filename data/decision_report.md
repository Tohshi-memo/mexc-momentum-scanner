# Decision Report

- generated_at: 2026-07-21T17:41:19.731882+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9199**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.34% / filled 20/20。**
- 全期間 MARKET基準: n=9199, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.34% | **+2.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.34% | **+2.34%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.12% | **+1.80%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.56% | **+0.34%** |
| LIMIT_ATR | 6/20 | 30.0% | +1.09% | **+0.33%** |
| LIMIT_BB3S | 2/17 | 11.8% | +1.84% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.21% | **-0.19%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.69% | **-0.35%** |
| MARKET_LONG | 20/20 | 100.0% | -0.37% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$106.97** / 初期 $100.00 (+6.97%)
- 確定トレード: 127件 (TP 44 / SL 78 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2511件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1451件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0261 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.03** / 初期 $100.00 (+1.03%)
- 確定: 355件 (Win 123 / Loss 155 / Flat 77) / pending 2件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $101.03

## 6. Latest Market Context

- 更新: 2026-07-21T17:41:12.991069+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=66468.8
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +10.75% | $1,609,333.01 |
| BANK/USDT:USDT | +6.54% | $117,633,583.23 |
| AKE/USDT:USDT | +4.46% | $13,835,954.66 |
| TLM/USDT:USDT | +3.78% | $1,341,011.28 |
| MUU/USDT:USDT | +3.71% | $1,359,766.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +4.86% | +4.92% |
| SNXX/USDT:USDT | below_1h_threshold | +4.15% | +4.21% |
| KORU/USDT:USDT | below_1h_threshold | +2.71% | +2.77% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.60% | +2.66% |
| MYX/USDT:USDT | below_1h_threshold | +2.21% | +2.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
