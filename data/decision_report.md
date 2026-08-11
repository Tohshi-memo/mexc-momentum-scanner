# Decision Report

- generated_at: 2026-08-11T22:56:27.186553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11306**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11306, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +0.94% | **+0.52%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.75% | **+0.49%** |
| LIMIT_BB3S | 3/15 | 20.0% | +2.32% | **+0.46%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.27% | **+1.14%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.30% | **+0.83%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.70% | **+0.76%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.21% | **+0.73%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.04% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3928件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.74** / 初期 $100.00 (+43.74%)
- 確定: 1560件 (Win 435 / Loss 363 / Flat 762) / skip 3157件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0022 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOLO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.64** / 初期 $100.00 (+14.64%)
- 確定: 1331件 (Win 407 / Loss 525 / Flat 399) / pending 0件 / skip 1451件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.64

## 6. Latest Market Context

- 更新: 2026-08-11T22:56:19.046043+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63634.5
- Funnel: target 967 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +48.34% | $1,285,676.55 |
| HOLO/USDT:USDT | +21.60% | $2,758,634.90 |
| LSK/USDT:USDT | +17.95% | $2,537,421.72 |
| CRWVSTOCK/USDT:USDT | +15.71% | $3,408,116.14 |
| BMT/USDT:USDT | +11.72% | $2,559,514.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +4.61% | +4.62% |
| HOLO/USDT:USDT | below_1h_threshold | +3.85% | +3.86% |
| BTW/USDT:USDT | below_1h_threshold | +2.46% | +2.47% |
| AKE/USDT:USDT | below_1h_threshold | +2.06% | +2.08% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +1.86% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
