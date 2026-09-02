# Decision Report

- generated_at: 2026-09-02T14:16:23.762224+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13338**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13338, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.22% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.11% | **+0.07%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.89% | **+1.61%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.01% | **+1.51%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.12% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.27% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$838.59** / 初期 $100.00 (+738.59%)
- 確定: 4964件 (Win 1505 / Loss 1628 / Flat 1831) / skip 4935件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $838.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.23** / 初期 $100.00 (+75.23%)
- 確定: 2317件 (Win 645 / Loss 554 / Flat 1118) / skip 4432件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0595 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $175.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000146 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T14:16:14.123843+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=77263.6
- Funnel: target 1044 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +45.17% | $13,407,526.24 |
| FONE/USDT:USDT | +43.02% | $1,888,835.16 |
| MAGMA/USDT:USDT | +42.04% | $11,267,959.64 |
| AKE/USDT:USDT | +28.94% | $7,242,774.20 |
| CASHCAT/USDT:USDT | +25.57% | $1,975,023.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.33% | +3.13% |
| FONE/USDT:USDT | below_1h_threshold | +3.01% | +2.81% |
| METASTOCK/USDT:USDT | below_1h_threshold | +2.95% | +2.75% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +2.47% | +2.27% |
| NEMSTOCK/USDT:USDT | below_1h_threshold | +1.93% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
