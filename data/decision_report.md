# Decision Report

- generated_at: 2026-09-02T20:11:30.620585+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13377**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13377, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.79% | **-1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.95% | **+0.99%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +7.46% | **+4.98%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.38% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.59% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$880.84** / 初期 $100.00 (+780.84%)
- 確定: 4989件 (Win 1513 / Loss 1634 / Flat 1842) / skip 4949件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FLOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.16% 残高後 $880.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.21** / 初期 $100.00 (+85.21%)
- 確定: 2356件 (Win 665 / Loss 567 / Flat 1124) / skip 4432件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1760 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $185.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 1件 / skip 2755件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000493 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T20:11:16.159798+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=77341.5
- Funnel: target 1044 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +74.65% | $35,322,811.78 |
| BONER/USDT:USDT | +21.36% | $3,024,725.15 |
| MARSCOIN/USDT:USDT | +16.76% | $3,104,185.58 |
| BULLA/USDT:USDT | +15.11% | $2,642,467.75 |
| BTW/USDT:USDT | +10.65% | $6,291,136.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +1.63% | +1.57% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.61% | +1.55% |
| SUI/USDT:USDT | below_1h_threshold | +1.58% | +1.52% |
| FONE/USDT:USDT | below_1h_threshold | +1.43% | +1.37% |
| APT/USDT:USDT | below_1h_threshold | +1.42% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
