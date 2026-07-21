# Decision Report

- generated_at: 2026-07-21T11:26:13.310138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9173**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9173, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_BB3S | 9/17 | 52.9% | +0.69% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.92% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.81% | **+1.36%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.22% | **+1.10%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.18% | **+0.87%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.62% | **+0.84%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$424.71** / 初期 $100.00 (+324.71%)
- 確定: 3235件 (Win 1017 / Loss 1032 / Flat 1186) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ERA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $424.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.48** / 初期 $100.00 (+32.48%)
- 確定: 1134件 (Win 304 / Loss 240 / Flat 590) / skip 1450件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0747 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $132.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 304件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T11:26:06.792362+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=66182.5
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +87.26% | $4,694,542.49 |
| ERA/USDT:USDT | +64.21% | $8,264,609.74 |
| ZHIPUSTOCK/USDT:USDT | +31.12% | $3,198,791.58 |
| ESPORTS/USDT:USDT | +27.11% | $6,254,239.56 |
| ON/USDT:USDT | +15.01% | $3,462,826.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ERA/USDT:USDT | below_1h_threshold | +4.52% | +4.49% |
| B/USDT:USDT | below_1h_threshold | +3.70% | +3.67% |
| UB/USDT:USDT | below_1h_threshold | +3.00% | +2.96% |
| ALLO/USDT:USDT | below_1h_threshold | +2.05% | +2.02% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.66% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
