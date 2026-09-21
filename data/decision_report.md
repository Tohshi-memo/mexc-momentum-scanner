# Decision Report

- generated_at: 2026-09-21T16:51:40.570485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15271**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15271, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.14% | **-2.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 17/20 | 85.0% | +1.01% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.80% | **+2.28%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.48% | **+2.26%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.66% | **+1.73%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.33% | **+1.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.65** / 初期 $100.00 (+1095.65%)
- 確定: 5762件 (Win 1716 / Loss 1851 / Flat 2195) / skip 6070件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,195.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3315件 (Win 915 / Loss 765 / Flat 1635) / skip 5367件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.68** / 初期 $100.00 (+22.68%)
- 確定: 3045件 (Win 895 / Loss 1191 / Flat 959) / pending 6件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000205 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.68

## 6. Latest Market Context

- 更新: 2026-09-21T16:51:22.676810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=85911.1
- Funnel: target 1055 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.1 >= 65=1, 4h RSI 75.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +33.95% | $1,972,066.63 |
| ALLO/USDT:USDT | +6.27% | $1,850,439.25 |
| AKE/USDT:USDT | +4.66% | $44,323,056.91 |
| SYN/USDT:USDT | +4.56% | $4,344,889.79 |
| STRK/USDT:USDT | +2.79% | $2,889,200.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.67% | +4.63% |
| SYN/USDT:USDT | below_1h_threshold | +4.65% | +4.62% |
| STRK/USDT:USDT | below_1h_threshold | +2.80% | +2.76% |
| BTW/USDT:USDT | below_1h_threshold | +2.52% | +2.48% |
| SEI/USDT:USDT | below_1h_threshold | +2.27% | +2.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
