# Decision Report

- generated_at: 2026-08-05T20:11:30.005900+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10456**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10456, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/19 | 42.1% | +2.01% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.39% | **+0.14%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.81% | **+0.48%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.66% | **+0.40%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.11% | **+0.28%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.44% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3247件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.53** / 初期 $100.00 (+40.53%)
- 確定: 1353件 (Win 378 / Loss 318 / Flat 657) / skip 2514件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1233 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $140.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 786件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000450 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T20:11:20.255483+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64849.9
- Funnel: target 948 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +39.54% | $1,463,327.46 |
| BLESS/USDT:USDT | +39.38% | $96,168,793.28 |
| HEI/USDT:USDT | +31.61% | $42,576,078.25 |
| UB/USDT:USDT | +21.58% | $22,435,655.85 |
| BICO/USDT:USDT | +18.70% | $13,111,710.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +3.14% | +3.06% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.07% | +3.00% |
| SOXS/USDT:USDT | below_1h_threshold | +2.20% | +2.12% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.85% | +1.77% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.63% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
