# Decision Report

- generated_at: 2026-10-27T05:06:29.910767+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17566**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17566, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.63% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.76% | **+1.50%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.11% | **+1.16%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.98% | **+0.99%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6722件 (Win 1956 / Loss 2152 / Flat 2614) / skip 7405件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$330.09** / 初期 $100.00 (+230.09%)
- 確定: 4095件 (Win 1125 / Loss 957 / Flat 2013) / skip 6882件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1768 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $330.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5726件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000476 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T05:06:14.810546+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=79828.3
- Funnel: target 1078 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +243.06% | $33,017,100.15 |
| AIN/USDT:USDT | +98.67% | $1,689,967.33 |
| SYN/USDT:USDT | +26.64% | $2,648,121.66 |
| TAG/USDT:USDT | +23.69% | $1,125,738.44 |
| DOOD/USDT:USDT | +16.69% | $5,507,413.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +1.42% | +1.28% |
| DOOD/USDT:USDT | below_1h_threshold | +1.26% | +1.13% |
| DASH/USDT:USDT | below_1h_threshold | +1.18% | +1.04% |
| IRYS/USDT:USDT | below_1h_threshold | +0.90% | +0.77% |
| CHIP/USDT:USDT | below_1h_threshold | +0.82% | +0.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
