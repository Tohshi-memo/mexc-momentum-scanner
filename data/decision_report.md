# Decision Report

- generated_at: 2026-09-16T10:36:22.029537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14663**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14663, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_BB3S | 6/12 | 50.0% | +0.84% | **+0.42%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.13% | **+0.10%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +2.67% | **+1.67%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.65% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.41% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,041.49** / 初期 $100.00 (+941.49%)
- 確定: 5541件 (Win 1650 / Loss 1791 / Flat 2100) / skip 5683件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,041.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.85** / 初期 $100.00 (+128.85%)
- 確定: 3069件 (Win 842 / Loss 722 / Flat 1505) / skip 5005件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0123 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $228.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.40** / 初期 $100.00 (+24.40%)
- 確定: 2952件 (Win 878 / Loss 1161 / Flat 913) / pending 2件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.40

## 6. Latest Market Context

- 更新: 2026-09-16T10:36:07.300278+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=75927.7
- Funnel: target 1058 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +110.78% | $16,668,350.32 |
| BR/USDT:USDT | +33.80% | $17,167,381.59 |
| LSK/USDT:USDT | +29.46% | $21,795,556.45 |
| USELESS/USDT:USDT | +15.28% | $7,405,110.87 |
| LONGXIA/USDT:USDT | +13.07% | $2,655,530.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +4.92% | +4.96% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.04% | +2.08% |
| 4/USDT:USDT | below_1h_threshold | +1.85% | +1.89% |
| AKE/USDT:USDT | below_1h_threshold | +1.62% | +1.66% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
