# Decision Report

- generated_at: 2026-08-05T22:26:23.342399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10469**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10469, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.07% | **+0.46%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +1.88% | **+0.94%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.83% | **+0.62%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.04% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3260件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.64** / 初期 $100.00 (+40.64%)
- 確定: 1355件 (Win 379 / Loss 319 / Flat 657) / skip 2525件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1602 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 802件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T22:26:15.213132+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64674.0
- Funnel: target 948 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1, 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +57.28% | $3,869,968.73 |
| BLESS/USDT:USDT | +42.51% | $100,959,576.90 |
| HEI/USDT:USDT | +36.62% | $43,860,314.81 |
| SITMSTOCK/USDT:USDT | +27.41% | $1,041,735.50 |
| ZBT/USDT:USDT | +24.82% | $1,150,833.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.22% | +4.28% |
| ZBT/USDT:USDT | below_1h_threshold | +3.77% | +3.83% |
| HEI/USDT:USDT | below_1h_threshold | +2.79% | +2.85% |
| SYN/USDT:USDT | below_1h_threshold | +2.00% | +2.06% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
