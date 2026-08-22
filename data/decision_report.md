# Decision Report

- generated_at: 2026-08-22T01:41:26.348946+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12287**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12287, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.36% | **-2.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.70% | **+1.48%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.97% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.38% | **+4.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +5.22% | **+3.92%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +4.26% | **+3.41%** |
| MARKET_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +4.29% | **+1.93%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$696.84** / 初期 $100.00 (+596.84%)
- 確定: 4406件 (Win 1350 / Loss 1440 / Flat 1616) / skip 4442件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $696.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.78** / 初期 $100.00 (+54.78%)
- 確定: 1893件 (Win 521 / Loss 452 / Flat 920) / skip 3805件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1998 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.87** / 初期 $100.00 (+17.87%)
- 確定: 1837件 (Win 545 / Loss 695 / Flat 597) / pending 4件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000502 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.87

## 6. Latest Market Context

- 更新: 2026-08-22T01:41:14.028313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77980.9
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +286.39% | $3,687,358.36 |
| CATE/USDT:USDT | +66.45% | $12,113,300.46 |
| AGI/USDT:USDT | +27.21% | $1,726,714.09 |
| RE/USDT:USDT | +20.71% | $7,034,579.40 |
| JIMOTHY/USDT:USDT | +20.09% | $1,658,706.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.73% | +3.64% |
| RE/USDT:USDT | below_1h_threshold | +3.55% | +3.47% |
| ZEN/USDT:USDT | below_1h_threshold | +3.37% | +3.29% |
| PYTH/USDT:USDT | below_1h_threshold | +2.81% | +2.73% |
| US/USDT:USDT | below_1h_threshold | +2.78% | +2.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
