# Decision Report

- generated_at: 2026-09-02T21:41:37.378996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13386**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13386, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.53% | **+0.11%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.05% | **-0.04%** |
| LIMIT_2PCT | 19/20 | 95.0% | -0.09% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.54%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.56% | **+1.25%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.37% | **+1.19%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.11% | **+1.06%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.46% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$883.50** / 初期 $100.00 (+783.50%)
- 確定: 4991件 (Win 1514 / Loss 1635 / Flat 1842) / skip 4956件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.81% 残高後 $883.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.72** / 初期 $100.00 (+87.72%)
- 確定: 2365件 (Win 670 / Loss 570 / Flat 1125) / skip 4432件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1564 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $187.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.07** / 初期 $100.00 (+15.07%)
- 確定: 2100件 (Win 613 / Loss 821 / Flat 666) / pending 6件 / skip 2756件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000525 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.07

## 6. Latest Market Context

- 更新: 2026-09-02T21:41:22.610674+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77357.4
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1, 4h RSI 77.4 >= 65=1, 4h RSI 93.1 >= 65=1, 4h RSI 88.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +160.80% | $53,806,708.35 |
| BULLA/USDT:USDT | +29.33% | $2,937,751.21 |
| SNOWSTOCK/USDT:USDT | +21.26% | $1,304,583.82 |
| BTW/USDT:USDT | +20.17% | $7,580,978.12 |
| BONER/USDT:USDT | +15.38% | $2,318,202.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.25% | +4.26% |
| MUBARAK/USDT:USDT | below_1h_threshold | +4.05% | +4.06% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.63% | +2.64% |
| BTW/USDT:USDT | below_1h_threshold | +2.19% | +2.20% |
| T/USDT:USDT | below_1h_threshold | +1.97% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
