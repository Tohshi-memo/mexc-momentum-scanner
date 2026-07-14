# Decision Report

- generated_at: 2026-07-14T14:51:13.187119+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8695**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8695, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.68% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.54% | **+2.83%** |
| LIMIT_BB3S_LONG | 11/12 | 91.7% | +2.96% | **+2.71%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.60% | **+2.16%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.37% | **+2.01%** |
| MARKET_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.58** / 初期 $100.00 (+231.58%)
- 確定: 2861件 (Win 894 / Loss 929 / Flat 1038) / skip 2395件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SXT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.25% 残高後 $331.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.49** / 初期 $100.00 (+5.49%)
- 確定: 691件 (Win 161 / Loss 162 / Flat 368) / skip 1415件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0031 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SXT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 59件 (Win 19 / Loss 39 / Flat 1) / pending 0件 / skip 106件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000212 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SXT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T14:51:06.938506+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=63939.1
- Funnel: target 862 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +73.37% | $36,966,876.26 |
| BSB/USDT:USDT | +32.35% | $6,163,676.86 |
| AIOT/USDT:USDT | +28.20% | $8,806,583.49 |
| CASHCAT/USDT:USDT | +27.27% | $1,011,246.94 |
| HEI/USDT:USDT | +22.14% | $1,674,885.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXTISTOCK/USDT:USDT | below_1h_threshold | +4.79% | +4.58% |
| AIOT/USDT:USDT | below_1h_threshold | +4.06% | +3.85% |
| JPMSTOCK/USDT:USDT | below_1h_threshold | +3.81% | +3.60% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.79% | +3.58% |
| BSB/USDT:USDT | below_1h_threshold | +2.60% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
