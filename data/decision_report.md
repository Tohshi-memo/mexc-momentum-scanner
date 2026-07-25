# Decision Report

- generated_at: 2026-07-25T12:51:21.585574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9513**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=9513, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.50% | **+0.88%** |
| LIMIT_BB3S | 6/19 | 31.6% | +2.52% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.61% | **+0.52%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.38% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.28% | **+0.96%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.08% | **+0.92%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.98% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$428.19** / 初期 $100.00 (+328.19%)
- 確定: 3341件 (Win 1054 / Loss 1083 / Flat 1204) / skip 2733件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $428.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.48** / 初期 $100.00 (+31.48%)
- 確定: 1167件 (Win 314 / Loss 254 / Flat 599) / skip 1757件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1008 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $131.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$106.23** / 初期 $100.00 (+6.23%)
- 確定: 560件 (Win 188 / Loss 216 / Flat 156) / pending 4件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000429 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $106.23

## 6. Latest Market Context

- 更新: 2026-07-25T12:51:11.029523+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64070.0
- Funnel: target 898 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +58.86% | $9,285,601.07 |
| DEXE/USDT:USDT | +40.77% | $116,328,032.78 |
| AKE/USDT:USDT | +30.42% | $48,642,846.57 |
| PROM/USDT:USDT | +23.53% | $4,761,673.57 |
| ESPORTS/USDT:USDT | +11.49% | $14,641,420.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.01% | +2.95% |
| BANK/USDT:USDT | below_1h_threshold | +1.94% | +1.88% |
| PROM/USDT:USDT | below_1h_threshold | +1.32% | +1.26% |
| OPENAI/USDT:USDT | below_1h_threshold | +0.96% | +0.90% |
| BASED/USDT:USDT | below_1h_threshold | +0.94% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
