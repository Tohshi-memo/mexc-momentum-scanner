# Decision Report

- generated_at: 2026-09-19T19:56:38.976635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15090**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15090, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/13 | 53.8% | +2.70% | **+1.46%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.60% | **+0.57%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.75% | **+0.56%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.32% | **+0.46%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.31% | **+0.85%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.68% | **+0.80%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.51% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6011件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.08** / 初期 $100.00 (+143.08%)
- 確定: 3204件 (Win 888 / Loss 761 / Flat 1555) / skip 5297件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0281 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $243.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 0件 / skip 3592件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000441 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T19:56:21.839397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=81325.4
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 87.0 >= 65=1, 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +44.08% | $32,244,953.19 |
| OFC/USDT:USDT | +39.86% | $1,493,212.48 |
| AKE/USDT:USDT | +20.57% | $82,640,000.58 |
| CATE/USDT:USDT | +11.92% | $1,477,403.06 |
| BANK/USDT:USDT | +11.73% | $1,649,021.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.76% | +3.85% |
| JASMY/USDT:USDT | below_1h_threshold | +2.64% | +2.73% |
| EVAA/USDT:USDT | below_1h_threshold | +2.62% | +2.71% |
| ENA/USDT:USDT | below_1h_threshold | +2.43% | +2.52% |
| INJ/USDT:USDT | below_1h_threshold | +2.24% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
