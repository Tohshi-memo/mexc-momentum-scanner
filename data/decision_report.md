# Decision Report

- generated_at: 2026-07-04T12:19:24.936587+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8260**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8260, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.80% | **-1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +2.01% | **+0.50%** |
| LIMIT_7PCT | 2/20 | 10.0% | +3.10% | **+0.31%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.52% | **+0.26%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.35% | **+0.11%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.46% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.37% | **+2.37%** |
| MARKET_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.35% | **+0.94%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.06% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$335.27** / 初期 $100.00 (+235.27%)
- 確定: 2577件 (Win 815 / Loss 858 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $335.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1034件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0432 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T12:19:13.038560+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=62547.8
- Funnel: target 834 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +98.02% | $67,845,121.36 |
| HMSTR/USDT:USDT | +85.90% | $10,630,305.88 |
| TLM/USDT:USDT | +83.17% | $52,499,338.39 |
| ANSEM/USDT:USDT | +83.13% | $5,700,092.74 |
| BAS/USDT:USDT | +44.08% | $4,456,515.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.94% | +4.80% |
| EPIC/USDT:USDT | below_1h_threshold | +3.82% | +3.67% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.19% | +3.05% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.78% | +2.64% |
| BTW/USDT:USDT | below_1h_threshold | +2.71% | +2.57% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
