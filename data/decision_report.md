# Decision Report

- generated_at: 2026-09-19T19:21:32.415816+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15085**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15085, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +3.03% | **+1.06%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.98% | **+0.74%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.42% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.73% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.98% | **+0.59%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.85% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6006件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.77** / 初期 $100.00 (+143.77%)
- 確定: 3200件 (Win 887 / Loss 760 / Flat 1553) / skip 5296件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0279 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $243.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 0件 / skip 3586件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000410 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T19:21:19.239277+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81408.7
- Funnel: target 1050 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +34.83% | $30,484,669.96 |
| OFC/USDT:USDT | +34.15% | $1,465,330.29 |
| AKE/USDT:USDT | +14.27% | $75,676,188.21 |
| PEPE/USDT:USDT | +12.46% | $156,599,006.17 |
| CATE/USDT:USDT | +8.52% | $1,451,154.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.43% | +2.42% |
| SYN/USDT:USDT | below_1h_threshold | +2.34% | +2.33% |
| JASMY/USDT:USDT | below_1h_threshold | +1.82% | +1.80% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.64% | +1.62% |
| PEPE/USDT:USDT | below_1h_threshold | +1.51% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
