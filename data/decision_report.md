# Decision Report

- generated_at: 2026-09-19T19:46:34.933966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15088**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15088, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.15% | **+0.86%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.82% | **+0.78%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.25%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.98% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.06% | **+0.79%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.39% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6009件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.08** / 初期 $100.00 (+143.08%)
- 確定: 3203件 (Win 888 / Loss 761 / Flat 1554) / skip 5296件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0528 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $243.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 0件 / skip 3590件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000441 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T19:46:22.851620+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=81294.9
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1, 4h RSI 86.6 >= 65=1, 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +43.29% | $31,771,456.89 |
| OFC/USDT:USDT | +40.89% | $1,483,702.87 |
| AKE/USDT:USDT | +31.88% | $80,668,905.35 |
| BANK/USDT:USDT | +10.76% | $1,632,132.26 |
| CATE/USDT:USDT | +10.56% | $1,471,776.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +2.32% | +2.45% |
| ENA/USDT:USDT | below_1h_threshold | +2.22% | +2.35% |
| JASMY/USDT:USDT | below_1h_threshold | +2.09% | +2.21% |
| BR/USDT:USDT | below_1h_threshold | +2.03% | +2.15% |
| SUI/USDT:USDT | below_1h_threshold | +1.81% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
