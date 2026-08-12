# Decision Report

- generated_at: 2026-08-12T07:31:27.781937+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11338**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11338, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.48%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.06% | **+0.32%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.57% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +5.72% | **+2.86%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.76%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.12% | **+0.39%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.51% | **+0.28%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.62% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3940件 (Win 1230 / Loss 1285 / Flat 1425) / skip 3959件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.68** / 初期 $100.00 (+44.68%)
- 確定: 1574件 (Win 439 / Loss 364 / Flat 771) / skip 3175件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0275 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $144.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.27** / 初期 $100.00 (+14.27%)
- 確定: 1353件 (Win 409 / Loss 529 / Flat 415) / pending 3件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000048 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.27

## 6. Latest Market Context

- 更新: 2026-08-12T07:31:17.881075+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63705.0
- Funnel: target 968 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +61.53% | $1,094,566.09 |
| PROM/USDT:USDT | +34.65% | $7,119,567.15 |
| JIMOTHY/USDT:USDT | +30.59% | $2,031,692.68 |
| BEAT/USDT:USDT | +25.84% | $90,844,952.90 |
| CRWVSTOCK/USDT:USDT | +17.36% | $4,357,376.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +4.62% | +4.60% |
| APR/USDT:USDT | below_1h_threshold | +4.24% | +4.21% |
| CRV/USDT:USDT | below_1h_threshold | +2.26% | +2.23% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.62% |
| TRB/USDT:USDT | below_1h_threshold | +1.14% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
