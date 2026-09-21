# Decision Report

- generated_at: 2026-09-21T18:56:22.416981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15278**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15278, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +0.81% | **+0.65%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.88% | **+0.22%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.06% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.14% | **+2.35%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.94% | **+2.05%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.04% | **+1.73%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.35% | **+1.29%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.02% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,198.70** / 初期 $100.00 (+1098.70%)
- 確定: 5769件 (Win 1717 / Loss 1852 / Flat 2200) / skip 6070件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.76% 残高後 $1,198.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.53** / 初期 $100.00 (+150.53%)
- 確定: 3320件 (Win 918 / Loss 766 / Flat 1636) / skip 5369件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0749 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $250.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.42** / 初期 $100.00 (+23.42%)
- 確定: 3051件 (Win 898 / Loss 1192 / Flat 961) / pending 4件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000381 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.42

## 6. Latest Market Context

- 更新: 2026-09-21T18:56:12.107367+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=86014.7
- Funnel: target 1055 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +27.11% | $6,210,833.47 |
| SYN/USDT:USDT | +11.54% | $4,646,168.15 |
| EVAA/USDT:USDT | +10.17% | $1,215,832.80 |
| PTB/USDT:USDT | +7.80% | $1,193,718.90 |
| BTW/USDT:USDT | +5.07% | $4,856,361.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGU/USDT:USDT | below_1h_threshold | +4.88% | +4.69% |
| SPX/USDT:USDT | below_1h_threshold | +4.70% | +4.51% |
| EVAA/USDT:USDT | below_1h_threshold | +3.23% | +3.04% |
| ZETA/USDT:USDT | below_1h_threshold | +3.19% | +3.01% |
| RAY/USDT:USDT | below_1h_threshold | +3.07% | +2.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
