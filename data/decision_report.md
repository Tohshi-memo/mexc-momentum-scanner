# Decision Report

- generated_at: 2026-08-30T06:51:29.961917+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13031**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13031, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 14/18 | 77.8% | +1.49% | **+1.16%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.29% | **+0.07%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.14% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| MARKET_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.58% | **+1.11%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$798.40** / 初期 $100.00 (+698.40%)
- 確定: 4801件 (Win 1463 / Loss 1578 / Flat 1760) / skip 4791件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.68% 残高後 $798.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.08** / 初期 $100.00 (+73.08%)
- 確定: 2115件 (Win 591 / Loss 516 / Flat 1008) / skip 4327件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $173.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.73** / 初期 $100.00 (+17.73%)
- 確定: 2074件 (Win 610 / Loss 803 / Flat 661) / pending 6件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000250 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.73

## 6. Latest Market Context

- 更新: 2026-08-30T06:51:17.437098+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=78243.1
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1, 4h RSI 75.0 >= 65=1, 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +80.36% | $36,625,000.66 |
| PONS/USDT:USDT | +74.49% | $1,682,246.55 |
| NIULAI/USDT:USDT | +72.65% | $2,908,014.73 |
| FONE/USDT:USDT | +40.73% | $1,455,729.69 |
| PROM/USDT:USDT | +31.10% | $15,496,308.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +4.92% | +4.75% |
| UAI/USDT:USDT | below_1h_threshold | +4.54% | +4.37% |
| HEMI/USDT:USDT | below_1h_threshold | +2.32% | +2.15% |
| PROM/USDT:USDT | below_1h_threshold | +1.41% | +1.24% |
| DOS/USDT:USDT | below_1h_threshold | +1.06% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
